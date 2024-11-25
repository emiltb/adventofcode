const INPUT: &str = include_str!("../../data/2.in");

struct PW {
    range: (usize, usize),
    letter: char,
    password: String
}

impl PW {
    fn count_letter(&self) -> usize {
        self.password.chars().filter(|&c| c == self.letter).count()
    }
}

fn main() {
    let password_entries: Vec<PW> = INPUT
        .lines()
        .filter_map(|line| parse_line(&line))
        .collect();

    let mut p1 = 0;

    for password in password_entries {
        let count = password.count_letter();
        if password.range.0 <= count && count <= password.range.1 {
            p1 += 1;
        }
    }

    println!("{}", p1);        
}

fn parse_line(line: &str) -> Option<PW> {
    let parts: Vec<&str> = line.split_whitespace().collect();
    let range: Vec<&str> = parts[0].split('-').collect();
    let min: usize = range[0].parse().ok()?;
    let max: usize = range[1].parse().ok()?;
    let range: (usize,usize) = (min, max);

    let letter: char = parts[1].chars().next()?;

    let password = parts[2].to_string();

    Some(PW {range, letter, password})
}