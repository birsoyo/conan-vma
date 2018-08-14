
#include "vulkan/vulkan.hpp"

#define VMA_IMPLEMENTATION
#include "vk_mem_alloc.h"

#include <iostream>

int main()
{
  auto app_info = vk::ApplicationInfo{}
    .setPApplicationName("vma conan package tester")
    .setApplicationVersion(VK_MAKE_VERSION(1, 0, 0))
    .setPEngineName("No Engine")
    .setEngineVersion(VK_MAKE_VERSION(1, 0, 0))
    .setApiVersion(VK_API_VERSION_1_0)
  ;

  auto ici = vk::InstanceCreateInfo{}
    .setPApplicationInfo(&app_info)
  ;

  auto vkinstance = vk::createInstance(ici);

  if (!vkinstance)
  {
    return 1;
  }

  auto physical_devices = vkinstance.enumeratePhysicalDevices();
  auto physical_device = physical_devices[0];
  if (!physical_device)
  {
    return 2;
  }

  auto dci = vk::DeviceCreateInfo{};

  auto device = physical_device.createDevice(dci);
  if (!device)
  {
    return 3;
  }

  VmaAllocatorCreateInfo allocatorInfo = {};
  allocatorInfo.physicalDevice = physical_device;
  allocatorInfo.device = device;
  VmaAllocator allocator;
  vmaCreateAllocator(&allocatorInfo, &allocator);
  if (!allocator)
  {
    return 4;
  }

  auto stats = VmaStats{};
  vmaCalculateStats(allocator, &stats);

  char* stats_cstr;
  vmaBuildStatsString(allocator, &stats_cstr, VK_TRUE);
  std::cout << stats_cstr << std::endl;
  vmaFreeStatsString(allocator, stats_cstr);

  vmaDestroyAllocator(allocator);

  device.destroy();
  vkinstance.destroy();

  return 0;
}
