# Atapi.py
#
# EfiPy2.MdePkg.IndustryStandard.Atapi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class ATA5_IDENTIFY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("config",                                  UINT16),
    ("cylinders",                               UINT16),
    ("reserved_2",                              UINT16),
    ("heads",                                   UINT16),
    ("vendor_data1",                            UINT16),
    ("vendor_data2",                            UINT16),
    ("sectors_per_track",                       UINT16),
    ("vendor_specific_7_9",                     UINT16 * 3),
    ("SerialNo",                                CHAR8  * 20),
    ("vendor_specific_20_21",                   UINT16 * 2),
    ("ecc_bytes_available",                     UINT16),
    ("FirmwareVer",                             CHAR8  * 8),
    ("ModelName",                               CHAR8  * 40),
    ("multi_sector_cmd_max_sct_cnt",            UINT16),
    ("reserved_48",                             UINT16),
    ("capabilities",                            UINT16),
    ("reserved_50",                             UINT16),
    ("pio_cycle_timing",                        UINT16),
    ("reserved_52",                             UINT16),
    ("field_validity",                          UINT16),
    ("current_cylinders",                       UINT16),
    ("current_heads",                           UINT16),
    ("current_sectors",                         UINT16),
    ("CurrentCapacityLsb",                      UINT16),
    ("CurrentCapacityMsb",                      UINT16),
    ("reserved_59",                             UINT16),
    ("user_addressable_sectors_lo",             UINT16),
    ("user_addressable_sectors_hi",             UINT16),
    ("reserved_62",                             UINT16),
    ("multi_word_dma_mode",                     UINT16),
    ("advanced_pio_modes",                      UINT16),
    ("min_multi_word_dma_cycle_time",           UINT16),
    ("rec_multi_word_dma_cycle_time",           UINT16),
    ("min_pio_cycle_time_without_flow_control", UINT16),
    ("min_pio_cycle_time_with_flow_control",    UINT16),
    ("reserved_69_79",                          UINT16 * 11),
    ("major_version_no",                        UINT16),
    ("minor_version_no",                        UINT16),
    ("command_set_supported_82",                UINT16),
    ("command_set_supported_83",                UINT16),
    ("command_set_feature_extn",                UINT16),
    ("command_set_feature_enb_85",              UINT16),
    ("command_set_feature_enb_86",              UINT16),
    ("command_set_feature_default",             UINT16),
    ("ultra_dma_mode",                          UINT16),
    ("reserved_89_127",                         UINT16 * 39),
    ("security_status",                         UINT16),
    ("vendor_data_129_159",                     UINT16 * 31),
    ("reserved_160_255",                        UINT16 * 96)
  ]

