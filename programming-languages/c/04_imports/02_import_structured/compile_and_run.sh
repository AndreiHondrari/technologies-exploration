
TARGET_DIR=target
PROG_NAME=prog.out

if [ ! -d $TARGET_DIR ]; then
    mkdir $TARGET_DIR
fi

gcc lib.c main.c -o $TARGET_DIR/$PROG_NAME -Wall

./$TARGET_DIR/$PROG_NAME
