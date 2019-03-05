# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools, RunEnvironment

class VmaTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def requirements(self):
        self.requires('vulkan/1.1.101.0@sesame/stable')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings) and not os.environ.get('CI', '') in ['True', 'true']:
            with tools.environment_append(RunEnvironment(self).vars), tools.chdir('bin'):
                self.run(f'.{os.sep}test_package')
