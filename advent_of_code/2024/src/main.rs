use std::fs;

pub mod day_01;
pub mod day_02;

fn main() {
    let input = fs::read_to_string("./input/day_02.txt").unwrap();

    let data_1 = day_02::parse_part_1(&input);
    let result_1 = day_02::solve_part_1(data_1);
    println!("{:?}", result_1);

    // let data_2 = day_01::parse_part_2(&input);
    // let result_2 = day_01::solve_part_2(data_2);
    // println!("{:?}", result_2);
}
