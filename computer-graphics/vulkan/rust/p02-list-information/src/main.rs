
use ash::*;
use std::os::raw::c_char;
use std::ffi::CStr;

fn main() {
    println!("#### START INFO LISTING #### \n");

    // entry to access Vulkan functions
    let entry = unsafe { Entry::load().unwrap() };

    // enumerate extension properties
    let properties = entry.enumerate_instance_extension_properties(None).unwrap();

    println!(" \n--- AVAILABLE INSTANCE PROPERTIES ---");
    for prop in properties {
        let raw_ext_name: [c_char; 256] = prop.extension_name;
        let cstr_ext_name = unsafe { CStr::from_ptr(raw_ext_name.as_ptr()) };
        let ext_name: String = String::from(cstr_ext_name.to_str().unwrap());
        println!("{}", ext_name);
    }

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

    // app info declaration (needed for create info)
    let app_info = vk::ApplicationInfo {
        api_version: vk::make_api_version(0, 1, 3, 261),
        ..Default::default()
    };

    // declare extensions to enable
    let mut extension_names: Vec<*const c_char> = Vec::new();
    extension_names.push(vk::KhrPortabilityEnumerationFn::name().as_ptr());  // needed for molten / macOS

    // instance creation information
    let create_info: vk::InstanceCreateInfo = vk::InstanceCreateInfo::builder()
        .application_info(&app_info)
        .flags(vk::InstanceCreateFlags::ENUMERATE_PORTABILITY_KHR)  // needed for molten / macOS
        .enabled_extension_names(&extension_names)
        .build();
    

    // create the Vulkan instance
    let instance_result = unsafe { entry.create_instance(&create_info, None) };

    // if instance_result.is_err() {
    //     println!("{:?}", instance_result.err().unwrap());
    // }

    let instance = instance_result.unwrap();

    
    let physical_devices = unsafe{instance.enumerate_physical_devices().unwrap()};
    
    println!(" \n--- AVAILABLE PHYSICAL DEVICES ---");
    for physical_device in physical_devices {
        let phyisical_device_properties = unsafe {instance.get_physical_device_properties(physical_device)};
        
        let cstr_device_name = unsafe { CStr::from_ptr(phyisical_device_properties.device_name.as_ptr()) };
        let device_name: String = String::from(cstr_device_name.to_str().unwrap());

        println!("{}", device_name);
    }

    println!("\n--- FIN ---");
}
