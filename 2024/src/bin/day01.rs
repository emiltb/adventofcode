const INPUT: &str = include_str!("../../data/1.in");

fn main() {
    let inp: Vec<String> = INPUT
        .lines()
        .filter_map(|line| line.parse::<String>().ok())
        .collect();

    let numbers: Vec<(i32,i32)> = inp
        .iter()
        .filter_map(|s| {
            let mut parts = s.split_whitespace();
            if let (Some(a), Some(b)) = (parts.next(), parts.next()) {
                if let (Ok(n1), Ok(n2)) = (a.parse::<i32>(), b.parse::<i32>()) {
                    Some((n1,n2))
                }
                else {
                    None
                }
            } else {
                None
            }
        })
        .collect();

    let mut vec1: Vec<i32> = numbers.iter().map(|&(a,_)| a).collect();
    let mut vec2: Vec<i32> = numbers.iter().map(|&(_,b)| b).collect();
    vec1.sort();
    vec2.sort();

    let mut p1 = 0;
    for (n1, n2) in vec1.iter().zip(vec2.iter()) {
        p1 += (n1 - n2).abs();
    }

    println!("{:?}", p1);

    let mut p2 = 0;
    for &n in &vec1 {
        let count = vec2.iter().filter(|&&x| x == n).count();
        p2 += n*count as i32;
    }

    println!("{:?}", p2);
}
