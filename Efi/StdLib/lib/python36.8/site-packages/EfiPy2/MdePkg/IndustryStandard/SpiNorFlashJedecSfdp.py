# SpiNorFlashJedecSfdp.py
#
# EfiPy2.MdePkg.IndustryStandard.SpiNorFlashJedecSfdp
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

SFDP_HEADER_SIGNATURE          = 0x50444653
SFDP_SUPPORTED_MAJOR_REVISION  = 0x1

SFDP_BASIC_PARAMETER_ID_LSB  = 0x00
SFDP_BASIC_PARAMETER_ID_MSB  = 0xFF

SFDP_SECTOR_MAP_PARAMETER_ID_LSB        = 0x81
SFDP_FOUR_BYTE_ADDRESS_INSTRUCTION_LSB  = 0x84
SFDP_SECTOR_MAP_PARAMETER_ID_MSB        = 0xFF

SFDP_FLASH_MEMORY_DENSITY_4GBIT  = 0x80000000

class SPDM_GET_VERSION_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT32),
    ("MinorRev",            UINT32, 8),
    ("MajorRev",            UINT32, 8),
    ("NumParameterHeaders", UINT32, 8),
    ("AccessProtocol",      UINT32, 8)
    ]

class SFDP_PARAMETER_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdLsb",         UINT32, 8),
    ("MinorRev",      UINT32, 8),
    ("MajorRev",      UINT32, 8),
    ("Length",        UINT32, 8),
    ("TablePointer",  UINT32, 24),
    ("IdMsb",         UINT32, 8)
    ]

class SFDP_BASIC_FLASH_PARAMETER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("EraseSizes",                        UINT32, 2),
  ("WriteGranularity",                  UINT32, 1),
  ("VolatileStatusBlockProtect",        UINT32, 1),
  ("WriteEnableVolatileStatus",         UINT32, 1),
  ("Unused1Dw1",                        UINT32, 3),
  ("FourKEraseInstr",                   UINT32, 8),
  ("FastRead112",                       UINT32, 1),
  ("AddressBytes",                      UINT32, 2),
  ("DtrClocking",                       UINT32, 1),
  ("FastRead122",                       UINT32, 1),
  ("FastRead144",                       UINT32, 1),
  ("FastRead114",                       UINT32, 1),
  ("Unused2Dw1",                        UINT32, 9),
  ("Density",                           UINT32),
  ("FastRead144Dummy",                  UINT32, 5),
  ("FastRead144ModeClk",                UINT32, 3),
  ("FastRead144Instr",                  UINT32, 8),
  ("FastRead114Dummy",                  UINT32, 5),
  ("FastRead114ModeClk",                UINT32, 3),
  ("FastRead114Instr",                  UINT32, 8),
  ("FastRead112Dummy",                  UINT32, 5),
  ("FastRead112ModeClk",                UINT32, 3),
  ("FastRead112Instr",                  UINT32, 8),
  ("FastRead122Dummy",                  UINT32, 5),
  ("FastRead122ModeClk",                UINT32, 3),
  ("FastRead122Instr",                  UINT32, 8),
  ("FastRead222",                       UINT32, 1),
  ("Unused1Dw5",                        UINT32, 3),
  ("FastRead444",                       UINT32, 1),
  ("Unused2Dw5",                        UINT32, 27),
  ("UnusedDw6",                         UINT32, 16),
  ("FastRead222Dummy",                  UINT32, 5),
  ("FastRead222ModeClk",                UINT32, 3),
  ("FastRead222Instr",                  UINT32, 8),
  ("UnusedDw7",                         UINT32, 16),
  ("FastRead444Dummy",                  UINT32, 5),
  ("FastRead444ModeClk",                UINT32, 3),
  ("FastRead444Instr",                  UINT32, 8),
  ("Erase1Size",                        UINT32, 8),
  ("Erase1Instr",                       UINT32, 8),
  ("Erase2Size",                        UINT32, 8),
  ("Erase2Instr",                       UINT32, 8),
  ("Erase3Size",                        UINT32, 8),
  ("Erase3Instr",                       UINT32, 8),
  ("Erase4Size",                        UINT32, 8),
  ("Erase4Instr",                       UINT32, 8),
  ("EraseMultiplier",                   UINT32, 4),
  ("Erase1Time",                        UINT32, 7),
  ("Erase2Time",                        UINT32, 7),
  ("Erase3Time",                        UINT32, 7),
  ("Erase4Time",                        UINT32, 7),
  ("ProgramMultiplier",                 UINT32, 4),
  ("PageSize",                          UINT32, 4),
  ("PPTime",                            UINT32, 6),
  ("BPFirstTime",                       UINT32, 5),
  ("BPAdditionalTime",                  UINT32, 5),
  ("ChipEraseTime",                     UINT32, 7),
  ("Unused1Dw11",                       UINT32, 1),
  ("ProgSuspendProhibit",               UINT32, 4),
  ("EraseSuspendProhibit",              UINT32, 4),
  ("Unused1Dw13",                       UINT32, 1),
  ("ProgResumeToSuspend",               UINT32, 4),
  ("ProgSuspendInProgressTime",         UINT32, 7),
  ("EraseResumeToSuspend",              UINT32, 4),
  ("EraseSuspendInProgressTime",        UINT32, 7),
  ("SuspendResumeSupported",            UINT32, 1),
  ("Unused13",                          UINT32),
  ("Unused14",                          UINT32),
  ("Unused15",                          UINT32),
  ("Unused16",                          UINT32),
  ("FastRead188Dummy",                  UINT32, 5),
  ("FastRead188ModeClk",                UINT32, 3),
  ("FastRead188Instr",                  UINT32, 8),
  ("FastRead118Dummy",                  UINT32, 5),
  ("FastRead118ModeClk",                UINT32, 3),
  ("FastRead118Instr",                  UINT32, 8),
  ("Unused18",                          UINT32),
  ("Unused19",                          UINT32),
  ("Unused20",                          UINT32),
  ("Unused21",                          UINT32),
  ("Unused22",                          UINT32),
  ("Unused23",                          UINT32)
    ]


