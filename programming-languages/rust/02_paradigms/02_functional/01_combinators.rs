fn main() {
    #[allow(non_snake_case)]
    let B = |f: Box<dyn Fn(u32) -> u32>| {
        |g: Box<dyn Fn(u32) -> u32>| {
            move |x: u32| f(g(x))
        }
    };
    let result = B(
        Box::new(|v: u32| v * 1000)
    )(
        Box::new(|v: u32| v * 2)
    )(7);
    println!("{}", result);
}
