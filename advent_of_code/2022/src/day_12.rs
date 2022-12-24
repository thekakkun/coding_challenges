use std::{
    cell::RefCell,
    collections::{HashMap, VecDeque},
    ops::Deref,
    rc::Rc,
};

pub fn parse_file(f: &str) -> (Rc<RefCell<HillSquare>>, Rc<RefCell<HillSquare>>) {
    let mut graph = HashMap::new();
    let mut start = None;
    let mut end = None;

    for (row_ix, row) in f.lines().enumerate() {
        for (col_ix, val) in row.chars().enumerate() {
            let node = HillSquare::new(val, (row_ix, col_ix));
            if val == 'S' {
                start = Some(Rc::clone(&node));
            } else if val == 'E' {
                end = Some(Rc::clone(&node));
            }

            graph.insert((row_ix, col_ix), Rc::clone(&node));

            if 0 < row_ix {
                if let Some(node_to_north) = &graph.get(&(row_ix - 1, col_ix)) {
                    HillSquare::connect(Rc::clone(&node), Rc::clone(node_to_north));
                }
            }

            if 0 < col_ix {
                if let Some(node_to_west) = &graph.get(&(row_ix, col_ix - 1)) {
                    HillSquare::connect(Rc::clone(&node), Rc::clone(node_to_west));
                }
            }
        }
    }

    (
        start.expect("start node not found"),
        end.expect("end node not found"),
    )
}

pub fn part_1(input: (Rc<RefCell<HillSquare>>, Rc<RefCell<HillSquare>>)) -> usize {
    let (start, end) = input;
    let path = HillSquare::get_path(start, end);

    path.unwrap().len() - 1
}

// pub fn part_2(mut input: Barrel) -> u8 {

// }

type Coord = (usize, usize);

#[derive(Debug)]
enum Path {
    Unexplored,
    Start,
    Parent(Rc<RefCell<HillSquare>>),
}

#[derive(Debug)]
pub struct HillSquare {
    height: u8,
    coord: Coord,
    edges: Vec<Rc<RefCell<Self>>>,
    path: Path,
}

impl HillSquare {
    fn new(val: char, coord: Coord) -> Rc<RefCell<Self>> {
        let height = if val == 'S' {
            b'a'
        } else if val == 'E' {
            b'z'
        } else {
            val as u8
        };

        Rc::new(RefCell::new(Self {
            height,
            coord,
            edges: vec![],
            path: Path::Unexplored,
        }))
    }

    // check accessibility between nodes, and connect eligible edges
    fn connect(node_1: Rc<RefCell<Self>>, node_2: Rc<RefCell<Self>>) {
        if node_1.borrow().height.abs_diff(node_2.borrow().height) <= 1 {
            node_1.borrow_mut().edges.push(Rc::clone(&node_2));
            node_2.borrow_mut().edges.push(Rc::clone(&node_1));
        } else if node_1.deref().borrow().height < node_2.deref().borrow().height {
            node_2.borrow_mut().edges.push(Rc::clone(&node_1));
        } else if node_2.deref().borrow().height < node_1.deref().borrow().height {
            node_1.borrow_mut().edges.push(Rc::clone(&node_2));
        }
    }

    fn get_path(
        start_node: Rc<RefCell<HillSquare>>,
        end_node: Rc<RefCell<HillSquare>>,
    ) -> Result<Vec<Rc<RefCell<HillSquare>>>, &'static str> {
        let mut queue = VecDeque::from([Rc::clone(&start_node)]);
        start_node.borrow_mut().path = Path::Start;

        while let Some(node) = queue.pop_front() {
            if Rc::ptr_eq(&node, &end_node) {
                let mut path = vec![Rc::clone(&end_node)];
                let mut node = Rc::clone(&end_node);

                while let Path::Parent(next_node) = &node.clone().borrow().path {
                    path.push(Rc::clone(next_node));
                    node = Rc::clone(next_node);
                }

                path.reverse();
                return Ok(path);
            }

            for neighbor in &node.borrow().edges {
                let mut mut_neighbor = neighbor.borrow_mut();

                match mut_neighbor.path {
                    Path::Unexplored => {
                        mut_neighbor.path = Path::Parent(Rc::clone(&node));
                        queue.push_back(Rc::clone(neighbor));
                    }
                    _ => continue,
                }
            }
        }

        Err("Path not found")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_example() {
        let (start, end) = parse_file(EXAMPLE_FILE);

        // check start node
        assert_eq!((0, 0), start.borrow().coord);
        // connected to southern node
        assert!(start
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (1, 0)));
        // connected to eastern node
        assert!(start
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (0, 1)));

        // check end node
        assert_eq!((2, 5), end.borrow().coord);
        //not connected to northern node
        assert!(end
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (1, 5)));
        //not connected to southern node
        assert!(end
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (3, 5)));
        //connected to eastern node
        assert!(end
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (2, 4)));
        //not connected to western node
        assert!(end
            .borrow()
            .edges
            .iter()
            .map(|node| node.borrow().coord)
            .any(|x| x == (2, 6)));
    }

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(31, part_1(input))
    }

    // #[test]
    // fn example_part_2() {
    //     let input = parse_file(EXAMPLE_FILE);
    //     assert_eq!(2713310158, part_2(input))
    // }

    const EXAMPLE_FILE: &str = "\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
";
}
