
enum PotatoSize {
  small,
  medium,
  large,
}

enum Potato {
  russet(
    size: PotatoSize.medium,
    pigmentation: 100,
  ),
  red(
    size: PotatoSize.small,
    pigmentation: 80,
  ),
  white(
    size: PotatoSize.large,
    pigmentation: 90,
  );

  final PotatoSize size;
  final int pigmentation;

  const Potato({
    required this.size,
    required this.pigmentation,
  });
}

void main(List<String> args) {
  print("\n--- Essentials — Enums ---\n");
  
  var myPotatoSize = PotatoSize.medium;

  switch (myPotatoSize) {
    case PotatoSize.small:
      print('P01-01: You selected a small potato.');
      break;
    case PotatoSize.medium:
      print('P01-02: You selected a medium potato.');
      break;
    case PotatoSize.large:
      print('P01-03: You selected a large potato.');
      break;
  }

  print("P02: Potato types and their pigmentation levels:");
  List<Potato> myPotatoes = [Potato.russet, Potato.white];
  
  for (var potato in myPotatoes) {
    print('- ${potato.name}: pigmentation level ${potato.pigmentation}');
  }
}