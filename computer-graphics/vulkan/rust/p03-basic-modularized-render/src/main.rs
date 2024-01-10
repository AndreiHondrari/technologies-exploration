
use ash::*;
use ash::extensions::ext::DebugUtils;
use ash::extensions::khr::Swapchain;
use ash::vk::Handle;

use sdl2;

mod graphics;
mod window_management;

const AMOUNT_IMAGES: u32 = 1;

const VERTICES: &[f32] = &[
    0.0, 0.1,
    -0.1, -0.1,
    0.1, -0.1,

    0.5, 0.5,
    0.9, 0.5,
    0.9, 0.9,
];

const VERTEX_COUNT: u32 = VERTICES.len() as u32 / 2;


fn setup_window() -> (
    sdl2::Sdl, 
    sdl2::video::Window
) {
    let sdl2_context: sdl2::Sdl = sdl2::init().unwrap();
    let video_subsystem: sdl2::VideoSubsystem = sdl2_context.video().unwrap();
    let mut window_builder: sdl2::video::WindowBuilder = video_subsystem.window("more stuff", 700, 700);

    let window: sdl2::video::Window = window_builder
        .vulkan()
        .position_centered()
        .build().unwrap();

    return (sdl2_context, window);
}

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

fn show_details(
    entry: &Entry
) {
    graphics::display::show_version(&entry);

    // enumerate extension properties
    let properties: Vec<vk::ExtensionProperties> = entry.enumerate_instance_extension_properties(None).unwrap();
    graphics::display::list_available_extension_properties(&properties);

    // enumerate layer properties
    let layer_properties: Vec<vk::LayerProperties> = entry.enumerate_instance_layer_properties().unwrap();
    graphics::display::list_available_layer_properties(&layer_properties);
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

fn select_physical_device(
    physical_devices: &Vec<vk::PhysicalDevice>
) -> vk::PhysicalDevice {
    let selected_physical_device: vk::PhysicalDevice = physical_devices[0];  // select GPU card here
    return selected_physical_device;
}

fn show_physical_device_details(
    instance: &Instance, 
    physical_devices: &Vec<vk::PhysicalDevice>
) {
    graphics::display::list_available_physical_devices(&instance, &physical_devices, false, false);
    graphics::display::list_queue_family_properties(&instance, &physical_devices);
}

fn handle_physical_devices(
    instance: &Instance
) -> vk::PhysicalDevice {
    let physical_devices: Vec<vk::PhysicalDevice> =  get_physical_devices(instance);
    let selected_physical_device: vk::PhysicalDevice = select_physical_device(&physical_devices);
    show_physical_device_details(instance, &physical_devices);

    return selected_physical_device;
}

fn select_graphics_queue(
    device: &Device
) -> vk::Queue {
    println!("Get graphics queue ...");

    unsafe{
        device.get_device_queue(0, 0)
    }
}

fn make_sdl_vulkan_surface(
    instance: &Instance, 
    window: &sdl2::video::Window
) -> vk::SurfaceKHR {
    let handle: u64 = instance.handle().as_raw();
    let sdl_surface: u64 = window_management::surface::create_surface(&window, handle);
    let surface_handle: vk::SurfaceKHR = vk::SurfaceKHR::from_raw(sdl_surface);
    
    return surface_handle;
}

fn handle_surface(
    entry: &Entry,
    instance: &Instance, 
    window: &sdl2::video::Window,
    selected_physical_device: vk::PhysicalDevice
) -> (
    vk::SurfaceKHR,
    vk::SurfaceCapabilitiesKHR
 ) {
    println!("Make a vulkan surface ...");
    let surface_handle: vk::SurfaceKHR = make_sdl_vulkan_surface(instance, window);
    
    println!("SURFACE HANDLE {:?}", surface_handle);

    let surface: extensions::khr::Surface = ash::extensions::khr::Surface::new(&entry, &instance);

    graphics::display::display_surface_support(&surface, surface_handle, selected_physical_device);
    
    let surface_capabilities: vk::SurfaceCapabilitiesKHR = unsafe {
        surface.get_physical_device_surface_capabilities(selected_physical_device, surface_handle).unwrap()
    };

    graphics::display::list_surface_capabilities(&surface_capabilities);
    graphics::display::list_surface_present_modes(&surface, surface_handle, selected_physical_device);

    // formats
    let surface_formats: Vec<vk::SurfaceFormatKHR> = unsafe {
        surface.get_physical_device_surface_formats(selected_physical_device, surface_handle).unwrap()
    };
    graphics::display::list_surface_formats(&surface_formats);
    
    // let selected_surface_format: &vk::SurfaceFormatKHR = surface_formats.first().unwrap();

    return (surface_handle, surface_capabilities);
}

fn handle_memory(
    instance: &Instance,
    device: &Device,
    selected_physical_device: vk::PhysicalDevice,
) -> (
    vk::Buffer,
    vk::DeviceMemory,
    *mut f32
) {
    let device_memory_properties: vk::PhysicalDeviceMemoryProperties = unsafe {
        instance.get_physical_device_memory_properties(selected_physical_device)
    };
    
    graphics::display::list_memory_properties(device_memory_properties);

    let selected_memory_type_index: u32 = graphics::memory::select_memory_type_index(device_memory_properties)
        .expect("Memory type index");
    
    println!("Selected memory type with index: {:?}", selected_memory_type_index);

    // create vertex buffer

    let size_vertex_data: vk::DeviceSize = std::mem::size_of_val(&VERTICES) as u64;
    println!("-> vertex data size: {:?}", size_vertex_data);

    let vertex_buffer: vk::Buffer = graphics::memory::create_device_buffer(&device, size_vertex_data, vk::BufferUsageFlags::VERTEX_BUFFER);

    let vertex_buffer_memory: vk::DeviceMemory;
    let vertex_mapped_memory: *mut f32;
    
    (
        vertex_buffer_memory,
        vertex_mapped_memory 
    ) = graphics::memory::allocate_memory(
        &device, 
        vertex_buffer, 
        selected_memory_type_index, 
        size_vertex_data
    );

    return (
        vertex_buffer,
        vertex_buffer_memory,
        vertex_mapped_memory
    )
    
}

fn setup_commands(
    device: &Device,
    framebuffers: &Vec<vk::Framebuffer>,
    render_pass: vk::RenderPass ,
    surface_capabilities: &vk::SurfaceCapabilitiesKHR,
    graphics_pipeline: vk::Pipeline ,
    vertex_buffer: &vk::Buffer 
) -> (
  vk::CommandPool,
  Vec<vk::CommandBuffer>
) {
    let pool: vk::CommandPool = graphics::command::create_command_pool(&device);
    let command_buffers: Vec<vk::CommandBuffer> = graphics::command::create_command_buffer(
        &device, 
        pool, 
        framebuffers.len()
    );

    for (i, &cmd_buf) in command_buffers.iter().enumerate() {
        let framebuf: vk::Framebuffer = framebuffers[i];
        graphics::command::add_instructions(
            &device, 
            cmd_buf, 
            render_pass, 
            framebuf, 
            surface_capabilities.current_extent,
            graphics_pipeline,
            VERTEX_COUNT,
            &vertex_buffer
        );
    }

    return (pool, command_buffers);
}

fn do_first_draw(
    device: &Device,
    graphics_queue: vk::Queue,
    swapchain_loader: &Swapchain,
    swapchain: vk::SwapchainKHR,
    sync_gates: &graphics::sync::SyncGates,
    command_buffers: &Vec<vk::CommandBuffer>
) {
    let current_image_index: usize = 0;
    
    let acquired_image_index: u32;
    (acquired_image_index, _) = unsafe {
        swapchain_loader.acquire_next_image(
            swapchain, 
            std::u64::MAX, 
            sync_gates.image_available[current_image_index as usize], 
            vk::Fence::null()
        ).unwrap()
    };

    unsafe {
        device.wait_for_fences(
            &[sync_gates.may_begin_drawing[current_image_index]],
            true,
            std::u64::MAX
        ).ok();

        device.reset_fences(
            &[sync_gates.may_begin_drawing[current_image_index]]
        ).ok();
    }

    let semaphores_available = [sync_gates.image_available[current_image_index]];
    let waiting_stages = [vk::PipelineStageFlags::COLOR_ATTACHMENT_OUTPUT];
    let semaphores_finished = [sync_gates.rendering_finished[current_image_index]];
    let target_command_buffers = [command_buffers[acquired_image_index as usize]];
    let submit_info = [
        vk::SubmitInfo::builder()
            .wait_semaphores(&semaphores_available)
            .wait_dst_stage_mask(&waiting_stages)
            .command_buffers(&target_command_buffers)
            .signal_semaphores(&semaphores_finished)
            .build()
    ];

    unsafe {
        device.queue_submit(
            graphics_queue, 
            &submit_info, 
            sync_gates.may_begin_drawing[current_image_index]
        ).ok();
    };

    let present_info = vk::PresentInfoKHR::builder()
        .wait_semaphores(&semaphores_finished)
        .swapchains(&[swapchain])
        .image_indices(&[acquired_image_index])
        .build();

    unsafe {
        swapchain_loader.queue_present(graphics_queue, &present_info).ok()
    };
}


fn main() {
    println!("#### START INFO LISTING #### \n");

    let sdl2_context: sdl2::Sdl;
    let window: sdl2::video::Window;
    
    (sdl2_context, window) = setup_window();

    // entry to access Vulkan functions
    let entry: Entry = load_entry().expect("Loaded entry");

    show_details(&entry);

    // create the vulkan instance
    let instance: Instance = graphics::instance::create_instance(&entry);

    let debug_utils_loader: DebugUtils;
    let debug_callback: vk::DebugUtilsMessengerEXT;
    (debug_utils_loader, debug_callback) = setup_debug(&entry, &instance);

    let selected_physical_device: vk::PhysicalDevice = handle_physical_devices(&instance);    
    
    let device: Device = graphics::logical_device::create_logical_device(&instance, selected_physical_device);
    
    let graphics_queue: vk::Queue = select_graphics_queue(&device);

    let surface_handle: vk::SurfaceKHR;
    let surface_capabilities: vk::SurfaceCapabilitiesKHR;

    (
        surface_handle,
        surface_capabilities
    ) = handle_surface(
        &entry, 
        &instance, 
        &window, 
        selected_physical_device
    );

    let selected_format = vk::Format::B8G8R8A8_SRGB;
    let color_space = vk::ColorSpaceKHR::SRGB_NONLINEAR;

    // SWAPCHAIN
    let swapchain_loader: Swapchain;
    let swapchain: vk::SwapchainKHR;
    
    (swapchain_loader, swapchain) = graphics::swapchain::create_swapchain(
        &instance, 
        &device, 
        surface_handle, 
        AMOUNT_IMAGES,
        surface_capabilities, 
        selected_format,
        color_space
    );

    println!("Swapchain images creation ...");
    let swapchain_images: Vec<vk::Image> = graphics::swapchain::create_images(&swapchain_loader, swapchain);
    println!("Created {} swapchain images!", &swapchain_images.len());
    
    let swapchain_imageviews: Vec<vk::ImageView> = graphics::swapchain::create_image_views(&device, &swapchain_images, selected_format);

    // create shaders
    let vert_module: vk::ShaderModule;
    let frag_module: vk::ShaderModule;
    (vert_module, frag_module) = graphics::shaders::get_shaders(&device);

    
    let vertex_buffer: vk::Buffer;
    let vertex_buffer_memory: vk::DeviceMemory;
    let vertex_mapped_memory: *mut f32;

    (
        vertex_buffer,
        vertex_buffer_memory,
        vertex_mapped_memory
    ) = handle_memory(
        &instance, 
        &device,
        selected_physical_device
    );

    // create pipeline
    let graphics_pipeline: vk::Pipeline;
    let pipeline_layout: vk::PipelineLayout;
    let render_pass: vk::RenderPass;
    (
        graphics_pipeline,
        pipeline_layout,
        render_pass
    ) = graphics::pipeline::create_pipeline(&device, surface_capabilities, selected_format, vert_module, frag_module);

    let framebuffers: Vec<vk::Framebuffer> = graphics::framebuffers::create_framebuffers(
        &device,
        &swapchain_imageviews,
        &surface_capabilities,
        render_pass
    );

    let command_pool: vk::CommandPool;
    let command_buffers: Vec<vk::CommandBuffer>;
    (
        command_pool,
        command_buffers
    ) = setup_commands(
        &device, 
        &framebuffers,
        render_pass,
        &surface_capabilities,
        graphics_pipeline,
        &vertex_buffer
    );
       
    // synchronization setup
    let sync_gates: graphics::sync::SyncGates = graphics::sync::setup_synchronization(&device, &swapchain_images);

    println!("⚠︎ Finished setting up vulkan structures.");

    // first draw

    // TODO test TO SEE
    unsafe {
        vertex_mapped_memory.copy_from_nonoverlapping(
            VERTICES.as_ptr(), 
            VERTICES.len()
        );
    };

    do_first_draw(
        &device, 
        graphics_queue, 
        &swapchain_loader, 
        swapchain, 
        &sync_gates, 
        &command_buffers
    );
 
    println!("Running main loop ... (press escape or close to quit program)");
    window_management::engine::run_main_loop(&sdl2_context);

    // --- CLEANUP ---
    unsafe{
        println!("{}", "-".repeat(50));

        device.device_wait_idle().ok();

        for fence in sync_gates.may_begin_drawing {
            device.destroy_fence(fence, None);
        }

        for semaphore in sync_gates.rendering_finished {
            device.destroy_semaphore(semaphore, None)
        }

        for semaphore in sync_gates.image_available {
            device.destroy_semaphore(semaphore, None)
        }

        device.destroy_command_pool(command_pool, None);

        for framebuffer in framebuffers {
            device.destroy_framebuffer(framebuffer, None);
        }

        device.destroy_buffer(vertex_buffer, None);

        device.unmap_memory(vertex_buffer_memory);
        device.free_memory(vertex_buffer_memory, None);
        
        device.destroy_render_pass(render_pass, None);
        device.destroy_pipeline_layout(pipeline_layout, None);
        device.destroy_pipeline(graphics_pipeline, None);

        device.destroy_shader_module(vert_module, None);
        device.destroy_shader_module(frag_module, None);

        for image_view in swapchain_imageviews { 
            device.destroy_image_view(image_view, None);
        };
        swapchain_loader.destroy_swapchain(swapchain, None);
        
        device.destroy_device(None);
        debug_utils_loader.destroy_debug_utils_messenger(debug_callback, None);
    };
    
    println!("\n--- FIN ---");
}