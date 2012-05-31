all:
	swig -python mondemandlib.i
	gcc -fpic -I/opt/include/python2.6 -c mondemandlib.c mondemandlib_wrap.c 
	ld -shared mondemandlib.o mondemandlib_wrap.o -o _mondemandlib.so
clean:
	rm -rf *.o *.so *.py *.pyc *_wrap.c
