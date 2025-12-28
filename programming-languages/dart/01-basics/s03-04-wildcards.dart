

void main(List<String> args) {
  int _ = 42;
  String _ = "Hello Jeff!";
  
  // Can not use wildcard '_' here
  print(_);  // ignore: undefined_identifier
}