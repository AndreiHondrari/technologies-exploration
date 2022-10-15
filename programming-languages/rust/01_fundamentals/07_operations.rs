/*
Various arithmetic and boolean operations.
*/

fn main() {
    println!("arithmetic operators");
    println!("+ {}", 1 + 2);
    println!("- {}", 33 - 11);
    println!("* {}", 11 * 4);
    println!("/ {}", 3 / 2);
    println!("% {}", 13 % 2);

    println!("\nboolean & bitwise operators");
    println!("!true  =  {}", !true);
    println!("!false =  {}", !false);

    let a: u8 = 0b0101;
    println!("!{a:08b} = {:08b}", !a);

    let b: u8 = 0b0011;
    println!("{a:04b} | {b:04b} => {:04b}", a | b);
    println!("{a:04b} & {b:04b} => {:04b}", a & b);
    println!("{a:04b} ^ {b:04b} => {:04b}", a ^ b);

    let c: u8 = 0b1101_1011;
    let d: u8 = 2;
    println!("{c:08b} >> {offset} => {:08b}", c >> d, offset = d);
    println!("{c:08b} << {offset} => {:08b}", c << d, offset = d);

    println!("t && t =  {}", true && true);
    println!("t && f =  {}", true && false);
    println!("t || f =  {}", true || false);
    println!("f || f =  {}", false || false);
}
