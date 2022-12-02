#![allow(dead_code)]

use std::cmp;

pub fn parse_input(f: &str) -> &str {
    f
}

pub fn part_1(input: &str) -> i32 {
    let mut max_cal = 0;

    let mut elf_cal = 0;
    for food_cal in input.lines() {
        if food_cal.is_empty() {
            max_cal = cmp::max(max_cal, elf_cal);
            elf_cal = 0;
        } else {
            elf_cal += food_cal.parse::<i32>().unwrap()
        }
    }

    if elf_cal != 0 {
        max_cal = cmp::max(max_cal, elf_cal);
    }

    max_cal
}

pub fn part_2(input: &str, elves: usize) -> i32 {
    let mut max_cals = vec![0; elves];

    let mut elf_cal = 0;
    for food_cal in input.lines() {
        if food_cal.is_empty() {
            max_cals[0] = cmp::max(max_cals[0], elf_cal);
            max_cals.sort();
            elf_cal = 0;
        } else {
            elf_cal += food_cal.parse::<i32>().unwrap()
        }
    }

    if elf_cal != 0 {
        max_cals[0] = cmp::max(max_cals[0], elf_cal);
    }

    max_cals.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
";

    #[test]
    fn part_1_example() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_1(input), 24000);
    }

    #[test]
    fn part_2_example() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_2(input, 3), 45000);
    }
}
