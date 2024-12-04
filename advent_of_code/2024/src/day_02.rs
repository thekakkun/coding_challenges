use std::{iter, ops::RangeInclusive};

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

fn is_valid(report: &Vec<i32>, mut allowed_range: Option<RangeInclusive<i32>>) -> bool {
    let mut report_iter = report.windows(2);
    report_iter.all(|vals: &[i32]| {
        if let [v_1, v_2] = vals {
            if let Some(range) = &allowed_range {
                return range.contains(&(v_1 - v_2));
            } else {
                allowed_range = match v_1.cmp(v_2) {
                    std::cmp::Ordering::Less if (-3..=-1).contains(&(v_1 - v_2)) => Some(-3..=-1),
                    std::cmp::Ordering::Greater if (1..=3).contains(&(v_1 - v_2)) => Some(1..=3),
                    _ => return false,
                };

                return allowed_range.as_ref().unwrap().contains(&(v_1 - v_2));
            }
        }
        false
    })
}

pub fn solve_part_1(data: ParsedData) -> usize {
    data.iter().filter(|&report| is_valid(report, None)).count()
}

pub fn parse_part_2(input: &str) -> ParsedData {
    parse_part_1(input)
}

fn is_valid_with_dampener(report: &Vec<i32>) -> bool {
    let mut allowed_range: Option<RangeInclusive<_>> = None;

    let mut report_iter = report.iter();
    let mut val_1 = report_iter.next();
    let mut val_2 = report_iter.next();

    let mut lookback: Option<&i32> = None;

    loop {
        if let None = val_2 {
            return true;
        }

        if let (Some(&v_1), Some(&v_2)) = (val_1, val_2) {
            if let Some(ref range) = allowed_range {
                if range.contains(&(v_1 - v_2)) {
                } else {
                    return is_valid(
                        &iter::once(v_1)
                            .chain(report_iter.clone().cloned())
                            .collect(),
                        allowed_range.clone(),
                    ) || match lookback {
                        Some(&lb) => is_valid(
                            &iter::once(lb)
                                .chain(iter::once(v_2))
                                .chain(report_iter.cloned())
                                .collect(),
                            allowed_range,
                        ),
                        None => is_valid(
                            &iter::once(v_2).chain(report_iter.cloned()).collect(),
                            allowed_range,
                        ),
                    };
                }
            } else {
                match v_1.cmp(&v_2) {
                    std::cmp::Ordering::Less if (-3..=-1).contains(&(v_1 - v_2)) => {
                        allowed_range = Some(-3..=-1);
                    }
                    std::cmp::Ordering::Greater if (1..=3).contains(&(v_1 - v_2)) => {
                        allowed_range = Some(1..=3);
                    }
                    _ => {
                        return {
                            is_valid(
                                &iter::once(v_1)
                                    .chain(report_iter.clone().cloned())
                                    .collect(),
                                None,
                            ) || match lookback {
                                Some(&lb) => is_valid(
                                    &iter::once(lb)
                                        .chain(iter::once(v_2))
                                        .chain(report_iter.cloned())
                                        .collect(),
                                    None,
                                ),
                                None => is_valid(
                                    &iter::once(v_2).chain(report_iter.cloned()).collect(),
                                    None,
                                ),
                            }
                        }
                    }
                }
            }

            lookback = val_1;
            val_1 = val_2;
            val_2 = report_iter.next();
            continue;
        }
    }
}

pub fn solve_part_2(data: ParsedData) -> usize {
    data.iter()
        .filter(|&report| is_valid_with_dampener(report))
        .count()
}

#[cfg(test)]
mod part_1_tests {
    use crate::day_02::is_valid;

    #[test]
    fn decreasing_gradually() {
        let report = vec![7, 6, 4, 2, 1];
        assert!(is_valid(&report, None));
    }

    #[test]
    fn increacing_rapidly() {
        let report = vec![1, 2, 7, 8, 9];
        assert!(!is_valid(&report, None));
    }

    #[test]
    fn decreasing_rapidly() {
        let report = vec![9, 7, 6, 2, 1];
        assert!(!is_valid(&report, None));
    }

    #[test]
    fn inconsistent_direction() {
        let report = vec![1, 3, 2, 4, 5];
        assert!(!is_valid(&report, None));
    }

    #[test]
    fn flat() {
        let report = vec![8, 6, 4, 4, 1];
        assert!(!is_valid(&report, None));
    }

    #[test]
    fn increasing_gradually() {
        let report = vec![1, 3, 6, 7, 9];
        assert!(is_valid(&report, None));
    }
}

#[cfg(test)]
mod part_2_tests {
    use crate::day_02::is_valid_with_dampener;

    #[test]
    fn decreasing_gradually() {
        let report = vec![7, 6, 4, 2, 1];
        assert!(is_valid_with_dampener(&report));
    }

    #[test]
    fn increacing_rapidly() {
        let report = vec![1, 2, 7, 8, 9];
        assert!(!is_valid_with_dampener(&report));
    }

    #[test]
    fn decreasing_rapidly() {
        let report = vec![9, 7, 6, 2, 1];
        assert!(!is_valid_with_dampener(&report));
    }

    #[test]
    fn inconsistent_direction() {
        let report = vec![1, 3, 2, 4, 5];
        assert!(is_valid_with_dampener(&report));
    }

    #[test]
    fn flat() {
        let report = vec![8, 6, 4, 4, 1];
        assert!(is_valid_with_dampener(&report));
    }

    #[test]
    fn increasing_gradually() {
        let report = vec![1, 3, 6, 7, 9];
        assert!(is_valid_with_dampener(&report));
    }
}
