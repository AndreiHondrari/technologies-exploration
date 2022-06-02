"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = { a: 11, b: 22 };
  console.log("OBJ |", obj1);

  console.log("isSealed?", Object.isSealed(obj1));
  console.log("seal ...");
  Object.seal(obj1);
  console.log("isSealed?", Object.isSealed(obj1));

  try {
    obj1.c = 33;
  } catch (e) {
    console.log("intentionally caught |", String(e));
  }

  console.log("Change a to 77 ...");
  obj1.a = 77;
  console.log("OBJ |", obj1);

  console.log("\n** END **");
}

main();
