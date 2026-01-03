use std::fs::*;

use ash::util::read_spv;
use ash::*;

use vk_shader_macros::include_glsl;

#[allow(dead_code)]
pub fn read_file(file_path: String) -> Result<Vec<u32>, String> {
    let shader_file = File::open(&file_path);

    if shader_file.is_err() {
        return Err(String::from(format!("Could not load shader {}", &file_path)));
    }

    let mut shader_file: File = shader_file.unwrap();
    let spv_result = read_spv(&mut shader_file);

    if spv_result.is_err() {
        let spv_error = spv_result.err().unwrap();
        return Err(String::from(format!("Problem with reading the SPIR-V code: {} due to {}", &file_path, spv_error)));
    }

    Ok(spv_result.unwrap())
}

pub fn create_shader_module(device: &Device, shader_code: &Vec<u32>) -> vk::ShaderModule {
    // let shader_code: &[u8] = shader_code.into();
    
    let create_info: vk::ShaderModuleCreateInfo = vk::ShaderModuleCreateInfo::builder()
        .code(shader_code.as_slice())
        .build();
    
    return unsafe{
        device.create_shader_module(&create_info, None).unwrap()
    };
}

pub fn get_comp_shader(
    device: &Device,
) -> vk::ShaderModule {
    let comp_shader_code: &[u32] = include_glsl!("./src/shaders/operation_1.comp", kind: comp);
    let comp_shader_code: Vec<u32> = comp_shader_code.to_vec();
    let comp_module: vk::ShaderModule = create_shader_module(&device, &comp_shader_code);
    return comp_module;
}
