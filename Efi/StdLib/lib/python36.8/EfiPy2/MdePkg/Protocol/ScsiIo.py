# ScsiIo.py
#
# EfiPy2.MdePkg.Protocol.ScsiIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiScsiIoProtocolGuid  = \
  EFI_GUID (0x932f47e6, 0x2362, 0x4002, (0x80, 0x3e, 0x3c, 0xd5, 0x4b, 0x13, 0x8f, 0x85 ))

class EFI_SCSI_IO_PROTOCOL (Structure):
  pass

EFI_SCSI_IO_TYPE_DISK                                  = 0x00
EFI_SCSI_IO_TYPE_TAPE                                  = 0x01
EFI_SCSI_IO_TYPE_PRINTER                               = 0x02
EFI_SCSI_IO_TYPE_PROCESSOR                             = 0x03
EFI_SCSI_IO_TYPE_WORM                                  = 0x04
EFI_SCSI_IO_TYPE_CDROM                                 = 0x05
EFI_SCSI_IO_TYPE_SCANNER                               = 0x06
EFI_SCSI_IO_TYPE_OPTICAL                               = 0x07
EFI_SCSI_IO_TYPE_MEDIUMCHANGER                         = 0x08
EFI_SCSI_IO_TYPE_COMMUNICATION                         = 0x09
MFI_SCSI_IO_TYPE_A                                     = 0x0A
MFI_SCSI_IO_TYPE_B                                     = 0x0B
MFI_SCSI_IO_TYPE_RAID                                  = 0x0C
MFI_SCSI_IO_TYPE_SES                                   = 0x0D
MFI_SCSI_IO_TYPE_RBC                                   = 0x0E
MFI_SCSI_IO_TYPE_OCRW                                  = 0x0F
MFI_SCSI_IO_TYPE_BRIDGE                                = 0x10
MFI_SCSI_IO_TYPE_OSD                                   = 0x11
EFI_SCSI_IO_TYPE_RESERVED_LOW                          = 0x12
EFI_SCSI_IO_TYPE_RESERVED_HIGH                         = 0x1E
EFI_SCSI_IO_TYPE_UNKNOWN                               = 0x1F

EFI_SCSI_IO_DATA_DIRECTION_READ                        = 0
EFI_SCSI_IO_DATA_DIRECTION_WRITE                       = 1
EFI_SCSI_IO_DATA_DIRECTION_BIDIRECTIONAL               = 2

EFI_SCSI_IO_STATUS_HOST_ADAPTER_OK                     = 0x00
EFI_SCSI_IO_STATUS_HOST_ADAPTER_TIMEOUT_COMMAND        = 0x09
EFI_SCSI_IO_STATUS_HOST_ADAPTER_TIMEOUT                = 0x0b
EFI_SCSI_IO_STATUS_HOST_ADAPTER_MESSAGE_REJECT         = 0x0d
EFI_SCSI_IO_STATUS_HOST_ADAPTER_BUS_RESET              = 0x0e
EFI_SCSI_IO_STATUS_HOST_ADAPTER_PARITY_ERROR           = 0x0f
EFI_SCSI_IO_STATUS_HOST_ADAPTER_REQUEST_SENSE_FAILED   = 0x10
EFI_SCSI_IO_STATUS_HOST_ADAPTER_SELECTION_TIMEOUT      = 0x11
EFI_SCSI_IO_STATUS_HOST_ADAPTER_DATA_OVERRUN_UNDERRUN  = 0x12
EFI_SCSI_IO_STATUS_HOST_ADAPTER_BUS_FREE               = 0x13
EFI_SCSI_IO_STATUS_HOST_ADAPTER_PHASE_ERROR            = 0x14
EFI_SCSI_IO_STATUS_HOST_ADAPTER_OTHER                  = 0x7f

EFI_SCSI_IO_STATUS_TARGET_GOOD                         = 0x00
EFI_SCSI_IO_STATUS_TARGET_CHECK_CONDITION              = 0x02
EFI_SCSI_IO_STATUS_TARGET_CONDITION_MET                = 0x04
EFI_SCSI_IO_STATUS_TARGET_BUSY                         = 0x08
EFI_SCSI_IO_STATUS_TARGET_INTERMEDIATE                 = 0x10
EFI_SCSI_IO_STATUS_TARGET_INTERMEDIATE_CONDITION_MET   = 0x14
EFI_SCSI_IO_STATUS_TARGET_RESERVATION_CONFLICT         = 0x18
EFI_SCSI_IO_STATUS_TARGET_COMMOND_TERMINATED           = 0x22
EFI_SCSI_IO_STATUS_TARGET_QUEUE_FULL                   = 0x28

class EFI_SCSI_IO_SCSI_REQUEST_PACKET (Structure):
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

EFI_SCSI_IO_PROTOCOL_GET_DEVICE_TYPE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_IO_PROTOCOL),  # IN      *This
  POINTER(UINT8)                  #    OUT  *DeviceType
  )

EFI_SCSI_IO_PROTOCOL_GET_DEVICE_LOCATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_IO_PROTOCOL),  # IN      *This
  POINTER(POINTER(UINT8)),        # IN OUT  **Target
  POINTER(UINT64)                 #    OUT  *Lun
  )

EFI_SCSI_IO_PROTOCOL_RESET_BUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_IO_PROTOCOL)   # IN      *This
  )

EFI_SCSI_IO_PROTOCOL_RESET_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_IO_PROTOCOL)   # IN      *This
  )

EFI_SCSI_IO_PROTOCOL_EXEC_SCSI_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SCSI_IO_PROTOCOL),            # IN      *This
  POINTER(EFI_SCSI_IO_SCSI_REQUEST_PACKET), # IN OUT  *Packet,
  EFI_EVENT                                 # IN      Event  OPTIONAL
  )

EFI_SCSI_IO_PROTOCOL._fields_ = [
    ("GetDeviceType",       EFI_SCSI_IO_PROTOCOL_GET_DEVICE_TYPE),
    ("GetDeviceLocation",   EFI_SCSI_IO_PROTOCOL_GET_DEVICE_LOCATION),
    ("ResetBus",            EFI_SCSI_IO_PROTOCOL_RESET_BUS),
    ("ResetDevice",         EFI_SCSI_IO_PROTOCOL_RESET_DEVICE),
    ("ExecuteScsiCommand",  EFI_SCSI_IO_PROTOCOL_EXEC_SCSI_COMMAND),   
    ("IoAlign",             UINT32)
  ]

