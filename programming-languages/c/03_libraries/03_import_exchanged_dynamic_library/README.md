# Dynamic Link Library

## Overview

The idea of a dynamic link library is that the executable code gets fragmented
over several files and not in one big fat binary.

## What happens if you recompile the library

Let's assume that you change the implementation body of the library. If you
recompile this library and overwrite the previous library file, used by the main
binary, then the binary will start using the new implementation when
re-executed.
