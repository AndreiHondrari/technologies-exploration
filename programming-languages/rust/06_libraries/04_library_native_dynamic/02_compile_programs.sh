
TARGET_DIR=target

echo "Compiling main ..."
rustc \
    -L. -L$TARGET_DIR \
    -C rpath \
    main.rs \
    -o $TARGET_DIR/main

echo "Compiling main 2 ..."
rustc \
    -L. -L$TARGET_DIR \
    -l dylib=some \
    -C rpath \
    main2.rs \
    -o $TARGET_DIR/main2
