# NvdimmLabel.py
#
# EfiPy2.MdePkg.Protocol.NvdimmLabel
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiNvdimmLabelProtocolGuid    = \
  EFI_GUID (0xd40b6b80, 0x97d5, 0x4282, (0xbb, 0x1d, 0x22, 0x3a, 0x16, 0x91, 0x80, 0x58 ))

class EFI_NVDIMM_LABEL_PROTOCOL (Structure):
  pass

EFI_NVDIMM_LABEL_INDEX_SIG_LEN  = 16
EFI_NVDIMM_LABEL_INDEX_ALIGN    = 256

class EFI_NVDIMM_LABEL_INDEX_BLOCK (Structure):
  _fields_ = [
    ("Sig",         CHAR8 * EFI_NVDIMM_LABEL_INDEX_SIG_LEN),
    ("Flags",       UINT8 * 3),
    ("LabelSize",   UINT8),
    ("Seq",         UINT32),
    ("MyOff",       UINT64),
    ("MySize",      UINT64),
    ("OtherOff",    UINT64),
    ("LabelOff",    UINT64),
    ("NSlot",       UINT32),
    ("Major",       UINT16),
    ("Minor",       UINT16),
    ("Checksum",    UINT64),
    ("ree",         UINT8 * 0)
  ]

EFI_NVDIMM_LABEL_NAME_LEN  = 64

EFI_NVDIMM_LABEL_FLAGS_ROLABEL  = 0x00000001

EFI_NVDIMM_LABEL_FLAGS_LOCAL  = 0x00000002

EFI_NVDIMM_LABEL_FLAGS_RESERVED  = 0x00000004
EFI_NVDIMM_LABEL_FLAGS_UPDATING  = 0x00000008

class EFI_NVDIMM_LABEL (Structure):
  _fields_ = [
    ("Uuid",                    EFI_GUID),
    ("Name",                    CHAR8 * EFI_NVDIMM_LABEL_NAME_LEN),
    ("Flags",                   UINT32),
    ("NLabel",                  UINT16),
    ("Position",                UINT16),
    ("SetCookie",               UINT64),
    ("LbaSize",                 UINT64),
    ("Dpa",                     UINT64),
    ("RawSize",                 UINT64),
    ("Slot",                    UINT32),
    ("Alignment",               UINT8),
    ("Reserved",                UINT8 * 3),
    ("TypeGuid",                EFI_GUID),
    ("AddressAbstractionGuid",  EFI_GUID),
    ("Reserved1",               UINT8 * 88),
    ("Checksum",                UINT64)
  ]

class EFI_NVDIMM_LABEL_SET_COOKIE_MAP (Structure):
  _fields_ = [
    ("RegionOffset",            UINT64),
    ("SerialNumber",            UINT32),
    ("VendorId",                UINT16),
    ("ManufacturingDate",       UINT16),
    ("ManufacturingLocation",   UINT8),
    ("Reserved",                UINT8 * 31)
  ]

class EFI_NVDIMM_LABEL_SET_COOKIE_INFO (Structure):
  _fields_ = [
    ("Mapping",            EFI_NVDIMM_LABEL_SET_COOKIE_MAP * 0)
  ]

EFI_NVDIMM_LABEL_STORAGE_INFORMATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVDIMM_LABEL_PROTOCOL),   #   IN  *This
  POINTER(UINT32),                      #   OUT *SizeOfLabelStorageArea,
  POINTER(UINT32)                       #   OUT *MaxTransferLength
  )

EFI_NVDIMM_LABEL_STORAGE_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVDIMM_LABEL_PROTOCOL),   #   IN  *This
  UINT32,                               #   IN  Offset,
  UINT32,                               #   IN  TransferLength,
  POINTER(UINT8)                        #   OUT *LabelData
  )

EFI_NVDIMM_LABEL_STORAGE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_NVDIMM_LABEL_PROTOCOL),   #   IN  *This
  UINT32,                               #   IN  Offset,
  UINT32,                               #   IN  TransferLength,
  POINTER(UINT8)                        #   OUT *LabelData
  )

EFI_NVDIMM_LABEL_PROTOCOL._fields_ = [
    ("LabelStorageInformation", EFI_NVDIMM_LABEL_STORAGE_INFORMATION),
    ("LabelStorageRead",        EFI_NVDIMM_LABEL_STORAGE_READ),
    ("LabelStorageWrite",       EFI_NVDIMM_LABEL_STORAGE_WRITE)
  ]

