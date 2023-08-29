
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

rustc --crate-type rlib --out-dir $TARGET_DIR some.rs
