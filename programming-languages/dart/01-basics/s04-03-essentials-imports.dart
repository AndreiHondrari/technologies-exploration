
import 'dart:math' as math;
import 's04-submods/m01-kek.dart' as kek;


void main(List<String> args) {
  print("\n--- Essentials — Imports ---\n");

  print("Using math library:");
  print("Square root of 16 is ${math.sqrt(16)}");

  print("\nUsing custom submodule:");
  kek.doKek();
}