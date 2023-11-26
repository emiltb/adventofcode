fn main() {
    let input = include_str!("1.in");

    let elves = input
        .split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
        .collect::<Vec<u32>>();
    let elves_part2 = elves.clone();

    let part1 = elves.iter().max().unwrap();
    println!("{part1}");

    let mut part2 = elves_part2;
    part2.sort();
    let part2 = part2.into_iter().rev().take(3).sum::<u32>();
    println!("{part2}");
}
