
use ash::*;


pub struct SyncGates {
    pub image_available: Vec<vk::Semaphore>,
    pub rendering_finished: Vec<vk::Semaphore>,
    pub may_begin_drawing: Vec<vk::Fence>
}


pub fn setup_synchronization(
    device: &Device,
    swapchain_images: &Vec<vk::Image>
) -> SyncGates {
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

    SyncGates {
        image_available,
        rendering_finished,
        may_begin_drawing
    }
}