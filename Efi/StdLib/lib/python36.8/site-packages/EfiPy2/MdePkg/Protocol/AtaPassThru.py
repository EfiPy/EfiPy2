# AtaPassThru.py
#
# EfiPy2.MdePkg.Protocol.AtaPassThru
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiAtaPassThruProtocolGuid             = \
  EFI_GUID (0x1d3de7f0, 0x807, 0x424f, (0xaa, 0x69, 0x11, 0xa5, 0x4e, 0x19, 0xa4, 0x6f ))

class EFI_ATA_PASS_THRU_PROTOCOL (Structure):
  pass

class EFI_ATA_PASS_THRU_MODE (Structure):
  _fields_ = [
    ("Attributes",  UINT32),
    ("IoAlign",     UINT32),
  ]

EFI_ATA_PASS_THRU_ATTRIBUTES_PHYSICAL   = 0x0001
EFI_ATA_PASS_THRU_ATTRIBUTES_LOGICAL    = 0x0002
EFI_ATA_PASS_THRU_ATTRIBUTES_NONBLOCKIO = 0x0004

class EFI_ATA_COMMAND_BLOCK (Structure):
  _fields_ = [
    ("Reserved1",           UINT8 * 2),
    ("AtaCommand",          UINT8),
    ("AtaFeatures",         UINT8),
    ("AtaSectorNumber",     UINT8),
    ("AtaCylinderLow",      UINT8),
    ("AtaCylinderHigh",     UINT8),
    ("AtaDeviceHead",       UINT8),
    ("AtaSectorNumberExp",  UINT8),
    ("AtaCylinderLowExp",   UINT8),
    ("AtaCylinderHighExp",  UINT8),
    ("AtaFeaturesExp",      UINT8),
    ("AtaSectorCount",      UINT8),
    ("AtaSectorCountExp",   UINT8),
    ("Reserved2",           UINT8 * 6)
  ]

class EFI_ATA_STATUS_BLOCK (Structure):
  _fields_ = [
    ("Reserved1",           UINT8 * 2),
    ("AtaStatus",           UINT8),
    ("AtaError",            UINT8),
    ("AtaSectorNumber",     UINT8),
    ("AtaCylinderLow",      UINT8),
    ("AtaCylinderHigh",     UINT8),
    ("AtaDeviceHead",       UINT8),
    ("AtaSectorNumberExp",  UINT8),
    ("AtaCylinderLowExp",   UINT8),
    ("AtaCylinderHighExp",  UINT8),
    ("Reserved2",           UINT8),
    ("AtaSectorCount",      UINT8),
    ("AtaSectorCountExp",   UINT8),
    ("Reserved3",           UINT8 * 6)
  ]

EFI_ATA_PASS_THRU_CMD_PROTOCOL                = UINT8

EFI_ATA_PASS_THRU_PROTOCOL_ATA_HARDWARE_RESET = 0x00
EFI_ATA_PASS_THRU_PROTOCOL_ATA_SOFTWARE_RESET = 0x01
EFI_ATA_PASS_THRU_PROTOCOL_ATA_NON_DATA       = 0x02
EFI_ATA_PASS_THRU_PROTOCOL_PIO_DATA_IN        = 0x04
EFI_ATA_PASS_THRU_PROTOCOL_PIO_DATA_OUT       = 0x05
EFI_ATA_PASS_THRU_PROTOCOL_DMA                = 0x06
EFI_ATA_PASS_THRU_PROTOCOL_DMA_QUEUED         = 0x07
EFI_ATA_PASS_THRU_PROTOCOL_DEVICE_DIAGNOSTIC  = 0x08
EFI_ATA_PASS_THRU_PROTOCOL_DEVICE_RESET       = 0x09
EFI_ATA_PASS_THRU_PROTOCOL_UDMA_DATA_IN       = 0x0A
EFI_ATA_PASS_THRU_PROTOCOL_UDMA_DATA_OUT      = 0x0B
EFI_ATA_PASS_THRU_PROTOCOL_FPDMA              = 0x0C
EFI_ATA_PASS_THRU_PROTOCOL_RETURN_RESPONSE    = 0xFF

