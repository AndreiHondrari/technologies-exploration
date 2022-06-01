"use strict";

function main() {
  console.log("** START **\n");

  const msg = new String("Potatoes are awesome");

  console.log("charAt |", msg.charAt(0));
  console.log("charCodeAt |", msg.charCodeAt(0));
  console.log("codePointAt |", msg.codePointAt(0));

  console.log("\n** END **");
}

main();