class ATA_IDENTIFY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("config",                                      UINT16),
    ("obsolete_1",                                  UINT16),
    ("specific_config",                             UINT16),
    ("obsolete_3",                                  UINT16),
    ("retired_4_5",                                 UINT16 * 2),
    ("obsolete_6",                                  UINT16),
    ("cfa_reserved_7_8",                            UINT16 * 2),
    ("retired_9",                                   UINT16),
    ("SerialNo",                                    CHAR8  * 20),
    ("retired_20_21",                               UINT16 * 2),
    ("obsolete_22",                                 UINT16),
    ("FirmwareVer",                                 CHAR8  * 8),
    ("ModelName",                                   CHAR8  * 40),
    ("multi_sector_cmd_max_sct_cnt",                UINT16),
    ("trusted_computing_support",                   UINT16),
    ("capabilities_49",                             UINT16),
    ("capabilities_50",                             UINT16),
    ("obsolete_51_52",                              UINT16 * 2),
    ("field_validity",                              UINT16),
    ("obsolete_54_58",                              UINT16 * 5),
    ("multi_sector_setting",                        UINT16),
    ("user_addressable_sectors_lo",                 UINT16),
    ("user_addressable_sectors_hi",                 UINT16),
    ("obsolete_62",                                 UINT16),
    ("multi_word_dma_mode",                         UINT16),
    ("advanced_pio_modes",                          UINT16),
    ("min_multi_word_dma_cycle_time",               UINT16),
    ("rec_multi_word_dma_cycle_time",               UINT16),
    ("min_pio_cycle_time_without_flow_control",     UINT16),
    ("min_pio_cycle_time_with_flow_control",        UINT16),
    ("additional_supported",                        UINT16),
    ("reserved_70",                                 UINT16),
    ("reserved_71_74",                              UINT16 * 4),
    ("queue_depth",                                 UINT16),
    ("serial_ata_capabilities",                     UINT16),
    ("reserved_77",                                 UINT16),
    ("serial_ata_features_supported",               UINT16),
    ("serial_ata_features_enabled",                 UINT16),
    ("major_version_no",                            UINT16),
    ("minor_version_no",                            UINT16),
    ("command_set_supported_82",                    UINT16),
    ("command_set_supported_83",                    UINT16),
    ("command_set_feature_extn",                    UINT16),
    ("command_set_feature_enb_85",                  UINT16),
    ("command_set_feature_enb_86",                  UINT16),
    ("command_set_feature_default",                 UINT16),
    ("ultra_dma_mode",                              UINT16),
    ("time_for_security_erase_unit",                UINT16),
    ("time_for_enhanced_security_erase_unit",       UINT16),
    ("advanced_power_management_level",             UINT16),
    ("master_password_identifier",                  UINT16),
    ("hardware_configuration_test_result",          UINT16),
    ("obsolete_94",                                 UINT16),
    ("stream_minimum_request_size",                 UINT16),
    ("streaming_transfer_time_for_dma",             UINT16),
    ("streaming_access_latency_for_dma_and_pio",    UINT16),
    ("streaming_performance_granularity",           UINT16 * 2),
    ("maximum_lba_for_48bit_addressing",            UINT16 * 4),
    ("streaming_transfer_time_for_pio",             UINT16),
    ("max_no_of_512byte_blocks_per_data_set_cmd",   UINT16),
    ("phy_logic_sector_support",                    UINT16),
    ("interseek_delay_for_iso7779",                 UINT16),
    ("world_wide_name",                             UINT16 * 4),
    ("reserved_for_128bit_wwn_112_115",             UINT16 * 4),
    ("reserved_for_technical_report",               UINT16),
    ("logic_sector_size_lo",                        UINT16),
    ("logic_sector_size_hi",                        UINT16),
    ("features_and_command_sets_supported_ext",     UINT16),
    ("features_and_command_sets_enabled_ext",       UINT16),
    ("reserved_121_126",                            UINT16 * 6),
    ("obsolete_127",                                UINT16),
    ("security_status",                             UINT16),
    ("vendor_specific_129_159",                     UINT16 * 31),
    ("cfa_power_mode",                              UINT16),
    ("reserved_for_compactflash_161_167",           UINT16 * 7),
    ("device_nominal_form_factor",                  UINT16),
    ("is_data_set_cmd_supported",                   UINT16),
    ("additional_product_identifier",               CHAR8  * 8),
    ("reserved_174_175",                            UINT16),
    ("media_serial_number",                         CHAR8  * 60),
    ("sct_command_transport",                       UINT16),
    ("reserved_207_208",                            UINT16 * 2),
    ("alignment_logic_in_phy_blocks",               UINT16),
    ("write_read_verify_sector_count_mode3",        UINT16 * 2),
    ("verify_sector_count_mode2",                   UINT16 * 2),
    ("nv_cache_capabilities",                       UINT16),
    ("nv_cache_size_in_logical_block_lsw",          UINT16),
    ("nv_cache_size_in_logical_block_msw",          UINT16),
    ("nominal_media_rotation_rate",                 UINT16),
    ("reserved_218",                                UINT16),
    ("nv_cache_options",                            UINT16),
    ("write_read_verify_mode",                      UINT16),
    ("reserved_221",                                UINT16),
    ("transport_major_revision_number",             UINT16),
    ("transport_minor_revision_number",             UINT16),
    ("reserved_224_229",                            UINT16 * 6),
    ("extended_no_of_addressable_sectors",          UINT64),
    ("min_number_per_download_microcode_mode3",     UINT16),
    ("max_number_per_download_microcode_mode3",     UINT16),
    ("reserved_236_254",                            UINT16 * 19),
    ("integrity_word",                              UINT16)
  ]

