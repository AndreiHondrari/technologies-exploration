"use strict";

function main() {
  console.log("** START **\n");

  let a = true;
  let b = 42;
  let c = Number("55");
  let d = BigInt("123456789012345678901234567890");
  let e = 123456789012345678901234567890;
  let f = "Kekus magnificus";
  let g = String("Lolus excalibrvs");
  let h = Symbol("what");
  let i = 29.34;
  let j = 23E+10;
  let k = 55.678E+10;
  let l = 66778899E-4;
  let m = 0xAF; // 175
  let n = 0b1001_0010; // 146
  let o = 0o701;

  let x = [11, 22, 33, 44];
  let y = { x: 11, y: 22 };

  console.log("bool.................|", a);
  console.log("integer..............|", b);
  console.log("Number...............|", c);
  console.log("BigInt...............|", d);
  console.log("large int............|", e);
  console.log("plain string.........|", f);
  console.log("String().............|", g);
  console.log("Symbol().............|", h);
  console.log("float................|", i);
  console.log("exponential integer..|", j);
  console.log("exponential float....|", k);
  console.log("negative exponent....|", l);
  console.log("hexadecimal..........|", m);
  console.log("binary...............|", n);
  console.log("octal................|", o);

  console.log("array................|", x);
  console.log("object...............|", y);

  console.log("\n** END **");
}

main();
