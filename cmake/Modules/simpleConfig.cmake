INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SIMPLE simple)

FIND_PATH(
    SIMPLE_INCLUDE_DIRS
    NAMES simple/api.h
    HINTS $ENV{SIMPLE_DIR}/include
        ${PC_SIMPLE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SIMPLE_LIBRARIES
    NAMES gnuradio-simple
    HINTS $ENV{SIMPLE_DIR}/lib
        ${PC_SIMPLE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SIMPLE DEFAULT_MSG SIMPLE_LIBRARIES SIMPLE_INCLUDE_DIRS)
MARK_AS_ADVANCED(SIMPLE_LIBRARIES SIMPLE_INCLUDE_DIRS)

