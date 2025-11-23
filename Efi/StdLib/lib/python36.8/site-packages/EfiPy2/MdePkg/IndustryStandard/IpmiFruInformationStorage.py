# IpmiFruInformationStorage.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiFruInformationStorage
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class IPMI_FRU_COMMON_HEADER_FORMAT_VERSION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FormatVersionNumber", UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_FRU_COMMON_HEADER_FORMAT_VERSION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_FRU_COMMON_HEADER_FORMAT_VERSION_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_FRU_COMMON_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FormatVersion",               IPMI_FRU_COMMON_HEADER_FORMAT_VERSION),
    ("InternalUseStartingOffset",   UINT8),
    ("ChassisInfoStartingOffset",   UINT8),
    ("BoardAreaStartingOffset",     UINT8),
    ("ProductInfoStartingOffset",   UINT8),
    ("MultiRecInfoStartingOffset",  UINT8),
    ("Pad",                         UINT8),
    ("Checksum",                    UINT8)
    ]

class IPMI_FRU_MULTI_RECORD_HEADER_FORMAT_VERSION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordFormatVersion", UINT8, 4),
    ("Reserved",            UINT8, 3),
    ("EndofList",           UINT8, 1)
    ]

class IPMI_FRU_MULTI_RECORD_HEADER_FORMAT_VERSION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_FRU_MULTI_RECORD_HEADER_FORMAT_VERSION_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_FRU_MULTI_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordTypeId",    UINT8),
    ("FormatVersion",   IPMI_FRU_COMMON_HEADER_FORMAT_VERSION),
    ("RecordLength",    UINT8),
    ("RecordChecksum",  UINT8),
    ("HeaderChecksum",  UINT8)
    ]

class IPMI_SYSTEM_UUID_SUB_RECORD_WITH_CHECKSUM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordChecksum",  UINT8),
    ("SubRecordId",     UINT8),
    ("Uuid",            EFI_GUID)
    ]
