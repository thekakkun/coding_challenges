pub fn parse_input(f: &str) -> Vec<Vec<&str>> {
    f.lines()
        .map(|line| line.split_whitespace().collect())
        .collect()
}

enum Hand {
    Rock,
    Paper,
    Scissors,
}

impl Hand {
    fn from_str(input: &str) -> Result<Hand, &str> {
        match input {
            "X" | "A" => Ok(Hand::Rock),
            "Y" | "B" => Ok(Hand::Paper),
            "Z" | "C" => Ok(Hand::Scissors),
            _ => Err("Unknown play"),
        }
    }

    fn value(&self) -> i32 {
        match self {
            Hand::Rock => 1,
            Hand::Paper => 2,
            Hand::Scissors => 3,
        }
    }

    fn against(&self, opponent: &Hand) -> GameResult {
        match [opponent, self] {
            [Hand::Rock, Hand::Paper] => GameResult::Win,
            [Hand::Paper, Hand::Rock] => GameResult::Lose,
            [Hand::Paper, Hand::Scissors] => GameResult::Win,
            [Hand::Scissors, Hand::Paper] => GameResult::Lose,
            [Hand::Scissors, Hand::Rock] => GameResult::Win,
            [Hand::Rock, Hand::Scissors] => GameResult::Lose,
            _ => GameResult::Draw,
        }
    }

    fn want(&self, result: &GameResult) -> Hand {
        match self {
            Hand::Rock => match result {
                GameResult::Win => Hand::Paper,
                GameResult::Draw => Hand::Rock,
                GameResult::Lose => Hand::Scissors,
            },
            Hand::Paper => match result {
                GameResult::Win => Hand::Scissors,
                GameResult::Draw => Hand::Paper,
                GameResult::Lose => Hand::Rock,
            },
            Hand::Scissors => match result {
                GameResult::Win => Hand::Rock,
                GameResult::Draw => Hand::Scissors,
                GameResult::Lose => Hand::Paper,
            },
        }
    }
}

enum GameResult {
    Win,
    Draw,
    Lose,
}

impl GameResult {
    fn from_str(input: &str) -> Result<GameResult, &str> {
        match input {
            "X" => Ok(GameResult::Lose),
            "Y" => Ok(GameResult::Draw),
            "Z" => Ok(GameResult::Win),
            _ => Err("Unknown play"),
        }
    }

    fn value(&self) -> i32 {
        match self {
            GameResult::Win => 6,
            GameResult::Draw => 3,
            GameResult::Lose => 0,
        }
    }
}

pub fn part_1(input: &[Vec<&str>]) -> i32 {
    input
        .iter()
        .map(|game| {
            let opponent_hand = Hand::from_str(game[0]).unwrap();
            let your_hand = Hand::from_str(game[1]).unwrap();
            your_hand.value() + your_hand.against(&opponent_hand).value()
        })
        .sum()
}

pub fn part_2(input: &[Vec<&str>]) -> i32 {
    input
        .iter()
        .map(|game| {
            let opponent_hand = Hand::from_str(game[0]).unwrap();

            let your_result = GameResult::from_str(game[1]).unwrap();
            your_result.value() + opponent_hand.want(&your_result).value()
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE_FILE: &str = "\
A Y
B X
C Z
";

    #[test]
    fn test_parse_input() {
        assert_eq!(
            parse_input(EXAMPLE_FILE),
            [["A", "Y"], ["B", "X"], ["C", "Z"]]
        )
    }

    #[test]
    fn test_part_1() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_1(&input), 15);
    }

    #[test]
    fn test_part_2() {
        let input = parse_input(EXAMPLE_FILE);
        assert_eq!(part_2(&input), 12);
    }
}
