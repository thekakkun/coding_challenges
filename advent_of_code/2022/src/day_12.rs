use std::{
    cell::RefCell,
    collections::{HashMap, VecDeque},
    rc::Rc,
};

pub fn parse_file(f: &str) -> (RR<Node>, RR<Node>) {
    let mut graph = HashMap::new();
    let mut start = None;
    let mut end = None;

    for (row_ix, row) in f.lines().enumerate() {
        for (col_ix, val) in row.chars().enumerate() {
            let node = Node::new(val, (row_ix, col_ix));
            if val == 'S' {
                start = Some(Rc::clone(&node));
            } else if val == 'E' {
                end = Some(Rc::clone(&node));
            }

            graph.insert((row_ix, col_ix), Rc::clone(&node));

            if 0 < row_ix {
                if let Some(node_to_north) = &graph.get(&(row_ix - 1, col_ix)) {
                    Node::connect(&node, node_to_north);
                }
            }

            if 0 < col_ix {
                if let Some(node_to_west) = &graph.get(&(row_ix, col_ix - 1)) {
                    Node::connect(&node, node_to_west);
                }
            }
        }
    }

    (
        start.expect("start node not found"),
        end.expect("end node not found"),
    )
}

pub fn part_1(input: (RR<Node>, RR<Node>)) -> usize {
    let (start, end) = input;

    let path = Node::get_path(
        start,
        |src, dst| dst.borrow().height as i8 - src.borrow().height as i8 <= 1,
        |node| Rc::ptr_eq(node, &end),
    );

    path.unwrap().len() - 1
}

pub fn part_2(input: (RR<Node>, RR<Node>)) -> usize {
    let (_, end) = input;

    let path = Node::get_path(
        end,
        |src, dst| src.borrow().height as i8 - dst.borrow().height as i8 <= 1,
        |node| node.borrow().height == b'a',
    );

    path.unwrap().len() - 1
}

type Coord = (usize, usize);
type RR<T> = Rc<RefCell<T>>;

#[derive(Debug)]
enum Path {
    Unexplored,
    Start,
    Parent(RR<Node>),
}

#[derive(Debug)]
pub struct Node {
    height: u8,
    coord: Coord,
    edges: Vec<RR<Self>>,
    path: Path,
}

impl Node {
    fn new(val: char, coord: Coord) -> RR<Self> {
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

    fn connect(node_1: &RR<Self>, node_2: &RR<Self>) {
        node_1.borrow_mut().edges.push(Rc::clone(node_2));
        node_2.borrow_mut().edges.push(Rc::clone(node_1));
    }

    fn get_path(
        start_node: RR<Node>,
        is_accessible: impl Fn(&RR<Node>, &RR<Node>) -> bool, // takes src and dst node, tests for accessibility.
        is_end: impl Fn(&RR<Node>) -> bool,
    ) -> Result<Vec<RR<Node>>, &'static str> {
        let mut queue = VecDeque::from([Rc::clone(&start_node)]);
        start_node.borrow_mut().path = Path::Start;

        while let Some(node) = queue.pop_front() {
            if is_end(&node) {
                let mut path = vec![Rc::clone(&node)];
                let mut node = Rc::clone(&node);

                while let Path::Parent(next_node) = &node.clone().borrow().path {
                    path.push(Rc::clone(next_node));
                    node = Rc::clone(next_node);
                }

                path.reverse();
                return Ok(path);
            }

            for neighbor in node
                .borrow()
                .edges
                .iter()
                .filter(|&neighbor| is_accessible(&node, neighbor))
            {
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

        // check end node
        assert_eq!((2, 5), end.borrow().coord);
    }

    #[test]
    fn example_part_1() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(31, part_1(input))
    }

    #[test]
    fn example_part_2() {
        let input = parse_file(EXAMPLE_FILE);
        assert_eq!(29, part_2(input))
    }

    const EXAMPLE_FILE: &str = "\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
";
}
