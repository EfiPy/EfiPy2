# SdramSpd.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpd
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import SdramSpdDdr3, SdramSpdDdr4, SdramSpdLpDdr

SPD_MEMORY_TYPE                 = 2
SPD_SDRAM_ROW_ADDR              = 3
SPD_SDRAM_COL_ADDR              = 4
SPD_SDRAM_MODULE_ROWS           = 5
SPD_SDRAM_MODULE_DATA_WIDTH_LSB = 6
SPD_SDRAM_MODULE_DATA_WIDTH_MSB = 7
SPD_SDRAM_ECC_SUPPORT           = 11
SPD_SDRAM_REFRESH               = 12
SPD_SDRAM_WIDTH                 = 13
SPD_SDRAM_ERROR_WIDTH           = 14
SPD_SDRAM_BURST_LENGTH          = 16
SPD_SDRAM_NO_OF_BANKS           = 17
SPD_SDRAM_CAS_LATENCY           = 18
SPD_SDRAM_MODULE_ATTR           = 21

SPD_SDRAM_TCLK1_PULSE           = 9
SPD_SDRAM_TAC1_PULSE            = 10
SPD_SDRAM_TCLK2_PULSE           = 23
SPD_SDRAM_TAC2_PULSE            = 24
SPD_SDRAM_TCLK3_PULSE           = 25
SPD_SDRAM_TAC3_PULSE            = 26
SPD_SDRAM_MIN_PRECHARGE         = 27
SPD_SDRAM_ACTIVE_MIN            = 28
SPD_SDRAM_RAS_CAS               = 29
SPD_SDRAM_RAS_PULSE             = 30
SPD_SDRAM_DENSITY               = 31

SPD_VAL_SDR_TYPE    = 4
SPD_VAL_DDR_TYPE    = 7
SPD_VAL_DDR2_TYPE   = 8
SPD_VAL_DDR3_TYPE   = 11
SPD_VAL_DDR4_TYPE   = 12
SPD_VAL_LPDDR3_TYPE = 15
SPD_VAL_LPDDR4_TYPE = 16

SPD_ECC_TYPE_NONE    = 0x00
SPD_ECC_TYPE_PARITY  = 0x01
SPD_ECC_TYPE_ECC     = 0x02

SPD_BUFFERED    = 0x01
SPD_REGISTERED  = 0x02

