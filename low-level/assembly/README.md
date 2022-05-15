# Assembly

## Lessons learned

### Inputs to subroutines

It is best always to map subroutines arguments in "alphabetical order" (eax,
ebx, ecx, edx) and internally remap the values in between registers.

### Stack can be very useful

Pushing and popping data via the stack can serve multiple purposes:

- state snapshot and restoration at the beginning and end of a subroutine
- enqueue data for processing
- use as a temporary storage medium for intermediary values

### State save and restoration order

Since the stack is a LIFO (last in first out) or FILO (first in last out) type
of memory, it is highly important how you do the state save/restoration. During
restoration you should always pop the registers in the exact reverse order than
they were pushed onto the stack.
