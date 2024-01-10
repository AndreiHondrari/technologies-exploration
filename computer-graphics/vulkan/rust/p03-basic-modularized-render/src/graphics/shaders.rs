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

pub fn get_shaders(device: &Device) -> (vk::ShaderModule, vk::ShaderModule) {
    /*
    Shaders can be precompiled and then imported as SPIR-V bytecode to be passed to the pipeline.
    They can also be compiled to SPIR-V on the spot, using shaderc library.

    There seems to be an orthogonal opportunity here to:
    - use JIT shader compilation for debugging purposes
    - use pre-compiled SPIR-V shaders for production purposes
    */
    
    // manual way to import the SPIR-V code -> needs to be pre-compiled
    // let vert_shader_code: Vec<u32> = graphics::shaders::read_file(String::from("src/shaders/vert.spv")).unwrap();
    // let frag_shader_code: Vec<u32> = graphics::shaders::read_file(String::from("src/shaders/frag.spv")).unwrap();

    // using an existing crate to import the raw shaders and compile them on the spot
    let vert_shader_code: &[u32] = include_glsl!("./src/shaders/shader.vert");
    let frag_shader_code: &[u32] = include_glsl!("./src/shaders/shader.frag", kind: frag);

    let vert_shader_code: Vec<u32> = vert_shader_code.to_vec();
    let frag_shader_code: Vec<u32> = frag_shader_code.to_vec();

    let vert_module: vk::ShaderModule = create_shader_module(&device, &vert_shader_code);
    let frag_module: vk::ShaderModule = create_shader_module(&device, &frag_shader_code);

    return (vert_module, frag_module);
}
