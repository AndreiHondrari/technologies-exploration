/*
Control flow - loops - breaking outer loop by label

Loops can get labels that can be used to break from an inner loop
*/


fn main() {

    let mut i = 0;

    'out_loop: loop {

        let mut j = 0;

        loop {
            println!("PAIR {i} {j}");

            if i >= 3 && j >= 3 {
                break 'out_loop  // breaks outside loop -> no need for special exit flags
                println!("break out loop");
            };

            if j >= 3 {
                break
            };
            j += 1;
        }

        i += 1;
    }

    println!("Done");
}
