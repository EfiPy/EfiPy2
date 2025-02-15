# Copyright (c) 2006-2008 The Trustees of Indiana University.
# Copyright (c) 2025 MaxWu EfiPy.core@gmail.com
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# - Neither the Indiana University nor the names of its contributors may be
#   used to endorse or promote products derived from this software without
#   specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# 

import ctypes
import EfiPy2 as EfiPy

size_char   = ctypes.sizeof(ctypes.c_char);
size_short  = ctypes.sizeof(ctypes.c_short);
size_int    = ctypes.sizeof(ctypes.c_int);
size_long   = ctypes.sizeof(ctypes.c_long);
size_float  = ctypes.sizeof(ctypes.c_float);
size_double = ctypes.sizeof(ctypes.c_double);

def has_huge_pages ():
  return 0

def alloc_hugemem ():
  return 0

def free_hugemem ():
  return 0

def realloc_hugemem ():
  return 0

def get_hugepage_size ():
  return 0

def get_page_size ():
  return EfiPy.EFI_PAGE_SIZE

def synchronize ():
  pass

def alloc_mem(size):

  pages  = EfiPy.EFI_SIZE_TO_PAGES (size)
  Buffer = EfiPy.EFI_PHYSICAL_ADDRESS(0)

  Status = EfiPy.gBS.AllocatePages (
                       EfiPy.AllocateAnyPages,
                       EfiPy.EfiRuntimeServicesCode,
                       pages,
                       EfiPy.byref (Buffer)
                       )

  # print "EfiPy.gBS.AllocatePages: %X" % Buffer.value

  if Status != EfiPy.EFI_SUCCESS:
    return 0
  else:
    EfiPy.gBS.SetMem (Buffer.value, size, 0x00)
    return Buffer.value

def realloc_mem (mem, oldsize, newsize):

  # print "mem = %X, oldsize = %X, newsize = %X" % (mem, oldsize, newsize)

  if mem == 0:
    return alloc_mem (newsize)

  if newsize == 0:
    return 0

  OldBuffer = mem
  NewBuffer = alloc_mem (newsize)

  if oldsize > newsize:
    newsize = oldsize

  EfiPy.gBS.CopyMem (NewBuffer, OldBuffer, newsize)

  EfiPy.gBS.FreePages (mem, 1)

  return NewBuffer

def free_mem(addr):

  EfiPy.gBS.FreePages (addr, 1)

def zero_mem (addr, size):

  EfiPy.gBS.SetMem (addr, size, 0x00)

def copy_direct (dst, src, size):
  EfiPy.gBS.CopyMem (dst, src, size)

def byteswap_2 (mem, elems):

  Source = (EfiPy.UINT8 * 2).from_address(mem)

  for idx in range (elems):

    Source[idx] = (Source[idx] >> 8 ) | (Source[idx] << 8 )

def byteswap_4 (mem, elems):

  Source = (EfiPy.UINT8 * 4).from_address(mem)

  for idx in range (elems):

    Source[idx] = (Source[idx] << 24 ) | ((Source[idx] >> 8 ) & 0xFF00) | \
                  (Source[idx] >> 24 ) | ((Source[idx] & 0xFF00) << 8)

def byteswap_8 (mem, elems):

  Source = (EfiPy.UINT8 * 8).from_address(mem)

  for idx in range (elems):

    Source[idx] = (Source[idx] << 56 )               | ((Source[idx] >> 48 ) & 0x0000FF00) |  \
                 ((Source[idx] << 24 ) & 0x00FF0000) | ((Source[idx] >>  8 ) & 0xFF000000) |  \
                 ((Source[idx] & 0xFF000000) <<  8 ) | ((Source[idx] & 0x00FF0000) << 24 ) |  \
                 ((Source[idx] & 0x0000FF00) << 48 ) |  (Source[idx]               >> 56 )

def setitem_schar (mem, ind, val):

  Buffer = (EfiPy.INT8 * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_uchar (mem, ind, val):

  Buffer = (EfiPy.UINT8 * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_sshort (mem, ind, val):

  Buffer = (EfiPy.c_short * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_ushort (mem, ind, val):

  Buffer = (EfiPy.c_ushort * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_sint (mem, ind, val):

  Buffer = (EfiPy.INTN * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_uint (mem, ind, val):

  Buffer = (EfiPy.UINTN * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_slong (mem, ind, val):

  Buffer = (EfiPy.c_long * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_ulong (mem, ind, val):

  Buffer = (EfiPy.c_ulong * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_float (mem, ind, val):

  Buffer = (EfiPy.c_float * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def setitem_double (mem, ind, val):

  Buffer = (EfiPy.c_double * (ind + 1)).from_address(mem)
  Buffer[ind] = val

def getitem_schar (mem, ind, val):

  Buffer = (EfiPy.c_char * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_uchar (mem, ind, val):

  Buffer = (EfiPy.c_ubyte * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_sshort (mem, ind, val):

  Buffer = (EfiPy.c_short * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_ushort (mem, ind, val):

  Buffer = (EfiPy.c_ushort * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_sint (mem, ind, val):

  Buffer = (EfiPy.c_int * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_uint (mem, ind, val):

  Buffer = (EfiPy.c_uint * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_slong (mem, ind, val):

  Buffer = (EfiPy.c_long * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_ulong (mem, ind, val):

  Buffer = (EfiPy.c_ulong * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_float (mem, ind, val):

  Buffer = (EfiPy.c_float * (ind + 1)).from_address(mem)
  return Buffer[ind]

def getitem_double (mem, ind, val):

  Buffer = (EfiPy.c_double * (ind + 1)).from_address(mem)
  return Buffer[ind]
