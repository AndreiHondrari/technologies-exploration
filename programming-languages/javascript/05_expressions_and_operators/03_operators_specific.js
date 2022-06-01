"use strict";

function main() {
  console.log("** START **\n");

  // TERNARY
  console.log("# ternary");
  console.log("TERNARY_A |", true ? 11 : 22);
  console.log("TERNARY_B |", false ? 33 : 44);

  // TYPEOF
  console.log("\n# typeof");
  console.log("TYPEOF_A", typeof 123);
  console.log("TYPEOF_B", typeof "kek");

  // VOID
  console.log("\n# void");
  function f1(value) {
    console.log("F1", value);
    return value * 111;
  }

  let f2 = () => f1(5);
  let f3 = () => void f1(7);

  let x = f2();
  let y = f3();
  console.log("X", x);
  console.log("Y", y);

  // IN
  console.log("\n# in");
  console.log("IN_A", 22 in [11, 22, 33]);
  console.log("IN_B", 77 in [11, 22, 33]);
  console.log("IN_C", 1 in [11, 22, 33]); // array has index 1
  console.log("IN_D", 3 in [11, 22, 33]);
  console.log("IN_E", "zar" in { kek: 11, lol: 22 });
  console.log("IN_F", "kek" in { kek: 11, lol: 22 });

  console.log("\n** END **");
}

main();
