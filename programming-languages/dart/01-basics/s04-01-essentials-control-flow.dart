
void main(List<String> args) {
  print("\n--- Essentials — Control Flow ---\n");

  /**
    * if-else statement
    */
  int x = 22;
  
  if (x > 10) {
    print("P01: x is greater than 10");
  } else {
    print("P02: x is 10 or less");
  }

  x = 9;

  if (x > 10) {
    print("P03: x is greater than 10");
  } else {
    print("P04: x is 10 or less");
  }

  /**
    * switch-case statement
    */
  String grade = 'B';

  switch (grade) {
    case 'A':
      print("P05: Excellent!");
      break;
    case 'B':
      print("P06: Good job!");
      break;
    case 'C':
      print("P07: You passed.");
      break;
    case 'D':
      print("P08: Better try again.");
      break;
    default:
      print("P09: Invalid grade.");
  }

  /**
    * for loop
    */
  for (int i = 1; i <= 5; i++) {
    print("P10: Loop iteration $i");
  }

  /**
    * while loop
    */
  int count = 1;
  while (count <= 5) {
    print("P11: Count is $count");
    count++;
  }

  print("\n--- End of Essentials — Control Flow ---\n");
  assert(false, "Intentional Assertion — End of program reached.");
}