class ATAPI_IDENTIFY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("config",                                   UINT16),
    ("reserved_1",                               UINT16),
    ("specific_config",                          UINT16),
    ("reserved_3_9",                             UINT16 * 7),
    ("SerialNo",                                 CHAR8  * 20),
    ("reserved_20_22",                           UINT16 * 3),
    ("FirmwareVer",                              CHAR8  * 8),
    ("ModelName",                                CHAR8  * 40),
    ("reserved_47_48",                           UINT16 * 2),
    ("capabilities_49",                          UINT16),
    ("capabilities_50",                          UINT16),
    ("obsolete_51",                              UINT16),
    ("reserved_52",                              UINT16),
    ("field_validity",                           UINT16),
    ("reserved_54_61",                           UINT16 * 8),
    ("dma_dir",                                  UINT16),
    ("multi_word_dma_mode",                      UINT16),
    ("advanced_pio_modes",                       UINT16),
    ("min_multi_word_dma_cycle_time",            UINT16),
    ("rec_multi_word_dma_cycle_time",            UINT16),
    ("min_pio_cycle_time_without_flow_control",  UINT16),
    ("min_pio_cycle_time_with_flow_control",     UINT16),
    ("reserved_69_70",                           UINT16 * 2),
    ("obsolete_71_72",                           UINT16 * 2),
    ("reserved_73_74",                           UINT16 * 2),
    ("obsolete_75",                              UINT16),
    ("serial_ata_capabilities",                  UINT16),
    ("reserved_77",                              UINT16),
    ("serial_ata_features_supported",            UINT16),
    ("serial_ata_features_enabled",              UINT16),
    ("major_version_no",                         UINT16),
    ("minor_version_no",                         UINT16),
    ("cmd_set_support_82",                       UINT16),
    ("cmd_set_support_83",                       UINT16),
    ("cmd_feature_support",                      UINT16),
    ("cmd_feature_enable_85",                    UINT16),
    ("cmd_feature_enable_86",                    UINT16),
    ("cmd_feature_default",                      UINT16),
    ("ultra_dma_select",                         UINT16),
    ("time_required_for_sec_erase",              UINT16),
    ("time_required_for_enhanced_sec_erase",     UINT16),
    ("advanced_power_management_level",          UINT16),
    ("master_pwd_revison_code",                  UINT16),
    ("hardware_reset_result",                    UINT16),
    ("obsolete_94",                              UINT16),
    ("reserved_95_107",                          UINT16 * 13),
    ("world_wide_name",                          UINT16 * 4),
    ("reserved_for_128bit_wwn_112_115",          UINT16 * 4),
    ("reserved_116_118",                         UINT16 * 3),
    ("command_and_feature_sets_supported",       UINT16),
    ("command_and_feature_sets_supported_enable",UINT16),
    ("reserved_121_124",                         UINT16 * 4),
    ("atapi_byte_count_0_behavior",              UINT16),
    ("obsolete_126_127",                         UINT16 * 2),
    ("security_status",                          UINT16),
    ("reserved_129_159",                         UINT16 * 31),
    ("cfa_reserved_160_175",                     UINT16 * 16),
    ("reserved_176_221",                         UINT16 * 46),
    ("transport_major_version",                  UINT16),
    ("transport_minor_version",                  UINT16),
    ("reserved_224_254",                         UINT16 * 31),
    ("integrity_word",                           UINT16)
  ]

class ATAPI_INQUIRY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("peripheral_type",         UINT8),
    ("RMB",                     UINT8),
    ("version",                 UINT8),
    ("response_data_format",    UINT8),
    ("addnl_length",            UINT8),
    ("reserved_5",              UINT8),
    ("reserved_6",              UINT8),
    ("reserved_7",              UINT8),
    ("vendor_info",             UINT8 * 8),
    ("product_id",              UINT8 * 16),
    ("product_revision_level",  UINT8 * 4),
    ("vendor_specific_36_55",   UINT8 * (55 - 36 + 1)),
    ("reserved_56_95",          UINT8 * (95 - 56 + 1)),
    ("vendor_specific_96_253",  UINT8 * (253 - 96 + 1))
  ]

class ATAPI_REQUEST_SENSE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("error_code",                  UINT8, 7),
    ("valid",                       UINT8, 1),
    ("reserved_1",                  UINT8),
    ("sense_key",                   UINT8, 4),
    ("reserved_2",                  UINT8, 1),
    ("Vendor_specifc_1",            UINT8, 3),
    ("vendor_specific_3",           UINT8),
    ("vendor_specific_4",           UINT8),
    ("vendor_specific_5",           UINT8),
    ("vendor_specific_6",           UINT8),
    ("addnl_sense_length",          UINT8),
    ("vendor_specific_8",           UINT8),
    ("vendor_specific_9",           UINT8),
    ("vendor_specific_10",          UINT8),
    ("vendor_specific_11",          UINT8),
    ("addnl_sense_code",            UINT8),
    ("addnl_sense_code_qualifier",  UINT8),
    ("field_replaceable_unit_code", UINT8),
    ("sense_key_specific_15",       UINT8, 7),
    ("SKSV",                        UINT8, 1),
    ("sense_key_specific_16",       UINT8),
    ("sense_key_specific_17",       UINT8)
  ]

class ATAPI_READ_CAPACITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LastLba3",    UINT8),
    ("LastLba2",    UINT8),
    ("LastLba1",    UINT8),
    ("LastLba0",    UINT8),
    ("BlockSize3",  UINT8),
    ("BlockSize2",  UINT8),
    ("BlockSize1",  UINT8),
    ("BlockSize0",  UINT8)
  ]