SPI_UNIFORM_4K_ERASE_SUPPORTED    = 0x01
SPI_UNIFORM_4K_ERASE_UNSUPPORTED  = 0x03

SPI_ADDR_3BYTE_ONLY  = 0x00
SPI_ADDR_3OR4BYTE    = 0x01
SPI_ADDR_4BYTE_ONLY  = 0x02

FDP_ERASE_TYPES_NUMBER  = 4
SFDP_ERASE_TYPE_1        = 0x0001
SFDP_ERASE_TYPE_2        = 0x0002
SFDP_ERASE_TYPE_3        = 0x0003
SFDP_ERASE_TYPE_4        = 0x0004

SPI_FLASH_READ                    = 0x03
SPI_FLASH_READ_DUMMY                = 0x00
SPI_FLASH_READ_ADDR_BYTES           = SPI_ADDR_3OR4BYTE
SPI_FLASH_FAST_READ               = 0x0B
SPI_FLASH_FAST_READ_DUMMY           = 0x01
SPI_FLASH_FAST_READ_ADDR_BYTES      = SPI_ADDR_3OR4BYTE
SPI_FLASH_PP                      = 0x02
SPI_FLASH_PP_DUMMY                  = 0x00
SPI_FLASH_PP_ADDR_BYTES             = SPI_ADDR_3OR4BYTE
SPI_FLASH_PAGE_SIZE                 = 256
SPI_FLASH_SE                      = 0x20
SPI_FLASH_SE_DUMMY                  = 0x00
SPI_FLASH_SE_ADDR_BYTES             = SPI_ADDR_3OR4BYTE
SPI_FLASH_BE32K                   = 0x52
SPI_FLASH_BE32K_DUMMY               = 0x00
SPI_FLASH_BE32K_ADDR_BYTES          = SPI_ADDR_3OR4BYTE
SPI_FLASH_BE                      = 0xD8
SPI_FLASH_BE_DUMMY                  = 0x00
SPI_FLASH_BE_ADDR_BYTES             = SPI_ADDR_3OR4BYTE
SPI_FLASH_CE                      = 0x60
SPI_FLASH_CE_DUMMY                  = 0x00
SPI_FLASH_CE_ADDR_BYTES             = SPI_ADDR_3OR4BYTE
SPI_FLASH_RDID                    = 0x9F
SPI_FLASH_RDID_DUMMY                = 0x00
SPI_FLASH_RDID_ADDR_BYTES           = SPI_ADDR_3OR4BYTE

