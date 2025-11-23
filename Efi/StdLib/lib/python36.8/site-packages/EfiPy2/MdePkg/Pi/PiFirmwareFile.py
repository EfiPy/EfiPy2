# PiFirmwareFile.py
#
# EfiPy2.MdePkg.Pi.PiFirmwareFile
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class EFI_FFS_INTEGRITY_CHECK_Checksum (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",   UINT8),
    ("File",     UINT8)
  ]

class EFI_FFS_INTEGRITY_CHECK (Union):
  _pack_   = 1
  _fields_ = [
    ("Checksum",     EFI_FFS_INTEGRITY_CHECK_Checksum),
    ("Checksum16",   UINT16)
  ]

FFS_FIXED_CHECKSUM  = 0xAA

EFI_FV_FILETYPE             = UINT8
EFI_FFS_FILE_ATTRIBUTES     = UINT8
EFI_FFS_FILE_STATE          = UINT8

EFI_FV_FILETYPE_ALL                    = 0x00
EFI_FV_FILETYPE_RAW                    = 0x01
EFI_FV_FILETYPE_FREEFORM               = 0x02
EFI_FV_FILETYPE_SECURITY_CORE          = 0x03
EFI_FV_FILETYPE_PEI_CORE               = 0x04
EFI_FV_FILETYPE_DXE_CORE               = 0x05
EFI_FV_FILETYPE_PEIM                   = 0x06
EFI_FV_FILETYPE_DRIVER                 = 0x07
EFI_FV_FILETYPE_COMBINED_PEIM_DRIVER   = 0x08
EFI_FV_FILETYPE_APPLICATION            = 0x09
EFI_FV_FILETYPE_MM                     = 0x0A
EFI_FV_FILETYPE_SMM                    = EFI_FV_FILETYPE_MM
EFI_FV_FILETYPE_FIRMWARE_VOLUME_IMAGE  = 0x0B
EFI_FV_FILETYPE_COMBINED_MM_DXE        = 0x0C
EFI_FV_FILETYPE_COMBINED_SMM_DXE       = EFI_FV_FILETYPE_COMBINED_MM_DXE
EFI_FV_FILETYPE_MM_CORE                = 0x0D
EFI_FV_FILETYPE_SMM_CORE               = EFI_FV_FILETYPE_MM_CORE
EFI_FV_FILETYPE_MM_STANDALONE          = 0x0E
EFI_FV_FILETYPE_MM_CORE_STANDALONE     = 0x0F
EFI_FV_FILETYPE_OEM_MIN                = 0xc0
EFI_FV_FILETYPE_OEM_MAX                = 0xdf
EFI_FV_FILETYPE_DEBUG_MIN              = 0xe0
EFI_FV_FILETYPE_DEBUG_MAX              = 0xef
EFI_FV_FILETYPE_FFS_MIN                = 0xf0
EFI_FV_FILETYPE_FFS_MAX                = 0xff
EFI_FV_FILETYPE_FFS_PAD                = 0xf0

FFS_ATTRIB_LARGE_FILE        = 0x01
FFS_ATTRIB_DATA_ALIGNMENT_2  = 0x02
FFS_ATTRIB_FIXED             = 0x04
FFS_ATTRIB_DATA_ALIGNMENT    = 0x38
FFS_ATTRIB_CHECKSUM          = 0x40

EFI_FILE_HEADER_CONSTRUCTION  = 0x01
EFI_FILE_HEADER_VALID         = 0x02
EFI_FILE_DATA_VALID           = 0x04
EFI_FILE_MARKED_FOR_UPDATE    = 0x08
EFI_FILE_DELETED              = 0x10
EFI_FILE_HEADER_INVALID       = 0x20

class EFI_FFS_FILE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Name",            EFI_GUID),
    ("IntegrityCheck",  EFI_FFS_INTEGRITY_CHECK),
    ("Type",            EFI_FV_FILETYPE),
    ("Attributes",      EFI_FFS_FILE_ATTRIBUTES),
    ("Size",            UINT8 * 3),
    ("State",           EFI_FFS_FILE_STATE)
  ]

class EFI_FFS_FILE_HEADER2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Name",            EFI_GUID),
    ("IntegrityCheck",  EFI_FFS_INTEGRITY_CHECK),
    ("Type",            EFI_FV_FILETYPE),
    ("Attributes",      EFI_FFS_FILE_ATTRIBUTES),
    ("Size",            UINT8 * 3),
    ("State",           EFI_FFS_FILE_STATE),
    ("ExtendedSize",    UINT64)
  ]

def IS_FFS_FILE2(FfsFileHeaderPtr):
  return (FfsFileHeaderPtr.Attributes & FFS_ATTRIB_LARGE_FILE) == FFS_ATTRIB_LARGE_FILE

def FFS_FILE_SIZE(FfsFileHeaderPtr):
  return FfsFileHeaderPtr.Size & 0x00ffffff

def FFS_FILE2_SIZE(FfsFileHeaderPtr):
  return FfsFileHeaderPtr.ExtendedSize

EFI_SECTION_TYPE  = UINT8

EFI_SECTION_ALL                   = 0x00

EFI_SECTION_COMPRESSION           = 0x01

EFI_SECTION_GUID_DEFINED          = 0x02

EFI_SECTION_DISPOSABLE            = 0x03

