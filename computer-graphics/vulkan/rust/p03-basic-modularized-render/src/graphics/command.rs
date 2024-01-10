use ash::{vk::{self, CommandPool, CommandBuffer, Framebuffer}, Device};

pub fn create_command_pool(device: &Device) -> CommandPool{
    let pool_create_info: vk::CommandPoolCreateInfo = vk::CommandPoolCreateInfo::builder()
        .queue_family_index(0)
        .flags(vk::CommandPoolCreateFlags::RESET_COMMAND_BUFFER)
        .build();

    let command_pool: CommandPool = unsafe {
        device
            .create_command_pool(&pool_create_info, None)
            .unwrap()
    };

    command_pool
}

pub fn create_command_buffer(
    device: &Device,
    pool: CommandPool,
    amount: usize
) -> Vec<vk::CommandBuffer> {
    let cmd_buf_alloc_info: vk::CommandBufferAllocateInfo = vk::CommandBufferAllocateInfo::builder()
        .command_pool(pool)
        .command_buffer_count(amount as u32)
        .build();

    let command_buffers: Vec<vk::CommandBuffer> = unsafe {
        device
            .allocate_command_buffers(&cmd_buf_alloc_info).unwrap()
    };

    command_buffers
}

pub fn add_instructions(
    device: &Device,
    command_buffer: CommandBuffer,
    render_pass: vk::RenderPass,
    framebuffer: Framebuffer,
    extent: vk::Extent2D,
    pipeline: vk::Pipeline,
    vertex_count: u32,
    vertex_buffer: &vk::Buffer,
    color_buffer: &vk::Buffer,
) {


    unsafe {
        // begin commands
        let cmd_buf_begin_info = vk::CommandBufferBeginInfo::builder()
            .build();
        
        device.begin_command_buffer(command_buffer, &cmd_buf_begin_info).ok();

        let clear_values = [
            vk::ClearValue {
                color: vk::ClearColorValue {
                    float32: [0.0, 0.0, 0.0, 1.0]
                }
            }
        ];
        
        // begin render pass 
        let render_pass_begin = vk::RenderPassBeginInfo::builder()
            .render_pass(render_pass)
            .framebuffer(framebuffer)
            .render_area(vk::Rect2D {
                offset: vk::Offset2D {x: 0, y: 0 },
                extent: extent  
            })
            .clear_values(&clear_values)
            .build();

        device.cmd_begin_render_pass(command_buffer, &render_pass_begin, vk::SubpassContents::INLINE);
        
        // bind pipeline
        device.cmd_bind_pipeline(
            command_buffer,
            vk::PipelineBindPoint::GRAPHICS, 
            pipeline
        );

        // 
        device.cmd_bind_vertex_buffers(command_buffer, 0, &[*vertex_buffer], &[0]);
        device.cmd_bind_vertex_buffers(command_buffer, 1, &[*color_buffer], &[0]);
        
        // draw
        device.cmd_draw(command_buffer, vertex_count, 1, 0, 0);

        // end render pass
        device.cmd_end_render_pass(command_buffer);

        // end commands
        device.end_command_buffer(command_buffer).ok();
    }
}