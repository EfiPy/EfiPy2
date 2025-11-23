# Tcg2Protocol.py
#
# EfiPy2.MdePkg.Protocol.Tcg2Protocol
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.UefiTcgPlatform import TCG_PCRINDEX, TCG_EVENTTYPE

gEfiTcg2ProtocolGuid  = \
  EFI_GUID (0x607f766c, 0x7455, 0x42be, ( 0x93, 0x0b, 0xe4, 0xd7, 0x6d, 0xb2, 0x72, 0x0f ))

class EFI_TCG2_PROTOCOL (Structure):
  pass

class EFI_TCG2_VERSION (Structure):
  _fields_ = [
    ("Major", UINT8),
    ("Minor", UINT8)
  ]

EFI_TCG2_EVENT_LOG_BITMAP = UINT32
EFI_TCG2_EVENT_LOG_FORMAT = UINT32
EFI_TCG2_EVENT_ALGORITHM_BITMAP = UINT32

EFI_TCG2_EVENT_LOG_FORMAT_TCG_1_2       = 0x00000001
EFI_TCG2_EVENT_LOG_FORMAT_TCG_2         = 0x00000002

class EFI_TCG2_BOOT_SERVICE_CAPABILITY (Structure):
  _fields_ = [
    ("Size",                UINT8),
    ("StructureVersion",    EFI_TCG2_VERSION),
    ("ProtocolVersion",     EFI_TCG2_VERSION),
    ("HashAlgorithmBitmap", EFI_TCG2_EVENT_ALGORITHM_BITMAP),
    ("SupportedEventLogs",  EFI_TCG2_EVENT_LOG_BITMAP),
    ("TPMPresentFlag",      BOOLEAN),
    ("MaxCommandSize",      UINT16),
    ("MaxResponseSize",     UINT16),
    ("ManufacturerID",      UINT32),
    ("NumberOfPCRBanks",    UINT32),
    ("ActivePcrBanks",      EFI_TCG2_EVENT_ALGORITHM_BITMAP)
  ]

EFI_TCG2_BOOT_HASH_ALG_SHA1    = 0x00000001
EFI_TCG2_BOOT_HASH_ALG_SHA256  = 0x00000002
EFI_TCG2_BOOT_HASH_ALG_SHA384  = 0x00000004
EFI_TCG2_BOOT_HASH_ALG_SHA512  = 0x00000008
EFI_TCG2_BOOT_HASH_ALG_SM3_256 = 0x00000010

EFI_TCG2_EXTEND_ONLY  = 0x0000000000000001

PE_COFF_IMAGE     = 0x0000000000000010

MAX_PCR_INDEX  = 23

EFI_TCG2_EVENT_HEADER_VERSION  = 1

class EFI_TCG2_EVENT_HEADER (Structure):
  _pack_ = 1
  _fields_ = [
    ("HeaderSize",    UINT32),
    ("HeaderVersion", UINT16),
    ("PCRIndex",      TCG_PCRINDEX),
    ("EventType",     TCG_EVENTTYPE)
  ]

class EFI_TCG2_EVENT (Structure):
  _pack_ = 1
  _fields_ = [
    ("Size",    UINT32),
    ("Header",  EFI_TCG2_EVENT_HEADER),
    ("Event",   UINT8 * 1)
  ]

EFI_TCG2_GET_CAPABILITY = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_TCG2_PROTOCOL),                # IN *This
  POINTER (EFI_TCG2_BOOT_SERVICE_CAPABILITY), # IN *ProtocolCapability
  )

EFI_TCG2_GET_EVENT_LOG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL),     # IN  *This,
  EFI_TCG2_EVENT_LOG_FORMAT,      # IN  EventLogFormat,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT *EventLogLocation,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT *EventLogLastEntry,
  POINTER(BOOLEAN)                # OUT *EventLogTruncated
  )

EFI_TCG2_HASH_LOG_EXTEND_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL),     # IN  *This,
  UINT64,                         # IN Flags,
  EFI_PHYSICAL_ADDRESS,           # IN DataToHash,
  UINT64,                         # IN DataToHashLen,
  POINTER(EFI_TCG2_EVENT)         # IN *EfiTcgEvent
  )

EFI_TCG2_SUBMIT_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL),     # IN  *This,
  UINT32,                         # IN InputParameterBlockSize,
  POINTER(UINT8),                 # IN *InputParameterBlock,
  UINT32,                         # IN OutputParameterBlockSize,
  POINTER(UINT8)                  # IN *OutputParameterBlock
  )

EFI_TCG2_GET_ACTIVE_PCR_BANKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL), # IN  *This,
  POINTER(UINT32)             # OUT *ActivePcrBanks
  )

EFI_TCG2_SET_ACTIVE_PCR_BANKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL), # IN  *This,
  UINT32                      # IN  ActivePcrBanks
  )

EFI_TCG2_GET_RESULT_OF_SET_ACTIVE_PCR_BANKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG2_PROTOCOL), # IN  *This,
  POINTER(UINT32),            # OUT *OperationPresent,
  POINTER(UINT32)             # OUT *Response
  )

EFI_TCG2_PROTOCOL._fields_ = [
  ("GetCapability",                 EFI_TCG2_GET_CAPABILITY),
  ("GetEventLog",                   EFI_TCG2_GET_EVENT_LOG),
  ("HashLogExtendEvent",            EFI_TCG2_HASH_LOG_EXTEND_EVENT),
  ("SubmitCommand",                 EFI_TCG2_SUBMIT_COMMAND),
  ("GetActivePcrBanks",             EFI_TCG2_GET_ACTIVE_PCR_BANKS),
  ("SetActivePcrBanks",             EFI_TCG2_SET_ACTIVE_PCR_BANKS),
  ("GetResultOfSetActivePcrBanks",  EFI_TCG2_GET_RESULT_OF_SET_ACTIVE_PCR_BANKS)
  ]

gEfiTcg2FinalEventsTableGuid  = \
  EFI_GUID (0x1e2ed096, 0x30e2, 0x4254, ( 0xbd, 0x89, 0x86, 0x3b, 0xbe, 0xf8, 0x23, 0x25 ))

class EFI_TCG2_FINAL_EVENTS_TABLE (Structure):
  _fields_ = [
    ("Version",         UINT64),
    ("NumberOfEvents",  UINT64)
    # ("Event",           TCG_PCR_EVENT2 * 1)
  ]

EFI_TCG2_FINAL_EVENTS_TABLE_VERSION   = 1

