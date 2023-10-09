
use ash::*;
use ash::prelude::*;
use std::ffi::CStr;
use std::os::raw::c_char;


pub fn get_required_extensions() -> Vec<*const c_char> {
    // declare extensions to enable
    let mut extension_names: Vec<*const c_char> = Vec::new();
    
    extension_names.push(vk::KhrPortabilityEnumerationFn::name().as_ptr());  // needed for molten / macOS
    extension_names.push(vk::ExtDebugUtilsFn::name().as_ptr());
    extension_names.push(vk::LunargDirectDriverLoadingFn::name().as_ptr());
    extension_names.push(vk::ExtSwapchainColorspaceFn::name().as_ptr());
    // extension_names.push(vk::ExtMetalSurfaceFn::name().as_ptr());
    extension_names.push(vk::KhrSurfaceFn::name().as_ptr());
    
    return extension_names;
}


pub fn get_required_layer_names() -> Vec<*const c_char> {
    let mut layer_names: Vec<*const c_char> = Vec::new();

    // layer_names.push(CStr::from_bytes_with_nul(b"VK_LAYER_LUNARG_api_dump\0").ok().unwrap().as_ptr());
    layer_names.push(CStr::from_bytes_with_nul(b"VK_LAYER_KHRONOS_validation\0").ok().unwrap().as_ptr());
    
    return layer_names;
}


pub fn compose_create_info(
    app_info: &vk::ApplicationInfo, 
    extension_names: &Vec<*const c_char>,
    layer_names: &Vec<*const c_char> 
) -> vk::InstanceCreateInfo{
    vk::InstanceCreateInfo::builder()
        .application_info(&app_info)
        .flags(vk::InstanceCreateFlags::ENUMERATE_PORTABILITY_KHR)  // needed for molten / macOS
        .enabled_extension_names(&extension_names)
        .enabled_layer_names(&layer_names)
        .build()
}


pub fn create_instance(entry: &Entry) -> Instance {
    // app info declaration (needed for create info)
    let app_info: vk::ApplicationInfo = vk::ApplicationInfo {
        api_version: vk::make_api_version(0, 1, 3, 261),
        ..Default::default()
    };

    // extensions for instance
    let extension_names: Vec<*const i8> = get_required_extensions();

    // validation layers for instance
    let layer_names: Vec<*const c_char> = get_required_layer_names();
    
    // instance creation information
    let create_info: vk::InstanceCreateInfo = compose_create_info(&app_info, &extension_names, &layer_names);

    // create the Vulkan instance
    let instance_result: VkResult<Instance> = unsafe { entry.create_instance(&create_info, None) };

    // if instance_result.is_err() {
    //     println!("{:?}", instance_result.err().unwrap());
    // }

    let instance: Instance = instance_result.unwrap();

    return instance;
}