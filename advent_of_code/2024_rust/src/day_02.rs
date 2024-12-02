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

fn is_inc_or_dec(report: &Vec<i32>) -> bool {
    let mut report_iter = report.windows(2);

    if let Some([val_1, val_2]) = report_iter.next() {
        let op = match val_1.cmp(val_2) {
            std::cmp::Ordering::Less => PartialOrd::lt,
            std::cmp::Ordering::Greater => PartialOrd::gt,
            std::cmp::Ordering::Equal => return false,
        };

        report_iter.all(|vals| {
            if let [val_1, val_2] = vals {
                op(val_1, val_2)
            } else {
                false
            }
        })
    } else {
        return false;
    }
}

pub fn solve_part_1(data: ParsedData) -> i32 {

    // data.iter().map((|report| {

    // }))
}
