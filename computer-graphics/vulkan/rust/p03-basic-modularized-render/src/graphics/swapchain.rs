use ash::*;
use ash::extensions::khr::Swapchain;

pub type SwapchainLoader = Swapchain;
pub type SwapchainHandle = vk::SwapchainKHR;

pub fn create_swapchain(
    instance: &Instance,
    device: &Device,
    surface_handle: vk::SurfaceKHR,
    amount_images: u32,
    surface_capabilities: vk::SurfaceCapabilitiesKHR,
    selected_format: vk::Format,
    color_space: vk::ColorSpaceKHR,
) -> (SwapchainLoader, SwapchainHandle) {
    let swapchain_create_info_builder = vk::SwapchainCreateInfoKHR::builder()
        .surface(surface_handle)
        .min_image_count(
            amount_images.max(surface_capabilities.min_image_count).min(surface_capabilities.max_image_count)
        )
        .image_format(selected_format)
        .image_color_space(color_space)
        .image_extent(surface_capabilities.current_extent)
        .image_array_layers(1)
        .image_usage(vk::ImageUsageFlags::COLOR_ATTACHMENT)
        .image_sharing_mode(vk::SharingMode::EXCLUSIVE)
        // .queue_family_indices(&)
        .pre_transform(surface_capabilities.current_transform)
        .composite_alpha(vk::CompositeAlphaFlagsKHR::OPAQUE)
        .present_mode(vk::PresentModeKHR::FIFO)
    ;

    let swapchain_create_info = swapchain_create_info_builder.build();

    let swapchain_loader = Swapchain::new(instance, device);
    let swapchain_handle: SwapchainHandle = unsafe { 
        swapchain_loader.create_swapchain(
            &swapchain_create_info,
            None
        ).unwrap() 
    };
    
    return (swapchain_loader, swapchain_handle);

}

pub fn create_images(
    swapchain_loader: &SwapchainLoader,
    swapchain_handle: SwapchainHandle
) -> Vec<vk::Image> {
    unsafe {
        swapchain_loader.get_swapchain_images(swapchain_handle).unwrap()
    }
}

pub fn create_image_views(
    device: &Device,
    swapchain_images: &Vec<vk::Image>,
    selected_format: vk::Format
) -> Vec<vk::ImageView> {
    let mut swapchain_imageviews: Vec<vk::ImageView> = Vec::with_capacity(swapchain_images.len());

    for image in swapchain_images {
        let subresource_range = vk::ImageSubresourceRange::builder()
            .aspect_mask(vk::ImageAspectFlags::COLOR)
            .base_mip_level(0)
            .level_count(1)
            .base_array_layer(0)
            .layer_count(1)
            .build();

        let imageview_create_info = vk::ImageViewCreateInfo::builder()
            .image(*image)
            .view_type(vk::ImageViewType::TYPE_2D)
            .format(selected_format)
            .subresource_range(subresource_range)
            .build()
        ;

        let image_view = unsafe { 
            device.create_image_view(&imageview_create_info, None).unwrap()
        };

        swapchain_imageviews.push(image_view);   
    }

    return swapchain_imageviews;
}