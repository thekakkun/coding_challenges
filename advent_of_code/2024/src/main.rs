use std::fs;

pub mod day_01;

fn main() {
    let input = fs::read_to_string("./input/day_01.txt").unwrap();

    let data = day_01::parse_part_1(&input);
    let part_1 = day_01::part_1(data);
    println!("{:?}", part_1)
}
