"use strict";

function main() {
  console.log("** START **\n");

  // outside definition
  function f1() {
    console.log("F1_X_IS", this.x);
  }

  // object declaration
  const obj1 = {
    x: 11,

    // a method
    doThis: function () {
      console.log("THIS_X_IS", this.x);
    },

    // another method
    doThat() {
      console.log("THAT_X_IS", this.x);
    },
  };

  // third method
  obj1.doSome = f1;

  console.log(" \n# Calling the methods");
  obj1.doThis();
  obj1.doThat();
  obj1.doSome();

  console.log("\n** END **");
}

main();
