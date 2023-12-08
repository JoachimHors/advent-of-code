fn main() {
    let input = include_str!("./input1.txt");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> u64 {
    let _input: String = input.to_string();
    let mut sum: u64 = 0;
    let words_to_nums = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ];

    for line in _input.lines() {
        let mut first: char = 'a';
        let mut last: char = 'a';

        let mut line_string = line.to_string(); // Convert line to String

        for word in &words_to_nums {
            line_string = line_string.replace(&word.0, &word.1); // Use string slices
        }

        for character in line_string.chars() {
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
    fn test_part_2() {
        const TEST_INPUT: &str = "two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen";
        let result = super::part2(TEST_INPUT);
        assert_eq!(result, 281);
    }
}
