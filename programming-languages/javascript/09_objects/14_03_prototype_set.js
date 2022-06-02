"use strict";

function main() {
  console.log("** START **\n");

  const kek = {
    doSome() {
      console.log("DOSOM", this);
    },
  };

  const obj1 = { a: 11 };
  const obj2 = { a: 22 };

  Object.setPrototypeOf(obj1, kek);
  Object.setPrototypeOf(obj2, kek);

  obj1.doSome();
  obj2.doSome();

  console.log("\n** END **");
}

main();
