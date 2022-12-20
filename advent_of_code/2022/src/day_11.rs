use std::{cell::RefCell, collections::VecDeque};

use regex::Regex;

pub fn parse_file(f: &str) -> Barrel {
    let re = Regex::new(
        r"(?m)Monkey (?P<id>\d+):$
  Starting items: (?P<items>.*)$
  Operation: new = old (?P<operator>[\+\-\*/]) (?P<operand>(?:old|\d+))$
  Test: divisible by (?P<test>\d*)$
    If true: throw to monkey (?P<t_target>\d+)$
    If false: throw to monkey (?P<f_target>\d+)$",
    )
    .unwrap();

    Barrel::new(
        re.captures_iter(f)
            .map(|cap| {
                Monkey::from_str(
                    cap.name("items").unwrap().as_str(),
                    (
                        cap.name("operator").unwrap().as_str(),
                        cap.name("operand").unwrap().as_str(),
                    ),
                    (
                        cap.name("test").unwrap().as_str(),
                        cap.name("t_target").unwrap().as_str(),
                        cap.name("f_target").unwrap().as_str(),
                    ),
                )
            })
            .collect(),
    )
}

pub fn part_1(mut input: Barrel) -> u32 {
    (0..20).for_each(|_| input.do_round());

    input.inspection_count.sort();
    input.inspection_count.iter().rev().take(2).product()
}
pub fn part_2(mut input: Barrel) -> u32 {
    (0..10000).for_each(|_| input.do_round());

    input.inspection_count.sort();
    input.inspection_count.iter().rev().take(2).product()
}

pub struct Barrel {
    monkeys: Vec<Monkey>,
    inspection_count: Vec<u32>,
}

impl Barrel {
    pub fn new(monkeys: Vec<Monkey>) -> Self {
        Self {
            inspection_count: vec![0; monkeys.len()],
            monkeys,
        }
    }

    pub fn do_round(&mut self) {
        for (id, monkey) in self.monkeys.iter().enumerate() {
            while let Some(item) = monkey.items.borrow_mut().pop_front() {
                let new_val = (monkey.operation)(item);
                let target = (monkey.throw_to)(new_val);

                self.inspection_count[id] += 1;

                self.monkeys[target].items.borrow_mut().push_back(new_val);
            }
        }
    }
}

pub struct Monkey {
    items: RefCell<VecDeque<u32>>,
    operation: Box<dyn Fn(u32) -> u32>,
    throw_to: Box<dyn Fn(u32) -> usize>,
}

impl Monkey {
    pub fn from_str(
        items: &str,
        (op, operand): (&str, &str),
        (test, t_target, f_target): (&str, &str, &str),
    ) -> Self {
        Self {
            items: RefCell::new(Monkey::items_from_str(items)),
            operation: Box::new(Monkey::operation_from_str(op, operand)),
            throw_to: Box::new(Monkey::throw_to_from_str(test, t_target, f_target)),
        }
    }

    fn items_from_str(items: &str) -> VecDeque<u32> {
        items
            .split(", ")
            .map(|item| item.parse().unwrap())
            .collect()
    }

    fn operation_from_str(operator: &str, operand: &str) -> impl Fn(u32) -> u32 {
        let operator = operator.to_owned();
        let operand = operand.to_owned();

        move |val| {
            let new_val = if let Ok(num) = operand.parse::<u32>() {
                match operator.as_str() {
                    "+" => val + num,
                    "*" => val * num,
                    _ => panic!("unknown operator: {operator}"),
                }
            } else if operator == "*" && operand == "old" {
                val * val
            } else {
                panic!("unable to parse operation: {operator} {operand}");
            };

            new_val / 3
        }
    }

    fn throw_to_from_str(test: &str, t_target: &str, f_target: &str) -> impl Fn(u32) -> usize {
        if let (Ok(test), Ok(t_target), Ok(f_target)) =
            (test.parse::<u32>(), t_target.parse(), f_target.parse())
        {
            move |val| {
                if val % test == 0 {
                    t_target
                } else {
                    f_target
                }
            }
        } else {
            panic!("unable to parse throwing rules")
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_example() {
        let mut input = parse_file(EXAMPLE_FILE);
        assert_eq!(4, input.monkeys.len());
        assert_eq!(*input.monkeys[0].items.borrow(), [79, 98]);

        input.do_round();
        assert_eq!(*input.monkeys[0].items.borrow(), [20, 23, 27, 26]);
        assert_eq!(
            *input.monkeys[1].items.borrow(),
            [2080, 25, 167, 207, 401, 1046]
        );

        input.do_round();
        assert_eq!(*input.monkeys[0].items.borrow(), [695, 10, 71, 135, 350]);
    }

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(10605, part_1(input));
    }

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(2713310158, part_2(input));
    }

    const EXAMPLE_FILE: &str = "\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
";
}
