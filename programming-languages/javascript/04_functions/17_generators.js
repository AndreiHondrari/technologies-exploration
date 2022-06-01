"use strict";

function main() {
  console.log("** START **\n");

  function* counter() {
    let k = 1;

    while (true) {
      yield k;
      ++k;
    }
  }

  const c1 = counter();

  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());

  console.log("\n** END **");
}

main();
