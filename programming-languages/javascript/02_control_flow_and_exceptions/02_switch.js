"use strict";

function main() {
  console.log("** START **\n");

  const x = 2;

  switch (x) {
    case 1:
      console.log("LEVEL 1");
      break;

    case 2:
      console.log("LEVEL 2");
      /* falls through */
    case 3:
      console.log("LEVEL 3");
      break;

    case 4:
      console.log("LEVEL 4");
      break;

    default:
      console.log("level untouchable");
  }

  console.log("\n** END **");
}

main();
