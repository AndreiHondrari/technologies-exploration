"use strict";

function main() {
  console.log("** START **\n");

  function toBinaryString(value, characters = 4) {
    return (value).toString(2).padStart(characters, "0");
  }

  console.log("AND  |", toBinaryString(0b0101 & 0b0100));
  console.log("OR   |", toBinaryString(0b0001 | 0b1000));
  console.log("XOR  |", toBinaryString(0b1010 ^ 0b1000));

  console.log(
    "NOT  |",
    toBinaryString(~0b0011, 4),
    "<->",
    toBinaryString(~0b0011, 4).replace("-", "1"),
  );

  console.log("LSHIFT |", toBinaryString(0b0000_0011 << 4, 8));
  console.log("RSHIFT |", toBinaryString(0b1110_1111 >> 4, 8));

  console.log("\n** END **");
}

main();