SPI_FLASH_WREN                              = 0x06
SPI_FLASH_WREN_DUMMY                          = 0x00
SPI_FLASH_WREN_ADDR_BYTES                     = SPI_ADDR_3OR4BYTE
SPI_FLASH_WRDI                              = 0x04
SPI_FLASH_WRDI_DUMMY                          = 0x00
SPI_FLASH_WRDI_ADDR_BYTES                     = SPI_ADDR_3OR4BYTE
SPI_FLASH_RDSR                              = 0x05
SPI_FLASH_RDSR_DUMMY                          = 0x00
SPI_FLASH_RDSR_ADDR_BYTES                     = SPI_ADDR_3OR4BYTE
SPI_FLASH_SR_NOT_WIP                          = 0x0
SPI_FLASH_SR_WIP                              = BIT0
SPI_FLASH_SR_WEL                              = BIT1
SPI_FLASH_WRSR                              = 0x01
SPI_FLASH_WRSR_DUMMY                          = 0x00
SPI_FLASH_WRSR_ADDR_BYTES                     = SPI_ADDR_3OR4BYTE
SPI_FLASH_WREN_50H                          = 0x50
SPI_FLASH_RDSFDP                            = 0x5A
SPI_FLASH_RDSFDP_DUMMY                        = 0x01
SPI_FLASH_RDSFDP_ADDR_BYTES                   = SPI_ADDR_3BYTE_ONLY
ERASE_TYPICAL_TIME_UNITS_MASK                 = 0x60
ERASE_TYPICAL_TIME_BIT_POSITION               = 5
ERASE_TYPICAL_TIME_UNIT_1_MS_BITMAP             = 0x00
ERASE_TYPICAL_TIME_UNIT_1_MS                    = 1
ERASE_TYPICAL_TIME_UNIT_16_MS_BITMAP            = 0x01
ERASE_TYPICAL_TIME_UNIT_16_MS                   = 16
ERASE_TYPICAL_TIME_UNIT_128_MS_BITMAP           = 0x02
ERASE_TYPICAL_TIME_UNIT_128_MS                  = 128
ERASE_TYPICAL_TIME_UNIT_1000_MS_BITMAP          = 0x03
ERASE_TYPICAL_TIME_UNIT_1000_MS                 = 1000
ERASE_TYPICAL_TIME_COUNT_MASK                 = 0x1f

class SFDP_SECTOR_CONFIGURATION_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorEnd",               UINT32, 1),
    ("DescriptorType",              UINT32, 1),
    ("Reserve1",                    UINT32, 6),
    ("DetectionInstruction",        UINT32, 8),
    ("DetectionLatency",            UINT32, 4),
    ("Reserve2",                    UINT32, 2),
    ("DetectionCommandAddressLen",  UINT32, 2),
    ("ReadDataMask",                UINT32, 8),
    ("CommandAddress",              UINT32, 32)
    ]

SFDP_SECTOR_MAP_TABLE_ENTRY_TYPE_COMMAND  = 0
SFDP_SECTOR_MAP_TABLE_ENTRY_TYPE_MAP      = 1
SFDP_SECTOR_MAP_TABLE_ENTRY_LAST          = 1

SpdfConfigurationCommandAddressNone     = 0
SpdfConfigurationCommandAddress3Byte    = 1
SpdfConfigurationCommandAddress4Byte    = 2
SpdfConfigurationCommandAddressVariable = 3
SPDF_CONFIGURATION_COMMAND_ADDR_LENGTH  = ENUM

class SFDP_SECTOR_CONFIGURATION_MAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorEnd",   UINT32, 1),
    ("DescriptorType",  UINT32, 1),
    ("Reserve1",        UINT32, 6),
    ("ConfigurationID", UINT32, 8),
    ("RegionCount",     UINT32, 8),
    ("Reserve2",        UINT32, 8)
    ]

class SFDP_SECTOR_CONFIGURATION_GENERIC_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorEnd",   UINT32, 1),
    ("DescriptorType",  UINT32, 1)
    ]

class SFDP_SECTOR_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EraseType1", UINT32, 1),
    ("EraseType2", UINT32, 1),
    ("EraseType3", UINT32, 1),
    ("EraseType4", UINT32, 1),
    ("Reserve1",   UINT32, 4),
    ("RegionSize", UINT32, 24)
    ]

SFDP_SECTOR_REGION_SIZE_UNIT  = 256

class SFDP_SECTOR_MAP_TABLE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("GenericHeader",         SFDP_SECTOR_CONFIGURATION_GENERIC_HEADER),
    ("ConfigurationCommand",  SFDP_SECTOR_CONFIGURATION_COMMAND       ),
    ("ConfigurationMap",      SFDP_SECTOR_CONFIGURATION_MAP           )
    ]
