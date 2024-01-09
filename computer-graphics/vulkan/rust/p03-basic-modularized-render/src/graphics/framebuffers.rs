
use ash::*;


pub fn create_framebuffers(
    device: &Device,
    swapchain_imageviews: &Vec<vk::ImageView>,
    surface_capabilities: &vk::SurfaceCapabilitiesKHR,
    render_pass: vk::RenderPass
) -> Vec<vk::Framebuffer> {
    let mut swapchain_framebuffers: Vec<vk::Framebuffer> = Vec::new();

    for image_view in swapchain_imageviews {
        let iview_attachments = [*image_view];
        let framebuffer_create_info = vk::FramebufferCreateInfo::builder()
            .render_pass(render_pass)
            .attachments(&iview_attachments)
            .width(surface_capabilities.current_extent.width)
            .height(surface_capabilities.current_extent.height)
            .layers(1)
            .build();

        let framebuffer = unsafe {
            device.create_framebuffer(
                &framebuffer_create_info, 
                None
            ).unwrap()
        };

        swapchain_framebuffers.push(framebuffer);
    }

    swapchain_framebuffers
}