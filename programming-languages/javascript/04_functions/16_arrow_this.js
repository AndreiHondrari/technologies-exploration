"use strict";

function main() {
  console.log("** START **\n");

  function f1() {
    let innerFunc = () => {
      // this will be from the outer scope
      console.log("THIS", this);
    };

    return innerFunc;
  }

  const f2 = f1.bind(1234); // bind this
  const f3 = f2(); // get the inner function

  f3(); // call the inner function

  console.log("\n** END **");
}

main();
