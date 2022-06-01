"use strict";

function main() {
  console.log("** START **\n");

  function doSome(a, b, ...whatever) {
    console.log("DO_SOME A |", a);
    console.log("DO_SOME B |", b);
    console.log("DO_SOME W/E |", whatever);
  }

  console.log("\n# Call A");
  doSome();

  console.log("\n# Call B");
  doSome(11);

  console.log("\n# Call C");
  doSome(11, 22);

  console.log("\n# Call D");
  doSome(11, 22, 33, 44, 55, 66);

  console.log("\n** END **");
}

main();
