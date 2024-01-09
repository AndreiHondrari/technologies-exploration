use std::ffi::CStr;
use ash::*;
use ash::vk::{PipelineShaderStageCreateInfo, GraphicsPipelineCreateInfo, PipelineCache, ShaderStageFlags, PipelineDynamicStateCreateInfo, PipelineVertexInputStateCreateInfo, PipelineInputAssemblyStateCreateInfo, PipelineViewportStateCreateInfo, PipelineRasterizationStateCreateInfo, PipelineMultisampleStateCreateInfo, PipelineColorBlendStateCreateInfo, PipelineLayoutCreateInfo, PipelineLayout, RenderPass, PrimitiveTopology, PolygonMode, CullModeFlags, FrontFace, SampleCountFlags, LogicOp, PipelineColorBlendAttachmentState, ColorComponentFlags, BlendFactor, AttachmentDescription, AttachmentReference, SubpassDescription, RenderPassCreateInfo, AttachmentLoadOp, AttachmentStoreOp, ImageLayout, PipelineBindPoint, ShaderModule};

fn create_render_pass(device: &Device, selected_format: vk::Format) -> RenderPass {
    let attachment_description = AttachmentDescription::builder()
        .format(selected_format)
        .samples(SampleCountFlags::TYPE_1)
        .load_op(AttachmentLoadOp::CLEAR)
        .store_op(AttachmentStoreOp::STORE)
        .stencil_load_op(AttachmentLoadOp::DONT_CARE)
        .stencil_store_op(AttachmentStoreOp::DONT_CARE)
        .initial_layout(ImageLayout::UNDEFINED)
        .final_layout(ImageLayout::PRESENT_SRC_KHR)
        .build();

    let attachment_reference: AttachmentReference = AttachmentReference::builder()
        .layout(ImageLayout::COLOR_ATTACHMENT_OPTIMAL)
        .build();

    let subpass_description = SubpassDescription::builder()
        .pipeline_bind_point(PipelineBindPoint::GRAPHICS)
        .color_attachments(&[attachment_reference])
        .build();

    let render_pass_create_info = RenderPassCreateInfo::builder()
        .attachments(&[attachment_description])
        .subpasses(&[subpass_description])
        .build();
    
    let render_pass_result = unsafe {
        device.create_render_pass(
            &render_pass_create_info,
            None
        )
    };

    let render_pass: RenderPass = render_pass_result.unwrap();


    return render_pass;
}

