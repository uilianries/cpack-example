#ifndef _FOOBAR_FOOBAR_HPP
#define _FOOBAR_FOOBAR_HPP

#ifdef WIN32
  #define FOOBAR_EXPORT __declspec(dllexport)
#else
  #define FOOBAR_EXPORT
#endif

namespace foobar {

FOOBAR_EXPORT void hello();

}

#endif  //  _FOOBAR_FOOBAR_HPP
