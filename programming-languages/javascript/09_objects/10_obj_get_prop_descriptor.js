"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = { a: 11, b: 22 };

  let pDescr = Object.getOwnPropertyDescriptor(obj1, "a");
  console.log(pDescr);

  console.log("Freeze object ...");
  Object.freeze(obj1);

  pDescr = Object.getOwnPropertyDescriptor(obj1, "a");
  console.log(pDescr);

  console.log(" \n# All obj prop descriptors");
  console.log(Object.getOwnPropertyDescriptors(obj1));

  console.log("\n** END **");
}

main();
