#[derive(Debug, Copy, Clone)]
pub struct Tree {
    height: u32,
    visible: bool,
}

impl Tree {
    fn new(height: u32) -> Self {
        Self {
            height,
            visible: false,
        }
    }
}

struct TreeMap {
    map: Vec<Vec<Tree>>,
}

// impl TreeMap {
//     fn get_directional_iterators(&self) {
//         let north_iter = (0..self.map[0].len()).map(|col| self.map.iter().map(move |row| row[col]));
//         let south_iter = (0..self.map[0].len())
//             .rev()
//             .map(|col| self.map.iter().rev().map(move |row| row[col]));
//         let west_iter = self.map.iter().map(|row| row.iter());
//         let east_iter = self.map.iter().rev().map(|row| row.iter().rev());

//         let foo = (north_iter, south_iter, west_iter, east_iter);
//     }
// }

pub fn parse_file(f: &str) -> Vec<Vec<Tree>> {
    f.lines()
        .map(|line| {
            line.chars()
                .map(|c| Tree::new(c.to_digit(10).unwrap()))
                .collect()
        })
        .collect()
}

// pub fn part_1(input: &mut Vec<Vec<Tree>>) -> usize {
//     let mut max_from_west = vec![(0, -1); input.len()];
//     let mut max_from_north = vec![(0, -1); input[0].len()];

//     for (row_ix, row) in input.iter_mut().enumerate() {
//         for (col_ix, tree) in row.iter_mut().enumerate() {
//             let (_, max_in_row) = max_from_west[row_ix];

//             if max_in_row < tree.height.try_into().unwrap() {
//                 // tree is tallest we've seen in row, update data
//                 max_from_west[row_ix] = (col_ix, tree.height.try_into().unwrap());
//                 tree.visible = true;
//             }

//             let (_, max_in_col) = max_from_north[col_ix];
//             if max_in_col < tree.height.try_into().unwrap() {
//                 // tree is tallest we've seen in row, update data
//                 max_from_north[col_ix] = (row_ix, tree.height.try_into().unwrap());
//                 tree.visible = true;
//             }
//         }
//     }

//     let mut max_from_east = vec![(0, -1); input.len()];
//     let mut max_from_south = vec![(0, -1); input[0].len()];

//     for (row_ix, row) in input.iter_mut().enumerate().rev() {
//         for (col_ix, tree) in row.iter_mut().enumerate().rev() {
//             let (_, max_in_row) = max_from_east[row_ix];
//             if max_in_row < tree.height.try_into().unwrap() {
//                 // tree is tallest we've seen in row, update data
//                 max_from_east[row_ix] = (col_ix, tree.height.try_into().unwrap());
//                 tree.visible = true;
//             }

//             let (_, max_in_col) = max_from_south[col_ix];
//             if max_in_col < tree.height.try_into().unwrap() {
//                 // tree is tallest we've seen in row, update data
//                 max_from_south[col_ix] = (row_ix, tree.height.try_into().unwrap());
//                 tree.visible = true;
//             }
//         }
//     }

//     input.iter().flatten().filter(|tree| tree.visible).count()
// }

pub fn part_1(input: &[Vec<Tree>]) -> usize {
    let mut visibility_map = input.to_owned();

    // Loop through rows
    let mut max_from_west = vec![-1; input.len()];
    let mut max_from_east = vec![-1; input.len()];
    for (row_ix, row) in visibility_map.iter_mut().enumerate() {
        // check trees from west
        for tree in row.iter_mut() {
            if max_from_west[row_ix] < tree.height as i32 {
                tree.visible = true;
                max_from_west[row_ix] = tree.height as i32;

                if tree.height == 9 {
                    break;
                }
            }
        }

        // check trees from east
        for tree in row.iter_mut().rev() {
            if max_from_east[row_ix] < tree.height as i32 {
                tree.visible = true;
                max_from_east[row_ix] = tree.height as i32;

                if tree.height as i32 == max_from_west[row_ix] {
                    break;
                }
            }
        }
    }

    // loop through columns
    let mut max_from_north = vec![-1; input[0].len()];
    let mut max_from_south = vec![-1; input[0].len()];
    for (col_ix, _) in input[0].iter().enumerate() {
        // check trees from north
        for tree in visibility_map.iter_mut().map(|row| &mut row[col_ix]) {
            if max_from_north[col_ix] < tree.height as i32 {
                tree.visible = true;
                max_from_north[col_ix] = tree.height as i32;

                if tree.height == 9 {
                    break;
                }
            }
        }

        // check trees from south
        for tree in visibility_map.iter_mut().rev().map(|row| &mut row[col_ix]) {
            if max_from_south[col_ix] < tree.height as i32 {
                tree.visible = true;
                max_from_south[col_ix] = tree.height as i32;

                if tree.height as i32 == max_from_north[col_ix] {
                    break;
                }
            }
        }
    }

    visibility_map
        .iter()
        .flatten()
        .filter(|tree| tree.visible)
        .count()
}

// pub fn part_2() -> i32 {}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
30373
25512
65332
33549
35390
";

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(21, part_1(&input));
    }

    // #[test]
    // fn example_part_2() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!(24933642, part_2(input, 70000000, 30000000));
    // }
}
