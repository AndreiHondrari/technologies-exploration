
class Foo {

  String title;
  int? x;

  Foo(this.title, [this.x]);

  @override
  String toString() {
    return "Foo(title: $title, x: $x)";
  }

  void doKek() {
    print("Kek from Foo: $title");
  }

  void alterBla() {
    this.x ??= 0; // NO SIDE EFFECTS !
    this.x = this.x! + 100;
  }
}


void main(List<String> args) {
  print("\n--- Essentials — Classes ---\n");

  var foo1 = Foo("Jeff");
  print("P01: foo1: $foo1");
  
  var foo2 = Foo("Lebowski", 42);
  print("P02: foo2: $foo2");

  print("P03: Calling doKek on foo1:");
  foo1.doKek();

  print("P04: Altering bla on foo2:");
  foo2.alterBla();
  foo2.alterBla();
  foo2.alterBla();
  print("P05: foo2 after altering bla: $foo2");

  print("P05: Altering when null");
  try {
    foo1.alterBla();
  } catch (e) {
    print("Caught error: $e");
  }
  print("P06: foo1 after attempting to alter bla: $foo1");
}