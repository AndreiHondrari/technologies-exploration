"use strict";

function main() {
  console.log("** START **\n");

  // object declaration
  const obj1 = {
    x: 11,

    get z() {
      return this.x;
    },

    set z(new_value) {
      this.x = new_value * 11;
    },
  };

  console.log("OBJ1 |", obj1);
  console.log("OBJ1 GET |", obj1.z);

  obj1.z = 7;
  console.log("OBJ1 AFTER SET |", obj1);

  console.log("\n** END **");
}

main();
