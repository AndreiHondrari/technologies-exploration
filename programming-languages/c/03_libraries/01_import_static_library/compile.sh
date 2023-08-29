
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

# compile library
gcc -c some.c -o $TARGET_DIR/some.o

# archive into static library archive
ar -rvs $TARGET_DIR/some.a $TARGET_DIR/some.o

# compile binary
gcc main.c $TARGET_DIR/some.a -o $TARGET_DIR/main.out
