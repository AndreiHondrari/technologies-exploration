

void main(List<String> args) {
  print("\n\n--- Types — Nullable ---");
  // Dart has sound null safety, which means that values can't be null unless you say they can be.
  
  // Non-nullable type
  int a = 5;
  // a = null; // This would cause a compile-time error

  // Nullable type
  int? b = 10;
  b = null; // This is allowed

  print('Non-nullable int a: $a');
  print('Nullable int b: $b');
}