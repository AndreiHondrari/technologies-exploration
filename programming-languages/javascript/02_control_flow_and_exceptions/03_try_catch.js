"use strict";

function main() {
  console.log("** START **\n");

  // simple exception
  console.log("# Simple exception\n");
  try {
    throw "pinkberries";
  } catch (e) {
    console.log("Caught exception intentionally |", e);
  }

  // error objects
  console.log("\n# Error objects\n");
  try {
    throw (new Error("error-object-is-error-object"));
  } catch (e) {
    console.log("Caught errobj |", String(e));
    console.log("Errobj name |", e.name);
    console.log("Errobj message |", e.message);
  }

  // error objects with names
  console.log("\n# Error objects with names\n");
  try {
    const newErr = new Error("something terribly bad has happened");
    newErr.name = "SarumanTheBringerOfDestruction";
    throw newErr;
  } catch (e) {
    console.log("Caught errobj |", String(e));
    console.log("Errobj name |", e.name);
    console.log("Errobj message |", e.message);
  }

  class SomethingBad extends Error {
    constructor(message = "", ...args) {
      super(message, ...args);
      this.name = "SomethingBad";
    }
  }

  console.log("\n# Error objects with inheritance\n");
  try {
    throw (new SomethingBad("why is this happening?!"));
  } catch (e) {
    console.log("Caught errobj |", String(e));
    console.log("Errobj name |", e.name);
    console.log("Errobj message |", e.message);

    if (e instanceof SomethingBad) {
      console.log(
        "Your error instance is SomethingBad",
      );
    } else {
      console.log("Error instance identified as:", typeof (e));
    }
  }

  console.log("\n** END **");
}

main();
