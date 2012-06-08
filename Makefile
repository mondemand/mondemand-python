PKG_CONFIG_PATH=/usr/lib/pkgconfig
CFLAGS=`PKG_CONFIG_PATH=/usr/lib/pkgconfig pkg-config mondemand-4.0 --cflags`
LIBS=`PKG_CONFIG_PATH=/usr/lib/pkgconfig pkg-config mondemand-4.0 --libs`

all:
	/opt/bin/swig -python mondemand.i
	gcc -fPIC $(CFLAGS) -I/opt/include/python2.6 -c mondemand_wrap.c 
	gcc -shared mondemand_wrap.o -o _mondemand.so $(LIBS)
clean:
	rm -rf *.o *.so mondemand.py *.pyc *_wrap.c
