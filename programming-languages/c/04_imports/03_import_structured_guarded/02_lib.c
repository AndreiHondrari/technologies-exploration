#include <stdio.h>

#include "01_sub_lib.h"
#include "02_lib.h"

void doSomething() {
  Kogaion koga = giveKoga();
  Kogaion koga2 = giveKoga();

  printf("Koga 1: %d %d\n", koga.x, koga.y);
  printf("Koga 2: %d %d\n", koga2.x, koga2.y);
}
