const INPUT: &str = include_str!("../../data/1.in");

fn main() {
    let numbers: Vec<i32> = INPUT
        .lines()
        .filter_map(|line| line.parse::<i32>().ok())
        .collect();

    let (a,b): (i32, i32) = find_values(&numbers);
    println!("{}", a*b);
        
}

fn find_values(numbers: &[i32]) -> (i32, i32) {
    for i in 0..numbers.len() {
        for j in i + 1..numbers.len() {
            if numbers[i] + numbers[j] == 2020 {
                return (numbers[i], numbers[j]);
            }
        }
    }
    panic!("No vals");
}