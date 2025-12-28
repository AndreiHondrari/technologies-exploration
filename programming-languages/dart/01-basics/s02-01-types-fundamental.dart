

import 'dart:typed_data';

void main(List<String> args) {
  print("\n\n--- Types — Fundamental ---");
  
  int x01 = 10;
  int x02 = 0x1421;
  double x11 = 20;
  double x12 = 3.1532152;

  print('x01: $x01, x02: $x02, x11: $x11, x12: $x12');

  var n1 = 1_000_000;
  var n2 = 0.000_000_000_01;
  var n3 = 0x00_14_22_01_23_45; // MAC address
  var n4 = 555_123_4567; // US Phone number
  var n5 = 100__000_000__000_000; // one hundred million million!
  print('n1: $n1, n2: $n2, n3: $n3, n4: $n4, n5: $n5');

  String s1 = "Kekus Maximus";
  String s2 = "Proxima Centauri";
  String s3 = s1 + ' ' + s2;
  print(s3);

  var s4 = r'raw string \n no escapes';
  print(s4);

  var s5 = """
--- MULTILINE STRING DISPLAY ---

This is a multiline string.
You can write as many lines as you want.
\t- It supports indentation
\t- And special characters like \n new line

List:
  1. Item one
  2. Item two
  3. Item three
""";
  print(s5);

  bool b1 = true;
  bool b2 = false;
  print('b1: $b1, b2: $b2');

  List<int> list1 = [1, 2, 3, 4, 5];
  print('list1: $list1');

  Map<String, int> map1 = {
    'one': 1,
    'two': 2,
    'three': 3,
  };
  print('map1: $map1');

  Set<String> set1 = {'apple', 'banana', 'orange'};
  print('set1: $set1');

  Uint8List byteData = Uint8List.fromList([0, 255, 128, 64]);
  print('byteData: $byteData');

  Symbol sym1 = #mySymbol;
  print('sym1: $sym1');

  var record1 = (name: 'Alice', isKek: true, 30, "ZERO", [1, 2, 3], [5, 6, 7]);
  (int, String, List<int>, List<int>, {bool isKek, String name}) record2 = record1;
  print('record2: $record2');

  (int p1, int p2) record3 = (10, 20);  // p1 and p2 are just for documentation purposes]
  print('record3: $record3');

  var record4 = (10, name: "Bob", isKek: false, "Lorem ipsum");
  print("\nrecord4 decomposition:");
  print("record4.\$1: ${record4.$1}");
  print("record4.name: ${record4.name}");
  print("record4.isKek: ${record4.isKek}");
  print("record4.\$2: ${record4.$2}");

  var (p3, p4) = record3;
  print("\nDecomposed record3: p3: $p3, p4: $p4");

  var (:foo, :bar) = (foo: "Iota", bar: "Zeta");
  print("Decomposed $foo, $bar");

}