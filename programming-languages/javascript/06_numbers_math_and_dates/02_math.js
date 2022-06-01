"use strict";

const degToRad = (degrees) => degrees * (Math.PI / 180);

function main() {
  console.log("** START **\n");

  console.log("# Enumerate math predefined values");

  for (const prop of Object.getOwnPropertyNames(Math)) {
    const thing = Math[prop];
    if (typeof (thing) === "number") {
      console.log(`Math.${prop} = ${thing}`);
    }
  }

  console.log("\n# Functions");
  console.log("SIN |", Math.sin(degToRad(90)));
  console.log("COS |", Math.cos(degToRad(0)));

  console.log("SQRT |", Math.sqrt(16));
  console.log("CBRT |", Math.cbrt(27));

  console.log("CLZ32 |", Math.clz32(0xffff)); // 16 bits left

  // ln(e) = 1
  // log_a(a) = 1
  console.log("LOG (natural) A |", Math.log(Math.E));

  // ln(e^2) = 2
  // log_a(x^n) = n * log_a(x)
  console.log("LOG (natural) B |", Math.log(Math.E ** 2));

  console.log("\n** END **");
}

main();
