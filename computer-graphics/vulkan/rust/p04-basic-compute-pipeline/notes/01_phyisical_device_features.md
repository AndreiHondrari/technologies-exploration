# Physical Device Features

## robust_buffer_access

access to buffers is bound-checked against the buffer range descriptor

## full_draw_index_uint32

32-bit range supported when using `VkIndexType` with `VK_INDEX_TYPE_UINT32`.

## image_cube_array

specified if `VkImageViewType` of type `VK_IMAGE_VIEW_TYPE_CUBE_ARRAY` can be
created

## independent_blend

specified if `VkPipelineColorBlendAttachmentState` settings are controlled
independently per-attachment.

## geometry_shader

specifies if geometry shaders are supported otherwise
`VK_SHADER_STAGE_GEOMETRY_BIT` and `VK_PIPELINE_STAGE_GEOMETRY_SHADER_BIT` can't
be used.

## tessellation_shader

specified whether tessellation control and evaluation shaders are supported,
otherwise:

- `VK_SHADER_STAGE_TESSELLATION_CONTROL_BIT`
- `VK_SHADER_STAGE_TESSELLATION_EVALUATION_BIT`
- `VK_PIPELINE_STAGE_TESSELLATION_CONTROL_SHADER_BIT`
- `VK_PIPELINE_STAGE_TESSELLATION_EVALUATION_SHADER_BIT`
- `VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO`

may not be used

## sample_rate_shading

specifies whether sample shading and multisample interpolation are supported.

## dual_src_blend

specifies if blend operations with two sources are supported.

## logic_op

whether logic operations are supported.

## multi_draw_indirect

whether multiple draw indirect is supported.

## draw_indirect_first_instance

## depth_clamp

## depth_bias_clamp

## fill_mode_non_solid

## depth_bounds

## wide_lines

## large_points

## alpha_to_one

## multi_viewport

## sampler_anisotropy

## texture_compression_etc2

## texture_compression_astc_ldr

## texture_compression_bc

## occlusion_query_precise

## pipeline_statistics_query

## vertex_pipeline_stores_and_atomics

## fragment_stores_and_atomics

## shader_tessellation_and_geometry_point_size

## shader_image_gather_extended

## shader_storage_image_extended_formats

## shader_storage_image_multisample

## shader_storage_image_read_without_format

## shader_storage_image_write_without_format

## shader_uniform_buffer_array_dynamic_indexing

## shader_sampled_image_array_dynamic_indexing

## shader_storage_buffer_array_dynamic_indexing

## shader_storage_image_array_dynamic_indexing

## shader_clip_distance

## shader_cull_distance

## shader_float64

## shader_int64

## shader_int16

## shader_resource_residency

## shader_resource_min_lod

## sparse_binding

## sparse_residency_buffer

## sparse_residency_image2_d

## sparse_residency_image3_d

## sparse_residency2_samples

## sparse_residency4_samples

## sparse_residency8_samples

## sparse_residency16_samples

## sparse_residency_aliased

## variable_multisample_rate

## inherited_queries
