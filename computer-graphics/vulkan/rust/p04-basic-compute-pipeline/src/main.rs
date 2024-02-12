use ash::*;
use ash::extensions::ext::DebugUtils;

mod graphics;

use graphics::memory::BufferParts;
use graphics::resources::WriteDescriptorSetContext;

const DATA_VALUES: &[u32] = &[
    7, 2, 3, 4, 10, 20, 30, 40,
];

fn load_entry() -> Result<Entry, ()> {
    let entry_result: Result<Entry, LoadingError> = unsafe { Entry::load() };

    if entry_result.is_err() {
        println!("COULD NOT LOAD ENTRY");
        println!("{:?}", entry_result.as_ref().err());
        return Err(());
    }

    let entry: Entry = entry_result.unwrap();

    Ok(entry)
}

fn setup_debug(
    entry: &Entry, 
    instance: &Instance
) -> (
    DebugUtils,
    vk::DebugUtilsMessengerEXT
) {
    let debug_utils_loader: DebugUtils = DebugUtils::new(&entry, &instance);
    let debug_callback: vk::DebugUtilsMessengerEXT = graphics::debug_utils::setup_debug(&debug_utils_loader);

    return (debug_utils_loader, debug_callback);
}

fn get_physical_devices(
    instance: &Instance
) -> Vec<vk::PhysicalDevice> {
    unsafe{
        instance.enumerate_physical_devices().expect("Physical devices")
    }
}

fn handle_physical_devices(
    instance: &Instance
) -> vk::PhysicalDevice {
    let physical_devices: Vec<vk::PhysicalDevice> =  get_physical_devices(instance);
    let selected_physical_device: vk::PhysicalDevice = physical_devices[0];  // select GPU card here

    return selected_physical_device;
}

fn select_queue(
    device: &Device
) -> vk::Queue {
    println!("Get queue ...");

    unsafe{
        device.get_device_queue(0, 0)
    }
}

fn handle_memory_type_index(
    instance: &Instance,
    selected_physical_device: vk::PhysicalDevice,
) -> u32 {
    let device_memory_properties: vk::PhysicalDeviceMemoryProperties = unsafe {
        instance.get_physical_device_memory_properties(selected_physical_device)
    };

    let selected_memory_type_index: u32 = graphics::memory::select_memory_type_index(device_memory_properties)
        .expect("Memory type index");
    
    println!("Selected memory type with index: {:?}", selected_memory_type_index);
    return selected_memory_type_index;
    
}

fn setup_descriptors(
    device: &Device,
    data_buffer: vk::Buffer,
    out_buffer: vk::Buffer,
) -> (
  vk::DescriptorSetLayout,
  vk::DescriptorPool,
  vk::DescriptorSet,
) {
    let descriptor_set_layout: vk::DescriptorSetLayout = graphics::resources::create_layout(
        device,
        2
    );

    let pool = graphics::resources::create_pool(
        device, 
        2
    );

    let descriptor_set: vk::DescriptorSet = *graphics::resources::allocate_descriptor_sets(device, descriptor_set_layout, pool)
        .first().expect("Descriptor Set");

    let input_wds: WriteDescriptorSetContext = WriteDescriptorSetContext::new(data_buffer, descriptor_set, 0);
    let output_wds: WriteDescriptorSetContext = WriteDescriptorSetContext::new(out_buffer, descriptor_set, 1);

    graphics::resources::update_descriptor_sets(&device, input_wds, output_wds);

    return (descriptor_set_layout, pool, descriptor_set);
}

fn setup_commands(
    device: &Device,
    compute_pipeline: vk::Pipeline,
    compute_pipeline_layout: vk::PipelineLayout,
    compute_descriptor_set: vk::DescriptorSet,
) -> (
  vk::CommandPool,
  vk::CommandBuffer,
) {
    let pool: vk::CommandPool = graphics::command::create_command_pool(&device);

    let cmd_buf_alloc_info: vk::CommandBufferAllocateInfo = vk::CommandBufferAllocateInfo::builder()
        .command_pool(pool)
        .command_buffer_count(1)
        .build();

    let command_buffers: Vec<vk::CommandBuffer> = unsafe {
        device
            .allocate_command_buffers(&cmd_buf_alloc_info).unwrap()
    };

    let compute_command_buffer: &vk::CommandBuffer = command_buffers.first().expect("Command buffer");

    unsafe {
        let cmd_buf_begin_info = vk::CommandBufferBeginInfo::builder()
            .build();

        device.begin_command_buffer(
            *compute_command_buffer, 
            &cmd_buf_begin_info
        ).ok();
        
        device.cmd_bind_pipeline(
            *compute_command_buffer, 
            vk::PipelineBindPoint::COMPUTE, 
            compute_pipeline
        );

        device.cmd_bind_descriptor_sets(
            *compute_command_buffer, 
            vk::PipelineBindPoint::COMPUTE, 
            compute_pipeline_layout, 
            0, 
            &[compute_descriptor_set], 
            &[]
        );

        device.cmd_dispatch(*compute_command_buffer, DATA_VALUES.len() as u32, 1, 1);

        device.end_command_buffer(
            *compute_command_buffer
        ).ok();
    }
  
    return (pool, *compute_command_buffer);
}

