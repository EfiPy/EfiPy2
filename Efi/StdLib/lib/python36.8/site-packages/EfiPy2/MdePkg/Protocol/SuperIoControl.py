# SuperIoControl.py
#
# EfiPy2.MdePkg.Protocol.SuperIoControl
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSioControlProtocolGuid    = \
  EFI_GUID (0xb91978df, 0x9fc1, 0x427d, ( 0xbb, 0x5, 0x4c, 0x82, 0x84, 0x55, 0xca, 0x27 ))

class EFI_SIO_CONTROL_PROTOCOL (Structure):
  pass
PEFI_SIO_CONTROL_PROTOCOL       = POINTER (EFI_SIO_CONTROL_PROTOCOL)

EFI_SIO_CONTROL_ENABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_CONTROL_PROTOCOL)     # IN      *This
  )

EFI_SIO_CONTROL_DISABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIO_CONTROL_PROTOCOL)     # IN      *This
  )

EFI_SIO_CONTROL_PROTOCOL._fields_ = [
    ("Version",       UINT32),
    ("EnableDevice",  EFI_SIO_CONTROL_ENABLE),
    ("DisableDevice", EFI_SIO_CONTROL_DISABLE)
  ]

