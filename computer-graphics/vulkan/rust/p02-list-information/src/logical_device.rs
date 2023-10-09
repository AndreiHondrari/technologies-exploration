
use ash::{
    *, 
    vk::KhrPortabilitySubsetFn,
    extensions::khr::Swapchain
};


pub fn create_logical_device(instance: &Instance, physical_device: vk::PhysicalDevice) -> Device {

    println!(" \n--- CREATE LOGICAL DEVICE ---");
    println!("Physical device selected: {:?}", physical_device);

    let priorities = [1.0];

    let device_queue_create_infos = [
        vk::DeviceQueueCreateInfo::builder()
            .queue_family_index(0)
            .queue_priorities(&priorities)
            .build()
    ];

    let device_extension_names = [
        KhrPortabilitySubsetFn::name().as_ptr(),
        Swapchain::name().as_ptr(),
    ];

    let features = vk::PhysicalDeviceFeatures::default();
    
    let device_create_info = vk::DeviceCreateInfo::builder()
        .queue_create_infos(&device_queue_create_infos)
        .enabled_extension_names(&device_extension_names)
        .enabled_features(&features)
        .build();

    println!("Create the device ...\n");
    let device: Device = unsafe{
        instance.create_device(
            physical_device,
            &device_create_info, 
            None
        )
    }.unwrap();

    return device;
}