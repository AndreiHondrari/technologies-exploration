"use strict";

function main() {
  console.log("** START **\n");

  const msg = new String("Potatoes are awesome");

  console.log("substring |", msg.substring(10, 5));
  console.log("toLowerCase |", msg.toLowerCase());
  console.log("toUpperCase |", msg.toUpperCase());
  console.log("repeat |", msg.repeat(3));
  console.log("slice |", msg.slice(3, 15));
  console.log("concat |", msg.concat(" Or are they? ", "Hmmm.. perhaps"));

  console.log("\n** END **");
}

main();
