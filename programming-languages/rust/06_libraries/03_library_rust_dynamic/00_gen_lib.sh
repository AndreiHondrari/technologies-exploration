
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

echo "Generating library for $1"

rustc --crate-type dylib \
    --crate-name some \
    -C prefer-dynamic \
    -C "link-args=-Wl,-install_name,libsome.dylib" \
    $1 \
    -o $TARGET_DIR/libsome.dylib
