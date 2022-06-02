"use strict";

function main() {
  console.log("** START **\n");

  // define a prototype
  const SomePrototype = {
    a: undefined,
    b: undefined,

    doThis() {
      console.log(`SOME DO_THIS ${this.a} ${this.b}`);
    },
  };

  // define a constructor
  function Some(a) {
    this.a = a;
  }

  // associated the prototype with the constructor
  Some.prototype = SomePrototype;

  // instantiate
  const o1 = new Some(11);

  // use
  o1.doThis();

  console.log(" \n# Enumerate fields");
  console.log(Object.getOwnPropertyDescriptors(o1));

  console.log("\n** END **");
}

main();
