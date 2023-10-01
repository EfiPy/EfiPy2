# SmbusHc.py
#
# EfiPy2.MdePkg.Protocol.SmbusHc
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.SmBus   import  EFI_SMBUS_DEVICE_COMMAND,   \
                                                    EFI_SMBUS_OPERATION,        \
                                                    EFI_SMBUS_UDID,             \
                                                    EFI_SMBUS_DEVICE_MAP,       \
                                                    EFI_SMBUS_DEVICE_ADDRESS

gEfiSmbusHcProtocolGuid     = \
  EFI_GUID (0xe49d33ed, 0x513d, 0x4634, ( 0xb6, 0x98, 0x6f, 0x55, 0xaa, 0x75, 0x1c, 0x1b))

class EFI_SMBUS_HC_PROTOCOL (Structure):
  pass

EFI_SMBUS_HC_EXECUTE_OPERATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL), # IN      *This
  EFI_SMBUS_DEVICE_ADDRESS,       # IN      SlaveAddress,
  EFI_SMBUS_DEVICE_COMMAND,       # IN      Command,
  EFI_SMBUS_OPERATION,            # IN      Operation,
  BOOLEAN,                        # IN      PecCheck,
  POINTER(UINTN),                 # IN OUT  *Length,
  PVOID                           # IN OUT  *Buffer
  )

EFI_SMBUS_HC_PROTOCOL_ARP_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),       # IN      *This
  BOOLEAN,                              # IN      ArpAll,
  POINTER(EFI_SMBUS_UDID),              # IN      *SmbusUdid,   OPTIONAL
  POINTER(EFI_SMBUS_DEVICE_ADDRESS)     # IN OUT  *SlaveAddress OPTIONAL
  )

EFI_SMBUS_HC_PROTOCOL_GET_ARP_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),           # IN      *This
  POINTER(UINTN),                           # IN OUT  *Length,
  POINTER(POINTER(EFI_SMBUS_DEVICE_MAP))    # IN OUT  **SmbusDeviceMap
  )

EFI_SMBUS_NOTIFY_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  EFI_SMBUS_DEVICE_ADDRESS, # IN  SlaveAddress,
  UINTN                     # IN  Data
  )

EFI_SMBUS_HC_PROTOCOL_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBUS_HC_PROTOCOL),   # IN  *This,
  EFI_SMBUS_DEVICE_ADDRESS,         # IN  SlaveAddress,
  UINTN,                            # IN  Data,
  EFI_SMBUS_NOTIFY_FUNCTION         # IN  NotifyFunction
  )

EFI_SMBUS_HC_PROTOCOL._fields_ = [
    ("Execute",   EFI_SMBUS_HC_EXECUTE_OPERATION),
    ("ArpDevice", EFI_SMBUS_HC_PROTOCOL_ARP_DEVICE),
    ("GetArpMap", EFI_SMBUS_HC_PROTOCOL_GET_ARP_MAP),
    ("Notify",    EFI_SMBUS_HC_PROTOCOL_NOTIFY)
  ]

