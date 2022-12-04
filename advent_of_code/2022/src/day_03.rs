#![allow(unused)]

use std::collections::{HashMap, HashSet};

pub fn parse_input(f: &str) -> Vec<[HashMap<char, i32>; 2]> {
    f.lines()
        .map(|line| {
            let (mut ruck_0, mut ruck_1) = (HashMap::new(), HashMap::new());

            let mut item_iter = line.chars();

            while let (Some(ruck_0_item), Some(ruck_1_item)) =
                (item_iter.next(), item_iter.next_back())
            {
                let (rs_0_count, rs_1_count) = (
                    ruck_0.entry(ruck_0_item).or_insert(0),
                    ruck_1.entry(ruck_1_item).or_insert(0),
                );

                *rs_0_count += 1;
                *rs_1_count += 1;
            }

            [ruck_0, ruck_1]
        })
        .collect()
}

pub fn part_1(input: &[[HashMap<char, i32>; 2]]) -> i32 {
    input
        .iter()
        .map(|rucks| {
            let ruck_0_contents: HashSet<&char> = HashSet::from_iter(rucks[0].keys());
            let ruck_1_contents: HashSet<&char> = HashSet::from_iter(rucks[1].keys());

            let shared_content = ruck_0_contents
                .intersection(&ruck_1_contents)
                .next()
                .unwrap();

            char2priority(**shared_content)
        })
        .sum()
}

pub fn part_2(input: &[[HashMap<char, i32>; 2]]) -> i32 {
    let mut total = 0;

    let groups = input.chunks(3);

    for group in groups {
        let unique_items = group
            .iter()
            .map(|rucks| {
                let items: HashSet<_> = (rucks[0].keys().chain(rucks[1].keys())).copied().collect();
                items
            })
            .reduce(|acc, item| {
                let unique_item: HashSet<_> = acc.intersection(&item).copied().collect();
                unique_item
            })
            .unwrap();

        let unique_item = unique_items
            .iter()
            .next()
            .unwrap();

        total += char2priority(*unique_item);
    }

    total
}

fn char2priority(char: char) -> i32 {
    match char {
        'a'..='z' => (char as i32) - 96,
        'A'..='Z' => (char as i32) - 38,
        _ => unreachable!("Should never happen."),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
";

    #[test]
    fn test() {
        println!("{:?}", 'a'..='Z');
    }

    #[test]
    fn test_part_1() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_1(&input), 157);
    }

    #[test]
    fn test_part_2() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_2(&input), 70);
    }
}
