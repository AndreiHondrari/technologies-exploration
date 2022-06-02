"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = {
    a: 11,
    b: 22,
  };

  // try something
  try {
    Object.defineProperties(obj1, { x: 33, y: 44 });
  } catch (e) {
    console.error("Intentionally caught |", String(e));
  }

  // do it properly
  const newProps = {
    p: { value: 33, enumerable: true, writable: true },
    q: { get: () => 11111 },
    r: { value: 44 },
    s: { value: 44, enumerable: true },
  };
  Object.defineProperties(obj1, newProps);
  console.log("OBJ AFTER NEW PROPS |", obj1);

  // change p
  obj1.p = 77;

  // try changing s
  try {
    obj1.s = 99;
  } catch (e) {
    console.error("intentionally caught |", String(e));
  }
  console.log("OBJ AFTER PROPS REASSIGN |", obj1);

  console.log("OBJ1.q |", obj1.q);

  console.log("\n** END **");
}

main();
