"use strict";

function main() {
  console.log("** START **\n");

  const o1 = {
    a: 11,
    b: 22,
    c: 33,
  };

  console.log("O |", o1);

  console.log(" \n# Object destructuring");
  const { a, b, z } = o1;
  console.log(a, b, z);

  console.log(" \n# Object destructuring (separate from declaration)");
  let h1;
  let h2;
  ({ h1, h2 } = { h1: "hash1", h2: "hash2" });
  console.log(h1, h2);

  console.log(" \n# Object destructuring (rename)");
  let { a: x, b: y } = o1;
  console.log(x, y);

  console.log(" \n# Object destructuring (defaults)");
  let { p = 77, q = 88 } = { q: 555 };
  console.log(p, q);

  console.log(" \n# Object destructuring (function args unpack)");
  const f1 = ({ k, m }) => console.log("F1 ->", k, m);
  f1({ k: 56, m: 78, p: 909 });

  console.log(" \n# Object destructuring (nested)");
  const someData = {
    kekus: "01",
    lolus: {
      aaa: "02",
      bbb: "03",
    },
    dubius: "04",
  };
  const {
    kekus: sparkling,
    lolus: {
      aaa: severus,
    },
  } = someData;
  console.log(sparkling, severus);

  console.log(" \n# Object destructuring (iteration)");
  const someData2 = [{ a: "01" }, { a: "02" }];
  for (const { a: value } of someData2) {
    console.log("VAL", value);
  }

  console.log(" \n# Object destructuring (dynamic property name)");

  const o2 = { a: "AAA", b: "BBB", c: "CCC" };
  let r1;
  ({ ["a"]: r1 } = o2);
  console.log(r1);

  ({ ["b"]: r1 } = o2);
  console.log(r1);

  const propName = "c";
  ({ [propName]: r1 } = o2);
  console.log(r1);

  console.log("\n** END **");
}

main();
