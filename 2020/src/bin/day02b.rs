const INPUT: &str = include_str!("../../data/2.in");

struct PW {
    range: (usize, usize),
    letter: char,
    password: String
}

impl PW {
    fn char_at(&self, idx: usize) -> Option<char> {
        self.password.chars().nth(idx-1)
    }
}

fn main() {
    let password_entries: Vec<PW> = INPUT
        .lines()
        .filter_map(|line| parse_line(&line))
        .collect();

    let mut p2 = 0;

    for p in password_entries {
        let first_pos = p.char_at(p.range.0) == Some(p.letter);
        let second_pos = p.char_at(p.range.1) == Some(p.letter);
        if first_pos ^ second_pos {
            p2 += 1;
        }
    }

    println!("{}", p2);        
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