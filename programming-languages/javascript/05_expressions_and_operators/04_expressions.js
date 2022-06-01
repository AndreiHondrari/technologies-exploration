"use strict";

function main() {
  console.log("** START **\n");

  const sampleArr = [11, 22, 33, 44, 55];

  // spread
  const arr1 = [11, 22];
  const arr2 = [33, 44];

  const arr3 = [555, ...arr1, 777, ...arr2, 999];
  console.log("ARRAY SPREAD | ", arr3);

  const o1 = { a: 11, b: 22 };
  const o2 = { b: 33, c: 44 };
  const o3 = { ...o1, ...o2 };
  console.log("OBJ SPREAD A |", o3);
  const o4 = { ...o2, ...o1 };
  console.log("OBJ SPREAD B |", o4); // notice that here o1.b overwrites o2.b

  // destructuring
  console.log(" \n# Destructuring A");
  const [k, p, ...rest] = sampleArr;
  console.log("K", k);
  console.log("P", p);
  console.log("R", rest);

  // destructuring defaults
  console.log(" \n# Destructuring B (defaults)");
  const [x = 77, y = 88] = [99];
  console.log(x, y);

  // destructuring swap
  console.log(" \n# Destructuring B (swap)");
  let a = 123;
  let b = 456;
  [a, b] = [b, a];
  console.log("A", a);
  console.log("B", b);

  // destructuring func args
  console.log(" \n# Destructuring B (func args)");
  const someArgs = ["keops", "archiles"];
  const someArgs2 = ["keops", "archiles", "potatoes", "excalibvr"];

  const f1 = (a1, a2, a3) => console.log("F1 ->", a1, a2, a3);
  f1(...someArgs);
  f1(...someArgs2);

  // destructuring func return
  console.log(" \n# Destructuring B (func return)");
  const f2 = () => ["xavier", "gerard", "fascicul"];
  let [r1, r2, r3] = f2();
  console.log(r1, r2, r3);

  // destructuring func return with ignore
  console.log(" \n# Destructuring B (func return)");
  const f3 = () => ["AAAA", "BBBB", "CCCC"];
  [r1, , r3] = f3(); // <-- NOTICE THE EMPTY SLOT
  console.log(r1, r3);

  console.log("\n** END **");
}

main();
