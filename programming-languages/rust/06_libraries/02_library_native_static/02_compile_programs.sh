
TARGET_DIR=target

gcc -lsome -L$TARGET_DIR main.c -o $TARGET_DIR/main_c.out

rustc -lsome -L$TARGET_DIR main.rs -o $TARGET_DIR/main_rust.out

rustc -L$TARGET_DIR main2.rs -o $TARGET_DIR/main_rust2.out
