"use strict";

function main() {
  console.log("** START **\n");

  const templateObj = {
    a: 11,
    doSome() {
      console.log("Do Some", this.a);
    },
  };

  const obj1 = Object.create(templateObj);
  obj1.x = 99;

  console.log(obj1);
  console.log(obj1.a); // gets the property from the template object
  obj1.doSome(); // gets the function from the template object

  console.log("isPrototypeOf?", templateObj.isPrototypeOf(obj1));

  console.log(" \n# Obj property descriptors");
  console.log(Object.getOwnPropertyDescriptors(obj1));

  console.log(" \n# Obj entries");
  console.log(...Object.entries(obj1));

  console.log("\n** END **");
}

main();
