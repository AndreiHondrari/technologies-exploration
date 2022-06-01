"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = [11, 22, 33, 44, 55, 66, 77];
  const arr2 = [11, 22, 33, 44, [666, 777, 888, ["a", "b"]]];
  const arr3 = ["aa bb cc", "dd ee ff"];
  const arr4 = [8, 2, 6, 3, 1, 0, 199, 513, 233];

  console.log("FILTER |", arr1.filter((v) => v > 50));
  console.log("\nMAP |", arr1.map((v) => v * 10));
  console.log("\nFLAT (1) |", arr2.flat());
  console.log("\nFLAT (2) |", arr2.flat(2));
  console.log("\nFLAT_MAP |", arr3.flatMap((v) => v.split(" ")));

  // NODEJS does not have groupBy yet
  // console.log(
  //   "\nGROUP_BY |",
  //   arr1.groupBy(
  //     (v) => String((v < 100) ? "SMALL" : "BIG"),
  //   ),
  // );

  console.log("\nJOIN |", arr1.join("_"));
  console.log("\nREDUCE |", arr1.reduce((a, b) => a * 100 + b));
  console.log("\nREDUCE_RIGHT |", arr1.reduceRight((a, b) => a * 100 + b));
  console.log("\nREVERSE |", arr1.reverse());
  console.log("\nSORT (1) |", arr4.sort());
  console.log("\nSORT (2) |", arr4.sort((a, b) => a > b));
  console.log("\nSLICE |", arr1.slice(2, 5));
  console.log("\nSPLICE |", arr1.splice(4), arr1);
  console.log("\nSHIFT (1) |", arr1.shift(), arr1);
  console.log("\nSHIFT (2) |", arr1.shift(), arr1);
  console.log("\nUNSHIFT |", arr1.unshift(888), arr1);

  console.log("\n** END **");
}

main();
