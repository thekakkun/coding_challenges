#![allow(unused)]

use std::collections::{HashMap, HashSet};

pub fn parse_file(f: &str) -> Vec<((i32, i32), (i32, i32))> {
    f.lines()
        .map(|pair| {
            let (first, second) = pair.split_once(',').unwrap();
            (parse_range(first), parse_range(second))
        })
        .collect()
}

fn parse_range(range: &str) -> (i32, i32) {
    let (start, end) = range.split_once('-').unwrap();
    (start.parse().unwrap(), end.parse().unwrap())
}

pub fn part_1(input: &[((i32, i32), (i32, i32))]) -> i32 {
    input
        .iter()
        .copied()
        .filter(|((first_start, first_end), (second_start, second_end))| {
            (first_start <= second_start && second_end <= first_end)
                || (second_start <= first_start && first_end <= second_end)
        })
        .count() as i32
}

pub fn part_2(input: &[((i32, i32), (i32, i32))]) -> i32 {
    todo!()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
";

    #[test]
    fn test_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(part_1(&input), 2);
    }

    // #[test]
    // fn test_part_2() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!(part_2(&input), 70);
    // }
}
