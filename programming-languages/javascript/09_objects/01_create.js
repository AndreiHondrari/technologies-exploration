"use strict";

function main() {
  console.log("** START **\n");

  const zName = "z";
  const obj1 = {
    x: 11,
    y: 22,
    [zName]: 33,
  };
  console.log("OBJ1 |", obj1);

  const obj2 = new Object();
  obj2.a = "kekus";
  obj2.b = "lolus";
  console.log("OBJ2 |", obj2);

  function Obj3Type() {
    this.p = ["aa", "bb", "cc"];
    this.q = 123456;
  }

  const obj3 = new Obj3Type();
  console.log("OBJ3 |", obj3);

  console.log("\n** END **");
}

main();
