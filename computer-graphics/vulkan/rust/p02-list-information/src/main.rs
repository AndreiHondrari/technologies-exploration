
use ash::*;
use ash::extensions::ext::DebugUtils;

mod display;
mod create;
mod debug_utils;
mod logical_device;


fn main() {
    println!("#### START INFO LISTING #### \n");

    // entry to access Vulkan functions
    let entry: Entry = unsafe { Entry::load().unwrap() };
    
    display::show_version(&entry);

    // enumerate extension properties
    let properties: Vec<vk::ExtensionProperties> = entry.enumerate_instance_extension_properties(None).unwrap();
    display::list_available_extension_properties(&properties);

    // enumerate layer properties
    let layer_properties: Vec<vk::LayerProperties> = entry.enumerate_instance_layer_properties().unwrap();
    display::list_available_layer_properties(&layer_properties);
    
    // create the vulkan instance
    let instance: Instance = create::create_instance(&entry);

    // setup debug
    let debug_utils_loader: DebugUtils = DebugUtils::new(&entry, &instance);
    let debug_callback: vk::DebugUtilsMessengerEXT = debug_utils::setup_debug(&debug_utils_loader);

    // get devices via the instance
    let physical_devices: Vec<vk::PhysicalDevice> = unsafe{instance.enumerate_physical_devices().unwrap()};
    display::list_available_physical_devices(&instance, &physical_devices, true, true);

    display::list_queue_family_properties(&instance, &physical_devices);
    
    let device: Device = logical_device::create_logical_device(&instance, physical_devices[0]);

    println!("Get graphics queue ...\n");
    let _graphics_queue: vk::Queue = unsafe{device.get_device_queue(0, 0)};

    println!(">>> AFTER EVERYTHING");

    // --- CLEANUP ---
    unsafe{
        device.destroy_device(None);
        debug_utils_loader.destroy_debug_utils_messenger(debug_callback, None);
    };
    
    println!("\n--- FIN ---");
}
