# AlertStandardFormatTable.py
#
# EfiPy2.MdePkg.IndustryStandard.AlertStandardFormatTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
from EfiPy2 import *

class EFI_ACPI_ASF_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",          UINT8),
    ("Reserved",      UINT8),
    ("RecordLength",  UINT16)
  ]

class EFI_ACPI_ASF_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",          EFI_ACPI_ASF_RECORD_HEADER),
    ("MinWatchDogResetValue", UINT8),
    ("MinPollingInterval",    UINT8),
    ("SystemID",              UINT16),
    ("IANAManufactureID",     UINT32),
    ("FeatureFlags",          UINT8),
    ("Reserved",              UINT8 * 3)
  ]

class EFI_ACPI_ASF_ALERTDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceAddress",     UINT8),
    ("Command",           UINT8),
    ("DataMask",          UINT8),
    ("CompareValue",      UINT8),
    ("EventSenseType",    UINT8),
    ("EventType",         UINT8),
    ("EventOffset",       UINT8),
    ("EventSourceType",   UINT8),
    ("EventSeverity",     UINT8),
    ("SensorNumber",      UINT8),
    ("Entity",            UINT8),
    ("EntityInstance",    UINT8)
  ]

class EFI_ACPI_ASF_ALRT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",            EFI_ACPI_ASF_RECORD_HEADER),
    ("AssertionEventBitMask",   UINT8),
    ("DeassertionEventBitMask", UINT8),
    ("NumberOfAlerts",          UINT8),
    ("ArrayElementLength",      UINT8),
    # ("DeviceArray",           EFI_ACPI_ASF_ALERTDATA * ANYSIZE_ARRAY)
  ]

class EFI_ACPI_ASF_CONTROLDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Function",      UINT8),
    ("DeviceAddress", UINT8),
    ("Command",       UINT8),
    ("DataValue",     UINT8)
  ]

class EFI_ACPI_ASF_RCTL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",        EFI_ACPI_ASF_RECORD_HEADER),
    ("NumberOfControls",    UINT8),
    ("ArrayElementLength",  UINT8),
    ("RctlReserved",        UINT8),
    # ("DeviceArray",       EFI_ACPI_ASF_CONTROLDATA * ANYSIZE_ARRAY)
  ]

class EFI_ACPI_ASF_RMCP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",                EFI_ACPI_ASF_RECORD_HEADER),
    ("RemoteControlCapabilities",   UINT8 * 7),
    ("RMCPCompletionCode",          UINT8),
    ("RMCPIANA",                    UINT32),
    ("RMCPSpecialCommand",          UINT8),
    ("RMCPSpecialCommandParameter", UINT8 * 2),
    ("RMCPBootOptions",             UINT8 * 2),
    ("RMCPOEMParameters",           UINT8 * 2)
  ]

class EFI_ACPI_ASF_ADDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",        EFI_ACPI_ASF_RECORD_HEADER),
    ("SEEPROMAddress",      UINT8),
    ("NumberOfDevices",     UINT8),
    # ("FixedSmbusAddresses", UINT8 * ANYSIZE_ARRAY)
  ]

EFI_ACPI_ASF_DESCRIPTION_HEADER = Acpi.EFI_ACPI_DESCRIPTION_HEADER

EFI_ACPI_2_0_ASF_DESCRIPTION_TABLE_REVISION   = 0x20

EFI_ACPI_ASF_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32 ('A', 'S', 'F', '!')
