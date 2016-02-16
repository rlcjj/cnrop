CXX = g++
LIBRARIES = -L/usr/local/boost_1_58_0/stage/lib/  -lboost_thread -lboost_python -lpython2.7
COMMON_FLAGS = -D__GNU__ -fPIC
INCLUDE = -I/usr/include/python2.7/
ROOTPATH = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))