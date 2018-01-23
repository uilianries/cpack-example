from conans import ConanFile, CMake, tools


class FoobarConan(ConanFile):
    name = "foobar"
    version = "0.1.0"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "installer": ["deb", "rpm", "tgz", "zip"]}
    default_options = "shared=False", "installer=deb"
    generators = "cmake"
    exports_sources = "src/*", "include/*", "CMakeLists.txt"
    exports = "LICENSE"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        self.run("cpack -G %s %s" % (str(self.options.installer).upper(), self.build_folder))

    def package(self):
        self.copy("LICENSE", dst="license")
        installer = "%s-%s.%s" % (self.name, self.version, ("tar.gz" if self.options.installer == "tgz" else str(self.options.installer)))
        self.copy(installer, dst="install")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
