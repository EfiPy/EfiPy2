# ShellDynamicCommand.py
#
# EfiPy2.MdePkg.Protocol.ShellDynamicCommand
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Shell           import EFI_SHELL_PROTOCOL

from EfiPy2.MdePkg.Protocol.ShellParameters import EFI_SHELL_PARAMETERS_PROTOCOL

gEfiShellDynamicCommandProtocolGuid           = \
  EFI_GUID (0x3c7200e9, 0x005f, 0x4ea4, ( 0x87, 0xde, 0xa3, 0xdf, 0xac, 0x8a, 0x27, 0xc3 ))

class EFI_SHELL_DYNAMIC_COMMAND_PROTOCOL (Structure):
  pass

SHELL_COMMAND_HANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SHELL_DYNAMIC_COMMAND_PROTOCOL),  #   IN *This
  POINTER(EFI_SYSTEM_TABLE),                    #   IN *SystemTable,
  POINTER(EFI_SHELL_PARAMETERS_PROTOCOL),       #   IN *ShellParameters,
  POINTER(EFI_SHELL_PROTOCOL)                   #   IN *Shell
  )

SHELL_COMMAND_GETHELP = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(EFI_SHELL_DYNAMIC_COMMAND_PROTOCOL),  #   IN       *This
  POINTER(CHAR8)                                #   IN CONST *Language
  )

EFI_SHELL_DYNAMIC_COMMAND_PROTOCOL._fields_ = [
    ("CommandName", POINTER(CHAR16)),
    ("Handler",     SHELL_COMMAND_HANDLER),
    ("GetHelp",     SHELL_COMMAND_GETHELP)
  ]

