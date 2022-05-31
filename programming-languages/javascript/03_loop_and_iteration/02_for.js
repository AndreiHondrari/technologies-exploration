"use strict";

function main() {
  console.log("** START **\n");

  const someArray = [11, 22, 33];
  const someObj = { a: 44, b: 55, c: 66 };

  // regular for
  for (let i = 0; i < 3; i += 1) {
    console.log("FOR |", i);
  }

  // for..in
  console.log("\n# for .. in array");
  for (const j in someArray) {
    console.log("FOR IN ARRAY |", j, someArray[j]);
  }

  console.log("\n# for .. in object");
  for (const p in someObj) {
    console.log("FOR IN OBJECT |", p, someObj[p]);
  }

  // for..of
  console.log("\n# for .. of array");
  for (const x of someArray) {
    console.log("FOR OF ARRAY |", x);
  }

  console.log("\n# for .. of object");
  try {
    for (const y of someObj) {
      console.log("FOR OF OBJECT |", y);
    }
  } catch (e) {
    console.error("Intentionally caught |", String(e));
  }

  console.log("\n** END **");
}

main();