class ATAPI_READ_FORMAT_CAPACITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("reserved_0",      UINT8),
    ("reserved_1",      UINT8),
    ("reserved_2",      UINT8),
    ("Capacity_Length", UINT8),
    ("LastLba3",        UINT8),
    ("LastLba2",        UINT8),
    ("LastLba1",        UINT8),
    ("LastLba0",        UINT8),
    ("DesCode",         UINT8, 2),
    ("reserved_9",      UINT8, 6),
    ("BlockSize2",      UINT8),
    ("BlockSize1",      UINT8),
    ("BlockSize0",      UINT8)
  ]

class ATAPI_TEST_UNIT_READY_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",      UINT8),
    ("reserved_1",  UINT8),
    ("reserved_2",  UINT8),
    ("reserved_3",  UINT8),
    ("reserved_4",  UINT8),
    ("reserved_5",  UINT8),
    ("reserved_6",  UINT8),
    ("reserved_7",  UINT8),
    ("reserved_8",  UINT8),
    ("reserved_9",  UINT8),
    ("reserved_10", UINT8),
    ("reserved_11", UINT8)
  ]

class ATAPI_INQUIRY_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",            UINT8),
    ("reserved_1",        UINT8 * 5),
    ("lun",               UINT8 * 3),
    ("page_code",         UINT8),
    ("reserved_3",        UINT8),
    ("allocation_length", UINT8),
    ("reserved_5",        UINT8),
    ("reserved_6",        UINT8),
    ("reserved_7",        UINT8),
    ("reserved_8",        UINT8),
    ("reserved_9",        UINT8),
    ("reserved_10",       UINT8),
    ("reserved_11",       UINT8)
  ]

class ATAPI_REQUEST_SENSE_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",            UINT8),
    ("reserved_1",        UINT8 * 5),
    ("lun",               UINT8 * 3),
    ("reserved_2",        UINT8),
    ("reserved_3",        UINT8),
    ("allocation_length", UINT8),
    ("reserved_5",        UINT8),
    ("reserved_6",        UINT8),
    ("reserved_7",        UINT8),
    ("reserved_8",        UINT8),
    ("reserved_9",        UINT8),
    ("reserved_10",       UINT8),
    ("reserved_11",       UINT8)
  ]

class ATAPI_READ10_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",      UINT8),
    ("reserved_1",  UINT8, 5),
    ("lun",         UINT8, 3),
    ("Lba0",        UINT8),
    ("Lba1",        UINT8),
    ("Lba2",        UINT8),
    ("Lba3",        UINT8),
    ("reserved_6",  UINT8),
    ("TranLen0",    UINT8),
    ("TranLen1",    UINT8),
    ("reserved_9",  UINT8),
    ("reserved_10", UINT8),
    ("reserved_11", UINT8)
  ]

class ATAPI_READ_FORMAT_CAP_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",                UINT8),
    ("reserved_1",            UINT8 * 5),
    ("lun",                   UINT8 * 3),
    ("reserved_2",            UINT8),
    ("reserved_3",            UINT8),
    ("reserved_4",            UINT8),
    ("reserved_5",            UINT8),
    ("reserved_6",            UINT8),
    ("allocation_length_hi",  UINT8),
    ("allocation_length_lo",  UINT8),
    ("reserved_9",            UINT8),
    ("reserved_10",           UINT8),
    ("reserved_11",           UINT8)
  ]

class ATAPI_MODE_SENSE_CMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("opcode",                    UINT8),
    ("reserved_1",                UINT8, 5),
    ("lun",                       UINT8, 3),
    ("page_code",                 UINT8, 6),
    ("page_control",              UINT8, 2),
    ("reserved_3",                UINT8),
    ("reserved_4",                UINT8),
    ("reserved_5",                UINT8),
    ("reserved_6",                UINT8),
    ("parameter_list_length_hi",  UINT8),
    ("parameter_list_length_lo",  UINT8),
    ("reserved_9",                UINT8),
    ("reserved_10",               UINT8),
    ("reserved_11",               UINT8)
  ]

class ATAPI_PACKET_COMMAND (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data16",              UINT16 * 6),
    ("TestUnitReady",       ATAPI_TEST_UNIT_READY_CMD),
    ("Read10",              ATAPI_READ10_CMD),
    ("RequestSence",        ATAPI_REQUEST_SENSE_CMD),
    ("Inquiry",             ATAPI_INQUIRY_CMD),
    ("ModeSense",           ATAPI_MODE_SENSE_CMD),
    ("ReadFormatCapacity;", ATAPI_READ_FORMAT_CAP_CMD)
  ]

