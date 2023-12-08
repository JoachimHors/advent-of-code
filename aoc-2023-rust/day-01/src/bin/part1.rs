fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> u32 {
    let output = input
        .lines()
        .map(|line| {
            let mut iter = line.chars().filter_map(|character| character.to_digit(10));
            let first = iter.next().expect("Expected a number");

            match iter.last() {
                Some(number) => format!("{first}{number}"),
                None => format!("{first}{first}"),
            }
            .parse::<u32>()
            .expect("Expected a valid number")
        })
        .sum::<u32>();

    output
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
