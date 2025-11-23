# DebugPort.py
#
# EfiPy2.MdePkg.Protocol.DebugPort
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL

gEfiDebugPortProtocolGuid               = \
  EFI_GUID (0xEBA4E8D2, 0x3858, 0x41EC, (0xA2, 0x81, 0x26, 0x47, 0xBA, 0x96, 0x60, 0xD0 ))

EFI_DEBUGPORT_PROTOCOL_GUID = gEfiDebugPortProtocolGuid

class EFI_DEBUGPORT_PROTOCOL (Structure):
  pass

EFI_DEBUGPORT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL) # IN *This
  )

EFI_DEBUGPORT_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             # IN     *Buffer
  )

EFI_DEBUGPORT_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             #    OUT *Buffer
  )

EFI_DEBUGPORT_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL)   # IN     *This
  )

EFI_DEBUGPORT_PROTOCOL._fields_ = [
    ("Reset",   EFI_DEBUGPORT_RESET),
    ("Write",   EFI_DEBUGPORT_WRITE),
    ("Read",    EFI_DEBUGPORT_READ),
    ("Poll",    EFI_DEBUGPORT_POLL)
  ]

EFI_DEBUGPORT_VARIABLE_NAME = "DEBUGPORT"
EFI_DEBUGPORT_VARIABLE_GUID = EFI_DEBUGPORT_PROTOCOL_GUID

gEfiDebugPortVariableGuid = gEfiDebugPortProtocolGuid

DEVICE_PATH_MESSAGING_DEBUGPORT  = EFI_DEBUGPORT_PROTOCOL_GUID

gEfiDebugPortDevicePathGuid = gEfiDebugPortProtocolGuid

class DEBUGPORT_DEVICE_PATH (Structure):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",    EFI_GUID)
  ]

