
use std::process::exit;

use ash::*;
use ash::extensions::ext::DebugUtils;

use ash::extensions::khr::Swapchain;
use ash::vk::{Handle, ShaderModule};
use sdl2;

use vk_shader_macros::include_glsl;

// use crate::window_management::render;

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


fn main() {
    println!("#### START INFO LISTING #### \n");

    let sdl2_context: sdl2::Sdl = sdl2::init().unwrap();
    let video_subsystem = sdl2_context.video().unwrap();
    let mut window_builder = video_subsystem.window("more stuff", 700, 700);

    let window: sdl2::video::Window = window_builder
        .vulkan()
        .position_centered()
        .build().unwrap();

    // entry to access Vulkan functions
    let entry_result: Result<Entry, LoadingError> = unsafe { Entry::load() };

    if entry_result.is_err() {
        println!("COULD NOT LOAD ENTRY");
        println!("{:?}", entry_result.as_ref().err());
        exit(123);
    }

    let entry: Entry = entry_result.unwrap();
    
    graphics::display::show_version(&entry);

    // enumerate extension properties
    let properties: Vec<vk::ExtensionProperties> = entry.enumerate_instance_extension_properties(None).unwrap();
    graphics::display::list_available_extension_properties(&properties);

    // enumerate layer properties
    let layer_properties: Vec<vk::LayerProperties> = entry.enumerate_instance_layer_properties().unwrap();
    graphics::display::list_available_layer_properties(&layer_properties);
    
    // create the vulkan instance
    let instance: Instance = graphics::instance::create_instance(&entry);

    // setup debug
    let debug_utils_loader: DebugUtils = DebugUtils::new(&entry, &instance);
    let debug_callback: vk::DebugUtilsMessengerEXT = graphics::debug_utils::setup_debug(&debug_utils_loader);

    // get devices via the instance
    let physical_devices: Vec<vk::PhysicalDevice> = unsafe{instance.enumerate_physical_devices().unwrap()};
    graphics::display::list_available_physical_devices(&instance, &physical_devices, false, false);

    graphics::display::list_queue_family_properties(&instance, &physical_devices);

    let selected_physical_device: vk::PhysicalDevice = physical_devices[0];  // select GPU card here
    
    let device: Device = graphics::logical_device::create_logical_device(&instance, selected_physical_device);

    println!("Get graphics queue ...");
    let graphics_queue: vk::Queue = unsafe{
        device.get_device_queue(0, 0)
    };

    // MAKE SURFACE
    println!("Make a vulkan surface ...");
    let handle: u64 = instance.handle().as_raw();
    let sdl_surface: u64 = window_management::surface::create_surface(&window, handle);
    let surface_handle: vk::SurfaceKHR = vk::SurfaceKHR::from_raw(sdl_surface);
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
    let selected_format = vk::Format::B8G8R8A8_SRGB;
    let color_space = vk::ColorSpaceKHR::SRGB_NONLINEAR;
    // let selected_surface_format: &vk::SurfaceFormatKHR = surface_formats.first().unwrap();
    // let selected_format: vk::Format = selected_surface_format.format;
    // let color_space: vk::ColorSpaceKHR = selected_surface_format.color_space;
    

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
    // let vert_shader_code: Vec<u32> = graphics::shaders::read_file(String::from("src/shaders/vert.spv")).unwrap();
    // let frag_shader_code: Vec<u32> = graphics::shaders::read_file(String::from("src/shaders/frag.spv")).unwrap();

    let vert_shader_code: &[u32] = include_glsl!("./src/shaders/shader.vert");
    let frag_shader_code: &[u32] = include_glsl!("./src/shaders/shader.frag", kind: frag);

    let vert_shader_code: Vec<u32> = vert_shader_code.to_vec();
    let frag_shader_code: Vec<u32> = frag_shader_code.to_vec();

    let vert_module: ShaderModule = graphics::shaders::create_shader_module(&device, &vert_shader_code);
    let frag_module: ShaderModule = graphics::shaders::create_shader_module(&device, &frag_shader_code);

    // MEMORY STUFF

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

    let vertex_mapped_memory: *mut f32;
    let vertex_buffer_memory: vk::DeviceMemory;
    
    (
        vertex_mapped_memory, 
        vertex_buffer_memory
    ) = graphics::memory::allocate_memory(
        &device, 
        vertex_buffer, 
        selected_memory_type_index, 
        size_vertex_data
    );

    unsafe {
        vertex_mapped_memory.copy_from_nonoverlapping(
            VERTICES.as_ptr(), 
            VERTICES.len()
        );
    }

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

    let pool: vk::CommandPool = graphics::command::create_command_pool(&device);
    let command_buffers: Vec<vk::CommandBuffer> = graphics::command::create_command_buffer(&device, pool, framebuffers.len());

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

    // synchronization setup
    let mut image_available: Vec<vk::Semaphore> = vec![];
    let mut rendering_finished: Vec<vk::Semaphore> = vec![];
    let mut may_begin_drawing: Vec<vk::Fence> = vec![];
    
    let semaphore_create_info = vk::SemaphoreCreateInfo::builder()
        .build();

    let fence_create_info = vk::FenceCreateInfo::builder()
        .flags(vk::FenceCreateFlags::SIGNALED)
        .build();

    for _ in 0..swapchain_images.len() {
        let semaphore_available: vk::Semaphore = unsafe {
            device.create_semaphore(&semaphore_create_info, None).unwrap()
        };
    
        let semaphore_finished: vk::Semaphore = unsafe {
            device.create_semaphore(&semaphore_create_info, None).unwrap()
        };
    
        image_available.push(semaphore_available);
        rendering_finished.push(semaphore_finished);
    
        let drawing_fence: vk::Fence = unsafe {
            device.create_fence(&fence_create_info, None).unwrap()
        };
        may_begin_drawing.push(drawing_fence);
    }

    // first draw

    let current_image_index: usize = 0;
    
    let acquired_image_index: u32;
    (acquired_image_index, _) = unsafe {
        swapchain_loader.acquire_next_image(
            swapchain, 
            std::u64::MAX, 
            image_available[current_image_index as usize], 
            vk::Fence::null()
        ).unwrap()
    };

    unsafe {
        device.wait_for_fences(
            &[may_begin_drawing[current_image_index]],
            true,
            std::u64::MAX
        ).ok();

        device.reset_fences(
            &[may_begin_drawing[current_image_index]]
        ).ok();
    }

    let semaphores_available = [image_available[current_image_index]];
    let waiting_stages = [vk::PipelineStageFlags::COLOR_ATTACHMENT_OUTPUT];
    let semaphores_finished = [rendering_finished[current_image_index]];
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
            may_begin_drawing[current_image_index]
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

    println!("⚠︎ Finished setting up vulkan structures.");

    println!("Running main loop ... (press escape or close to quit program)");
    window_management::engine::run_main_loop(&sdl2_context);

    // --- CLEANUP ---
    unsafe{
        println!("{}", "-".repeat(50));

        device.device_wait_idle().ok();

        for fence in may_begin_drawing {
            device.destroy_fence(fence, None);
        }

        for semaphore in rendering_finished {
            device.destroy_semaphore(semaphore, None)
        }

        for semaphore in image_available {
            device.destroy_semaphore(semaphore, None)
        }

        device.destroy_command_pool(pool, None);

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