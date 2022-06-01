"use strict";

function main() {
  console.log("** START **\n");

  function doSome() {
    function doThat() {
      console.log("DOING THAT");
    }

    console.log("About to call doThat ...");
    doThat();
    console.log("After doThat...");
  }

  // call
  doSome();

  console.log("\n** END **");
}

main();
