"use strict";

function main() {
  console.log("** START **\n");

  function* counter(up_to) {
    for (let k = 1; k <= up_to; ++k) {
      try {
        yield k;
      } catch (e) {
        console.error("Intentionally caught |", String(e));
      }
    }

    return 999;
  }

  const c1 = counter(10);

  console.log(c1.next());
  console.log(c1.next());
  console.log("E->", c1.throw(new Error("Something indeed A")));
  console.log("E->", c1.throw(new Error("Something indeed B")));
  console.log(c1.next());
  console.log(c1.next());

  console.log("\n** END **");
}

main();
