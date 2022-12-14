use std::{cmp::Ordering, collections::HashSet, hash::Hash};

pub fn parse_file(f: &str) -> Bridge {
    Bridge::new(f)
}

pub fn part_1(bridge: &mut Bridge) -> usize {
    bridge.get_nth_knot(1).position_history_size()
}

pub fn part_2(bridge: &mut Bridge) -> usize {
    bridge.get_nth_knot(9).position_history_size()
}

pub struct Bridge {
    knots: Vec<Knot>,
}

impl Bridge {
    pub fn new(motions: &str) -> Self {
        let mut head_knot = Knot::new();
        motions
            .lines()
            .for_each(|line| head_knot.follow_motion(line));

        Self {
            knots: vec![head_knot],
        }
    }

    pub fn add_knot(&mut self) {
        let mut knot = Knot::new();
        let lead_knot = &self.knots.last().unwrap();

        lead_knot.position_history.iter().for_each(|position| {
            knot.move_towards(position);
        });

        self.knots.push(knot);
    }

    pub fn get_nth_knot(&mut self, knot_ix: usize) -> &Knot {
        while self.knots.get(knot_ix).is_none() {
            self.add_knot()
        }

        self.knots.get(knot_ix).unwrap()
    }
}

pub struct Knot {
    position_history: Vec<Coordinate>,
}

impl Knot {
    pub fn new() -> Self {
        Self {
            position_history: vec![Coordinate { x: 0, y: 0 }],
        }
    }

    pub fn follow_motion(&mut self, motion: &str) {
        let mut current_pos = *self.position_history.last().unwrap();

        if let Some((direction, steps)) = motion.split_once(' ') {
            (1..=steps.parse().unwrap()).for_each(|_| {
                match direction {
                    "R" => current_pos.x += 1,
                    "L" => current_pos.x -= 1,
                    "U" => current_pos.y += 1,
                    "D" => current_pos.y -= 1,
                    _ => panic!("Unknown direction: {direction}"),
                };
                self.position_history.push(current_pos)
            });
        };
    }

    pub fn move_towards(&mut self, position: &Coordinate) {
        let mut current_pos = *self.position_history.last().unwrap();

        while 1 < (position.x - current_pos.x).abs() || 1 < (position.y - current_pos.y).abs() {
            match (current_pos.x).cmp(&position.x) {
                Ordering::Less => current_pos.x += 1,
                Ordering::Equal => (),
                Ordering::Greater => current_pos.x -= 1,
            };
            match (current_pos.y).cmp(&position.y) {
                Ordering::Less => current_pos.y += 1,
                Ordering::Equal => (),
                Ordering::Greater => current_pos.y -= 1,
            };
            self.position_history.push(current_pos);
        }
    }

    pub fn position_history_size(&self) -> usize {
        let positions: HashSet<_> = self.position_history.iter().collect();
        positions.len()
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct Coordinate {
    x: i32,
    y: i32,
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE_1: &str = "\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
";

    const EXAMPLE_FILE_2: &str = "\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
";

    #[test]
    fn example_part_1() {
        let mut input = parse_file(EXAMPLE_FILE_1);
        assert_eq!(13, part_1(&mut input));
    }

    #[test]
    fn example_part_2_1() {
        let mut input = parse_file(EXAMPLE_FILE_1);
        assert_eq!(1, part_2(&mut input));
    }

    #[test]
    fn example_part_2_2() {
        let mut input = parse_file(EXAMPLE_FILE_2);
        assert_eq!(36, part_2(&mut input));
    }
}
