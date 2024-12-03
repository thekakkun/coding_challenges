type ParsedData = Vec<Vec<i32>>;

pub fn parse_part_1(input: &str) -> ParsedData {
    input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|val| val.parse().unwrap())
                .collect()
        })
        .collect()
}

fn is_valid(report: &Vec<i32>) -> bool {
    let mut comparator: Option<fn(&i32, &i32) -> bool> = None;

    let mut report_iter = report.windows(2);
    report_iter.all(|vals: &[i32]| {
        if let [val_1, val_2] = vals {
            // Check increase/decrese tolerance
            if !(1..4 ).contains(&val_1.abs_diff(*val_2)) {
                return false;
            }

            // Check direction
            if let Some(op) = comparator {
                return op(val_1, val_2);
            } else {
                comparator = match val_1.cmp(val_2) {
                    std::cmp::Ordering::Less => Some(PartialOrd::lt),
                    std::cmp::Ordering::Greater => Some(PartialOrd::gt),
                    std::cmp::Ordering::Equal => return false,
                };
                return true;
            }
        }
        false
    })
}

pub fn solve_part_1(data: ParsedData) -> usize {
    data.iter().filter(|&report| is_valid(report)).count()
}

#[cfg(test)]
mod tests {
    use crate::day_02::is_valid;

    #[test]
    fn decreasing_gradually() {
        let report = vec![7, 6, 4, 2, 1];
        assert!(is_valid(&report));
    }

    #[test]
    fn increacing_rapidly() {
        let report = vec![1, 2, 7, 8, 9];
        assert!(!is_valid(&report));
    }

    #[test]
    fn decreasing_rapidly() {
        let report = vec![9, 7, 6, 2, 1];
        assert!(!is_valid(&report));
    }

    #[test]
    fn inconsistent_direction() {
        let report = vec![1, 3, 2, 4, 5];
        assert!(!is_valid(&report));
    }

    #[test]
    fn flat() {
        let report = vec![8, 6, 4, 4, 15];
        assert!(!is_valid(&report));
    }

    #[test]
    fn increasing_gradually() {
        let report = vec![1, 3, 6, 7, 9];
        assert!(!is_valid(&report));
    }
}
