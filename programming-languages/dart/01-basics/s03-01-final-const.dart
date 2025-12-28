
void main(List<String> args) {
  final String name = "Dart";
  const double pi = 3.14159;

  print("Final variable: $name");
  print("Const variable: $pi");

  pi = 64421; // ignore: assignment_to_const
  name = "Flutter"; // ignore: assignment_to_final_local
}