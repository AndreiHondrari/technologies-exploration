"use strict";

function main() {
  console.log("** START **\n");

  function doSome() {
    function doThat() {
      console.log("DOING THAT");
    }

    return doThat;
  }

  // call
  console.log("Getting the doThat func ...");
  const someFunc = doSome();

  console.log("Calling our returned doThat ...");
  someFunc();

  console.log("\n** END **");
}

main();
