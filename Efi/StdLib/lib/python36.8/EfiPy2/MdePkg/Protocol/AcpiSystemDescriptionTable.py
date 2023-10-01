# AcpiSystemDescriptionTable.py
#
# EfiPy2.MdePkg.Protocol.AcpiSystemDescriptionTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiAcpiSdtProtocolGuid                 = \
  EFI_GUID (0xeb97088e, 0xcfdf, 0x49c6, ( 0xbe, 0x4b, 0xd9, 0x6, 0xa5, 0xb2, 0xe, 0x86 ))

EFI_ACPI_TABLE_VERSION      = UINT32
EFI_ACPI_HANDLE             = PVOID

EFI_ACPI_TABLE_VERSION_NONE = (1 << 0)
EFI_ACPI_TABLE_VERSION_1_0B = (1 << 1)
EFI_ACPI_TABLE_VERSION_2_0  = (1 << 2)
EFI_ACPI_TABLE_VERSION_3_0  = (1 << 3)
EFI_ACPI_TABLE_VERSION_4_0  = (1 << 4)
EFI_ACPI_TABLE_VERSION_5_0  = (1 << 5)

EFI_ACPI_DATA_TYPE              = UINT32
EFI_ACPI_DATA_TYPE_NONE         = 0
EFI_ACPI_DATA_TYPE_OPCODE       = 1
EFI_ACPI_DATA_TYPE_NAME_STRING  = 2
EFI_ACPI_DATA_TYPE_OP           = 3
EFI_ACPI_DATA_TYPE_UINT         = 4
EFI_ACPI_DATA_TYPE_STRING       = 5
EFI_ACPI_DATA_TYPE_CHILD        = 6

class EFI_ACPI_SDT_HEADER (Structure):
  _fields_ = [
    ("Signature",       UINT32),
    ("Length",          UINT32),
    ("Revision",        UINT8),
    ("Checksum",        UINT8),
    ("OemId",           CHAR8 * 6),
    ("OemTableId",      CHAR8 * 8),
    ("OemRevision",     UINT32),
    ("CreatorId",       UINT32),
    ("CreatorRevision", UINT32)
  ]

EFI_ACPI_NOTIFICATION_FN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_ACPI_SDT_HEADER),         # IN *Table
  EFI_ACPI_TABLE_VERSION,               # IN Version
  UINTN                                 # IN TableKey
  )

EFI_ACPI_GET_ACPI_TABLE2 = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                                    # IN     Index,
  POINTER (POINTER (EFI_ACPI_SDT_HEADER)),  # OUT    **Table,
  POINTER (EFI_ACPI_TABLE_VERSION),         # OUT    *Version,
  POINTER (UINTN)                           # OUT    *TableKey
  )

EFI_ACPI_REGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  BOOLEAN,                  # IN  Register,
  EFI_ACPI_NOTIFICATION_FN  # IN  Notification
  )

EFI_ACPI_OPEN = CFUNCTYPE (
  EFI_STATUS,
  PVOID,                    # IN  *Buffer
  POINTER (EFI_ACPI_HANDLE) # OUT *Handle
  )

EFI_ACPI_OPEN_SDT = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                    # IN  TableKey
  POINTER (EFI_ACPI_HANDLE) # OUT *Handle
  )

EFI_ACPI_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  EFI_ACPI_HANDLE # OUT *Handle
  )

EFI_ACPI_GET_CHILD = CFUNCTYPE (
  EFI_STATUS,
  EFI_ACPI_HANDLE,          # IN  ParentHandle
  POINTER (EFI_ACPI_HANDLE) # OUT *Handle
  )

EFI_ACPI_GET_OPTION = CFUNCTYPE (
  EFI_STATUS,
  EFI_ACPI_HANDLE,              # IN        Handle
  UINTN,                        # IN        Index,
  POINTER (EFI_ACPI_DATA_TYPE), # OUT       *DataType,
  POINTER (PVOID),              # OUT CONST **Data,
  POINTER (UINTN)               # OUT       *DataSize
  )

EFI_ACPI_SET_OPTION = CFUNCTYPE (
  EFI_STATUS,
  EFI_ACPI_HANDLE,  # IN       Handle,
  UINTN,            # IN       Index,
  PVOID,            # IN CONST *Data,
  UINTN             # IN       *DataSize
  )

EFI_ACPI_FIND_PATH = CFUNCTYPE (
  EFI_STATUS,
  EFI_ACPI_HANDLE,          # IN       HandleIn,
  PVOID,                    # IN CONST *AcpiPath,
  POINTER (EFI_ACPI_HANDLE) # OUT      *HandleOut
  )

class EFI_ACPI_SDT_PROTOCOL (Structure):
  _fields_ = [
    ("AcpiVersion",     EFI_ACPI_TABLE_VERSION),
    ("GetAcpiTable",    EFI_ACPI_GET_ACPI_TABLE2),
    ("RegisterNotify",  EFI_ACPI_REGISTER_NOTIFY),
    ("Open",            EFI_ACPI_OPEN),
    ("OpenSdt",         EFI_ACPI_OPEN_SDT),
    ("Close",           EFI_ACPI_CLOSE),
    ("GetChild",        EFI_ACPI_GET_CHILD),
    ("GetOption",       EFI_ACPI_GET_OPTION),
    ("SetOption",       EFI_ACPI_SET_OPTION),
    ("FindPath",        EFI_ACPI_FIND_PATH)
    ]

