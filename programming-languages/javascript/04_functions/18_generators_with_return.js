"use strict";

function main() {
  console.log("** START **\n");

  function* counter(up_to) {
    for (let k = 1; k <= up_to; ++k) {
      yield k;
    }

    return 999;
  }

  const c1 = counter(3);

  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());
  console.log(c1.next());

  console.log("\n** END **");
}

main();