EFI_SECTION_PE32                   = 0x10
EFI_SECTION_PIC                    = 0x11
EFI_SECTION_TE                     = 0x12
EFI_SECTION_DXE_DEPEX              = 0x13
EFI_SECTION_VERSION                = 0x14
EFI_SECTION_USER_INTERFACE         = 0x15
EFI_SECTION_COMPATIBILITY16        = 0x16
EFI_SECTION_FIRMWARE_VOLUME_IMAGE  = 0x17
EFI_SECTION_FREEFORM_SUBTYPE_GUID  = 0x18
EFI_SECTION_RAW                    = 0x19
EFI_SECTION_PEI_DEPEX              = 0x1B
EFI_SECTION_MM_DEPEX               = 0x1C
EFI_SECTION_SMM_DEPEX              = EFI_SECTION_MM_DEPEX

class EFI_COMMON_SECTION_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",  UINT8 * 3),
    ("Type",  EFI_SECTION_TYPE)
  ]

class EFI_COMMON_SECTION_HEADER2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Size",          UINT8 * 3),
    ("Type",          EFI_SECTION_TYPE),
    ("ExtendedSize",  UINT32)
  ]

EFI_COMPATIBILITY16_SECTION  = EFI_COMMON_SECTION_HEADER
EFI_COMPATIBILITY16_SECTION2 = EFI_COMMON_SECTION_HEADER2

EFI_NOT_COMPRESSED        = 0x00
EFI_STANDARD_COMPRESSION  = 0x01

class EFI_COMPRESSION_SECTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",        EFI_COMMON_SECTION_HEADER),
    ("UncompressedLength",  UINT32),
    ("CompressionType",     UINT8)
  ]

class EFI_COMPRESSION_SECTION2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",        EFI_COMMON_SECTION_HEADER2),
    ("UncompressedLength",  UINT32),
    ("CompressionType",     UINT8)
  ]

EFI_DISPOSABLE_SECTION                  = EFI_COMMON_SECTION_HEADER
EFI_DISPOSABLE_SECTION2                 = EFI_COMMON_SECTION_HEADER2

EFI_DXE_DEPEX_SECTION                   = EFI_COMMON_SECTION_HEADER
EFI_DXE_DEPEX_SECTION2                  = EFI_COMMON_SECTION_HEADER2

EFI_FIRMWARE_VOLUME_IMAGE_SECTION       = EFI_COMMON_SECTION_HEADER
EFI_FIRMWARE_VOLUME_IMAGE_SECTION2      = EFI_COMMON_SECTION_HEADER2

class EFI_FREEFORM_SUBTYPE_GUID_SECTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",  EFI_COMMON_SECTION_HEADER),
    ("SubTypeGuid",   EFI_GUID)
  ]

class EFI_FREEFORM_SUBTYPE_GUID_SECTION2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",  EFI_COMMON_SECTION_HEADER2),
    ("SubTypeGuid",   EFI_GUID)
  ]

EFI_GUIDED_SECTION_PROCESSING_REQUIRED  = 0x01
EFI_GUIDED_SECTION_AUTH_STATUS_VALID    = 0x02

class EFI_GUID_DEFINED_SECTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",          EFI_COMMON_SECTION_HEADER),
    ("SectionDefinitionGuid", EFI_GUID),
    ("DataOffset",            UINT16),
    ("Attributes",            UINT16)
  ]

class EFI_GUID_DEFINED_SECTION2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",          EFI_COMMON_SECTION_HEADER2),
    ("SectionDefinitionGuid", EFI_GUID),
    ("DataOffset",            UINT16),
    ("Attributes",            UINT16)
  ]

EFI_PE32_SECTION                        = EFI_COMMON_SECTION_HEADER
EFI_PE32_SECTION2                       = EFI_COMMON_SECTION_HEADER2

EFI_PEI_DEPEX_SECTION                   = EFI_COMMON_SECTION_HEADER
EFI_PEI_DEPEX_SECTION2                  = EFI_COMMON_SECTION_HEADER2

EFI_PIC_SECTION                         = EFI_COMMON_SECTION_HEADER
EFI_PIC_SECTION2                        = EFI_COMMON_SECTION_HEADER2

EFI_TE_SECTION                          = EFI_COMMON_SECTION_HEADER
EFI_TE_SECTION2                         = EFI_COMMON_SECTION_HEADER2

EFI_RAW_SECTION                         = EFI_COMMON_SECTION_HEADER
EFI_RAW_SECTION2                        = EFI_COMMON_SECTION_HEADER2

EFI_SMM_DEPEX_SECTION                   = EFI_COMMON_SECTION_HEADER
EFI_SMM_DEPEX_SECTION2                  = EFI_COMMON_SECTION_HEADER2

class EFI_USER_INTERFACE_SECTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",    EFI_COMMON_SECTION_HEADER),
    ("FileNameString",  CHAR16 * 1)
  ]

class EFI_USER_INTERFACE_SECTION2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",    EFI_COMMON_SECTION_HEADER2),
    ("FileNameString",  CHAR16 * 1)
  ]

class EFI_VERSION_SECTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",  EFI_COMMON_SECTION_HEADER),
    ("BuildNumber",   UINT16),
    ("VersionString", CHAR16 * 1)
  ]

class EFI_VERSION_SECTION2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("CommonHeader",  EFI_COMMON_SECTION_HEADER2),
    ("BuildNumber",   UINT16),
    ("VersionString", CHAR16 * 1)
  ]

def SECTION_SIZE(SectionHeaderPtr):
  return SectionHeaderPtr.Size & 0x00ffffff

def IS_SECTION2(SectionHeaderPtr):
  return (SectionHeaderPtr.Size & 0x00ffffff) == 0x00ffffff

def SECTION2_SIZE(SectionHeaderPtr):
  return SectionHeaderPtr.ExtendedSize

