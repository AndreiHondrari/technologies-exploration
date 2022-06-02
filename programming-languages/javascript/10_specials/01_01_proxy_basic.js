"use strict";

function main() {
  console.log("** START **\n");

  const handler = {
    get(target, prop, receiver) {
      console.log("handler-get", target, prop, receiver);
      return 456;
    },
    set(target, prop, receiver) {
      console.log("handler-set", target, prop, receiver);
      return true;
    },
  };

  const someObj = {};

  const p = new Proxy(someObj, handler);

  console.log("# Get");
  let res = p.a;
  console.log("RES", res);

  console.log(" \n# Set");
  p.a = 123;

  console.log("\n** END **");
}

main();
