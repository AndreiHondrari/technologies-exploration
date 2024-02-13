# Computation Pipeline - Basic

## Purpose

The one most important reason to compute information using graphic processing units (GPU) or data processing units (DPU) is SIMD - Single Instruction Multiple Data, where data is stored into some buffers / "images", and then submitted to the hardware for parallel processing.

The benefits of this should be obvious -> GPUs and DPUs have many, many, many cores that can ingest large amounts of data and spit results fast.

Possible uses for this are:
* physics simulations
* matrix multiplications
* large data set manipulation
* geometric manipulation of entities

## Flow

* create instance
* select physical device
* initialize logical device
* select computation queue
* load computation shader module
* select memory type index
* make input and output buffers
* setup descriptors for the input and output buffers to have access in the shader module
    * create the descriptor set layout and declare bindings
    * create the descriptor pool
    * allocate descriptor sets with the previously created layout
    * update descriptors on the device by associating buffers with binding point on descriptor set
* setup the compute pipeline
* setup commands
    * create the command pool
    * create the command buffer
    * record commands, while also binding descriptor set containting the two (input and output) descriptors
* copy information into the input buffer
* submit command buffer for execution and wait for device to become idle
* collect results from the output buffer
