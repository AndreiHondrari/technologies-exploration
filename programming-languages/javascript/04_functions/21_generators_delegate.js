"use strict";

function main() {
  console.log("** START **\n");

  function* f1() {
    const nums = [11, 22, 33];

    for (let k of nums) {
      yield k;
    }
  }

  function* f2() {
    yield "KEK";
    yield* f1();
    yield "LOL";
  }

  const g1 = f2();

  console.log(g1.next());
  console.log(g1.next());
  console.log(g1.next());
  console.log(g1.next());
  console.log(g1.next());
  console.log(g1.next());

  console.log("\n** END **");
}

main();
