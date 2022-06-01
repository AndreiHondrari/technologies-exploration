"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = new Int8Array(4);
  arr1[0] = 42;
  arr1[1] = 127;
  arr1[2] = 128;
  arr1[3] = 456;
  arr1[4] = 1; // this is out of scope

  console.log("INT8_ARRAY |", arr1);

  const buf2 = new ArrayBuffer(2);
  const dview2 = new DataView(buf2);
  const arr2 = new Uint8Array(buf2);

  dview2.setUint8(0, 255);
  dview2.setUint8(1, 0xF7);
  console.log("ABUFF2 |", buf2);
  console.log("DVIEW2 |", dview2);
  console.log("UINT8_ARRAY |", arr2);

  try {
    dview2.setUint16(1, 0x8E);
  } catch (e) {
    console.error("Caught intentionally |", String(e));
  }

  console.log("\n** END **");
}

main();
