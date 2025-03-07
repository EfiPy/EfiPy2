# CcMeasurement.py
#
# EfiPy2.MdePkg.Protocol.CcMeasurement
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.UefiTcgPlatform import TCG_PCRINDEX
from EfiPy2.MdePkg.IndustryStandard.Tpm20           import TPML_DIGEST_VALUES
from EfiPy2.MdePkg.IndustryStandard.Acpi10          import EFI_ACPI_DESCRIPTION_HEADER

gEfiCcMeasurementProtocolGuid       = \
  EFI_GUID (0x96751a3d, 0x72f4, 0x41a6, ( 0xa7, 0x94, 0xed, 0x5d, 0x0e, 0x67, 0xae, 0x6b ))

class EFI_CC_MEASUREMENT_PROTOCOL (Structure):
  pass

class EFI_CC_VERSION (Structure):
  _fields_ = [
    ("Major",   UINT8),
    ("Minor",   UINT8)
  ]

EFI_CC_TYPE_NONE   = 0
EFI_CC_TYPE_SEV    = 1
EFI_CC_TYPE_TDX    = 2
EFI_CC_TYPE_APTEE  = 3

class EFI_CC_TYPE (Structure):
  _fields_ = [
    ("Type",    UINT8),
    ("SubType", UINT8)
  ]

EFI_CC_EVENT_LOG_BITMAP         = UINT32
EFI_CC_EVENT_LOG_FORMAT         = UINT32
EFI_CC_EVENT_ALGORITHM_BITMAP   = UINT32
EFI_CC_MR_INDEX                 = UINT32

TDX_MR_INDEX_MRTD   = 0
TDX_MR_INDEX_RTMR0  = 1
TDX_MR_INDEX_RTMR1  = 2
TDX_MR_INDEX_RTMR2  = 3
TDX_MR_INDEX_RTMR3  = 4

EFI_CC_EVENT_LOG_FORMAT_TCG_2  = 0x00000002
EFI_CC_BOOT_HASH_ALG_SHA384    = 0x00000004

EFI_CC_FLAG_EXTEND_ONLY  = 0x0000000000000001

EFI_CC_FLAG_PE_COFF_IMAGE  = 0x0000000000000010

EFI_CC_EVENT_HEADER_VERSION  = 1

class EFI_CC_EVENT_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderSize",      UINT32),
    ("HeaderVersion",   UINT16),
    ("MrIndex",         EFI_CC_MR_INDEX),
    ("EventType",       UINT32)
  ]

class EFI_CC_EVENT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",    UINT32),
    ("Header",  EFI_CC_EVENT_HEADER),
    ("Event",   UINT8 * 1)
  ]

class EFI_CC_BOOT_SERVICE_CAPABILITY (Structure):
  _fields_ = [
    ("Size",                UINT8),
    ("StructureVersion",    EFI_CC_VERSION),
    ("ProtocolVersion",     EFI_CC_VERSION),
    ("HashAlgorithmBitmap", EFI_CC_EVENT_ALGORITHM_BITMAP),
    ("SupportedEventLogs",  EFI_CC_EVENT_LOG_BITMAP),
    ("CcType",              EFI_CC_TYPE)
  ]

EFI_CC_GET_CAPABILITY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CC_MEASUREMENT_PROTOCOL),     # IN *This
  POINTER(EFI_CC_BOOT_SERVICE_CAPABILITY)   # IN *ProtocolCapability
  )

EFI_CC_GET_EVENT_LOG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CC_MEASUREMENT_PROTOCOL), # IN *This
  EFI_CC_EVENT_LOG_FORMAT,              # IN  EventLogFormat,
  POINTER(EFI_PHYSICAL_ADDRESS),        # OUT *EventLogLocation,
  POINTER(EFI_PHYSICAL_ADDRESS),        # OUT *EventLogLastEntry,
  POINTER(BOOLEAN)                      # OUT *EventLogTruncated
  )

EFI_CC_HASH_LOG_EXTEND_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CC_MEASUREMENT_PROTOCOL), # IN *This
  UINT64,                               #   IN Flags,
  EFI_PHYSICAL_ADDRESS,                 #   IN DataToHash,
  UINT64,                               #   IN DataToHashLen,
  POINTER(EFI_CC_EVENT)                 #   IN *EfiCcEvent
  )

EFI_CC_MAP_PCR_TO_MR_INDEX = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_CC_MEASUREMENT_PROTOCOL), # IN *This
  TCG_PCRINDEX,                         # IN  PcrIndex,
  POINTER(EFI_CC_MR_INDEX)              # OUT *MrIndex
  )

EFI_CC_MEASUREMENT_PROTOCOL._fields_ = [
    ("GetCapability",       EFI_CC_GET_CAPABILITY),
    ("GetEventLog",         EFI_CC_GET_EVENT_LOG),
    ("HashLogExtendEvent",  EFI_CC_HASH_LOG_EXTEND_EVENT),
    ("MapPcrToMrIndex",     EFI_CC_MAP_PCR_TO_MR_INDEX)
  ]

class CC_EVENT (Structure):
  _pack_   = 1
  _fields_ = [
    ("MrIndex",     EFI_CC_MR_INDEX),
    ("EventType",   UINT32),
    ("Digests",     TPML_DIGEST_VALUES),
    ("EventSize",   UINT32),
    ("Event",       UINT8 * 1)
  ]

class CC_EVENT_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("MrIndex",     EFI_CC_MR_INDEX),
    ("EventType",   UINT32),
    ("Digests",     TPML_DIGEST_VALUES),
    ("EventSize",   UINT32)
  ]

EFI_CC_FINAL_EVENTS_TABLE_VERSION  = 1

class EFI_CC_FINAL_EVENTS_TABLE (Structure):
  _fields_ = [
    ("Version",         UINT64),
    ("NumberOfEvents",  UINT64),
    ("Event",           CC_EVENT * 1)
  ]

gEfiCcFinalEventsTableGuid       = \
  EFI_GUID (0xdd4a4648, 0x2de7, 0x4665, (0x96, 0x4d, 0x21, 0xd9, 0xef, 0x5f, 0xb4, 0x46 ))

class EFI_CC_EVENTLOG_ACPI_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_ACPI_DESCRIPTION_HEADER),
    ("CcType",  EFI_CC_TYPE),
    ("Rsvd",    UINT16),
    ("Laml",    UINT64),
    ("Lasa",    UINT64)
  ]

EFI_CC_EVENTLOG_ACPI_TABLE_SIGNATURE  = SIGNATURE_32('C', 'C', 'E', 'L')
EFI_CC_EVENTLOG_ACPI_TABLE_REVISION   = 1

