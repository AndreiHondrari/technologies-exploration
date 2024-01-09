use sdl2;


pub fn create_surface(
    window: &sdl2::video::Window, 
    handle: u64
) -> u64 {
    let sdl_surface: Result<sdl2::video::VkSurfaceKHR, String> = window.vulkan_create_surface(handle as usize);
    
    if sdl_surface.is_err() {
        println!("SDL SURFACE CREATE ERROR {:?}", sdl_surface.unwrap_err());
        std::process::exit(0);
    }

    sdl_surface.unwrap()
}