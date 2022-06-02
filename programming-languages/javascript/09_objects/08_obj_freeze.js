"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = { a: 11, b: 22 };
  console.log("isFrozen?", Object.isFrozen(obj1));

  console.log("Freeze obj ...");
  Object.freeze(obj1);
  console.log("isFrozen?", Object.isFrozen(obj1));

  // try reassign prop value
  try {
    obj1.a = 66;
  } catch (e) {
    console.error("Intentionally caught |", String(e));
  }

  // try extend obj with prop
  try {
    obj1.c = 77;
  } catch (e) {
    console.error("Intentionally caught |", String(e));
  }

  console.log(obj1);

  console.log("\n** END **");
}

main();
