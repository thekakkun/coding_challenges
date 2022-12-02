use std::{fs, process, time::Instant};

mod day_01;
mod day_02;

fn main() {
    let f = fs::read_to_string("./input/day_02.txt").unwrap_or_else(|err| {
        eprintln! {"Problem reading file: {err}"};
        process::exit(1)
    });

    let input = day_02::parse_input(&f);

    let start = Instant::now();

    let part_1_result = day_02::part_1(&input);
    let split = Instant::now();
    println!(
        "Part 1: {} in {:?}",
        part_1_result,
        split.duration_since(start)
    );

    let part_2_result = day_02::part_2(&input);
    let done = Instant::now();
    println!(
        "Part 2: {} in {:?}",
        part_2_result,
        done.duration_since(split)
    );
}
