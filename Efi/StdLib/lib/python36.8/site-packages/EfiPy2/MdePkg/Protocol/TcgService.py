# TcgService.py
#
# EfiPy2.MdePkg.Protocol.TcgService
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.UefiTcgPlatform import TCG_PCR_EVENT

gEfiTcgProtocolGuid   = \
  EFI_GUID (0xf541796d, 0xa62e, 0x4954, ( 0xa7, 0x75, 0x95, 0x84, 0xf6, 0x1b, 0x9c, 0xdd ))

class EFI_TCG_PROTOCOL (Structure):
  pass

class TCG_VERSION (Structure):
  _fields_ = [
    ("Major",     UINT8),
    ("Minor",     UINT8),
    ("RevMajor",  UINT8),
    ("RevMinor",  UINT8)
  ]

class TCG_EFI_BOOT_SERVICE_CAPABILITY (Structure):
  _fields_ = [
    ("Size",                UINT8),
    ("StructureVersion",    TCG_VERSION),
    ("ProtocolSpecVersion", TCG_VERSION),
    ("HashAlgorithmBitmap", UINT8),
    ("TPMPresentFlag",      BOOLEAN),
    ("TPMDeactivatedFlag",  BOOLEAN)
  ]

TCG_ALGORITHM_ID = UINT32

EFI_TCG_STATUS_CHECK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG_PROTOCOL),                # IN      *This
  POINTER(TCG_EFI_BOOT_SERVICE_CAPABILITY), # OUT *ProtocolCapability,
  POINTER(UINT32),                          # OUT *TCGFeatureFlags,
  POINTER(EFI_PHYSICAL_ADDRESS),            # OUT *EventLogLocation,
  POINTER(EFI_PHYSICAL_ADDRESS)             # OUT *EventLogLastEntry
  )

EFI_TCG_HASH_ALL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG_PROTOCOL),  # IN      *This
  POINTER(UINT8),             # IN      *HashData,
  UINT64,                     # IN      HashDataLen,
  TCG_ALGORITHM_ID,           # IN      AlgorithmId,
  POINTER(UINT64),            # IN OUT  *HashedDataLen,
  POINTER(POINTER(UINT8))     # IN OUT  **HashedDataResult
  )

EFI_TCG_LOG_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG_PROTOCOL),              # IN      *This
  POINTER(TCG_PCR_EVENT),                 # IN      *TCGLogData,
  POINTER(UINT32),                        # IN OUT  *EventNumber,
  UINT32                                  # IN      Flags
  )

EFI_TCG_PASS_THROUGH_TO_TPM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG_PROTOCOL),  # IN      *This
  UINT32,                     # IN      TpmInputParameterBlockSize,
  POINTER(UINT8),             # IN      *TpmInputParameterBlock,
  UINT32,                     # IN      TpmOutputParameterBlockSize,
  POINTER(UINT8)              # IN      *TpmOutputParameterBlock
  )

EFI_TCG_HASH_LOG_EXTEND_EVENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TCG_PROTOCOL),              # IN      *This
  EFI_PHYSICAL_ADDRESS,                   # IN      HashData,
  UINT64,                                 # IN      HashDataLen,
  TCG_ALGORITHM_ID,                       # IN      AlgorithmId,
  POINTER(TCG_PCR_EVENT),                 # IN OUT  *TCGLogData,
  POINTER(UINT32),                        # IN OUT  *EventNumber,
  POINTER(EFI_PHYSICAL_ADDRESS)           #    OUT  *EventLogLastEntry
  )

EFI_TCG_PROTOCOL._fields_ = [
    ("StatusCheck",         EFI_TCG_STATUS_CHECK),
    ("HashAll",             EFI_TCG_HASH_ALL),
    ("LogEvent",            EFI_TCG_LOG_EVENT),
    ("PassThroughToTpm",    EFI_TCG_PASS_THROUGH_TO_TPM),
    ("HashLogExtendEvent",  EFI_TCG_HASH_LOG_EXTEND_EVENT)
  ]

