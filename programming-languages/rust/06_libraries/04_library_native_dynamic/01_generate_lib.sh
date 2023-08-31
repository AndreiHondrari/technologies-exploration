

TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

rustc \
    --crate-type cdylib \
    --crate-name some \
    -C prefer-dynamic \
    -C "link-args=-Wl,-install_name,libsome.dylib" \
    some.rs \
    -o $TARGET_DIR/libsome.dylib
