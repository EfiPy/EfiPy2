# SdMmcPassThru.py
#
# EfiPy2.MdePkg.Protocol.SdMmcPassThru
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSdMmcPassThruProtocolGuid           = \
  EFI_GUID (0x716ef0d9, 0xff83, 0x4f69, (0x81, 0xe9, 0x51, 0x8b, 0xd3, 0x9a, 0x8e, 0x70 ))

class EFI_SD_MMC_PASS_THRU_PROTOCOL (Structure):
  pass

SdMmcCommandTypeBc      = 1
SdMmcCommandTypeBcr     = 2
SdMmcCommandTypeAc      = 3
SdMmcCommandTypeAdtc    = 4
EFI_SD_MMC_COMMAND_TYPE = ENUM

SdMmcResponseTypeR1      = 1 
SdMmcResponseTypeR1b     = 2 
SdMmcResponseTypeR2      = 3 
SdMmcResponseTypeR3      = 4 
SdMmcResponseTypeR4      = 5 
SdMmcResponseTypeR5      = 6 
SdMmcResponseTypeR5b     = 7 
SdMmcResponseTypeR6      = 8 
SdMmcResponseTypeR7      = 9 
EFI_SD_MMC_RESPONSE_TYPE = ENUM

class EFI_SD_MMC_COMMAND_BLOCK (Structure):
  _fields_ = [
    ("CommandIndex",    UINT16),
    ("CommandArgument", UINT32),
    ("CommandType",     UINT32),
    ("ResponseType",    UINT32)
  ]

class EFI_SD_MMC_STATUS_BLOCK (Structure):
  _fields_ = [
    ("Resp0",    UINT32),
    ("Resp1",    UINT32),
    ("Resp2",    UINT32),
    ("Resp3",    UINT32)
  ]

class EFI_SD_MMC_PASS_THRU_COMMAND_PACKET (Structure):
  _fields_ = [
    ("Timeout",             UINT64),
    ("SdMmcCmdBlk",         POINTER(EFI_SD_MMC_COMMAND_BLOCK)),
    ("SdMmcStatusBlk",      POINTER(EFI_SD_MMC_STATUS_BLOCK)),
    ("InDataBuffer",        PVOID),
    ("OutDataBuffer",       PVOID),
    ("InTransferLength",    UINT32),
    ("OutTransferLength",   UINT32),
    ("TransactionStatus",   EFI_STATUS)
  ]

EFI_SD_MMC_PASS_THRU_PASSTHRU = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SD_MMC_PASS_THRU_PROTOCOL),       #   IN     *This
  UINT8,                                        #   IN     Slot,
  POINTER(EFI_SD_MMC_PASS_THRU_COMMAND_PACKET), #   IN OUT *Packet,
  EFI_EVENT                                     #   IN     Event    OPTIONAL
  )

EFI_SD_MMC_PASS_THRU_GET_NEXT_SLOT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SD_MMC_PASS_THRU_PROTOCOL),       #   IN     *This,
  POINTER(UINT8),                               #   IN OUT *Slot
  )

EFI_SD_MMC_PASS_THRU_BUILD_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SD_MMC_PASS_THRU_PROTOCOL),       #   IN     *This,
  UINT8,                                        #   IN     Slot,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))    #      OUT **DevicePath
  )

EFI_SD_MMC_PASS_THRU_GET_SLOT_NUMBER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SD_MMC_PASS_THRU_PROTOCOL),       #   IN  *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),            #   IN  *DevicePath,
  POINTER(UINT8)                                #   OUT *Slot
  )

EFI_SD_MMC_PASS_THRU_RESET_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SD_MMC_PASS_THRU_PROTOCOL),   #   IN  *This,
  UINT8                                     #   IN  Slot
  )

EFI_SD_MMC_PASS_THRU_PROTOCOL._fields_ = [
    ("IoAlign",         UINT32),
    ("PassThru",        EFI_SD_MMC_PASS_THRU_PASSTHRU),
    ("GetNextSlot",     EFI_SD_MMC_PASS_THRU_GET_NEXT_SLOT),
    ("BuildDevicePath", EFI_SD_MMC_PASS_THRU_BUILD_DEVICE_PATH),
    ("GetSlotNumber",   EFI_SD_MMC_PASS_THRU_GET_SLOT_NUMBER),
    ("ResetDevice",     EFI_SD_MMC_PASS_THRU_RESET_DEVICE)
  ]

