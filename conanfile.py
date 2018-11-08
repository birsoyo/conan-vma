# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class VmaConan(ConanFile):
    name = 'vma'
    version = '2.1.0'
    description = 'Easy to integrate Vulkan memory allocation library.'
    url = 'https://github.com/birsoyo/conan-vma'
    homepage = 'https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = 'MIT'

    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = 'https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator'
        tools.get(f'{source_url}/archive/v{self.version}.tar.gz')
        extracted_dir = f'VulkanMemoryAllocator-{self.version}'

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, 'src')
        self.copy(pattern='LICENSE', dst='license', src=self.source_subfolder)
        self.copy(pattern='*.h', dst='include', src=include_folder)
        self.copy(pattern='*.natvis', dst='vs', src=include_folder)

    def package_id(self):
        self.info.header_only()
