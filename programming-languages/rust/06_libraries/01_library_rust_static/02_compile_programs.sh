
TARGET_DIR=target

rustc --extern gandalf=$TARGET_DIR/libsome.rlib --out-dir $TARGET_DIR main.rs

rustc -L$TARGET_DIR --out-dir $TARGET_DIR main2.rs
