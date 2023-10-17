all: _x86_64_exec.so
	

_x86_64_exec.so: x86_64_exec_wrap.o
	ld -shared x86_64_exec_wrap.o -o _x86_64_exec.so

x86_64_exec_wrap.o: x86_64_exec_wrap.c x86_64_exec.h
	gcc -c -fPIC x86_64_exec.h x86_64_exec_wrap.c -I /usr/include/python3.10

x86_64_exec_wrap.c: x86_64_exec.i x86_64_exec.h
	swig -python x86_64_exec.i

clean:
	rm -f x86_64_exec_wrap.c x86_64_exec_wrap.o _x86_64_exec.so x86_64_exec.h.gch