use std::{fs, process};

mod day_01;

fn main() {
    let f = fs::read_to_string("./input/day_01.txt").unwrap_or_else(|err| {
        eprintln! {"Problem reading file: {err}"};
        process::exit(1)
    });

    let input = day_01::parse_input(f);

    println!("Part 1: {}", day_01::part_1(&input));
    println!("Part 2: {}", day_01::part_2(&input));
}
