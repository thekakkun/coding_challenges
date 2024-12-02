use std::{collections::HashMap, iter::zip};

pub fn parse_part_1(input: &str) -> (Vec<i32>, Vec<i32>) {
    let mut left = Vec::new();
    let mut right = Vec::new();

    input.lines().for_each(|line| {
        let (l, r) = line.split_once("   ").unwrap();
        left.push(l.parse().unwrap());
        right.push(r.parse().unwrap());
    });

    (left, right)
}

pub fn solve_part_1((mut left, mut right): (Vec<i32>, Vec<i32>)) -> i32 {
    left.sort();
    right.sort();

    zip(left, right).map(|(l, r)| (l - r).abs()).sum()
}

pub fn parse_part_2(input: &str) -> (Vec<i32>, Vec<i32>) {
    parse_part_1(input)
}

pub fn solve_part_2((left, right): (Vec<i32>, Vec<i32>)) -> i32 {
    let mut counter: HashMap<i32, i32> = HashMap::new();

    right.into_iter().for_each(|val| {
        *counter.entry(val).or_insert(0) += 1;
    });
    left.iter()
        .map(|val| val * counter.get(&val).unwrap_or(&0))
        .sum()
}
