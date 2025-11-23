# IdeControllerInit.py
#
# EfiPy2.MdePkg.Protocol.IdeControllerInit
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard import Atapi

gEfiIdeControllerInitProtocolGuid = \
  EFI_GUID (0xa1e37052, 0x80d9, 0x4e65, (0xa3, 0x17, 0x3e, 0x9a, 0x55, 0xc4, 0x3e, 0xc9 ))

class EFI_IDE_CONTROLLER_INIT_PROTOCOL (Structure):
  pass

EfiIdeBeforeChannelEnumeration          = 0
EfiIdeAfterChannelEnumeration           = 1
EfiIdeBeforeChannelReset                = 2
EfiIdeAfterChannelReset                 = 3
EfiIdeBusBeforeDevicePresenceDetection  = 4
EfiIdeBusAfterDevicePresenceDetection   = 5
EfiIdeResetMode                         = 6
EfiIdeBusPhaseMaximum                   = 7
EFI_IDE_CONTROLLER_ENUM_PHASE           = ENUM

EfiAtaSataTransferProtocol      = 0
EFI_ATA_EXT_TRANSFER_PROTOCOL   = ENUM

EFI_SATA_AUTO_SPEED  = 0

EFI_SATA_GEN1_SPEED  = 1

EFI_SATA_GEN2_SPEED  = 2

class EFI_ATA_MODE (Structure):
  _fields_ = [
    ("Valid", BOOLEAN),
    ("Mode",  UINT32)
  ]

class EFI_ATA_EXTENDED_MODE (Structure):
  _fields_ = [
    ("TransferProtocol",  EFI_ATA_EXT_TRANSFER_PROTOCOL),
    ("Mode",              UINT32)
  ]

class EFI_ATA_COLLECTIVE_MODE (Structure):
  _fields_ = [
    ("PioMode",             EFI_ATA_MODE),            
    ("SingleWordDmaMode",   EFI_ATA_MODE),            
    ("MultiWordDmaMode",    EFI_ATA_MODE),            
    ("UdmaMode",            EFI_ATA_MODE),            
    ("ExtModeCount",        UINT32),                  
    ("ExtMode",             EFI_ATA_EXTENDED_MODE * 1)
  ]

EFI_ATA_IDENTIFY_DATA   = Atapi.ATA_IDENTIFY_DATA
EFI_ATAPI_IDENTIFY_DATA = Atapi.ATAPI_IDENTIFY_DATA

EFI_ATAPI_DEVICE_IDENTIFY_DATA  = 0x8000

class EFI_IDENTIFY_DATA (Union):
  _fields_ = [
    ("AtaData",   EFI_ATA_IDENTIFY_DATA),
    ("AtapiData", EFI_ATAPI_IDENTIFY_DATA),
  ]

EFI_IDE_CONTROLLER_GET_CHANNEL_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  UINT8,                                      # IN  Channel,
  POINTER(BOOLEAN),                           # OUT *Enabled,
  POINTER(UINT8)                              # OUT *MaxDevices
  )

EFI_IDE_CONTROLLER_NOTIFY_PHASE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  EFI_IDE_CONTROLLER_ENUM_PHASE,              # IN  Phase,
  UINT8                                       # IN  Channel
  )

EFI_IDE_CONTROLLER_SUBMIT_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  UINT8,                                      # IN  Channel
  UINT8,                                      # IN  Device
  POINTER(EFI_IDENTIFY_DATA)                  # IN  *IdentifyData
  )

EFI_IDE_CONTROLLER_DISQUALIFY_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  UINT8,                                      # IN  Channel
  UINT8,                                      # IN  Device
  POINTER(EFI_ATA_COLLECTIVE_MODE)            # IN  *BadModes
  )

EFI_IDE_CONTROLLER_CALCULATE_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  UINT8,                                      # IN  Channel
  UINT8,                                      # IN  Device
  POINTER(POINTER(EFI_ATA_COLLECTIVE_MODE))   # OUT **SupportedModes
  )

EFI_IDE_CONTROLLER_SET_TIMING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_IDE_CONTROLLER_INIT_PROTOCOL),  # IN  *This
  UINT8,                                      # IN  Channel
  UINT8,                                      # IN  Device
  POINTER(EFI_ATA_COLLECTIVE_MODE)            # IN  *Modes
  )

EFI_IDE_CONTROLLER_INIT_PROTOCOL._fields_ = [
    ("GetChannelInfo", EFI_IDE_CONTROLLER_GET_CHANNEL_INFO),
    ("NotifyPhase",    EFI_IDE_CONTROLLER_NOTIFY_PHASE),
    ("SubmitData",     EFI_IDE_CONTROLLER_SUBMIT_DATA),
    ("DisqualifyMode", EFI_IDE_CONTROLLER_DISQUALIFY_MODE),
    ("CalculateMode",  EFI_IDE_CONTROLLER_CALCULATE_MODE),
    ("SetTiming",      EFI_IDE_CONTROLLER_SET_TIMING),
    ("EnumAll",        BOOLEAN),
    ("ChannelCount",   UINT8),
  ]

