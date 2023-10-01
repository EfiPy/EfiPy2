# PciHotPlugInit.py
#
# EfiPy2.MdePkg.Protocol.PciHotPlugInit
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPciHotPlugInitProtocolGuid  = \
  EFI_GUID (0xaa0e8bc1, 0xdabc, 0x46b0, (0xa8, 0x44, 0x37, 0xb8, 0x16, 0x9b, 0x2b, 0xea ))

class EFI_PCI_HOT_PLUG_INIT_PROTOCOL (Structure):
  pass

EFI_HPC_STATE = UINT16

EFI_HPC_STATE_INITIALIZED    = 0x01
EFI_HPC_STATE_ENABLED        = 0x02

class EFI_HPC_LOCATION (Structure):
  _fields_ = [
    ("HpcDevicePath", POINTER(EFI_DEVICE_PATH_PROTOCOL)),
    ("HpbDevicePath", POINTER(EFI_DEVICE_PATH_PROTOCOL))
  ]

EfiPaddingPciBus            = 0
EfiPaddingPciRootBridge     = 1
EFI_HPC_PADDING_ATTRIBUTES  = ENUM

EFI_GET_ROOT_HPC_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOT_PLUG_INIT_PROTOCOL),  # IN  *This,
  POINTER(UINTN),                           # OUT *HpcCount,
  POINTER(POINTER(EFI_HPC_LOCATION))        # OUT **HpcList
  )

EFI_INITIALIZE_ROOT_HPC = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOT_PLUG_INIT_PROTOCOL),  # IN  *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN  *HpcDevicePath,
  UINT64,                                   # IN  HpcPciAddress,
  EFI_EVENT,                                # IN  Event,           OPTIONAL
  POINTER(EFI_HPC_STATE)                    # OUT *HpcState
  )

EFI_GET_HOT_PLUG_PADDING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_HOT_PLUG_INIT_PROTOCOL),  # IN  *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),        # IN  *HpcDevicePath,
  UINT64,                                   # IN  HpcPciAddress,
  POINTER(EFI_HPC_STATE),                   # OUT *HpcState,
  POINTER(PVOID),                           # OUT **Padding,
  POINTER(EFI_HPC_PADDING_ATTRIBUTES)       # OUT *Attributes
  )

EFI_PCI_HOT_PLUG_INIT_PROTOCOL._fields_ = [
    ("GetRootHpcList",      EFI_GET_ROOT_HPC_LIST),
    ("InitializeRootHpc",   EFI_INITIALIZE_ROOT_HPC),
    ("GetResourcePadding",  EFI_GET_HOT_PLUG_PADDING)
  ]

