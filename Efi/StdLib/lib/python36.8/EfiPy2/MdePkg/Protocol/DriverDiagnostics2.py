# DriverDiagnostics2.py
#
# EfiPy2.MdePkg.Protocol.DriverDiagnostics2
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import DriverDiagnostics

gEfiDriverDiagnostics2ProtocolGuid       = \
  EFI_GUID (0x4d330321, 0x025f, 0x4aac, (0x90, 0xd8, 0x5e, 0xd9, 0x00, 0x17, 0x3b, 0x63 ))

class EFI_DRIVER_DIAGNOSTICS2_PROTOCOL (Structure):
  pass

EFI_DRIVER_DIAGNOSTICS2_RUN_DIAGNOSTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_DIAGNOSTICS2_PROTOCOL),    # IN  *This
  EFI_HANDLE,                                   # IN  ControllerHandle,
  EFI_HANDLE,                                   # IN  ChildHandle  OPTIONAL,
  DriverDiagnostics.EFI_DRIVER_DIAGNOSTIC_TYPE, # IN  DiagnosticType,
  PCHAR8,                                       # IN  *Language,
  POINTER(POINTER(EFI_GUID)),                   # OUT **ErrorType,
  POINTER(UINTN),                               # OUT *BufferSize,
  POINTER(PCHAR16)                              # OUT **Buffer
  )

EFI_DRIVER_DIAGNOSTICS2_PROTOCOL._fields_ = [
    ("RunDiagnostics",      EFI_DRIVER_DIAGNOSTICS2_RUN_DIAGNOSTICS),
    ("SupportedLanguages",  PCHAR8)
  ]

