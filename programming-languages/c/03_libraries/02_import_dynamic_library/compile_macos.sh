
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

# compile library
# some arguments are passed to 'ld' linker

# -install_name is to force a "relative path" that is stored inside the
# .dylib to guard against bad reference

# by default install name is the path passed to the -o argument
gcc -dynamiclib -install_name libsome.dylib some.c -o $TARGET_DIR/libsome.dylib

# compile binary
gcc main.c -lsome -L. -L./$TARGET_DIR -o $TARGET_DIR/main.out
