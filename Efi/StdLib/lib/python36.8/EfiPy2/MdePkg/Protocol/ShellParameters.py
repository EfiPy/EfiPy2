# ShellParameters.py
#
# EfiPy2.MdePkg.Protocol.ShellParameters
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Shell import SHELL_FILE_HANDLE

gEfiShellParametersProtocolGuid           = \
  EFI_GUID (0x752f3136, 0x4e16, 0x4fdc, ( 0xa2, 0x2a, 0xe5, 0xf4, 0x68, 0x12, 0xf4, 0xca ))

class EFI_SHELL_PARAMETERS_PROTOCOL (Structure):
  _fields_ = [
    ("Argv",    POINTER(POINTER(CHAR16))),
    ("Argc",    UINTN),
    ("StdIn",   SHELL_FILE_HANDLE),
    ("StdOut",  SHELL_FILE_HANDLE),
    ("StdErr",  SHELL_FILE_HANDLE)
  ]

