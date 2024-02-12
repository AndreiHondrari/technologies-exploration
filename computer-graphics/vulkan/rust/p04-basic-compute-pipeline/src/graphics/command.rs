use ash::*;


pub fn create_command_pool(device: &Device) -> vk::CommandPool{
    let pool_create_info: vk::CommandPoolCreateInfo = vk::CommandPoolCreateInfo::builder()
        .queue_family_index(0)
        .flags(vk::CommandPoolCreateFlags::RESET_COMMAND_BUFFER)
        .build();

    let command_pool: vk::CommandPool = unsafe {
        device
            .create_command_pool(&pool_create_info, None)
            .unwrap()
    };

    command_pool
}