fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u64 {
    let _input: String = input.to_string();
    let mut sum: u64 = 0;

    for line in _input.lines() {
        let mut first: char = 'a';
        let mut last: char = 'a';
        for character in line.chars() {
            if character.is_digit(10) {
                if first == 'a' {
                    first = character;
                }
                last = character;
            }
        }
        let concatenated = format!("{}{}", first, last);
        if let Ok(value) = concatenated.parse::<u64>() {
            sum += value;
        }
    }

    sum
}

// Tests

#[cfg(test)]
mod tests {
    #[test]
    fn test_part_1() {
        const TEST_INPUT: &str = "1abc2
                                pqr3stu8vwx
                                a1b2c3d4e5f
                                treb7uchet";
        let result = super::part1(TEST_INPUT);
        assert_eq!(result, 142);
    }
}
