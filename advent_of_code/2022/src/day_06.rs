pub fn parse_file(f: &str) -> &str {
    f
}

fn find_marker(input: &str, seq_size: usize) -> usize {
    let mut seq_start = 0;
    let mut c_loc = 1;

    loop {
        let seq = &input[seq_start..c_loc];
        let next_char = &input.chars().nth(c_loc).unwrap();

        match seq.find(*next_char) {
            // if next_char is found in seq, skip ahead so seq doesn't contain duplicate chars
            Some(i) => {
                seq_start += i + 1;
                c_loc = seq_start + 1;
                continue;
            }
            // make sure seq.len() is at least seq_size
            None => {
                if seq.len() + 1 < seq_size {
                    c_loc += 1;
                    continue;
                }
            }
        }

        return c_loc + 1;
    }
}

pub fn part_1(input: &str) -> usize {
    find_marker(input, 4)
}

pub fn part_2(input: &str) -> usize {
    find_marker(input, 14)
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE_1: &str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb";
    const EXAMPLE_FILE_2: &str = "bvwbjplbgvbhsrlpgdmjqwftvncz";
    const EXAMPLE_FILE_3: &str = "nppdvjthqldpwncqszvftbrmjlhg";
    const EXAMPLE_FILE_4: &str = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
    const EXAMPLE_FILE_5: &str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";

    #[test]
    fn test_part_1_1() {
        let input_1 = parse_file(EXAMPLE_FILE_1);
        assert_eq!(7, part_1(input_1));
    }
    #[test]
    fn test_part_1_2() {
        let input_2 = parse_file(EXAMPLE_FILE_2);
        assert_eq!(5, part_1(input_2));
    }
    #[test]
    fn test_part_1_3() {
        let input_3 = parse_file(EXAMPLE_FILE_3);
        assert_eq!(6, part_1(input_3));
    }
    #[test]
    fn test_part_1_4() {
        let input_4 = parse_file(EXAMPLE_FILE_4);
        assert_eq!(10, part_1(input_4));
    }
    #[test]
    fn test_part_1_5() {
        let input_5 = parse_file(EXAMPLE_FILE_5);
        assert_eq!(11, part_1(input_5));
    }

    #[test]
    fn test_part_2_1() {
        let input_1 = parse_file(EXAMPLE_FILE_1);
        assert_eq!(19, part_2(input_1));
    }
    #[test]
    fn test_part_2_2() {
        let input_2 = parse_file(EXAMPLE_FILE_2);
        assert_eq!(23, part_2(input_2));
    }
    #[test]
    fn test_part_2_3() {
        let input_3 = parse_file(EXAMPLE_FILE_3);
        assert_eq!(23, part_2(input_3));
    }
    #[test]
    fn test_part_2_4() {
        let input_4 = parse_file(EXAMPLE_FILE_4);
        assert_eq!(29, part_2(input_4));
    }
    #[test]
    fn test_part_2_5() {
        let input_5 = parse_file(EXAMPLE_FILE_5);
        assert_eq!(26, part_2(input_5));
    }
}
