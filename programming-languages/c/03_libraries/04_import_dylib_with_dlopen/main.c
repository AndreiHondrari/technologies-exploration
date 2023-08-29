
#include <stdio.h>
#include <stdlib.h>
// #include <link.h>
#include <dlfcn.h>


int main(int argc, char const *argv[]) {

  // initialization of the dynamic library
  void * dlhandle = dlopen("./libsome.dylib", RTLD_NOW);

  if (dlhandle == NULL) {
    fprintf(stderr, "dlopen() failed: %s\n", dlerror());
    exit(EXIT_FAILURE);
  }

  printf("dlhandle pointer: %p\n", dlhandle);

  // obtain function from dynamic library
  void (*doSomething)() = dlsym(dlhandle, "doSomething");

  if (doSomething == NULL) {
    fprintf(stderr, "dlsym could not load doSomething() function: %s\n", dlerror());
    exit(EXIT_FAILURE);
  }

  printf("Func pointer: %p\n", doSomething);

  printf("Call library function ...\n");
  doSomething();

  return 0;
}
