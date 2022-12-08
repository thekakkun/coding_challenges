use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
pub struct FileSystemItem {
    name: String,
    size: RefCell<i32>,
    parent: RefCell<Weak<FileSystemItem>>,
    children: RefCell<Option<Vec<Rc<FileSystemItem>>>>,
}

pub fn parse_file(f: &str) -> Rc<FileSystemItem> {
    let root = Rc::new(FileSystemItem {
        name: String::from("root"),
        size: RefCell::new(0),
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(Some(vec![])),
    });
    let mut current = root.clone();

    f.lines().for_each(|line| {
        println!("{line}");
        match line.split_once(' ') {
            Some(("$", command)) => match command.split_once(' ') {
                Some(("cd", dir)) => match dir {
                    "/" => {
                        current = root.clone();
                        println!("Current = {}", current.name);
                    }
                    ".." => {
                        let parent_folder = current.parent.borrow().upgrade().unwrap();
                        current = parent_folder;
                        println!("Current = {}", current.name);
                    }
                    _ => {
                        // create new_dir
                        let new_dir = Rc::new(FileSystemItem {
                            name: String::from(dir),
                            size: RefCell::new(0),
                            parent: RefCell::new(Rc::downgrade(&current)), // parent of new_dir is current
                            children: RefCell::new(Some(vec![])),
                        });

                        // Add new_dir as child to current
                        if let Some(ref mut siblings) = *current.children.borrow_mut() {
                            siblings.push(new_dir.clone());
                        }

                        // move into new_dir
                        current = new_dir;
                    }
                },
                Some(("ls", _)) => (),
                Some((command, _)) => panic!("unknown command: {command}"),
                None => (),
            },
            Some(("dir", _)) => (),
            Some((size, name)) => {
                let new_file = Rc::new(FileSystemItem {
                    name: String::from(name),
                    size: RefCell::new(size.parse().unwrap()),
                    parent: RefCell::new(Rc::downgrade(&current)), // parent of new_file is current
                    children: RefCell::new(None),                  // files have no children
                });

                let mut ancestor = new_file.clone();

                while let Some(older_ancestor) = ancestor.clone().parent.borrow().upgrade() {
                    older_ancestor
                        .size
                        .replace_with(|&mut s| s + size.parse::<i32>().unwrap());

                    ancestor = older_ancestor;
                }

                if let Some(ref mut siblings) = *current.children.borrow_mut() {
                    siblings.push(new_file);
                }
            }
            None => (),
        }
    });

    root
}

pub fn part_1(input: Rc<FileSystemItem>) -> i32 {
    let count = 0;

    count
}

// pub fn part_2(input: &str) -> usize {
//     find_marker(input, 14).unwrap()
// }

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

    // #[test]
    // fn example_part_1() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!("CMZ", part_1(&input));
    // }

    // #[test]
    // fn example_part_2() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!("MCD", part_2(&input));
    // }
}
