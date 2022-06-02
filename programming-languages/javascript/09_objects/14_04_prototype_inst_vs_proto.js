"use strict";

function main() {
  console.log("** START **\n");

  function Something(val, name) {
    this.x = val;
    this.name = name;
    this.doThis = function () {
      console.log(`${this.name} AAAA`);
    };
  }

  const o1 = new Something(11, "Jeff");
  const o2 = new Something(22, "Gandalf");

  console.log("# __proto__ vs prototype");
  console.log(
    "prototype vs __proto__ is same? (1):",
    Object.is(Something.prototype, o1.__proto__),
  );

  console.log(
    "prototype vs __proto__ is same? (2):",
    Object.is(Something.prototype, o2.__proto__),
  );

  /*
  Notice that the descriptors do not include functions
  manually added through the function Something constructor.
  That is because it happens during runtime, and the method "doThis"
  actually become part of the newly created object at instantiation time.
  */
  console.log(" \n# Something.prototype descriptors");
  console.log(Object.getOwnPropertyDescriptors(Something.prototype));

  console.log("\n** END **");
}

main();
