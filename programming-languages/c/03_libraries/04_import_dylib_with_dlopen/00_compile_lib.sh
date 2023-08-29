
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

echo "COMPILING" $1

# compile library
gcc -dynamiclib -install_name libsome.dylib $1 -o $TARGET_DIR/libsome.dylib
