#![allow(unused)]

use regex::Regex;

#[derive(Clone, Debug)]
pub struct SupplyStacks {
    stacks: Vec<Vec<char>>,
    procedures: Vec<(usize, usize, usize)>,
}

impl SupplyStacks {
    fn do_procedures(&mut self) {
        for (count, from, to) in &self.procedures {
            for i in 0..*count {
                let target = self.stacks[*from - 1].pop().unwrap();
                self.stacks[*to - 1].push(target);
            }
        }
    }

    fn get_tops(&self) -> String {
        let tops = self
            .stacks
            .iter()
            .map(|stack| stack.last().unwrap())
            .collect();
        tops
    }
}

pub fn parse_file(f: &str) -> SupplyStacks {
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut procedures = Vec::new();

    let (crate_f, procedures_f) = f.split_once("\n\n").unwrap();

    let crate_re = Regex::new(r"(?:\[([A-Z])\]|(\s{3}))(?:\s|$)").unwrap();
    crate_f.lines().rev().for_each(|line| {
        for (i, cap) in crate_re.captures_iter(line).enumerate() {
            if let Some(m) = cap.get(1) {
                let content = m.as_str().chars().next().unwrap();

                if let Some(target) = stacks.get_mut(i) {
                    target.push(content);
                } else {
                    stacks.push(vec![content]);
                }
            }
        }
    });

    let procedures_re = Regex::new(r"^move (\d*) from (\d*) to (\d*)$").unwrap();
    procedures_f.lines().for_each(|line| {
        let cap = procedures_re.captures(line).unwrap();
        procedures.push((
            cap[1].parse().unwrap(),
            cap[2].parse().unwrap(),
            cap[3].parse().unwrap(),
        ))
    });

    SupplyStacks { stacks, procedures }
}

pub fn part_1(mut input: SupplyStacks) -> String {
    input.do_procedures();
    input.get_tops()
}

// pub fn part_2(input: SupplyStacks) {
//     todo!()
// }

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
";

    #[test]
    fn test_parse_file() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(
            vec![vec!['Z', 'N'], vec!['M', 'C', 'D'], vec!['P']],
            input.stacks
        );
        assert_eq!(
            vec![(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)],
            input.procedures
        );
    }

    #[test]
    fn test_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(part_1(input), "CMZ");
    }

    // #[test]
    // fn test_part_2() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!(part_2(&input), 4);
    // }
}
