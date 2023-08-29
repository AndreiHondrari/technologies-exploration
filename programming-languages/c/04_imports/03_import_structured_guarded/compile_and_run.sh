
TARGET_DIR=target
PROG_NAME=prog.out

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

gcc 01_sub_lib.c 02_lib.c main.c -g -o $TARGET_DIR/$PROG_NAME -Wall

./$TARGET_DIR/$PROG_NAME
