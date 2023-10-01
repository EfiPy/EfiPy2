# ScsiPassThru.py
#
# EfiPy2.MdePkg.Protocol.ScsiPassThru
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiScsiPassThruProtocolGuid  = \
  EFI_GUID (0xa59e8fcf, 0xbda0, 0x43bb, (0x90, 0xb1, 0xd3, 0x73, 0x2e, 0xca, 0xa8, 0x77 ))

class EFI_SCSI_PASS_THRU_PROTOCOL (Structure):
  pass

EFI_SCSI_PASS_THRU_ATTRIBUTES_PHYSICAL    = 0x0001
EFI_SCSI_PASS_THRU_ATTRIBUTES_LOGICAL     = 0x0002
EFI_SCSI_PASS_THRU_ATTRIBUTES_NONBLOCKIO  = 0x0004

EFI_SCSI_STATUS_HOST_ADAPTER_OK                     = 0x00
EFI_SCSI_STATUS_HOST_ADAPTER_TIMEOUT_COMMAND        = 0x09
EFI_SCSI_STATUS_HOST_ADAPTER_TIMEOUT                = 0x0b
EFI_SCSI_STATUS_HOST_ADAPTER_MESSAGE_REJECT         = 0x0d
EFI_SCSI_STATUS_HOST_ADAPTER_BUS_RESET              = 0x0e
EFI_SCSI_STATUS_HOST_ADAPTER_PARITY_ERROR           = 0x0f
EFI_SCSI_STATUS_HOST_ADAPTER_REQUEST_SENSE_FAILED   = 0x10
EFI_SCSI_STATUS_HOST_ADAPTER_SELECTION_TIMEOUT      = 0x11
EFI_SCSI_STATUS_HOST_ADAPTER_DATA_OVERRUN_UNDERRUN  = 0x12
EFI_SCSI_STATUS_HOST_ADAPTER_BUS_FREE               = 0x13
EFI_SCSI_STATUS_HOST_ADAPTER_PHASE_ERROR            = 0x14
EFI_SCSI_STATUS_HOST_ADAPTER_OTHER                  = 0x7f

EFI_SCSI_STATUS_TARGET_GOOD                       = 0x00
EFI_SCSI_STATUS_TARGET_CHECK_CONDITION            = 0x02
EFI_SCSI_STATUS_TARGET_CONDITION_MET              = 0x04
EFI_SCSI_STATUS_TARGET_BUSY                       = 0x08
EFI_SCSI_STATUS_TARGET_INTERMEDIATE               = 0x10
EFI_SCSI_STATUS_TARGET_INTERMEDIATE_CONDITION_MET = 0x14
EFI_SCSI_STATUS_TARGET_RESERVATION_CONFLICT       = 0x18
EFI_SCSI_STATUS_TARGET_COMMOND_TERMINATED         = 0x22
EFI_SCSI_STATUS_TARGET_QUEUE_FULL                 = 0x28

class EFI_SCSI_PASS_THRU_SCSI_REQUEST_PACKET (Structure):
  _fields_ = [
    ("Timeout",           UINT64),
    ("DataBuffer",        PVOID),
    ("SenseData",         PVOID),
    ("Cdb",               PVOID),
    ("TransferLength",    UINT32),
    ("CdbLength",         UINT8),
    ("DataDirection",     UINT8),
    ("HostAdapterStatus", UINT8),
    ("TargetStatus",      UINT8),
    ("SenseDataLength",   UINT8)
  ]

class EFI_SCSI_PASS_THRU_MODE (Structure):
  _fields_ = [
    ("ControllerName",  PCHAR16),
    ("ChannelName",     PCHAR16),
    ("AdapterId",       UINT32),
    ("Attributes",      UINT32),
    ("IoAlign",         UINT32)
  ]

EFI_SCSI_PASS_THRU_PASSTHRU = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL),             # IN      *This
  UINT32,                                           # IN      Target,
  UINT64,                                           # IN      Lun,
  POINTER(EFI_SCSI_PASS_THRU_SCSI_REQUEST_PACKET),  # IN OUT  *Packet,
  EFI_EVENT                                         # IN      Event   OPTIONAL
  )

EFI_SCSI_PASS_THRU_GET_NEXT_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL), # IN      *This
  POINTER(UINT32),                      # IN OUT  *Target,
  POINTER(UINT64)                       # IN OUT  *Lun
  )

EFI_SCSI_PASS_THRU_BUILD_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL),       # IN      *This
  UINT32,                                     # IN      Target,
  UINT64,                                     # IN      Lun,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))  # IN OUT  **DevicePath
  )

EFI_SCSI_PASS_THRU_GET_TARGET_LUN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL),       # IN      *This
  POINTER(EFI_DEVICE_PATH_PROTOCOL),          # IN      *DevicePath
  POINTER(UINT32),                            #    OUT  *Target,
  POINTER(UINT64)                             #    OUT  *Lun
  )

EFI_SCSI_PASS_THRU_RESET_CHANNEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL)  # IN      *This
  )

EFI_SCSI_PASS_THRU_RESET_TARGET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_PASS_THRU_PROTOCOL), # IN      *This
  UINT32,                               # IN      Target,
  UINT64                                # IN      Lun
  )

EFI_SCSI_PASS_THRU_PROTOCOL._fields_ = [
    ("Mode",            POINTER(EFI_SCSI_PASS_THRU_MODE)),
    ("PassThru",        EFI_SCSI_PASS_THRU_PASSTHRU),
    ("GetNextDevice",   EFI_SCSI_PASS_THRU_GET_NEXT_DEVICE),
    ("BuildDevicePath", EFI_SCSI_PASS_THRU_BUILD_DEVICE_PATH),
    ("GetTargetLun",    EFI_SCSI_PASS_THRU_GET_TARGET_LUN),
    ("ResetChannel",    EFI_SCSI_PASS_THRU_RESET_CHANNEL),
    ("ResetTarget",     EFI_SCSI_PASS_THRU_RESET_TARGET)
  ]

