# ProcessorBind.py
#
# EfiPy2.MdePkg.Uefi.ProcessorBind
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from ctypes   import *

UINTN   = c_uint64
INTN    = c_int64
UINT64  = c_uint64
INT64   = c_int64
UINT32  = c_uint32
INT32   = c_int32
UINT16  = c_uint16
INT16   = c_int16
UINT8   = c_uint8
INT8    = c_int8
BOOLEAN = c_uint8
CHAR16  = c_wchar
PCHAR16 = c_wchar_p
CHAR8   = c_char
PCHAR8  = c_char_p

UINTN_BE   = c_uint64.__ctype_be__
INTN_BE    = c_int64.__ctype_be__
UINT64_BE  = c_uint64.__ctype_be__
INT64_BE   = c_int64.__ctype_be__
UINT32_BE  = c_uint32.__ctype_be__
INT32_BE   = c_int32.__ctype_be__
UINT16_BE  = c_uint16.__ctype_be__
INT16_BE   = c_int16.__ctype_be__
UINT8_BE   = c_uint8.__ctype_be__
INT8_BE    = c_int8.__ctype_be__
BOOLEAN_BE = c_uint8.__ctype_be__