fn main() {
    println!("#### START INFO LISTING #### \n");

    // entry to access Vulkan functions
    let entry: Entry = load_entry().expect("Loaded entry");

    // create the vulkan instance
    let instance: Instance = graphics::instance::create_instance(&entry);

    let debug_utils_loader: DebugUtils;
    let debug_callback: vk::DebugUtilsMessengerEXT;
    (debug_utils_loader, debug_callback) = setup_debug(&entry, &instance);

    let selected_physical_device: vk::PhysicalDevice = handle_physical_devices(&instance);    
    
    let device: Device = graphics::logical_device::create_logical_device(&instance, selected_physical_device);
    
    let compute_queue: vk::Queue = select_queue(&device);

    // create shaders
    let operation_1_shader_mod: vk::ShaderModule = graphics::shaders::get_comp_shader(&device);

    // create data instances
    let selected_memory_type_index: u32 = handle_memory_type_index(
        &instance, 
        selected_physical_device,
    );

    let data_size: vk::DeviceSize = std::mem::size_of_val(DATA_VALUES) as u64;
    println!("-> data size: {:?}", data_size);

    let data_buffer_parts: BufferParts<u32> = graphics::memory::make_memory(
        &device, 
        data_size, 
        selected_memory_type_index
    );

    let output_buffer_parts: BufferParts<u32> = graphics::memory::make_memory(
        &device, 
        data_size, 
        selected_memory_type_index
    );

    // descriptors
    let descriptor_set_layout: vk::DescriptorSetLayout;
    let descriptor_pool: vk::DescriptorPool;
    let compute_descriptor_set: vk::DescriptorSet;
    
    (
        descriptor_set_layout,
        descriptor_pool,
        compute_descriptor_set
    ) = setup_descriptors(
        &device, 
        data_buffer_parts.buffer, 
        output_buffer_parts.buffer
    );
    
    // create pipeline
    let compute_pipeline: vk::Pipeline;
    let compute_pipeline_layout: vk::PipelineLayout;
    (
        compute_pipeline,
        compute_pipeline_layout,
    ) = graphics::pipeline::create_compute_pipeline(
        &device, 
        operation_1_shader_mod,
        descriptor_set_layout
    );

    let compute_command_pool: vk::CommandPool;
    let compute_command_buffer: vk::CommandBuffer;
    (
        compute_command_pool,
        compute_command_buffer,
    ) = setup_commands(
        &device, 
        compute_pipeline,
        compute_pipeline_layout,
        compute_descriptor_set,
    );

    println!("⚠︎ Finished setting up vulkan structures.");

    // copy data to input buffer
    unsafe {
        data_buffer_parts.mapped.copy_from_nonoverlapping(
            DATA_VALUES.as_ptr(), 
            DATA_VALUES.len()
        );
    };

    // execute computation
    let target_command_buffers = [compute_command_buffer];
    let submit_info = [
        vk::SubmitInfo::builder()
            .command_buffers(&target_command_buffers)
            .build()
    ];

    println!("Submit queue ...");
    unsafe {
        device.queue_submit(
            compute_queue, 
            &submit_info,
            vk::Fence::null()
        ).ok();
    };

    unsafe {
        device.device_wait_idle().ok();
    };
    
    println!("Finished running.");

    let results: [u32; DATA_VALUES.len()] = [0; DATA_VALUES.len()];

    unsafe {
        output_buffer_parts.mapped.copy_to_nonoverlapping(
            results.as_ptr() as *mut u32, 
            DATA_VALUES.len()
        );
    }

    for x in results {
        println!("VALUE: {}", x);
    }

    // --- CLEANUP ---
    println!("Cleaning ...");
    
    unsafe{
        println!("{}", "-".repeat(50));

        device.device_wait_idle().ok();

        device.destroy_descriptor_pool(descriptor_pool, None);
        device.destroy_descriptor_set_layout(descriptor_set_layout, None);

        device.destroy_command_pool(compute_command_pool, None);

        device.destroy_buffer(data_buffer_parts.buffer, None);
        device.unmap_memory(data_buffer_parts.memory);
        device.free_memory(data_buffer_parts.memory, None);

        device.destroy_buffer(output_buffer_parts.buffer, None);
        device.unmap_memory(output_buffer_parts.memory);
        device.free_memory(output_buffer_parts.memory, None);
        
        device.destroy_pipeline_layout(compute_pipeline_layout, None);
        device.destroy_pipeline(compute_pipeline, None);

        device.destroy_shader_module(operation_1_shader_mod, None);

        device.destroy_device(None);
        debug_utils_loader.destroy_debug_utils_messenger(debug_callback, None);
    };
    
    println!("\n--- FIN ---");
}