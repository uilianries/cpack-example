cmake_minimum_required(VERSION 3.1)
project(foobar CXX)

# Project version #########################################################
set(VERSION_MAJOR 0)
set(VERSION_MINOR 1)
set(VERSION_PATCH 0)

# Verbose mode ############################################################
set(CMAKE_VERBOSE_MAKEFILE ON)

# Conan packages ##########################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Sub directories #########################################################
set(SOURCE_FILES src/foobar.cpp)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${CMAKE_SOURCE_DIR}/include)

# Install ##################################################################
install(TARGETS ${CMAKE_PROJECT_NAME}
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
install(DIRECTORY include/foobar DESTINATION include)

# Package Generator  #######################################################
set(CPACK_PACKAGE_DESCRIPTION "Just another CPacke example")
set(CPACK_PACKAGE_VERSION_MAJOR "${VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${VERSION_MINOR}")
set(CPACK_PACKAGE_VERSION_PATCH "${VERSION_PATCH}")
set(CPACK_PACKAGE_VENDOR "ACME")
set(CPACK_PACKAGE_CONTACT "support@acme.corp")
set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH}")
include (CPack)
