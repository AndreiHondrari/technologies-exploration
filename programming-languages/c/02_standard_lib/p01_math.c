#include <math.h>

const float PI = 3.1415926;

void show_sine(float arg) {
    float y = sinf(arg);
    printf("sin(%f) -> %f\n", arg, y);
}

int main(int argc, char const *argv[])
{
    show_sine(PI);
    show_sine(PI / 2);
    show_sine(PI * 2);
    return 0;
}
