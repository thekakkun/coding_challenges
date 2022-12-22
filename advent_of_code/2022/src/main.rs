use std::{fs, process, time::Instant};

mod day_01;
mod day_02;
mod day_03;
mod day_04;
mod day_05;
mod day_06;
mod day_07;
mod day_08;
mod day_09;
mod day_10;
mod day_11;

fn main() {
    let f = fs::read_to_string("./input/day_11.txt").unwrap_or_else(|err| {
        eprintln! {"Problem reading file: {err}"};
        process::exit(1)
    });

    let start = Instant::now();
    let input = day_11::parse_file(&f);
    let parse_file_split = Instant::now();
    println!(
        "Parsed input file in {:?}",
        parse_file_split.duration_since(start)
    );

    let part_1_result = day_11::part_1(input);
    let part_1_split = Instant::now();
    println!(
        "Part 1: {} in {:?}",
        part_1_result,
        part_1_split.duration_since(parse_file_split)
    );

    let input = day_11::parse_file(&f);
    let part_1_split = Instant::now();

    let part_2_result = day_11::part_2(input);
    let done = Instant::now();
    println!(
        "Part 2: {} in {:?}",
        part_2_result,
        done.duration_since(part_1_split)
    );
}
