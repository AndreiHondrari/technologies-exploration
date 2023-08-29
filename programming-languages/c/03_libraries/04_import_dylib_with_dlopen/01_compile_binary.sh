
TARGET_DIR=target

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi


gcc main.c -ldl -o $TARGET_DIR/main.out
