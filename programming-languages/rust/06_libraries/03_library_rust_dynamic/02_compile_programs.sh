
TARGET_DIR=target

# doing
# export DYLD_LIBRARY_PATH="$(rustc --print sysroot)/lib:$DYLD_LIBRARY_PATH"
# can be an alternative to '-C rpath'


rustc \
    -L. -L$TARGET_DIR \
    -C rpath \
    -C prefer-dynamic \
    --out-dir $TARGET_DIR \
    main.rs

rustc \
    -L. -L$TARGET_DIR \
    -C rpath \
    --out-dir $TARGET_DIR \
    main2.rs

rustc \
    -L. -L$TARGET_DIR \
    -C rpath \
    --extern=some \
    --out-dir $TARGET_DIR \
    main3.rs
