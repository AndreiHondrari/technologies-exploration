"use strict";

function main() {
  console.log("** START **\n");

  const msg = new String("Potatoes are awesome");

  console.log("startsWith A |", msg.startsWith("Mangos"));
  console.log("startsWith B |", msg.startsWith("Potatoes"));

  console.log("endsWith A |", msg.endsWith("fabulous"));
  console.log("endsWith B |", msg.endsWith("awesome"));

  console.log("includes A |", msg.includes("keks"));
  console.log("includes B |", msg.includes("toes"));

  console.log("\n** END **");
}

main();