ATAPI_MAX_DMA_EXT_CMD_SECTORS = 0x10000
ATAPI_MAX_DMA_CMD_SECTORS     = 0x100

ATA_SIGNATURE       = 0x0101
ATAPI_SIGNATURE     = 0xeb14
ATAPI_SIGNATURE_32  = 0xeb140101

ATA_SPINUP_CFG_REQUIRED_IDD_INCOMPLETE      = 0x37c8
ATA_SPINUP_CFG_REQUIRED_IDD_COMPLETE        = 0x738c
ATA_SPINUP_CFG_NOT_REQUIRED_IDD_INCOMPLETE  = 0x8c73
ATA_SPINUP_CFG_NOT_REQUIRED_IDD_COMPLETE    = 0xc837

ATA_CMD_FORMAT_UNIT                 = 0x04
ATA_CMD_SOFT_RESET                  = 0x08
ATA_CMD_PACKET                      = 0xA0
ATA_CMD_IDENTIFY_DEVICE             = 0xA1
ATA_CMD_SERVICE                     = 0xA2
ATA_CMD_TEST_UNIT_READY             = 0x00
ATA_CMD_REQUEST_SENSE               = 0x03
ATA_CMD_INQUIRY                     = 0x12
ATA_CMD_READ_FORMAT_CAPACITY        = 0x23
ATA_CMD_READ_CAPACITY               = 0x25
ATA_CMD_READ_10                     = 0x28
ATA_CMD_WRITE_10                    = 0x2A
ATA_CMD_ATAPI_SEEK                  = 0x2B
ATA_CMD_WRITE_AND_VERIFY            = 0x2E
ATA_CMD_VERIFY                      = 0x2F
ATA_CMD_READ_12                     = 0xA8
ATA_CMD_WRITE_12                    = 0xAA
ATA_CMD_START_STOP_UNIT             = 0x1B
ATA_CMD_PREVENT_ALLOW_MEDIA_REMOVAL = 0x1E
ATA_CMD_MODE_SELECT                 = 0x55

ATA_CMD_MODE_SENSE                          = 0x5A
ATA_PAGE_CODE_READ_WRITE_ERROR              = 0x01
ATA_PAGE_CODE_CACHING_PAGE                  = 0x08
ATA_PAGE_CODE_REMOVABLE_BLOCK_CAPABILITIES  = 0x1B
ATA_PAGE_CODE_TIMER_PROTECT_PAGE            = 0x1C
ATA_PAGE_CODE_RETURN_ALL_PAGES              = 0x3F

ATA_CMD_GET_CONFIGURATION         = 0x46
ATA_GCCD_RT_FIELD_VALUE_ALL       = 0x00
ATA_GCCD_RT_FIELD_VALUE_CURRENT   = 0x01
ATA_GCCD_RT_FIELD_VALUE_SINGLE    = 0x02
ATA_GCCD_RT_FIELD_VALUE_RESERVED  = 0x03

ATA_FEATURE_LIST_PROFILE_LIST       = 0x0000
ATA_FEATURE_LIST_CORE               = 0x0001
ATA_FEATURE_LIST_MORPHING           = 0x0002
ATA_FEATURE_LIST_REMOVEABLE_MEDIUM  = 0x0003
ATA_FEATURE_LIST_WRITE_PROTECT      = 0x0004

ATA_CMD_SUBOP_STOP_DISC           = 0x00
ATA_CMD_SUBOP_START_DISC          = 0x01
ATA_CMD_SUBOP_EJECT_DISC          = 0x02
ATA_CMD_SUBOP_CLOSE_TRAY          = 0x03

ATA_CMD_IDENTIFY_DRIVE          = 0xec
ATA_CMD_READ_BUFFER             = 0xe4
ATA_CMD_READ_SECTORS            = 0x20
ATA_CMD_READ_SECTORS_WITH_RETRY = 0x21
ATA_CMD_READ_LONG               = 0x22
ATA_CMD_READ_LONG_WITH_RETRY    = 0x23
ATA_CMD_READ_SECTORS_EXT        = 0x24
ATA_CMD_READ_MULTIPLE           = 0xc4
ATA_CMD_READ_MULTIPLE_EXT       = 0x29
ATA_CMD_READ_LOG_EXT            = 0x2f

ATA_CMD_FORMAT_TRACK              = 0x50
ATA_CMD_WRITE_BUFFER              = 0xe8
ATA_CMD_WRITE_SECTORS             = 0x30
ATA_CMD_WRITE_SECTORS_WITH_RETRY  = 0x31
ATA_CMD_WRITE_LONG                = 0x32
ATA_CMD_WRITE_LONG_WITH_RETRY     = 0x33
ATA_CMD_WRITE_VERIFY              = 0x3c
ATA_CMD_WRITE_SECTORS_EXT         = 0x34
ATA_CMD_WRITE_MULTIPLE            = 0xc5
ATA_CMD_WRITE_MULTIPLE_EXT        = 0x39

