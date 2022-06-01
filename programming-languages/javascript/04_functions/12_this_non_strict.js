// "use strict"; <-------- Notice we are not using strict mode

function main() {
  console.log("** START **\n");

  function f1() {
    console.log("THIS", String(this));
    console.log("THIS_KEYS", Object.keys(this));
  }

  f1();

  console.log("\n** END **");
}

main();
