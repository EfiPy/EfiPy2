# BluetoothHc.py
#
# EfiPy2.MdePkg.Protocol.BluetoothHc
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiBluetoothHcProtocolGuid         = \
  EFI_GUID (0xb3930571, 0xbeba, 0x4fc5, ( 0x92, 0x3, 0x94, 0x27, 0x24, 0x2e, 0x6a, 0x43 ))

class EFI_BLUETOOTH_HC_PROTOCOL (Structure):
  pass

EFI_BLUETOOTH_HC_SEND_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL), # IN      *This
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID,                              # IN      *Buffer,
  UINTN                               # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL), # IN      *This
  POINTER(UINTN),                     # IN OUT  *BufferSize,
  PVOID,                              #    OUT  *Buffer,
  UINTN                               # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  PVOID,      # IN  *Data,
  UINTN,      # IN  DataLength,
  PVOID       # IN  *Context
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL),   # IN *This
  BOOLEAN,                              # IN IsNewTransfer,
  UINTN,                                # IN PollingInterval,
  UINTN,                                # IN DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN Callback,
  PVOID                                 # IN *Context
  )

EFI_BLUETOOTH_HC_SEND_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_HC_PROTOCOL),   # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                # IN      *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                #    OUT  *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_ACL_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN  *This
  BOOLEAN,                              # IN  IsNewTransfer,
  UINTN,                                # IN  PollingInterval,
  UINTN,                                # IN  DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN  Callback,
  PVOID                                 # IN  *Context
  )

EFI_BLUETOOTH_HC_SEND_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                # IN      *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_RECEIVE_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN      *This
  POINTER (UINTN),                      # IN OUT  *BufferSize,
  PVOID,                                #    OUT  *Buffer,
  UINTN                                 # IN      Timeout
  )

EFI_BLUETOOTH_HC_ASYNC_RECEIVE_SCO_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLUETOOTH_HC_PROTOCOL),  # IN  *This
  BOOLEAN,                              # IN  IsNewTransfer,
  UINTN,                                # IN  PollingInterval,
  UINTN,                                # IN  DataLength,
  EFI_BLUETOOTH_HC_ASYNC_FUNC_CALLBACK, # IN  Callback,
  PVOID                                 # IN  *Context
  )

EFI_BLUETOOTH_HC_PROTOCOL._fields_ = [
    ("SendCommand",         EFI_BLUETOOTH_HC_SEND_COMMAND),
    ("ReceiveEvent",        EFI_BLUETOOTH_HC_RECEIVE_EVENT),
    ("AsyncReceiveEvent",   EFI_BLUETOOTH_HC_ASYNC_RECEIVE_EVENT),
    ("SendACLData",         EFI_BLUETOOTH_HC_SEND_ACL_DATA),
    ("ReceiveACLData",      EFI_BLUETOOTH_HC_RECEIVE_ACL_DATA),
    ("AsyncReceiveACLData", EFI_BLUETOOTH_HC_ASYNC_RECEIVE_ACL_DATA),
    ("SendSCOData",         EFI_BLUETOOTH_HC_SEND_SCO_DATA),
    ("ReceiveSCOData",      EFI_BLUETOOTH_HC_RECEIVE_SCO_DATA),
    ("AsyncReceiveSCOData", EFI_BLUETOOTH_HC_ASYNC_RECEIVE_SCO_DATA)
  ]

