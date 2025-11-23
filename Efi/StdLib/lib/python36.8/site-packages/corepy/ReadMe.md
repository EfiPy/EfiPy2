# Introduction
PYTHONPATH=$(PYTHONLAB) python3

# In Linux environment

## Build corepy/arch/x86_64/platform/linux/x86_64_exec from SWIG
```
swig -python x86_64_exec.i
gcc -c -fPIC x86_64_exec.h x86_64_exec_wrap.c -I /usr/include/python3.10
ld -shared x86_64_exec_wrap.o -o _x86_64_exec.so
```

## Build corepy/lib/extarray/alloc from SWIG
```
swig -python alloc.i
gcc -c -fPIC alloc_wrap.c -I /usr/include/python3.10
ld -shared alloc_wrap.o -o _alloc.so
```
