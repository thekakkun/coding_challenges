pub fn parse_input(f: String) -> Vec<Vec<i32>> {
    let mut elves = Vec::new();

    let mut elf: Vec<i32> = Vec::new();
    for line in f.lines() {
        if line.is_empty() {
            elves.push(elf);
            elf = Vec::new();
        } else {
            elf.push(line.parse().unwrap())
        }
    }
    elves.push(elf);
    elves
}

pub fn part_1(input: &[Vec<i32>]) -> i32 {
    let elves: Vec<i32> = input.iter().map(|elf| elf.iter().sum()).collect();

    *elves.iter().max().unwrap()
}

pub fn part_2(input: &[Vec<i32>]) -> i32 {
    let mut elves: Vec<i32> = input.iter().map(|elf| elf.iter().sum()).collect();

    elves.sort();
    elves.iter().rev().take(3).sum()
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

10000";

    #[test]
    fn part_1_example() {
        let input = parse_input(String::from(EXAMPLE_FILE));
        assert_eq!(part_1(&input), 24000);
    }

    #[test]
    fn part_2_example() {
        let input = parse_input(String::from(EXAMPLE_FILE));
        assert_eq!(part_2(&input), 45000);
    }
}
