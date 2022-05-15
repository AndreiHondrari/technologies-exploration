docker build --tag assembler:1 .
docker create --name assembler --volume $(pwd):/workspace assembler:1
