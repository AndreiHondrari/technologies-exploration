
use ash::{vk::DescriptorSet, *};


/*
The context is to preserve the memory held by _descriptor_buffer_infos intact,
as the pointer is passed over to Vulkan. -> Keeps it safe.
*/
pub struct WriteDescriptorSetContext {
    _descriptor_buffer_infos: Vec<vk::DescriptorBufferInfo>,
    write_descriptor_set: vk::WriteDescriptorSet,
}

impl WriteDescriptorSetContext {
    pub fn new(
        buffer: vk::Buffer,
        descriptor_set: vk::DescriptorSet,
        binding: u32
    ) -> Self {
        let descriptor_buffer_info: vk::DescriptorBufferInfo = vk::DescriptorBufferInfo::builder()
            .buffer(buffer)
            .range(vk::WHOLE_SIZE)
            .build();

        let buffer_infos: Vec<vk::DescriptorBufferInfo> = vec![descriptor_buffer_info];

        let write_descriptor_set = vk::WriteDescriptorSet::builder()
            .buffer_info(buffer_infos.as_slice())
            .descriptor_type(vk::DescriptorType::STORAGE_BUFFER)
            .dst_set(descriptor_set)
            .dst_binding(binding)
            .build();

        Self {
            // _buffer_info: dinfo,
            _descriptor_buffer_infos: buffer_infos,
            write_descriptor_set: write_descriptor_set,
        }
    }
}


pub fn create_layout(
    device: &Device, 
    count_bindings: u32
) -> vk::DescriptorSetLayout {

    let mut bindings: Vec<vk::DescriptorSetLayoutBinding> = vec![];
    
    for binding_index in 0..count_bindings {
        println!("Bind {binding_index:?}");
        let new_binding = vk::DescriptorSetLayoutBinding::builder()
            .binding(binding_index)
            .descriptor_type(vk::DescriptorType::STORAGE_BUFFER)
            .descriptor_count(1)
            .stage_flags(vk::ShaderStageFlags::COMPUTE)
            .build();

        bindings.push(new_binding);
    };

    let descriptor_set_layout_create_info = vk::DescriptorSetLayoutCreateInfo::builder()
        .bindings(bindings.as_slice())
        .build();

    return unsafe {
        device.create_descriptor_set_layout(
            &descriptor_set_layout_create_info, 
            None
        ).expect("Descriptor Set Layout")
    };
}


pub fn create_pool(
    device: &Device,
    descriptor_count: u32,
) -> vk::DescriptorPool {
    let pool_size = vk::DescriptorPoolSize::builder()
        .descriptor_count(descriptor_count)
        .ty(vk::DescriptorType::STORAGE_BUFFER)
        .build();

    let ds_pool_create_info = vk::DescriptorPoolCreateInfo::builder()
        .pool_sizes(&[pool_size])
        .max_sets(1)
        .build();

    return unsafe {
        device.create_descriptor_pool(&ds_pool_create_info, None).unwrap()
    };
}

pub fn allocate_descriptor_sets(
    device: &Device,
    layout: vk::DescriptorSetLayout,
    pool: vk::DescriptorPool
) -> Vec<DescriptorSet> {
    let ds_alloc = vk::DescriptorSetAllocateInfo::builder()
        .descriptor_pool(pool)
        .set_layouts(&[layout])
        .build();

    return unsafe {
        device.allocate_descriptor_sets(&ds_alloc).expect("Descriptor Sets Vector")
    };
}


pub fn update_descriptor_sets(
    device: &Device,
    input_write_descriptor_set_ctx: WriteDescriptorSetContext,
    output_write_descriptor_set_ctx: WriteDescriptorSetContext,
) {
    unsafe {
        device.update_descriptor_sets(
            &[
                input_write_descriptor_set_ctx.write_descriptor_set, 
                output_write_descriptor_set_ctx.write_descriptor_set,
            ],
            &[]
        );
    }
}