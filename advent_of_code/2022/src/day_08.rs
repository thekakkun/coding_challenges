#![allow(unused)]

use std::collections::HashMap;

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

pub fn parse_file(f: &str) -> Vec<Vec<Tree>> {
    f.lines()
        .map(|line| {
            line.chars()
                .map(|c| Tree::new(c.to_digit(10).unwrap()))
                .collect()
        })
        .collect()
}

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

#[derive(Debug, Copy, Clone)]
struct Visibility {
    north: usize,
    south: usize,
    east: usize,
    west: usize,
}

pub fn part_2(input: &[Vec<Tree>]) -> usize {
    let mut proposed_trees: HashMap<(usize, usize), Visibility> = HashMap::new();

    let rows_iter = input.iter().enumerate();
    // loop through each row of trees
    for (row_ix, row) in rows_iter {
        let mut cols_iter = row.iter().enumerate();
        cols_iter.next();

        let mut proposed_tree_col = 0;
        let mut proposed_tree_visibility = Visibility {
            north: 0,
            south: 0,
            east: 0,
            west: 0,
        };

        // starting from the first tree, check visibility to the east
        for (col_ix, tree) in cols_iter {
            proposed_tree_visibility.east += 1;

            // visibility range limit to the east reached. check western view range from next proposed tree
            if row[proposed_tree_col].height <= tree.height {
                proposed_trees.insert((row_ix, proposed_tree_col), proposed_tree_visibility);

                let mut visibility_to_west = 0;
                for col in (0..col_ix).rev() {
                    visibility_to_west += 1;
                    if input[row_ix][col_ix].height <= input[row_ix][col].height {
                        break;
                    }
                }

                proposed_tree_visibility = Visibility {
                    north: 0,
                    south: 0,
                    east: 0,
                    west: visibility_to_west,
                };
                proposed_tree_col = col_ix;
            }
        }

        proposed_trees.insert((row_ix, proposed_tree_col), proposed_tree_visibility);
    }

    // proposed trees is the list trees with good east/west visibility.
    for ((proposed_row_ix, proposed_col_ix), mut visibility) in proposed_trees.iter_mut() {
        if visibility.east == 0 || visibility.west == 0 {
            continue;
        }

        for row_ix in (0..*proposed_row_ix).rev() {
            visibility.north += 1;
            if input[*proposed_row_ix][*proposed_col_ix].height
                <= input[row_ix][*proposed_col_ix].height
            {
                break;
            }
        }
        for row_ix in *proposed_row_ix + 1..input.len() {
            visibility.south += 1;
            if input[*proposed_row_ix][*proposed_col_ix].height
                <= input[row_ix][*proposed_col_ix].height
            {
                break;
            }
        }
    }

    proposed_trees
        .values()
        .map(|visibility| visibility.north * visibility.south * visibility.east * visibility.west)
        .max()
        .unwrap()
}

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

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(8, part_2(&input));
    }
}
