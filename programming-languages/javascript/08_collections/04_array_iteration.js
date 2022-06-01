"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = [11, 22, 33, 44];
  const arr1Entries = arr1.entries();

  console.log("ARR1_ENTRIES |", arr1Entries);

  console.log(" \n# Entry with next");
  let kek;
  do {
    kek = arr1Entries.next();
    if (!kek.done) {
      console.log("ARR1_ENTRY |", kek.value);
    }
  } while (!kek.done);

  console.log(" \n# Entry with for..of");
  const arr1Entries2 = arr1.entries();
  for (const bla of arr1Entries2) {
    console.log(bla);
  }

  console.log(" \n# Entry with for..of and destructuring");
  const arr1Entries3 = arr1.entries();
  for (const [i, v] of arr1Entries3) {
    console.log(`ARR1[${i}] = ${v}`);
  }

  console.log(" \n# For each");
  arr1.forEach((v, i) => {
    console.log(`ARR1[${i}] = ${v}`);
  });

  console.log("\n** END **");
}

main();
