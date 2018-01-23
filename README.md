# CPack Example

Just another CPack example using Conan

### How to build
To build this project, as Conan package:

    $ conan create . uilianries/testing

During build some important artifacts will be provided:

* include/
  - All project header files
* lib/
  - All projects libraries (.a|.so|.lib|.dll|.dylib)
* license/
  - A license copy
* install/
  - Standalone project installer (.deb|.rpm|.zip|.tar.gz)

#### LICENSE
[MIT](LICENSE)
