#include "01_sub_lib.h"

Kogaion giveKoga() {
  static int x = 0;
  static int y = 0;

  x += 2;
  y += 10;

  Kogaion newKoga = {.x=x, .y=y};

  return newKoga;
}
