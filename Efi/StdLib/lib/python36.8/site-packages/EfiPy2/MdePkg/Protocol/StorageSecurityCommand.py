# StorageSecurityCommand.py
#
# EfiPy2.MdePkg.Protocol.StorageSecurityCommand
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiStorageSecurityCommandProtocolGuid  = \
  EFI_GUID (0xC88B0B6D, 0x0DFC, 0x49A7, (0x9C, 0xB4, 0x49, 0x07, 0x4B, 0x4C, 0x3A, 0x78 ))

class EFI_STORAGE_SECURITY_COMMAND_PROTOCOL (Structure):
  pass

EFI_STORAGE_SECURITY_RECEIVE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_STORAGE_SECURITY_COMMAND_PROTOCOL),   # IN  *This
  UINT32,                                           # IN  MediaId,
  UINT64,                                           # IN  Timeout,
  UINT8,                                            # IN  SecurityProtocolId,
  UINT16,                                           # IN  SecurityProtocolSpecificData,
  UINTN,                                            # IN  PayloadBufferSize,
  PVOID,                                            # OUT *PayloadBuffer,
  POINTER(UINTN)                                    # OUT *PayloadTransferSize
  )

EFI_STORAGE_SECURITY_SEND_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_STORAGE_SECURITY_COMMAND_PROTOCOL),   # IN  *This
  UINT32,                                           # IN  MediaId,
  UINT64,                                           # IN  Timeout,
  UINT8,                                            # IN  SecurityProtocolId,
  UINT16,                                           # IN  SecurityProtocolSpecificData,
  UINTN,                                            # IN  PayloadBufferSize,
  PVOID                                             # OUT *PayloadBuffer,
  )

EFI_STORAGE_SECURITY_COMMAND_PROTOCOL._fields_ = [
    ("ReceiveData", EFI_STORAGE_SECURITY_RECEIVE_DATA),
    ("SendData",    EFI_STORAGE_SECURITY_SEND_DATA)
  ]

