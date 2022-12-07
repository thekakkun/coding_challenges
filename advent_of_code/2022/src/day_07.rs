#![allow(unused)]

use std::ops::IndexMut;

#[derive(Clone, Debug)]
pub struct File {
    name: String,
    size: i32,
}

impl File {
    pub fn new(name: String, size: i32) -> Self {
        Self { name, size }
    }
}

#[derive(Clone, Debug)]
pub struct Dir {
    name: String,
    size: i32,
    children: Vec<FileSystemItem>,
}

impl Dir {
    pub fn new(name: String) -> Self {
        Self {
            name,
            size: 0,
            children: Vec::new(),
        }
    }

    fn add_child(&mut self, child: FileSystemItem) {
        self.size += child.get_size();
        self.children.push(child);
    }
}

#[derive(Clone, Debug)]
pub enum FileSystemItem {
    Dir(Dir),
    File(File),
}

impl FileSystemItem {
    fn get_size(&self) -> i32 {
        match self {
            FileSystemItem::Dir(item) => item.size,
            FileSystemItem::File(item) => item.size,
        }
    }
}

pub fn parse_file(f: &str) -> Dir {
    let mut root = Dir {
        size: 0,
        name: String::from("root"),
        children: Vec::new(),
    };
    let mut dirs = vec![&mut root];
    let mut lines = f.lines();

    for line in lines {
        match line.split_once(' ') {
            Some(("$", command)) => match command.split_once(' ') {
                Some(("cd", dir)) => match dir {
                    "/" => {
                        println!("dirs: {:?}", dirs);
                        dirs.drain(1..);
                        println!("went to root: {:?}", dirs);
                    }
                    ".." => {
                        println!("dirs: {:?}", dirs);
                        dirs.pop();
                        println!("go up: {:?}", dirs);
                    }
                    _ => {
                        let new_dir = FileSystemItem::Dir(Dir::new(dir.to_string()));
                        let current_dir = dirs[dirs.len()];
                        current_dir.add_child(new_dir);
                        dirs.push(current_dir);
                    }
                },
                Some((command, _)) => panic!("unknown command: {command}"),
                None => (),
            },
            Some(("dir", name)) => (),
            Some((size, name)) => {
                let new_file =
                    FileSystemItem::File(File::new(name.to_string(), size.parse().unwrap()));

                let current_dir = dirs[dirs.len()];
                current_dir.add_child(new_file);
            }
            None => (),
        }
    }

    println!("{:?}", root);

    root
}

// pub fn part_1(input: &str) -> usize {
//     find_marker(input, 4).unwrap()
// }

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
        parse_file(EXAMPLE_FILE);
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
