const INPUT: &str = include_str!("../../data/3.in");

fn main() {
    let mut grid: Vec<Vec<char>> = Vec::new();
    let lines: Vec<&str> = INPUT.lines().collect();

    for line in lines {
        let row: Vec<char> = line.chars().collect();
        grid.push(row);
    }

    let mut pos = (0,0);
    let grid_r = grid.len();
    let grid_c = grid[0].len();

    let mut p1 = 0;

    while pos.0 < grid_r {
        pos.0 += 1;
        pos.1 += 3;
        if pos.1 >= grid_c {
            pos.1 -= grid_c
        }

        if let Some(row) = grid.get(pos.0) {
            if let Some(col) = row.get(pos.1) {
                //println!("({},{}) = {}", pos.0, pos.1, col)
                if *col == '#' {
                    p1 += 1
                }
            }
        }

    }
    
    println!("{}", p1);

}
