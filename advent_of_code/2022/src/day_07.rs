#![allow(unused)]

use std::cell::RefCell;
use std::cmp;
use std::rc::{Rc, Weak};

#[derive(Debug, Clone)]
enum ItemType {
    Dir(Vec<Rc<FileSystemItem>>),
    File,
}

#[derive(Debug)]
pub struct FileSystemItem {
    name: String,
    size: RefCell<i32>,
    parent: RefCell<Weak<FileSystemItem>>,
    item_type: RefCell<ItemType>,
}

pub fn parse_file(f: &str) -> Rc<FileSystemItem> {
    let root = Rc::new(FileSystemItem {
        name: String::from("root"),
        size: RefCell::new(0),
        parent: RefCell::new(Weak::new()),
        item_type: RefCell::new(ItemType::Dir(vec![])),
    });
    let mut current = root.clone();

    f.lines().for_each(|line| {
        match line.split_whitespace().collect::<Vec<&str>>().as_slice() {
            ["$", "cd", "/"] => current = root.clone(),
            ["$", "cd", ".."] => {
                let parent_folder = current.parent.borrow().upgrade().unwrap();
                current = parent_folder;
            }
            ["$", "cd", dir] => {
                // create new_dir
                let new_dir = Rc::new(FileSystemItem {
                    name: String::from(*dir),
                    size: RefCell::new(0),
                    parent: RefCell::new(Rc::downgrade(&current)), // parent of new_dir is current
                    item_type: RefCell::new(ItemType::Dir(vec![])),
                });

                // Add new_dir as child to current
                if let ItemType::Dir(ref mut siblings) = *current.item_type.borrow_mut() {
                    siblings.push(new_dir.clone());
                }

                // move into new_dir
                current = new_dir;
            }
            ["$", "ls"] => (),
            ["$", command, ..] => panic!("unknown command: {command}"),
            ["dir", _name] => (),
            [size, name] => {
                let new_file = Rc::new(FileSystemItem {
                    name: String::from(*name),
                    size: RefCell::new(size.parse().unwrap()),
                    parent: RefCell::new(Rc::downgrade(&current)), // parent of new_file is current
                    item_type: RefCell::new(ItemType::File),
                });

                // While there's an ancestor, add file size to ancestor
                let mut ancestor = new_file.clone();
                while let Some(older_ancestor) = ancestor.clone().parent.borrow().upgrade() {
                    older_ancestor
                        .size
                        .replace_with(|&mut s| s + size.parse::<i32>().unwrap());

                    ancestor = older_ancestor;
                }

                // Add file to current's children
                if let ItemType::Dir(ref mut siblings) = *current.item_type.borrow_mut() {
                    siblings.push(new_file);
                }
            }
            _ => (),
        }
    });

    root
}

pub fn part_1(input: Rc<FileSystemItem>, max_size: i32) -> i32 {
    match *input.item_type.borrow() {
        ItemType::File => 0,
        ItemType::Dir(ref contents) => {
            let mut total_size = if *input.size.borrow() <= max_size {
                *input.size.borrow()
            } else {
                0
            };

            total_size += contents
                .iter()
                .cloned()
                .map(|child| part_1(child, max_size))
                .sum::<i32>();

            total_size
        }
    }
}

pub fn part_2(input: Rc<FileSystemItem>, total_space: i32, required_space: i32) -> i32 {
    let unused_space = total_space - *input.size.borrow();
    let mut smallest_dir = total_space;

    if let ItemType::Dir(mut deletion_candidates) = (*input.item_type.borrow()).clone() {
        while let Some(candidate) = deletion_candidates.pop() {
            if let ItemType::Dir(ref contents) = *candidate.item_type.borrow() {
                if required_space < unused_space + *candidate.size.borrow() {
                    smallest_dir = cmp::min(smallest_dir, *candidate.size.borrow());
                }

                deletion_candidates.extend(contents.clone());
            }
        }
    } else {
        return *input.size.borrow();
    };

    smallest_dir
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
";

    #[test]
    fn parse_example_file() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(48381165, *input.size.borrow());
    }

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(95437, part_1(input, 100000));
    }

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(24933642, part_2(input, 70000000, 30000000));
    }
}
