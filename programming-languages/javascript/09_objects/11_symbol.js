"use strict";

// CONTEXT 1
const context1_id = Symbol("id");

const context1 = {
  annotate(obj) {
    if (!this.hasOwnProperty("x")) {
      this.x = 1;
    }
    obj[context1_id] = `XXX_${this.x}`;
  },
};

// CONTEXT 2
const context2_id = Symbol("id");

const context2 = {
  annotate(obj) {
    if (!this.hasOwnProperty(this, "y")) {
      this.y = 100;
    }
    obj[context2_id] = `YYY_${this.y}`;
  },
};

function main() {
  console.log("** START **\n");

  const obj1 = {
    a: 11,
    b: 22,
  };

  /*
  The idea behind symbols is that a library can attack some
  metadata to an object without being worried that it would
  affect other libraries that might use the same "property name"
  for a different purpose
  */
  context1.annotate(obj1);
  context2.annotate(obj1);

  console.log(obj1);

  console.log("\n** END **");
}

main();
