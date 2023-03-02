HOME_TREE := ../

MODULE_NAME := $(notdir $(CURDIR))

include $(HOME_TREE)/mak_def.inc

CXXSRC += src/rplidar_driver.cpp \
          src/hal/thread.cpp

C_INCLUDES += -I$(CURDIR)/include -I$(CURDIR)/src

CXXSRC += src/arch/linux/net_serial.cpp \
          src/arch/linux/net_socket.cpp \
          src/arch/linux/timer.cpp 

all: build_sdk

include $(HOME_TREE)/mak_common.inc

clean: clean_sdk
