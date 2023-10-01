# Udf.py
#
# EfiPy2.MdePkg.IndustryStandard.Udf
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

UDF_BEA_IDENTIFIER   = b"BEA01"
UDF_NSR2_IDENTIFIER  = b"NSR02"
UDF_NSR3_IDENTIFIER  = b"NSR03"
UDF_TEA_IDENTIFIER   = b"TEA01"

UDF_LOGICAL_SECTOR_SHIFT  = 11
UDF_LOGICAL_SECTOR_SIZE   = (1  << UDF_LOGICAL_SECTOR_SHIFT)
UDF_VRS_START_OFFSET      = (16 << UDF_LOGICAL_SECTOR_SHIFT)

UdfPrimaryVolumeDescriptor          = 1
UdfAnchorVolumeDescriptorPointer    = 2
UdfVolumeDescriptorPointer          = 3
UdfImplemenationUseVolumeDescriptor = 4
UdfPartitionDescriptor              = 5
UdfLogicalVolumeDescriptor          = 6
UdfUnallocatedSpaceDescriptor       = 7
UdfTerminatingDescriptor            = 8
UdfLogicalVolumeIntegrityDescriptor = 9
UdfFileSetDescriptor                = 256
UdfFileIdentifierDescriptor         = 257
UdfAllocationExtentDescriptor       = 258
UdfFileEntry                        = 261
UdfExtendedFileEntry                = 266
UDF_VOLUME_DESCRIPTOR_ID            = ENUM

class UDF_DESCRIPTOR_TAG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TagIdentifier",       UINT16),
    ("DescriptorVersion",   UINT16),
    ("TagChecksum",         UINT8 ),
    ("Reserved",            UINT8 ),
    ("TagSerialNumber",     UINT16),
    ("DescriptorCRC",       UINT16),
    ("DescriptorCRCLength", UINT16),
    ("TagLocation",         UINT32)
  ]

class UDF_EXTENT_AD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtentLength",    UINT32),
    ("ExtentLocation",  UINT32)
  ]

class UDF_CHAR_SPEC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharacterSetType",    UINT8),
    ("CharacterSetInfo",    UINT8 * 63)
  ]

class UDF_ENTITY_ID_Suffix_Domain (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UdfRevision",    UINT16),
    ("DomainFlags",    UINT8),
    ("Reserved",       UINT8 * 5)
  ]

class UDF_ENTITY_ID_Suffix_Entity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UdfRevision",     UINT16),
    ("OSClass",         UINT8 ),
    ("OSIdentifier",    UINT8 ),
    ("Reserved",        UINT8 * 4)
  ]

class UDF_ENTITY_ID_Suffix_ImplementationEntity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OSClass",                 UINT8),
    ("OSIdentifier",            UINT8),
    ("ImplementationUseArea",   UINT8 * 6)
  ]

class UDF_ENTITY_ID_Suffix_ApplicationEntity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ApplicationUseArea",  UINT8 * 8)
  ]

class UDF_ENTITY_ID_Suffix_Raw (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    UINT8 * 8)
  ]

class UDF_ENTITY_ID_Suffix (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Entity",                  UDF_ENTITY_ID_Suffix_Entity),
    ("ImplementationEntity",    UDF_ENTITY_ID_Suffix_Entity),
    ("ApplicationEntity",       UDF_ENTITY_ID_Suffix_Entity),
    ("Raw",                     UDF_ENTITY_ID_Suffix_Raw)
  ]

class UDF_ENTITY_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Flags",       UINT8     ),
    ("Identifier",  UINT8 * 23),
    ("Suffix",      UDF_ENTITY_ID_Suffix)
  ]

class UDF_LB_ADDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogicalBlockNumber",      UINT32),
    ("PartitionReferenceNumber",UINT16)
  ]

class UDF_LONG_ALLOCATION_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtentLength",        UINT32),
    ("ExtentLocation",      UDF_LB_ADDR),
    ("ImplementationUse",   UINT8 * 6)
  ]

class UDF_ANCHOR_VOLUME_DESCRIPTOR_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorTag",                           UDF_DESCRIPTOR_TAG),
    ("MainVolumeDescriptorSequenceExtent",      UDF_EXTENT_AD     ),
    ("ReserveVolumeDescriptorSequenceExtent",   UDF_EXTENT_AD     ),
    ("Reserved",                                UINT8 * 480       )
  ]

class UDF_LOGICAL_VOLUME_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorTag",                   UDF_DESCRIPTOR_TAG            ),
    ("VolumeDescriptorSequenceNumber",  UINT32                        ),
    ("DescriptorCharacterSet",          UDF_CHAR_SPEC                 ),
    ("LogicalVolumeIdentifier",         UINT8 * 128                   ),
    ("LogicalBlockSize",                UINT32                        ),
    ("DomainIdentifier",                UDF_ENTITY_ID                 ),
    ("LogicalVolumeContentsUse",        UDF_LONG_ALLOCATION_DESCRIPTOR),
    ("MapTableLength",                  UINT32                        ),
    ("NumberOfPartitionMaps",           UINT32                        ),
    ("ImplementationIdentifier",        UDF_ENTITY_ID                 ),
    ("ImplementationUse",               UINT8 * 128                   ),
    ("IntegritySequenceExtent",         UDF_EXTENT_AD                 ),
    ("PartitionMaps",                   UINT8 * 6                     )
  ]

