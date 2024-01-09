

use ash::{*, vk::DeviceMemory};

pub fn select_memory_type_index(
    memory_properties: vk::PhysicalDeviceMemoryProperties
) -> Result<u32, ()> {    
    for index in 0..memory_properties.memory_type_count {
        let memory_type: vk::MemoryType = memory_properties.memory_types[index as usize];

        if memory_type.property_flags.contains(
            vk::MemoryPropertyFlags::HOST_VISIBLE | vk::MemoryPropertyFlags::HOST_COHERENT
        ) {
            return Ok(index);
        }
    }

    Err(())
}

pub fn create_device_buffer(
    device: &Device, 
    size: vk::DeviceSize, 
    usage: vk::BufferUsageFlags
) -> vk::Buffer {
    let buffer_create_info: vk::BufferCreateInfo = vk::BufferCreateInfo::builder()
        .size(size)
        .usage(usage)
        .sharing_mode(vk::SharingMode::EXCLUSIVE)
        .build();

    let buffer: vk::Buffer = unsafe {
        device
            .create_buffer(&buffer_create_info, None)
            .expect("Vertex buffer creation")
    };

    return buffer;
}

pub fn allocate_memory<T>(
    device: &Device, 
    buffer: vk::Buffer,
    memory_type_index: u32,
    memory_size: u64
) -> (*mut T, DeviceMemory) {

    let buffer_memory_requirements: vk::MemoryRequirements = unsafe {
        device.get_buffer_memory_requirements(buffer)
    };
   
    let buffer_memory_allocate_info = vk::MemoryAllocateInfo::builder()
        .allocation_size(buffer_memory_requirements.size)
        .memory_type_index(memory_type_index)
        .build();

    let buffer_memory = unsafe {
        device.allocate_memory(&buffer_memory_allocate_info, None).unwrap()
    };

    unsafe {
        device
            .bind_buffer_memory(buffer, buffer_memory, 0)
            .expect("Bind buffer memory");
    };

    let mapped_memory: *mut T = unsafe {
        device
            .map_memory(
                buffer_memory, 
                0, 
                memory_size, 
                vk::MemoryMapFlags::empty()
            )
            .expect("Map buffer memory") as *mut T
    };

    return (mapped_memory, buffer_memory);
}