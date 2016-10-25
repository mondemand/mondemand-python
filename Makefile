PKG_CONFIG_PATH=/usr/lib/pkgconfig
SWIG_EXE=/usr/local/bin/swig
CFLAGS=`PKG_CONFIG_PATH=/usr/lib/pkgconfig pkg-config mondemand-4.0 --cflags`
LIBS=`PKG_CONFIG_PATH=/usr/lib/pkgconfig pkg-config mondemand-4.0 --libs`
PYFLAGS=`python-config --includes`
PYSITE_PACKAGES=`python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`

BUILD_DIR=build
LIB_NAME=mondemand
RMFLAGS='-rvf'

.PHONY: directories

all: build
build: directories
	@echo "Building mondemand swig python wrapper."
	@$(SWIG_EXE) -module mondemand -python mondemand.i
	@mv mondemand.py $(BUILD_DIR)/$(LIB_NAME)/__init__.py
	@gcc -fPIC $(CFLAGS) $(PYFLAGS) -c mondemand_wrap.c
	@gcc -shared mondemand_wrap.o -o $(BUILD_DIR)/$(LIB_NAME)/_mondemand.so $(LIBS)
install:
	@echo "Installing mondemand python client."
	@echo "$(BUILD_DIR)/$(LIB_NAME) to $(PYSITE_PACKAGES)"
	@if [ -d $(BUILD_DIR)/$(LIB_NAME) ]; then mv $(BUILD_DIR)/$(LIB_NAME)/ $(PYSITE_PACKAGES); \
	else echo "No build found"; fi;
directories:
	@mkdir -p $(BUILD_DIR)/$(LIB_NAME)
clean:
	@rm $(RMFLAGS) *.o *.so mondemand.py *.pyc *_wrap.c
	@if [ -d $(BUILD_DIR)/$(LIB_NAME) ]; then rm $(RMFLAGS) $(BUILD_DIR)/$(LIB_NAME); fi;
	@if [ -d $(BUILD_DIR) ]; then rm $(RMFLAGS) build; fi;
uninstall: clean
	@echo "removing mondemand python client."
	@if [ -d $(PYSITE_PACKAGES)/$(LIB_NAME) ]; then rm $(RMFLAGS) $(PYSITE_PACKAGES)/$(LIB_NAME); \
	else echo "No install found"; fi;