EFI_ATA_PASS_THRU_LENGTH                      = UINT8
EFI_ATA_PASS_THRU_LENGTH_BYTES                = 0x80

EFI_ATA_PASS_THRU_LENGTH_MASK                 = 0x70
EFI_ATA_PASS_THRU_LENGTH_NO_DATA_TRANSFER     = 0x00
EFI_ATA_PASS_THRU_LENGTH_FEATURES             = 0x10
EFI_ATA_PASS_THRU_LENGTH_SECTOR_COUNT         = 0x20
EFI_ATA_PASS_THRU_LENGTH_TPSIU                = 0x30

EFI_ATA_PASS_THRU_LENGTH_COUNT                = 0x0F

class EFI_ATA_PASS_THRU_COMMAND_PACKET (Structure):
  _fields_ = [
    ("Asb",               POINTER (EFI_ATA_STATUS_BLOCK)),
    ("Acb",               POINTER (EFI_ATA_COMMAND_BLOCK)),
    ("Timeout",           UINT64),
    ("InDataBuffer",      PVOID),
    ("OutDataBuffer",     PVOID),
    ("InTransferLength",  UINT32),
    ("OutTransferLength", UINT32),
    ("Protocol",          EFI_ATA_PASS_THRU_CMD_PROTOCOL),
    ("Length",            EFI_ATA_PASS_THRU_LENGTH)
  ]

EFI_ATA_PASS_THRU_PASSTHRU = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL),       # IN     *This
  UINT16,                                     # IN     Port,
  UINT16,                                     # IN     PortMultiplierPort,
  POINTER (EFI_ATA_PASS_THRU_COMMAND_PACKET), # IN OUT *Packet,
  EFI_EVENT                                   # IN     Event OPTIONAL
  )

EFI_ATA_PASS_THRU_GET_NEXT_PORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL), # IN     *This
  POINTER (UINT16)                      # IN OUT *Port
  )

EFI_ATA_PASS_THRU_GET_NEXT_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL), # IN     *This
  UINT16,                               # IN     Port,
  POINTER (UINT16)                      # IN OUT *PortMultiplierPort
  )

EFI_ATA_PASS_THRU_BUILD_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL),         # IN     *This
  UINT16,                                       # IN     Port,
  UINT16,                                       # IN     PortMultiplierPort
  POINTER (POINTER (EFI_DEVICE_PATH_PROTOCOL))  # IN OUT **DevicePath
  )

EFI_ATA_PASS_THRU_GET_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL), # IN  *This
  POINTER (EFI_DEVICE_PATH_PROTOCOL),   # IN  *DevicePath,
  POINTER (UINT16),                     # OUT *Port,
  POINTER (UINT16)                      # OUT *PortMultiplierPort
  )

EFI_ATA_PASS_THRU_RESET_PORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL), # IN *This
  UINT16                                # IN Port
  )

EFI_ATA_PASS_THRU_RESET_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_ATA_PASS_THRU_PROTOCOL), # IN *This,
  UINT16,                               # IN Port,
  UINT16                                # IN PortMultiplierPort
  )

EFI_ATA_PASS_THRU_PROTOCOL._fields_ = [
    ("Mode",            POINTER (EFI_ATA_PASS_THRU_MODE)),
    ("PassThru",        EFI_ATA_PASS_THRU_PASSTHRU),
    ("GetNextPort",     EFI_ATA_PASS_THRU_GET_NEXT_PORT),
    ("GetNextDevice",   EFI_ATA_PASS_THRU_GET_NEXT_DEVICE),
    ("BuildDevicePath", EFI_ATA_PASS_THRU_BUILD_DEVICE_PATH),
    ("GetDevice",       EFI_ATA_PASS_THRU_GET_DEVICE),
    ("ResetPort",       EFI_ATA_PASS_THRU_RESET_PORT),
    ("ResetDevice",     EFI_ATA_PASS_THRU_RESET_DEVICE)
  ]

