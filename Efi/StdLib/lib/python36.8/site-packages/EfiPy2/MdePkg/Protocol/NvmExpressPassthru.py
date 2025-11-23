# NvmExpressPassthru.py
#
# EfiPy2.MdePkg.Protocol.NvmExpressPassthru
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiNvmExpressPassThruProtocolGuid  = \
  EFI_GUID (0x52c78312, 0x8edc, 0x4233, ( 0x98, 0xf2, 0x1a, 0x1a, 0xa5, 0xe3, 0x88, 0xa5 ))

class EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL (Structure):
  pass

class EFI_NVM_EXPRESS_PASS_THRU_MODE (Structure):
  _fields_ = [
    ("Attributes",  UINT32),
    ("IoAlign",     UINT32),
    ("NvmeVersion", UINT32)
  ]

EFI_NVM_EXPRESS_PASS_THRU_ATTRIBUTES_PHYSICAL        = 0x0001
EFI_NVM_EXPRESS_PASS_THRU_ATTRIBUTES_LOGICAL         = 0x0002
EFI_NVM_EXPRESS_PASS_THRU_ATTRIBUTES_NONBLOCKIO      = 0x0004
EFI_NVM_EXPRESS_PASS_THRU_ATTRIBUTES_CMD_SET_NVM     = 0x0008

NORMAL_CMD                  = 0x00
FUSED_FIRST_CMD             = 0x01
FUSED_SECOND_CMD            = 0x02

class NVME_CDW0 (Structure):
  _fields_ = [
    ("Opcode",          UINT32, 8),
    ("FusedOperation",  UINT32, 2),
    ("Reserved",        UINT32, 22)
  ]

CDW2_VALID                  = 0x01
CDW3_VALID                  = 0x02
CDW10_VALID                 = 0x04
CDW11_VALID                 = 0x08
CDW12_VALID                 = 0x10
CDW13_VALID                 = 0x20
CDW14_VALID                 = 0x40
CDW15_VALID                 = 0x80

NVME_ADMIN_QUEUE            = 0x00
NVME_IO_QUEUE               = 0x01

class EFI_NVM_EXPRESS_COMMAND (Structure):
  _fields_ = [
    ("Cdw0",  NVME_CDW0),
    ("Flags", UINT8),
    ("Nsid",  UINT32),
    ("Cdw2",  UINT32),
    ("Cdw3",  UINT32),
    ("Cdw10", UINT32),
    ("Cdw11", UINT32),
    ("Cdw12", UINT32),
    ("Cdw13", UINT32),
    ("Cdw14", UINT32),
    ("Cdw15", UINT32)
  ]

class EFI_NVM_EXPRESS_COMPLETION (Structure):
  _fields_ = [
    ("DW0", UINT32),
    ("DW1", UINT32),
    ("DW2", UINT32),
    ("DW3", UINT32)
  ]

class EFI_NVM_EXPRESS_PASS_THRU_COMMAND_PACKET (Structure):
  _fields_ = [
    ("CommandTimeout",  UINT64),
    ("TransferBuffer",  PVOID),
    ("TransferLength",  UINT32),
    ("MetadataBuffer",  PVOID),
    ("MetadataLength",  UINT32),
    ("QueueType",       UINT8),
    ("NvmeCmd",         POINTER(EFI_NVM_EXPRESS_COMMAND)),
    ("NvmeCompletion",  POINTER(EFI_NVM_EXPRESS_COMPLETION))
  ]

EFI_NVM_EXPRESS_PASS_THRU_PASSTHRU = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL),        # IN     *This,
  UINT32,                                             # IN     NamespaceId,
  POINTER(EFI_NVM_EXPRESS_PASS_THRU_COMMAND_PACKET),  # IN OUT *Packet,
  EFI_EVENT                                           # IN     Event OPTIONAL
  )

EFI_NVM_EXPRESS_PASS_THRU_GET_NEXT_NAMESPACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL),  # IN     *This,
  POINTER(UINT32)                               # IN OUT *NamespaceId
  )

EFI_NVM_EXPRESS_PASS_THRU_BUILD_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL),  # IN     *This,
  POINTER(UINT32),                              # IN OUT *NamespaceId,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))    # IN OUT **DevicePath
  )

EFI_NVM_EXPRESS_PASS_THRU_GET_NAMESPACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL),  # IN     *This,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),            # IN     *DevicePath
  POINTER(UINT32)                               #    OUT *NamespaceId,
  )

EFI_NVM_EXPRESS_PASS_THRU_PROTOCOL._fields_ = [
    ("Mode",              POINTER(EFI_NVM_EXPRESS_PASS_THRU_MODE)),
    ("PassThru",          EFI_NVM_EXPRESS_PASS_THRU_PASSTHRU),
    ("GetNextNamespace",  EFI_NVM_EXPRESS_PASS_THRU_GET_NEXT_NAMESPACE),
    ("BuildDevicePath",   EFI_NVM_EXPRESS_PASS_THRU_BUILD_DEVICE_PATH),
    ("GetNamespace",      EFI_NVM_EXPRESS_PASS_THRU_GET_NAMESPACE)
  ]

