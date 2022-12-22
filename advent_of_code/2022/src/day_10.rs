#![allow(unused)]

pub fn parse_file(f: &str) -> impl Iterator<Item = (i32, i32)> + '_ {
    let instructions = f.lines().filter_map(|line| match line.split_once(' ') {
        None if line == "noop" => Some(Instruction::Noop),
        Some(("addx", value)) => Some(Instruction::AddX(value.parse().unwrap())),
        _ => None,
    });

    let mut cycle = 1;
    let mut register = 1;

    instructions.flat_map(move |instruction| {
        let mut instruction_result = Vec::new();

        let add_to_register = match instruction {
            Instruction::Noop => {
                (0..1).for_each(|_| {
                    instruction_result.push((cycle, register));
                    cycle += 1
                });
                0
            }
            Instruction::AddX(val) => {
                (0..2).for_each(|_| {
                    instruction_result.push((cycle, register));
                    cycle += 1
                });
                val
            }
        };

        // instruction execution complete, update register
        register += add_to_register;

        // return list of during-cycle values
        instruction_result
    })
}

pub fn part_1(input: impl Iterator<Item = (i32, i32)>) -> i32 {
    input
        .filter_map(|(cycle, register)| {
            if (cycle - 20) % 40 == 0 {
                Some(cycle * register)
            } else {
                None
            }
        })
        .sum()
}

pub fn part_2(input: impl Iterator<Item = (i32, i32)>) -> String {
    const DISPLAY_COLS: i32 = 40;
    let mut result = String::from("\n");

    input.for_each(|(cycle, register)| {
        let pixel_loc = (cycle - 1) % DISPLAY_COLS;
        if register - 1 <= pixel_loc && pixel_loc <= register + 1 {
            result.push('#');
        } else {
            result.push('.');
        }

        if cycle % DISPLAY_COLS == 0 {
            result.push('\n');
        }
    });

    result
}

pub enum Instruction {
    Noop,
    AddX(i32),
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(13140, part_1(input));
    }

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(
            "
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
",
            part_2(input)
        );
    }

    const EXAMPLE_FILE: &str = "\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
";
}