ATA_CMD_ACK_MEDIA_CHANGE                = 0xdb 
ATA_CMD_BOOT_POST_BOOT                  = 0xdc
ATA_CMD_BOOT_PRE_BOOT                   = 0xdd
ATA_CMD_CHECK_POWER_MODE                = 0x98
ATA_CMD_CHECK_POWER_MODE_ALIAS          = 0xe5
ATA_CMD_DOOR_LOCK                       = 0xde
ATA_CMD_DOOR_UNLOCK                     = 0xdf
ATA_CMD_EXEC_DRIVE_DIAG                 = 0x90
ATA_CMD_IDLE_ALIAS                      = 0x97
ATA_CMD_IDLE                            = 0xe3
ATA_CMD_IDLE_IMMEDIATE                  = 0x95
ATA_CMD_IDLE_IMMEDIATE_ALIAS            = 0xe1
ATA_CMD_INIT_DRIVE_PARAM                = 0x91
ATA_CMD_RECALIBRATE                     = 0x10
ATA_CMD_READ_DRIVE_STATE                = 0xe9
ATA_CMD_SET_MULTIPLE_MODE               = 0xC6
ATA_CMD_READ_VERIFY                     = 0x40
ATA_CMD_READ_VERIFY_WITH_RETRY          = 0x41
ATA_CMD_SEEK                            = 0x70
ATA_CMD_SET_FEATURES                    = 0xef
ATA_CMD_STANDBY                         = 0x96
ATA_CMD_STANDBY_ALIAS                   = 0xe2
ATA_CMD_STANDBY_IMMEDIATE               = 0x94
ATA_CMD_STANDBY_IMMEDIATE_ALIAS         = 0xe0
ATA_CMD_SLEEP                           = 0xe6
ATA_CMD_READ_NATIVE_MAX_ADDRESS         = 0xf8
ATA_CMD_READ_NATIVE_MAX_ADDRESS_EXT     = 0x27

ATA_SUB_CMD_ENABLE_VOLATILE_WRITE_CACHE          = 0x02
ATA_SUB_CMD_SET_TRANSFER_MODE                    = 0x03
ATA_SUB_CMD_ENABLE_APM                           = 0x05
ATA_SUB_CMD_ENABLE_PUIS                          = 0x06
ATA_SUB_CMD_PUIS_SET_DEVICE_SPINUP               = 0x07
ATA_SUB_CMD_ENABLE_WRITE_READ_VERIFY             = 0x0b
ATA_SUB_CMD_ENABLE_SATA_FEATURE                  = 0x10
ATA_SUB_CMD_DISABLE_MEDIA_STATUS_NOTIFICATION    = 0x31
ATA_SUB_CMD_ENABLE_FREE_FALL_CONTROL             = 0x41
ATA_SUB_CMD_ACOUSTIC_MANAGEMENT_ENABLE           = 0x42
ATA_SUB_CMD_SET_MAX_HOST_INTERFACE_SECTOR_TIMES  = 0x43
ATA_SUB_CMD_EXTENDED_POWER_CONDITIONS            = 0x4a
ATA_SUB_CMD_DISABLE_READ_LOOK_AHEAD              = 0x55
ATA_SUB_CMD_EN_DIS_DSN_FEATURE                   = 0x63
ATA_SUB_CMD_DISABLE_REVERT_TO_POWER_ON_DEFAULTS  = 0x66
ATA_SUB_CMD_DISABLE_VOLATILE_WRITE_CACHE         = 0x82
ATA_SUB_CMD_DISABLE_APM                          = 0x85
ATA_SUB_CMD_DISABLE_PUIS                         = 0x86
ATA_SUB_CMD_DISABLE_WRITE_READ_VERIFY            = 0x8b
ATA_SUB_CMD_DISABLE_SATA_FEATURE                 = 0x90
ATA_SUB_CMD_ENABLE_MEDIA_STATUS_NOTIFICATION     = 0x95
ATA_SUB_CMD_ENABLE_READ_LOOK_AHEAD               = 0xaa
ATA_SUB_CMD_DISABLE_FREE_FALL_CONTROL            = 0xc1
ATA_SUB_CMD_ACOUSTIC_MANAGEMENT_DISABLE          = 0xc2
ATA_SUB_CMD_EN_DIS_SENSE_DATA_REPORTING          = 0xc3
ATA_SUB_CMD_ENABLE_REVERT_TO_POWER_ON_DEFAULTS   = 0xcc

