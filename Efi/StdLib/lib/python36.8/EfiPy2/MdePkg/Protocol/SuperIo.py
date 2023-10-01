# SuperIo.py
#
# EfiPy2.MdePkg.Protocol.SuperIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard  import Acpi

gEfiSioProtocolGuid   = \
  EFI_GUID (0x215fdd18, 0xbd50, 0x4feb, ( 0x89, 0xb, 0x58, 0xca, 0xb, 0x47, 0x39, 0xe9 ))

class ACPI_RESOURCE_HEADER_PTR (Union):
  _fields_ = [
    ("SmallHeader", POINTER(Acpi.ACPI_SMALL_RESOURCE_HEADER)),
    ("LargeHeader", POINTER(Acpi.ACPI_LARGE_RESOURCE_HEADER))
  ]

class EFI_SIO_REGISTER_MODIFY (Structure):
  _fields_ = [
    ("Register",  UINT8),
    ("AndMask",   UINT8),
    ("OrMask",    UINT8)
  ]

class EFI_SIO_PROTOCOL (Structure):
  pass

EFI_SIO_REGISTER_ACCESS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_PROTOCOL),            # IN      *This
  BOOLEAN,                              # IN      Write,
  BOOLEAN,                              # IN      ExitCfgMode,
  UINT8,                                # IN      Register,
  POINTER(UINT8)                        # IN OUT  *Value
  )

EFI_SIO_GET_RESOURCES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_PROTOCOL),            # IN      *This
  POINTER(ACPI_RESOURCE_HEADER_PTR)     #    OUT  *ResourceList
  )

EFI_SIO_SET_RESOURCES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_PROTOCOL),  # IN      *This
  ACPI_RESOURCE_HEADER_PTR    # IN      ResourceList
  )

EFI_SIO_POSSIBLE_RESOURCES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_PROTOCOL),            # IN      *This
  POINTER(ACPI_RESOURCE_HEADER_PTR)     #    OUT  *ResourceCollection
  )

EFI_SIO_MODIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_PROTOCOL),            # IN      *This
  POINTER(EFI_SIO_REGISTER_MODIFY),     # IN      *Command,
  UINTN                                 # IN      NumberOfCommands
  )

EFI_SIO_PROTOCOL._fields_ = [
    ("RegisterAccess",    EFI_SIO_REGISTER_ACCESS),
    ("GetResources",      EFI_SIO_GET_RESOURCES),
    ("SetResources",      EFI_SIO_SET_RESOURCES),
    ("PossibleResources", EFI_SIO_POSSIBLE_RESOURCES),
    ("Modify",            EFI_SIO_MODIFY)
  ]

