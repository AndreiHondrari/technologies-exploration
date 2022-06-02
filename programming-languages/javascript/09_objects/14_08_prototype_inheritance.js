"use strict";

function main() {
  console.log("** START **\n");

  // define types
  const TypeAPrototype = {
    x: 0,

    doThis() {
      console.log("TYPE_A DO_THIS", this.x);
    },

    doThat() {
      console.log("TYPE_A DO_THAT", this.x);
    },
  };

  const TypeBPrototype = {
    a: 0,

    // overwrite doThis from TypeA
    doThis() {
      console.log("TYPE_B DO_THIS", this.x, this.a);
    },

    // define a new method unique to TypeB
    doSome() {
      console.log("TYPE_B DO_SOME", this.a);
    },
  };

  // set inheritance relation
  Object.setPrototypeOf(TypeBPrototype, TypeAPrototype);

  function TypeA(x) {
    console.log("TYPE_A_CONSTRUCTOR", this);
    this.x = x;
  }
  TypeA.prototype = TypeAPrototype;
  TypeA.prototype.constructor = TypeA;

  function TypeB(a, x) {
    /*
    Equivalent would be:
    this.__proto__.__proto__.constructor.call(this, x);
    */
    TypeA.call(this, x);

    this.a = a;
  }
  TypeB.prototype = TypeBPrototype;
  TypeB.prototype.constructor = TypeB;

  const b1 = new TypeB(11, 22);

  b1.doThis();
  b1.doThat();
  b1.doSome();

  console.log("\n** END **");
}

main();