ATA_CMD_SMART               = 0xb0
ATA_CONSTANT_C2             = 0xc2
ATA_CONSTANT_4F             = 0x4f
ATA_SMART_READ_DATA  = 0xd0

ATA_SMART_AUTOSAVE         = 0xd2
ATA_AUTOSAVE_DISABLE_ATTR  = 0x00
ATA_AUTOSAVE_ENABLE_ATTR   = 0xf1

ATA_SMART_EXECUTE_OFFLINE_IMMEDIATE            = 0xd4
ATA_EXECUTE_SMART_OFFLINE_ROUTINE              = 0x00
ATA_EXECUTE_SMART_OFFLINE_SHORT_SELFTEST       = 0x01
ATA_EXECUTE_SMART_OFFLINE_EXTENDED_SELFTEST    = 0x02
ATA_EXECUTE_SMART_OFFLINE_CONVEYANCE_SELFTEST  = 0x03
ATA_EXECUTE_SMART_OFFLINE_SELECTIVE_SELFTEST   = 0x04
ATA_SMART_ABORT_SELF_TEST_SUBROUTINE           = 0x7f
ATA_EXECUTE_SMART_CAPTIVE_SHORT_SELFTEST       = 0x81
ATA_EXECUTE_SMART_CAPTIVE_EXTENDED_SELFTEST    = 0x82
ATA_EXECUTE_SMART_CAPTIVE_CONVEYANCE_SELFTEST  = 0x83
ATA_EXECUTE_SMART_CAPTIVE_SELECTIVE_SELFTEST   = 0x84

ATA_SMART_READLOG           = 0xd5
ATA_SMART_WRITELOG          = 0xd6
ATA_SMART_ENABLE_OPERATION  = 0xd8
ATA_SMART_DISABLE_OPERATION = 0xd9
ATA_SMART_RETURN_STATUS     = 0xda

ATA_SMART_THRESHOLD_NOT_EXCEEDED_VALUE  = 0xc24f
ATA_SMART_THRESHOLD_EXCEEDED_VALUE      = 0x2cf4

ATA_SMART_LOG_DIRECTORY             = 0x00
ATA_SMART_SUM_SMART_ERROR_LOG       = 0x01
ATA_SMART_COMP_SMART_ERROR_LOG      = 0x02
ATA_SMART_EXT_COMP_SMART_ERROR_LOG  = 0x03
ATA_SMART_SMART_SELFTEST_LOG        = 0x06
ATA_SMART_EXT_SMART_SELFTEST_LOG    = 0x07
ATA_SMART_SELECTIVE_SELFTEST_LOG    = 0x09
ATA_SMART_HOST_VENDOR_SPECIFIC      = 0x80
ATA_SMART_DEVICE_VENDOR_SPECIFIC    = 0xa0

ATA_CMD_READ_DMA              = 0xc8
ATA_CMD_READ_DMA_WITH_RETRY   = 0xc9
ATA_CMD_READ_DMA_EXT          = 0x25
ATA_CMD_WRITE_DMA             = 0xca
ATA_CMD_WRITE_DMA_WITH_RETRY  = 0xcb
ATA_CMD_WRITE_DMA_EXT         = 0x35

ATA_CMD_SECURITY_SET_PASSWORD      = 0xf1
ATA_CMD_SECURITY_UNLOCK            = 0xf2
ATA_CMD_SECURITY_ERASE_PREPARE     = 0xf3
ATA_CMD_SECURITY_ERASE_UNIT        = 0xf4
ATA_CMD_SECURITY_FREEZE_LOCK       = 0xf5
ATA_CMD_SECURITY_DISABLE_PASSWORD  = 0xf6

ATA_SECURITY_BUFFER_LENGTH  = 512

ATA_CMD_DEV_CONFIG_OVERLAY             = 0xb1
ATA_CMD_DEV_CONFIG_RESTORE_FEATURE     = 0xc0
ATA_CMD_DEV_CONFIG_FREEZELOCK_FEATURE  = 0xc1
ATA_CMD_DEV_CONFIG_IDENTIFY_FEATURE    = 0xc2
ATA_CMD_DEV_CONFIG_SET_FEATURE         = 0xc3

ATA_CMD_TRUSTED_NON_DATA     = 0x5b
ATA_CMD_TRUSTED_RECEIVE      = 0x5c
ATA_CMD_TRUSTED_RECEIVE_DMA  = 0x5d
ATA_CMD_TRUSTED_SEND         = 0x5e
ATA_CMD_TRUSTED_SEND_DMA     = 0x5f

