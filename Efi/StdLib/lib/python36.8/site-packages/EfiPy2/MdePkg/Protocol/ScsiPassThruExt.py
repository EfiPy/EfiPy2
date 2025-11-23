# ScsiPassThruExt.py
#
# EfiPy2.MdePkg.Protocol.ScsiPassThruExt
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiExtScsiPassThruProtocolGuid = \
  EFI_GUID (0x143b7632, 0xb81b, 0x4cb7, (0xab, 0xd3, 0xb6, 0x25, 0xa5, 0xb9, 0xbf, 0xfe ))

class EFI_EXT_SCSI_PASS_THRU_PROTOCOL (Structure):
  pass

TARGET_MAX_BYTES                             = 0x10

EFI_EXT_SCSI_PASS_THRU_ATTRIBUTES_PHYSICAL   = 0x0001
EFI_EXT_SCSI_PASS_THRU_ATTRIBUTES_LOGICAL    = 0x0002
EFI_EXT_SCSI_PASS_THRU_ATTRIBUTES_NONBLOCKIO = 0x0004

EFI_EXT_SCSI_DATA_DIRECTION_READ             = 0
EFI_EXT_SCSI_DATA_DIRECTION_WRITE            = 1
EFI_EXT_SCSI_DATA_DIRECTION_BIDIRECTIONAL    = 2

EFI_EXT_SCSI_STATUS_HOST_ADAPTER_OK                    = 0x00
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_TIMEOUT_COMMAND       = 0x09
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_TIMEOUT               = 0x0b
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_MESSAGE_REJECT        = 0x0d
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_BUS_RESET             = 0x0e
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_PARITY_ERROR          = 0x0f
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_REQUEST_SENSE_FAILED  = 0x10
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_SELECTION_TIMEOUT     = 0x11
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_DATA_OVERRUN_UNDERRUN = 0x12
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_BUS_FREE              = 0x13
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_PHASE_ERROR           = 0x14
EFI_EXT_SCSI_STATUS_HOST_ADAPTER_OTHER                 = 0x7f

EFI_EXT_SCSI_STATUS_TARGET_GOOD                        = 0x00
EFI_EXT_SCSI_STATUS_TARGET_CHECK_CONDITION             = 0x02
EFI_EXT_SCSI_STATUS_TARGET_CONDITION_MET               = 0x04
EFI_EXT_SCSI_STATUS_TARGET_BUSY                        = 0x08
EFI_EXT_SCSI_STATUS_TARGET_INTERMEDIATE                = 0x10
EFI_EXT_SCSI_STATUS_TARGET_INTERMEDIATE_CONDITION_MET  = 0x14
EFI_EXT_SCSI_STATUS_TARGET_RESERVATION_CONFLICT        = 0x18
EFI_EXT_SCSI_STATUS_TARGET_TASK_SET_FULL               = 0x28
EFI_EXT_SCSI_STATUS_TARGET_ACA_ACTIVE                  = 0x30
EFI_EXT_SCSI_STATUS_TARGET_TASK_ABORTED                = 0x40

class EFI_EXT_SCSI_PASS_THRU_MODE (Structure):
  _fields_ = [
    ("AdapterId",       UINT32),
    ("Attributes",      UINT32),
    ("IoAlign",         UINT32)
  ]

class EFI_EXT_SCSI_PASS_THRU_SCSI_REQUEST_PACKET (Structure):
  _fields_ = [
    ("Timeout",           UINT64),
    ("InDataBuffer",      PVOID),
    ("OutDataBuffer",     PVOID),
    ("SenseData",         PVOID),
    ("Cdb",               PVOID),
    ("InTransferLength",  UINT32),
    ("OutTransferLength", UINT32),
    ("CdbLength",         UINT8),
    ("DataDirection",     UINT8),
    ("HostAdapterStatus", UINT8),
    ("TargetStatus",      UINT8),
    ("SenseDataLength",   UINT8)
  ]

EFI_EXT_SCSI_PASS_THRU_PASSTHRU = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL),             # IN      *This
  UINT8,                                                # IN      Target,
  UINT64,                                               # IN      Lun,
  POINTER(EFI_EXT_SCSI_PASS_THRU_SCSI_REQUEST_PACKET),  # IN OUT  *Packet,
  EFI_EVENT                                             # IN      Event   OPTIONAL
  )

EFI_EXT_SCSI_PASS_THRU_GET_NEXT_TARGET_LUN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL), # IN      *This
  POINTER(POINTER(UINT8)),                  # IN OUT  **Target,
  POINTER(UINT64)                           # IN OUT  *Lun
  )

EFI_EXT_SCSI_PASS_THRU_BUILD_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL),   # IN      *This
  POINTER(UINT8),                             # IN      *Target,
  UINT64,                                     # IN      *Lun,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))  # IN OUT  **DevicePath
  )

EFI_EXT_SCSI_PASS_THRU_GET_TARGET_LUN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL),   # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),          # IN      *DevicePath
  POINTER(POINTER(UINT8)),                    #     OUT **Target,
  POINTER(UINT64)                             #     OUT *Lun
  )

EFI_EXT_SCSI_PASS_THRU_RESET_CHANNEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL)    # IN      *This
  )

EFI_EXT_SCSI_PASS_THRU_RESET_TARGET_LUN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL),   # IN      *This
  POINTER(UINT8),                             # IN      *Target,
  UINT64                                      # IN      Lun
  )

EFI_EXT_SCSI_PASS_THRU_GET_NEXT_TARGET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EXT_SCSI_PASS_THRU_PROTOCOL),   # IN      *This
  POINTER(POINTER(UINT8))                     # IN      **Target
  )

EFI_EXT_SCSI_PASS_THRU_PROTOCOL._fields_ = [
    ("Mode",              POINTER(EFI_EXT_SCSI_PASS_THRU_MODE)),
    ("PassThru",          EFI_EXT_SCSI_PASS_THRU_PASSTHRU),
    ("GetNextTargetLun",  EFI_EXT_SCSI_PASS_THRU_GET_NEXT_TARGET_LUN),
    ("BuildDevicePath",   EFI_EXT_SCSI_PASS_THRU_BUILD_DEVICE_PATH),
    ("GetTargetLun",      EFI_EXT_SCSI_PASS_THRU_GET_TARGET_LUN),
    ("ResetChannel",      EFI_EXT_SCSI_PASS_THRU_RESET_CHANNEL),
    ("ResetTargetLun",    EFI_EXT_SCSI_PASS_THRU_RESET_TARGET_LUN),
    ("GetNextTarget",     EFI_EXT_SCSI_PASS_THRU_GET_NEXT_TARGET)
  ]

