use std::ffi::CStr;
use ash::*;
use ash::vk::{
    ComputePipelineCreateInfo, 
    PipelineCache, 
    PipelineLayout, 
    PipelineLayoutCreateInfo, 
    PipelineShaderStageCreateInfo, 
    ShaderModule, 
    ShaderStageFlags,
};

pub fn create_compute_pipeline(
    device: &Device,
    comp_module: ShaderModule,
    descriptor_set_layout: vk::DescriptorSetLayout,
) -> (vk::Pipeline, vk::PipelineLayout) {
    
    let main_string: String = String::from("main\0");
    let main_cstring: &CStr = CStr::from_bytes_with_nul(main_string.as_bytes()).unwrap();

    let comp_stage: PipelineShaderStageCreateInfo = PipelineShaderStageCreateInfo::builder()
        .module(comp_module)
        .stage(ShaderStageFlags::COMPUTE)
        .name(main_cstring)
        .build();


    // layout
    let layout_create_info = PipelineLayoutCreateInfo::builder()
        .set_layouts(&[descriptor_set_layout])
        .build();

    let layout: PipelineLayout = unsafe {
        device.create_pipeline_layout(
            &layout_create_info,
            None
        ).unwrap()
    };

    let compute_pipeline_create_info = ComputePipelineCreateInfo::builder()
        .stage(comp_stage)
        .layout(layout)
        .build();

    let compute_pipelines: Vec<vk::Pipeline> = unsafe {
        device.create_compute_pipelines(
            PipelineCache::null(), 
            &[compute_pipeline_create_info], 
            None
        ).unwrap()
    };

    return (*compute_pipelines.first().unwrap(), layout);
}