ATA_TR_RETURN_SECURITY_PROTOCOL_INFORMATION  = 0x00
ATA_TR_SECURITY_PROTOCOL_JEDEC_RESERVED      = 0xec
ATA_TR_SECURITY_PROTOCOL_SDCARD_RESERVED     = 0xed
ATA_TR_SECURITY_PROTOCOL_IEEE1667_RESERVED   = 0xee

ATA_ACOUSTIC_LEVEL_BYPASS               = 0xff
ATA_ACOUSTIC_LEVEL_MAXIMUM_PERFORMANCE  = 0xfe
ATA_ACOUSTIC_LEVEL_QUIET                = 0x80

ATA_CMD_DIPM_SUB  = 0x03
ATA_DIPM_ENABLE   = 0x10
ATA_DIPM_DISABLE  = 0x90

ATA_CMD_DEVSLEEP_SUB  = 0x09
ATA_DEVSLEEP_ENABLE   = 0x10
ATA_DEVSLEEP_DISABLE  = 0x90

ATA_DEVSLP_EXIT_TIMEOUT            = 20
ATA_DEVSLP_MINIMUM_DETECTION_TIME  = 10
ATA_DEVSLP_MINIMUM_ASSERTION_TIME  = 10

ATA_CMD_SET_MAX_ADDRESS_EXT  = 0x37
ATA_CMD_SET_MAX_ADDRESS      = 0xf9
ATA_SET_MAX_SET_PASSWORD     = 0x01
ATA_SET_MAX_LOCK             = 0x02
ATA_SET_MAX_UNLOCK           = 0x03
ATA_SET_MAX_FREEZE_LOCK      = 0x04

ATA_DEFAULT_CTL           = 0x0a

ATA_DEFAULT_CMD           = 0xa0

ATAPI_MAX_BYTE_COUNT  = 0xfffe

ATA_REQUEST_SENSE_ERROR = 0x70

ATA_SK_NO_SENSE         = 0x0
ATA_SK_RECOVERY_ERROR   = 0x1
ATA_SK_NOT_READY        = 0x2
ATA_SK_MEDIUM_ERROR     = 0x3
ATA_SK_HARDWARE_ERROR   = 0x4
ATA_SK_ILLEGAL_REQUEST  = 0x5
ATA_SK_UNIT_ATTENTION   = 0x6
ATA_SK_DATA_PROTECT     = 0x7
ATA_SK_BLANK_CHECK      = 0x8
ATA_SK_VENDOR_SPECIFIC  = 0x9
ATA_SK_RESERVED_A       = 0xA
ATA_SK_ABORT            = 0xB
ATA_SK_RESERVED_C       = 0xC
ATA_SK_OVERFLOW         = 0xD
ATA_SK_MISCOMPARE       = 0xE
ATA_SK_RESERVED_F       = 0xF

ATA_ASC_NOT_READY                   = 0x04
ATA_ASC_MEDIA_ERR1                  = 0x10
ATA_ASC_MEDIA_ERR2                  = 0x11
ATA_ASC_MEDIA_ERR3                  = 0x14
ATA_ASC_MEDIA_ERR4                  = 0x30
ATA_ASC_MEDIA_UPSIDE_DOWN           = 0x06
ATA_ASC_INVALID_CMD                 = 0x20
ATA_ASC_LBA_OUT_OF_RANGE            = 0x21
ATA_ASC_INVALID_FIELD               = 0x24
ATA_ASC_WRITE_PROTECTED             = 0x27
ATA_ASC_MEDIA_CHANGE                = 0x28
ATA_ASC_RESET                       = 0x29
ATA_ASC_ILLEGAL_FIELD               = 0x26
ATA_ASC_NO_MEDIA                    = 0x3A
ATA_ASC_ILLEGAL_MODE_FOR_THIS_TRACK = 0x64

ATA_ASCQ_IN_PROGRESS  = 0x01

ATA_ERRREG_BBK   = BIT7
ATA_ERRREG_UNC   = BIT6
ATA_ERRREG_MC    = BIT5
ATA_ERRREG_IDNF  = BIT4
ATA_ERRREG_MCR   = BIT3
ATA_ERRREG_ABRT  = BIT2
ATA_ERRREG_TK0NF = BIT1
ATA_ERRREG_AMNF  = BIT0

ATA_STSREG_BSY   = BIT7
ATA_STSREG_DRDY  = BIT6
ATA_STSREG_DWF   = BIT5
ATA_STSREG_DF    = BIT5
ATA_STSREG_DSC   = BIT4
ATA_STSREG_DRQ   = BIT3
ATA_STSREG_CORR  = BIT2
ATA_STSREG_IDX   = BIT1
ATA_STSREG_ERR   = BIT0

ATA_CTLREG_SRST  = BIT2
ATA_CTLREG_IEN_L = BIT1

