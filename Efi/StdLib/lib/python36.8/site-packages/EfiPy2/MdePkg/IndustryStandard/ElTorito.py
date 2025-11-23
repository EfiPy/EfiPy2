# ElTorito.py
#
# EfiPy2.MdePkg.IndustryStandard.ElTorito
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

CDVOL_TYPE_STANDARD = 0x0
CDVOL_TYPE_CODED    = 0x1
CDVOL_TYPE_END      = 0xFF

CDVOL_ID  = "CD001"

CDVOL_ELTORITO_ID = "EL TORITO SPECIFICATION"

ELTORITO_ID_CATALOG               = 0x01
ELTORITO_ID_SECTION_BOOTABLE      = 0x88
ELTORITO_ID_SECTION_NOT_BOOTABLE  = 0x00
ELTORITO_ID_SECTION_HEADER        = 0x90
ELTORITO_ID_SECTION_HEADER_FINAL  = 0x91

ELTORITO_NO_EMULATION = 0x00
ELTORITO_12_DISKETTE  = 0x01
ELTORITO_14_DISKETTE  = 0x02
ELTORITO_28_DISKETTE  = 0x03
ELTORITO_HARD_DISK    = 0x04

class CDROM_VOLUME_DESCRIPTOR_Unknown (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",      UINT8),
    ("Id",        CHAR8 * 5),
    ("Version",   CHAR8 * 82)
  ]

class CDROM_VOLUME_DESCRIPTOR_BootRecordVolume (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        UINT8),
    ("Id",          CHAR8 * 5),
    ("Version",     UINT8),
    ("SystemId",    CHAR8 * 32),
    ("Unused",      CHAR8 * 32),
    ("EltCatalog",  UINT8 * 4),
    ("Unused2",     CHAR8 * 13)
  ]

class CDROM_VOLUME_DESCRIPTOR_PrimaryVolume (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",          UINT8),
    ("Id",            CHAR8  * 5),
    ("Version",       UINT8),
    ("Unused",        UINT8),
    ("SystemId",      CHAR8  * 32),
    ("VolumeId",      CHAR8  * 32),
    ("Unused2",       UINT8  * 8),
    ("VolSpaceSize",  UINT32 * 2)
  ]

class CDROM_VOLUME_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unknown",           CDROM_VOLUME_DESCRIPTOR_Unknown),
    ("BootRecordVolume",  CDROM_VOLUME_DESCRIPTOR_BootRecordVolume),
    ("PrimaryVolume",     CDROM_VOLUME_DESCRIPTOR_PrimaryVolume)
  ]

class ELTORITO_CATALOG_Unknown (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",  CHAR8 * 0x20)
  ]

class ELTORITO_CATALOG_Catalog (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",   UINT8),
    ("PlatformId",  UINT8),
    ("Reserved",    UINT16),
    ("ManufacId",   UINT8 * 24),
    ("Checksum",    UINT16),
    ("Id55AA",      UINT16)
  ]

class ELTORITO_CATALOG_Boot (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",   UINT8),
    ("MediaType",   UINT8, 4),
    ("Reserved1",   UINT8, 4),
    ("LoadSegment", UINT16),
    ("SystemType",  UINT8),
    ("Reserved2",   UINT8),
    ("SectorCount", UINT16),
    ("Lba",         UINT32)
  ]

class ELTORITO_CATALOG_Section (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",       UINT8),
    ("PlatformId",      UINT8),
    ("SectionEntries",  UINT16),
    ("Id",              UINT8 * 28)
  ]

class ELTORITO_CATALOG (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unknown", ELTORITO_CATALOG_Unknown),
    ("Catalog", ELTORITO_CATALOG_Catalog),
    ("Boot",    ELTORITO_CATALOG_Boot),
    ("Section", ELTORITO_CATALOG_Section)
  ]