pub fn create_pipeline(
    device: &Device,
    surface_capabilities: vk::SurfaceCapabilitiesKHR,
    selected_format: vk::Format,
    vert_module: ShaderModule,
    frag_module: ShaderModule
) -> (vk::Pipeline, vk::PipelineLayout, vk::RenderPass) {
    
    let main_string: String = String::from("main\0");
    let main_cstring: &CStr = CStr::from_bytes_with_nul(main_string.as_bytes()).unwrap();

    let vert_stage: PipelineShaderStageCreateInfo = PipelineShaderStageCreateInfo::builder()
        .module(vert_module)
        .stage(ShaderStageFlags::VERTEX)
        .name(main_cstring)
        .build();

    let frag_stage: PipelineShaderStageCreateInfo = PipelineShaderStageCreateInfo::builder()
        .module(frag_module)
        .stage(ShaderStageFlags::FRAGMENT)
        .name(main_cstring)
        .build();

    let shader_stages: [PipelineShaderStageCreateInfo; 2] = [vert_stage, frag_stage];

    // vertex input state
    let vertex_attribute_descriptions = [vk::VertexInputAttributeDescription {
        binding: 0,
        location: 0,
        offset: 0,
        format: vk::Format::R32G32_SFLOAT,
    }];
    let vertex_binding_descriptions = [vk::VertexInputBindingDescription {
        binding: 0,
        stride: (std::mem::size_of::<f32>() * 2) as u32,
        input_rate: vk::VertexInputRate::VERTEX,
    }];

    let vertex_input_state_create_info = PipelineVertexInputStateCreateInfo::builder()
        .vertex_attribute_descriptions(&vertex_attribute_descriptions)
        .vertex_binding_descriptions(&vertex_binding_descriptions)
        .build();

    // input assembly state
    let input_assembly_state_create_info = PipelineInputAssemblyStateCreateInfo::builder()
        .topology(PrimitiveTopology::TRIANGLE_LIST)
        .build();

    // viewport state
    let viewport = vk::Viewport::builder()
        .x(0.0f32)
        .y(0.0f32)
        .width(surface_capabilities.current_extent.width as f32)
        .height(surface_capabilities.current_extent.height as f32)
        .min_depth(0.0f32)
        .max_depth(1.0f32)
        .build();

    let scissor_offset = vk::Offset2D::builder()
        .x(0).y(0)
        .build();
    
    let scissor = vk::Rect2D::builder()
        .offset(scissor_offset)
        .extent(surface_capabilities.current_extent)
        .build();

    let viewports: [vk::Viewport; 1] = [viewport];
    let scissors: [vk::Rect2D; 1] = [scissor];
    let viewport_state_create_info = PipelineViewportStateCreateInfo::builder()
        .viewports(&viewports)
        .scissors(&scissors)
        .build();

    // rasterization state
    let rasterization_state_create_info = PipelineRasterizationStateCreateInfo::builder()
        .depth_clamp_enable(false)
        .rasterizer_discard_enable(false)
        .polygon_mode(PolygonMode::FILL)
        .line_width(1.0f32)
        .cull_mode(CullModeFlags::BACK)
        // .cull_mode(CullModeFlags::NONE)
        .front_face(FrontFace::CLOCKWISE)
        // .front_face(FrontFace::COUNTER_CLOCKWISE)
        .depth_bias_enable(false)
        .depth_bias_constant_factor(0.0f32)
        .depth_bias_clamp(0.0f32)
        .depth_bias_slope_factor(0.0f32)
        .build();

    // multisample state
    let multisample_state_create_info = PipelineMultisampleStateCreateInfo::builder()
        .sample_shading_enable(false)
        .rasterization_samples(SampleCountFlags::TYPE_1)
        .min_sample_shading(1.0f32)
        // .sample_mask(&[])
        .alpha_to_coverage_enable(false)
        .alpha_to_one_enable(false)
        .build();

    // depth stencil state
    // let depth_stencil_state_create_info = PipelineDepthStencilStateCreateInfo::builder()
    //     .build();

    // color blend state
    let color_blend_attachment_state = PipelineColorBlendAttachmentState::builder()
        .color_write_mask(ColorComponentFlags::RGBA)
        .blend_enable(false)
        .src_color_blend_factor(BlendFactor::ONE)
        .dst_color_blend_factor(BlendFactor::ZERO)
        .color_blend_op(vk::BlendOp::ADD)
        .src_alpha_blend_factor(BlendFactor::ONE)
        .dst_alpha_blend_factor(BlendFactor::ZERO)
        .alpha_blend_op(vk::BlendOp::ADD)
        .build();
    
    let color_blend_state_create_info = PipelineColorBlendStateCreateInfo::builder()
        .logic_op_enable(false)
        .logic_op(LogicOp::COPY)
        .attachments(&[color_blend_attachment_state])
        .blend_constants([0.0f32, 0.0f32, 0.0f32, 0.0f32])
        .build();

    // dynamic state
    let dynamic_states = [
        // DynamicState::VIEWPORT, 
        // DynamicState::SCISSOR
    ];
    let dynamic_state_create_info = PipelineDynamicStateCreateInfo::builder()
        .dynamic_states(&dynamic_states)
        .build();

    // layout
    let layout_create_info = PipelineLayoutCreateInfo::builder()
        // .set_layouts(set_layouts)
        // .push_constant_ranges(push_constant_ranges)
        .build();

    let layout: PipelineLayout = unsafe {
        device.create_pipeline_layout(
            &layout_create_info,
            None
        ).unwrap()
    };

    // render pass
    let render_pass = create_render_pass(device, selected_format);

    let graphics_pipeline_create_info = GraphicsPipelineCreateInfo::builder()
        .vertex_input_state(&vertex_input_state_create_info)
        .input_assembly_state(&input_assembly_state_create_info)
        .viewport_state(&viewport_state_create_info)
        .rasterization_state(&rasterization_state_create_info)
        .multisample_state(&multisample_state_create_info)
        // .depth_stencil_state(&depth_stencil_state_create_info)
        .color_blend_state(&color_blend_state_create_info)
        .dynamic_state(&dynamic_state_create_info)
        .layout(layout)
        .render_pass(render_pass)
        .subpass(0)
        .base_pipeline_handle(vk::Pipeline::null())
        .base_pipeline_index(-1)
        .stages(&shader_stages)
        .build();

    let graphics_pipeline: Vec<vk::Pipeline> = unsafe {
        device.create_graphics_pipelines(
            PipelineCache::null(), 
            &[graphics_pipeline_create_info],
            None
        ).unwrap()
    };

    return (*graphics_pipeline.first().unwrap(), layout, render_pass);
}