"use strict";

function main() {
  console.log("** START **\n");

  function Something(val, name) {
    this.x = val;
    this.name = name;
    this.doThis = function () {
      console.log(`${this.name} AAAA`);
    };
  }

  const o1 = new Something(11, "Jeff");
  const o2 = new Something(22, "Gandalf");

  console.log("# inst.doThis");
  o1.doThis();
  o2.doThis();

  console.log(" \nChange prototype directly ...");

  // add new method directly on the Function object
  Something.doKek = function () {
    console.log("DO KEK");
  };

  // alter method on the prototype
  Something.prototype.doThis = function () {
    console.log(`${this.name} BBBB`);
  };

  // add new method on the prototype
  Something.prototype.doThat = function () {
    console.log(`${this.name} DOING_THAT`);
  };

  console.log(" \n# Something.doKek()");
  Something.doKek();

  console.log(" \n# instance.doKek()");
  try {
    o1.doKek();
  } catch (e) {
    console.log("Intentionall caught |", String(e));
  }

  try {
    o2.doKek();
  } catch (e) {
    console.log("Intentionall caught |", String(e));
  }

  /*
  Notice that doThis has not changed behaviour due to the fact that
  when doThis is being looked up it is first looked up in the current object
  and only then in the prototype it inherits from.
  Since doThis was already attached to this object during instantiation time,
  JS does not feel the need to look further than the current object,
  hence there will be a doThis in the current object and a doThis in the
  prototype.
  */
  console.log(" \n# inst.doThis");
  o1.doThis();
  o2.doThis();

  /*
  This however did not exist in the current object before,
  so it is accessible now from both instances.
  */
  console.log(" \n# inst.doThat");
  o1.doThat();
  o2.doThat();

  console.log("\n** END **");
}

main();
