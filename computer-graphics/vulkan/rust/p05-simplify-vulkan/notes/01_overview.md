# Simplify Vulkan API

## Reason

Right now Vulkan API is way too verbose and there are many edge cases for which
the client is responsible when using it.

For example:

- When creating a descriptor pool (via the create info), if the pool size count
  is not 0 then the array of pool sizes must have the same length as indicated
  by the pool size count -> this could easily be avoided by simply passing the
  exact length of the array -> it doesn't make sense for the client to be
  responsible for this number

- Trying to record cmd_draw with a compute pipeline bound to the command buffer
  will result in an error since that is an invalid use of the Vulkan API

- Viceversa, trying to record cmd_dispatch with a graphics pipeline will also
  result in an error.

All these invalid use cases of the Vulkan API can be abstracted away.

## What to simplify

- counts of arrays
- correspondence between layouts and the existence of instances of various
  structures
- necessary information or structures before calling functions
