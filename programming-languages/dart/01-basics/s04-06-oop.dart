
class SomeBase {
  void doSomething() {
    print('Doing something in SomeBase');
  }
}

// inheritance
class Foo extends SomeBase {
  void doFoo() {
    print('Doing foo in Foo');
  }
}

// mixins
mixin BarMixin {
  void doBar() {
    print('Doing bar in BarMixin');
  }
}

class Bar with BarMixin {}

// interfaces & abstract classes


void main(List<String> args) {
  print("\n--- Essentials — OOP ---\n");
  
  var foo = Foo();
  foo.doSomething(); // from SomeBase
  foo.doFoo();      // from Foo

  var bar = Bar();
  bar.doBar();      // from BarMixin
}
