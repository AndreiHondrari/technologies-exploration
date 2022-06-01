"use strict";

function main() {
  console.log("** START **\n");

  const msg = "Funny butterflies kek 123777aaa999 leonardos kekus";
  const expr1 = /[a-z]+/;
  const expr2 = /[a-z]+/g;
  const expr3 = /([a-z]+)/ig;

  console.log(" \n# match A |", msg.match(expr1));
  console.log(" \n# match B |", msg.match(expr2));
  console.log(" \n# match C |", msg.match(expr3));

  try {
    console.log(" \n# matchAll A |", msg.matchAll(expr1));
  } catch (e) {
    console.error("Caught intentionally |", String(e));
  }

  const result = msg.matchAll(expr2);
  console.log(" \n# matchAll B |", result);
  console.log([...result]);

  console.log(" \n# Search");
  let res = msg.search("XENOMORPH");
  console.log("SEARCH_A |", res);

  res = msg.search("butter");
  const res_extr = msg.slice(res).split(" ")[0];
  console.log("SEARCH_B |", res, "->", res_extr);

  console.log(" \n# Replace");
  let new_msg = msg.replace(/[0-9]/, "X");
  console.log("REPLACE_A |", new_msg);

  new_msg = msg.replace(/[0-9]/g, "Y");
  console.log("REPLACE_B |", new_msg);

  new_msg = msg.replace("kek", "KOK");
  console.log("REPLACE_C |", new_msg);

  new_msg = msg.replaceAll(/[0-9]/g, "Z");
  console.log("REPLACE_ALL_A |", new_msg);

  new_msg = msg.replaceAll("kek", "KOK");
  console.log("REPLACE_ALL_B |", new_msg);

  console.log(" \n# Match groups");

  const msg2 = "xoxoxo";
  res = msg2.match(/(xo)/);
  console.log("MATCH_GROUPS_A |", res);

  res = msg2.match(/(?<XOGRP>xo)/);
  console.log("MATCH_GROUPS_B |", res.groups);

  console.log("\n** END **");
}

main();
