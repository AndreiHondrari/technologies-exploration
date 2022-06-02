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

  obj1.doSome();

  console.log("Alter the prototype ...");
  templateObj.a = 22;

  obj1.doSome();

  console.log("\n** END **");
}

main();
