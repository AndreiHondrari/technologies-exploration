
TARGET_DIR=target

# compile binary
gcc main.c -lsome -L. -L./$TARGET_DIR -o $TARGET_DIR/main.out
