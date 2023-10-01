# DriverDiagnostics.py
#
# EfiPy2.MdePkg.Protocol.DriverDiagnostics
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDriverDiagnosticsProtocolGuid       = \
  EFI_GUID (0x0784924f, 0xe296, 0x11d4, (0x9a, 0x49, 0x0, 0x90, 0x27, 0x3f, 0xc1, 0x4d ))

class EFI_DRIVER_DIAGNOSTICS_PROTOCOL (Structure):
  pass

EfiDriverDiagnosticTypeStandard     = 0
EfiDriverDiagnosticTypeExtended     = 1
EfiDriverDiagnosticTypeManufacturing= 2
EfiDriverDiagnosticTypeCancel       = 3
EfiDriverDiagnosticTypeMaximum      = 4
EFI_DRIVER_DIAGNOSTIC_TYPE          = ENUM

EFI_DRIVER_DIAGNOSTICS_RUN_DIAGNOSTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_DIAGNOSTICS_PROTOCOL), # IN  *This
  EFI_HANDLE,                               # IN  ControllerHandle,
  EFI_HANDLE,                               # IN  ChildHandle  OPTIONAL,
  EFI_DRIVER_DIAGNOSTIC_TYPE,               # IN  DiagnosticType,
  PCHAR8,                                   # IN  *Language,
  POINTER(POINTER(EFI_GUID)),               # OUT **ErrorType,
  POINTER(UINTN),                           # OUT *BufferSize,
  POINTER(PCHAR16)                          # OUT **Buffer
  )

EFI_DRIVER_DIAGNOSTICS_PROTOCOL._fields_ = [
    ("RunDiagnostics",      EFI_DRIVER_DIAGNOSTICS_RUN_DIAGNOSTICS),
    ("SupportedLanguages",  PCHAR8)
  ]

