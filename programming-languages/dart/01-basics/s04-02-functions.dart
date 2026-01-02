

void f1() {
  print('SF01: Function with no parameters and no return value');
}

int f2(String msg) {
  print("SF02: Hereby message: $msg");
  return 123;
}

void f3(Function callback) {
  print('F04: Function with a callback parameter');
  callback("Call from f3");
}

void main(List<String> args) {
  print("\n--- Essentials — Functions ---\n");

  // call function directly
  f1();

  // call function with parameters and return value
  print("P02: ${f2("CAll from f2")}");

  // pass static function to another function (as callback)
  f3(f2);

  // pass anonymous function to another function (as callback)
  f3((String msg) => print("C01: Closure with message: $msg"));

  // pass named function to another function (as callback)
  void kek(String msg) {
    print("F01: $msg");
  }

  f3(kek);
}