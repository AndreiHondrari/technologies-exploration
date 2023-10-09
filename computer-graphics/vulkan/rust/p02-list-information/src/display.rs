use ash::*;

use std::os::raw::c_char;
use std::ffi::CStr;

pub fn from_cchar(cchar_array: &[c_char]) -> String 
{
    let cstr_ext_name: &CStr = unsafe { CStr::from_ptr(cchar_array.as_ptr()) };
    String::from(cstr_ext_name.to_str().unwrap())
}


pub fn show_version(entry: &Entry) {
    println!(" \n--- VERSION ---");
    match entry.try_enumerate_instance_version().unwrap() {
        Some(version) => {
            let variant = vk::api_version_variant(version);
            let major = vk::api_version_major(version);
            let minor = vk::api_version_minor(version);
            let patch = vk::api_version_patch(version);
            println!("VERSION: {version} | {variant}.{major}.{minor}.{patch}");
        },

        None => {
            println!("-> No version available !");
        }
    };
}


pub fn list_available_extension_properties(
    extension_properties: &Vec<vk::ExtensionProperties>
) {
    println!(" \n--- AVAILABLE EXTENSION PROPERTIES ---");
    for prop in extension_properties {
        let ext_name: String = from_cchar(&prop.extension_name);
        println!("{}", ext_name);
    }
}

pub fn list_available_layer_properties(
    layer_properties: &Vec<vk::LayerProperties>
) {
    println!(" \n--- AVAILABLE LAYER PROPERTIES ---");
    for prop in layer_properties {
        let layer_prop_name: String = from_cchar(&prop.layer_name);
        let layer_prop_description: String = from_cchar(&prop.description);
        println!("{:<40} | {}", layer_prop_name, layer_prop_description);
    }
}

pub fn show_phyisical_device_name(
    instance: &Instance,
    physical_device: &vk::PhysicalDevice
) {
    let phyisical_device_properties: vk::PhysicalDeviceProperties = unsafe {instance.get_physical_device_properties(*physical_device)};
    let device_name: String = from_cchar(&phyisical_device_properties.device_name);
    println!("\n»»» {} «««", device_name);
}

pub fn list_available_physical_devices(
    instance: &Instance,
    physical_devices: &Vec<vk::PhysicalDevice>,
    show_limits: bool,
    show_features: bool
) {
    println!(" \n--- AVAILABLE PHYSICAL DEVICES ---");
    for physical_device in physical_devices {
        show_phyisical_device_name(&instance, &physical_device);
        
        if show_limits {
            let phyisical_device_properties: vk::PhysicalDeviceProperties = unsafe {instance.get_physical_device_properties(*physical_device)};
            let limits: vk::PhysicalDeviceLimits = phyisical_device_properties.limits;

            println!("max image dim 1 {}", limits.max_image_dimension1_d);
            println!("max image dim 2 {}", limits.max_image_dimension2_d);
            println!("max image dim 3 {}", limits.max_image_dimension3_d);
            println!("max memory alloc count {}", limits.max_memory_allocation_count);
            println!("max viewport dim {:?}", limits.max_viewport_dimensions);
            println!("max draw indexed index value {:?}", limits.max_draw_indexed_index_value);
        }

        if show_features {
            let pd_features: vk::PhysicalDeviceFeatures = unsafe {instance.get_physical_device_features(*physical_device)};
            println!(" \n{:#?}", pd_features);
        }
        
    }
}

pub fn list_queue_family_properties(
    instance: &Instance,
    physical_devices: &Vec<vk::PhysicalDevice>
) {
    println!(" \n--- AVAILABLE QUEUE FAMILY PROPERTIES ---");
    for physical_device in physical_devices {
        // show name
        show_phyisical_device_name(&instance, &physical_device);
        
        let queue_family_properties: Vec<vk::QueueFamilyProperties> = unsafe{
            instance.get_physical_device_queue_family_properties(*physical_device)
        };

        let mut i = 0;
        for prop in queue_family_properties {
            println!("{} ... {:?}", i, prop.queue_flags);
            i += 1;
        }
    }
}
