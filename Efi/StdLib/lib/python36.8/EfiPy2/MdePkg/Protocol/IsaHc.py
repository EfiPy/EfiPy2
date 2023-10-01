# IsaHc.py
#
# EfiPy2.MdePkg.Protocol.IsaHc
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiIsaHcProtocolGuid               = \
  EFI_GUID (0xbcdaf080, 0x1bde, 0x4e22, (0xae, 0x6a, 0x43, 0x54, 0x1e, 0x12, 0x8e, 0xc4))

gEfiIsaHcServiceBindingProtocolGuid = \
  EFI_GUID (0xfad7933a, 0x6c21, 0x4234, (0xa4, 0x34, 0x0a, 0x8a, 0x0d, 0x2b, 0x07, 0x81))

class EFI_ISA_HC_PROTOCOL (Structure):
  pass

PEFI_ISA_HC_PROTOCOL = POINTER(EFI_ISA_HC_PROTOCOL)

EFI_ISA_HC_OPEN_IO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_HC_PROTOCOL),   # IN  *This
  UINT16,                         # IN  IoAddress,
  UINT16,                         # IN  IoLength,
  POINTER(UINT64)                 # OUT *IoApertureHandle
  )

EFI_ISA_HC_CLOSE_IO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ISA_HC_PROTOCOL),   # IN  *This
  UINT64                          # IN  IoApertureHandle
  )

EFI_ISA_HC_PROTOCOL._fields_ = [
  ("Version",         UINT32),
  ("OpenIoAperture",  EFI_ISA_HC_OPEN_IO),
  ("CloseIoAperture", EFI_ISA_HC_CLOSE_IO)
  ]

