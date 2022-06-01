"use strict";

function main() {
  console.log("** START **\n");

  function doSome(name) {
    function doThat() {
      console.log(`My name is ${name}`);
    }
    return doThat;
  }

  const jeffFunc = doSome("Jeff");
  const gandalfFunc = doSome("Gandalf");

  console.log("Calling jeffs");
  jeffFunc();
  jeffFunc();
  jeffFunc();

  console.log("Calling gandalfs");
  gandalfFunc();
  gandalfFunc();

  console.log("\n** END **");
}

main();
