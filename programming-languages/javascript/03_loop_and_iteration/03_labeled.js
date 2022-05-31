"use strict";

function main() {
  console.log("** START **\n");

  let k = 0;
  main_loop:
  while (true) {
    inner_loop:
    for (let i = 0; i < 10; ++i) {
      console.log(`I: ${i} K: ${k}`);
      if (i === 2) {
        k += 1;

        if (k >= 3) {
          console.log(`Breaking main loop ... at K = ${k}`);
          break main_loop;
        }
        console.log("Breaking inner loop ...");
        break inner_loop;
      }
    }
  }

  console.log("\n** END **");
}

main();
