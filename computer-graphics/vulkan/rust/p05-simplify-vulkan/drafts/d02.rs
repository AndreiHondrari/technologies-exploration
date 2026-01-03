
use ash::*;

pub type Binding = u32;

/*
Descriptor
*/

pub struct Resource<ResourceType> {
    pub resource: ResourceType,
    pub binding: Binding
}

pub type BufferResource = Resource<vk::Buffer>;

/*
Resource Set Context
*/


#[derive(Default)]
pub struct ResourceSetContext<ResourceType>
{
    pub descriptor_type: vk::DescriptorType,
    pub stage_flags: vk::ShaderStageFlags,
    pub descriptors: Vec<Resource<ResourceType>>,

}

pub struct FreshResourceSet<ResourceType> {
    resource_set_context: ResourceSetContext<ResourceType>,
}

pub struct PlannedResourceSet<ResourceType> {
    resource_set_context: ResourceSetContext<ResourceType>,
    descriptor_set_layout: vk::DescriptorSetLayout,
    descriptor_pool: vk::DescriptorPool,
}

pub struct AllocatedResourceSet<ResourceType> {
    resource_set_context: ResourceSetContext<ResourceType>,
    descriptor_set_layout: vk::DescriptorSetLayout,
    descriptor_pool: vk::DescriptorPool,
    descriptor_sets:
}

pub type FreshBufferResourceSet = FreshResourceSet<vk::Buffer>;
pub type PlannedBufferResourceSet = PlannedResourceSet<vk::Buffer>;
pub type AllocatedBufferResourceSet = AllocatedResourceSet<vk::Buffer>;

pub struct AllocatedBufferResourceSetContext {
    resource_set_context: BufferResourceSetContext,
    descriptor_set: vk::DescriptorSet,
}

pub trait ResourceBindings {
    fn get_bindings(&self) -> Vec<Binding>;
}

impl<ResourceType> ResourceBindings for ResourceSetContext<ResourceType>
where
    ResourceType: Clone
{
    fn get_bindings(&self) -> Vec<Binding> {
        self.descriptors.iter().map(|descriptor: &Resource<ResourceType>| descriptor.binding).collect()
    }
}

pub trait ResourceWriteDescriptorSets {
    fn make_write_descriptor_set_instances(&self) -> Vec<vk::WriteDescriptorSet>;
}

impl ResourceWriteDescriptorSets for BufferResourceSetContext {
    fn make_write_descriptor_set_instances(&self) -> Vec<vk::WriteDescriptorSet> {
        let mut wds_collection: Vec<vk::WriteDescriptorSet> = Vec::new();

        for descriptor in self.descriptors {
            let ds_buffer_info = vk::DescriptorBufferInfo::builder()
                .buffer(descriptor.resource)
                .range(vk::WHOLE_SIZE)
                .build();

            let write_ds = vk::WriteDescriptorSet::builder()
                .buffer_info(ds_buffer_info)
                .descriptor_type(self.descriptor_type)
                .dst_set
                .build();
        }

        wds_collection
    }
}

/*
Resource services
*/
pub fn plan_resource_set<ResourceType>(
    device: &Device,
    FreshBufferResourceSetContext,
    // resource_set_context: &ResourceSetContext<ResourceType>
) -> Result<PlannedBufferResourceSetContext, vk::Result>
where
    ResourceType: Clone
{

    let mut dsl_bindings: Vec<vk::DescriptorSetLayoutBinding> = Vec::new();

    // add bindings for the descriptor set
    for binding in resource_set_context.get_bindings() {
        let dsl_binding = vk::DescriptorSetLayoutBinding::builder()
            .binding(binding)
            .descriptor_type(resource_set_context.descriptor_type)
            .descriptor_count(resource_set_context.descriptors.len() as u32)
            .build();

        dsl_bindings.push(dsl_binding);
    }

    let dsl_bindings = dsl_bindings;

    // define DS Layout Create Info
    let dsl_create_info = vk::DescriptorSetLayoutCreateInfo::builder()
        .bindings(dsl_bindings.as_slice());

    // create the descriptor set layout
    let descriptor_set_layout_result = unsafe {
        device.create_descriptor_set_layout(&dsl_create_info, None)
    };

    match descriptor_set_layout_result {
        Ok(planned_resource_set_context) => {
            Ok(AllocatedBufferResourceSetContext {
                resource_set_context: resource_set_context.

            })
        },

        Err(vk_result) => {
            Err(vk_result)
        }
    }

}

pub fn allocate_descriptor_sets(
    device: &Device,
    resource_set_context: &ResourceSetContext<ResourceType>

) -> (vk::DescriptorPool, ) {

}

pub fn update_descriptor_sets(
    device: &Device,
    resource_set_context: &ResourceSetContext<ResourceType>

)
where
    ResourceType: Clone
{
    let write_descriptor_set_instances: Vec<vk::WriteDescriptorSet> = resource_set_context.make_write_descriptor_set_instances();
}
