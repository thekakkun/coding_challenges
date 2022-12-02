use std::{fs, process, time::Instant};

mod day_01;

fn main() {
    let f = fs::read_to_string("./input/day_01.txt").unwrap_or_else(|err| {
        eprintln! {"Problem reading file: {err}"};
        process::exit(1)
    });

    let input = day_01::parse_input(&f);

    let start = Instant::now();

    let part_1_result = day_01::part_1(input);
    let part_1_done = Instant::now();
    println!(
        "Part 1: {} in {:?}",
        part_1_result,
        part_1_done.duration_since(start)
    );

    let part_2_result = day_01::part_2(input, 3);
    let part_2_done = Instant::now();
    println!(
        "Part 1: {} in {:?}",
        part_2_result,
        part_2_done.duration_since(start)
    );
}
