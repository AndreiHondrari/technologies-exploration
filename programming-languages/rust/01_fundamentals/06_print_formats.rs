/*
Various print formats.
*/

fn main() {
    println!("# 01_01 {1} {} {0} {}", 11, 22);
    println!("# 01_02 {kek}, {foo}", foo=44, kek=33);

    let a = 22 + 33;
    println!("# 02_01 {a}");

    println!("# 03_01 AAA {:20} CCC", "BBB");
    println!("# 03_02 AAA {:1$} CCC", "BBB", 20);
    println!("# 03_03 AAA {0:1$} CCC", "BBB", 20);
    println!("# 03_04 AAA {:b$} CCC", "BBB", b = 20);

    let b = 20;
    println!("# 03_05 AAA {:b$} CCC", "BBB");

    println!("# 04_01 AAA {:<20} CCC", "BBB");
    println!("# 04_02 AAA {:>20} CCC", "BBB");
    println!("# 04_03 AAA {:^20} CCC", "BBB");
    println!("# 04_04 AAA {:_<20} CCC", "BBB");
    println!("# 04_05 AAA {:_>20} CCC", "BBB");
    println!("# 04_06 AAA {:_^20} CCC", "BBB");
    println!("# 04_07 AAA {:_^k$} CCC", "BBB", k = 6);

    println!("# 05_01 {:+}", -123);

    let c = 127;
    println!("# 06_01 {k} => {k:#x}", k = c);

    println!("# 07_01 {:020}", 2345);
    println!("# 07_02 {:020}", -2345);

    println!("# 08_01 {:#b}", 5);
    println!("# 08_02 {:#06b}", 5);  // 6 to include the 0b also
    println!("# 08_03 {:04b}", 5);
    println!("# 08_04 {:04b}", 0b1100_0101);  // notice it does not get trimmed

    println!("# 09_01 {:.4}", 3.1425678903456);

    println!("# 09_02 {:.*}", 5, 3.1425678903456);
    println!("# 09_03 {1} {2:.*}", 7, "x", 3.1425678903456);
}
