# EfiShellInterface.py
#
# EfiPy2.ShellPkg.Protocol.EfiShellInterface
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.LoadedImage         import EFI_LOADED_IMAGE_PROTOCOL
from EfiPy2.MdePkg.Protocol.SimpleFileSystem    import EFI_FILE_PROTOCOL

gEfiShellInterfaceGuid                 = \
  EFI_GUID (0x47c7b223, 0xc42a, 0x11d2, (0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

ARG_NO_ATTRIB         = 0x0
ARG_IS_QUOTED         = BIT0
ARG_PARTIALLY_QUOTED  = BIT1
ARG_FIRST_HALF_QUOTED = BIT2
ARG_FIRST_CHAR_IS_ESC = BIT3
EFI_SHELL_ARG_INFO_TYPES = ENUM

class EFI_SHELL_ARG_INFO (Structure):
  _fields_ = [
    ("Attributes",  UINT32)
  ]

class EFI_SHELL_INTERFACE (Structure):
  _fields_ = [
    ("ImageHandle;  ", EFI_HANDLE),
    ("Info;         ", POINTER(EFI_LOADED_IMAGE_PROTOCOL)),
    ("Argv;         ", POINTER(POINTER(CHAR16))),
    ("Argc;         ", UINTN),
    ("RedirArgv;    ", POINTER(POINTER(CHAR16))),
    ("RedirArgc;    ", UINTN),
    ("StdIn;        ", POINTER(EFI_FILE_PROTOCOL)),
    ("StdOut;       ", POINTER(EFI_FILE_PROTOCOL)),
    ("StdErr;       ", POINTER(EFI_FILE_PROTOCOL)),
    ("ArgInfo;      ", POINTER(EFI_SHELL_ARG_INFO)),
    ("EchoOn;       ", BOOLEAN)
  ]

