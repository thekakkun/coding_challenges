use std::{
    cell::RefCell,
    collections::VecDeque,
    ops::{Add, Mul},
};

use regex::Regex;

pub fn parse_file(f: &str) -> Barrel {
    let re = Regex::new(
        r"(?m)Monkey (?P<id>\d+):$
  Starting items: (?P<items>.*)$
  Operation: new = old (?P<operator>[\+\-\*/]) (?P<operand>(?:old|\d+))$
  Test: divisible by (?P<modulus>\d*)$
    If true: throw to monkey (?P<t_target>\d+)$
    If false: throw to monkey (?P<f_target>\d+)$",
    )
    .unwrap();

    Barrel::new(
        re.captures_iter(f)
            .map(|cap| {
                let items = cap
                    .name("items")
                    .unwrap()
                    .as_str()
                    .split(", ")
                    .map(|worry| worry.parse().expect("unable to parse value"))
                    .collect();

                let operator = match cap.name("operator").unwrap().as_str() {
                    "+" => Add::add,
                    "*" => Mul::mul,
                    op => panic!("unknown operator: {op}"),
                };
                let operand = cap.name("operand").unwrap().as_str().parse().ok();

                let modulus = cap
                    .name("modulus")
                    .unwrap()
                    .as_str()
                    .parse()
                    .expect("unable to parse modulus");
                let target = (
                    cap.name("t_target")
                        .unwrap()
                        .as_str()
                        .parse()
                        .expect("unable to parse t_target"),
                    cap.name("f_target")
                        .unwrap()
                        .as_str()
                        .parse()
                        .expect("unable to parse f_target"),
                );

                Monkey::new(items, operator, operand, modulus, target)
            })
            .collect(),
    )
}

pub fn part_1(mut input: Barrel) -> u64 {
    (0..20).for_each(|_| input.do_round(|worry| worry / 3));
    input.get_monkey_business()
}

pub fn part_2(mut input: Barrel) -> u64 {
    let common_mod: u64 = input
        .monkeys
        .iter()
        .map(|monkey| monkey.modulus as u64)
        .product();

    (0..10000).for_each(|_| input.do_round(|worry| worry % common_mod));

    input.get_monkey_business()
}

pub struct Barrel {
    monkeys: Vec<Monkey>,
    inspection_count: Vec<u64>,
}

impl Barrel {
    pub fn new(monkeys: Vec<Monkey>) -> Self {
        Self {
            inspection_count: vec![0; monkeys.len()],
            monkeys,
        }
    }

    pub fn do_round(&mut self, worry_manager: impl Fn(u64) -> u64) {
        for (id, monkey) in self.monkeys.iter().enumerate() {
            while let Some(worry) = monkey.items.borrow_mut().pop_front() {
                self.inspection_count[id] += 1;

                let new_worry = worry_manager((monkey.operator)(
                    worry,
                    match monkey.operand {
                        Some(operand) => operand.into(),
                        None => worry,
                    },
                ));

                let target = if new_worry % monkey.modulus as u64 == 0 {
                    monkey.target.0
                } else {
                    monkey.target.1
                };

                self.monkeys[target].items.borrow_mut().push_back(new_worry);
            }
        }
    }

    pub fn get_monkey_business(&mut self) -> u64 {
        self.inspection_count.sort();

        self.inspection_count[self.monkeys.len() - 1]
            * self.inspection_count[self.monkeys.len() - 2]
    }
}

pub struct Monkey {
    items: RefCell<VecDeque<u64>>,
    operator: Box<dyn Fn(u64, u64) -> u64>,
    operand: Option<u8>,
    modulus: u8,
    target: (usize, usize),
}

impl Monkey {
    pub fn new(
        items: Vec<u64>,
        operator: impl Fn(u64, u64) -> u64 + 'static,
        operand: Option<u8>,
        modulus: u8,
        target: (usize, usize),
    ) -> Self {
        Self {
            items: RefCell::new(items.into()),
            operator: Box::new(operator),
            operand,
            modulus,
            target,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_example() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(4, input.monkeys.len());
        assert_eq!(*input.monkeys[0].items.borrow(), [79, 98]);
        assert_eq!(*input.monkeys[1].items.borrow(), [54, 65, 75, 74]);
    }

    #[test]
    fn part_1_operation() {
        let mut input = parse_file(EXAMPLE_FILE);
        let worry_manager = |worry| worry / 3;

        input.do_round(worry_manager);
        assert_eq!(*input.monkeys[0].items.borrow(), [20, 23, 27, 26]);
        assert_eq!(
            *input.monkeys[1].items.borrow(),
            [2080, 25, 167, 207, 401, 1046]
        );

        input.do_round(worry_manager);
        assert_eq!(*input.monkeys[0].items.borrow(), [695, 10, 71, 135, 350]);
    }

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(10605, part_1(input))
    }

    #[test]
    fn part_2_operation() {
        let mut input = parse_file(EXAMPLE_FILE);
        let common_mod: u64 = input
            .monkeys
            .iter()
            .map(|monkey| -> u64 { monkey.modulus.into() })
            .product();
        let worry_manager = |worry| worry % common_mod;

        input.do_round(worry_manager);
        assert_eq!(input.inspection_count, [2, 4, 3, 6]);

        input = parse_file(EXAMPLE_FILE);
        (1..=20).for_each(|_| input.do_round(worry_manager));
        assert_eq!(input.inspection_count, [99, 97, 8, 103]);
    }

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(2713310158, part_2(input))
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
