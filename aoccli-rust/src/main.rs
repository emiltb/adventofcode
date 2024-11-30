use std::env;
use clap::Parser;
use clap::ArgAction;
use reqwest::blocking;
use std::fs;
use std::path::Path;
use std::io::Write;


/// Downloads AOC input and creates a rust template file
#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    year: u16,
    day: u8,
    #[arg(long, short, action=ArgAction::SetTrue)]
    force: bool
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args = Cli::parse();
    let aoc_cookie = env::var("AOC_COOKIE").expect("AOC_COOKIE not set");
    let aoc_cookie = format!("session={}", aoc_cookie);
    let url = &format!("https://adventofcode.com/{}/day/{}/input", args.year, args.day);
    let input_path = format!("{}/data/{}.in", args.year, args.day);
    let script_path = format!("{}/src/bin/day{:0>2}a.rs", args.year, args.day);

    if Path::new(&input_path).exists() && !args.force {
        println!("Input for {} day {} already downloaded", args.year, args.day);
        std::process::exit(1);
    }
    
    let client = blocking::Client::new();
    let response = client.get(url)
    .header("User-Agent", "github.com/emiltb/adventofcode by emilbp@gmail.com")
    .header("cookie", aoc_cookie)
    .send()?
    .text()?;

    fs::write(&input_path, response)?;

    if !Path::new(&script_path).exists() || args.force {
        let mut file = fs::File::create(&script_path)?;
        let content = format!("const INPUT: &str = include_str!(\"../../data/{}.in\");

fn main() {{
    let numbers: Vec<i32> = INPUT
        .lines()
        .filter_map(|line| line.parse::<i32>().ok())
        .collect();

    println!(\"{{:?}}\", numbers);
}}", args.day);
        writeln!(file, "{}", content)?;
    }

    println!("Downloaded AOC input for year: {:?}, day: {:?}", args.year, args.day);
    Ok(())
}
