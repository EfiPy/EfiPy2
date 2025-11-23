# TpmTis.py
#
# EfiPy2.MdePkg.IndustryStandard.TpmTis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class TIS_PC_REGISTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Access",            UINT8),
    ("Reserved1",         UINT8 * 7),
    ("IntEnable",         UINT32),
    ("IntVector",         UINT8),
    ("Reserved2",         UINT8 * 3),
    ("IntSts",            UINT32),
    ("IntfCapability",    UINT32),
    ("Status",            UINT8),
    ("BurstCount",        UINT16),
    ("Reserved3",         UINT8 * 9),
    ("DataFifo",          UINT32),
    ("Reserved4",         UINT8 * 0xed8),
    ("Vid",               UINT16),
    ("Did",               UINT16),
    ("Rid",               UINT8),
    ("Reserved",          UINT8 * 0x7b),
    ("LegacyAddress1",    UINT32),
    ("LegacyAddress1Ex",  UINT32),
    ("LegacyAddress2",    UINT32),
    ("LegacyAddress2Ex",  UINT32),
    ("VendorDefined",     UINT8 * 0x70)
  ]

TIS_PC_ACC_ACTIVE           = BIT5
TIS_PC_ACC_SEIZED           = BIT4
TIS_PC_ACC_SEIZE            = BIT3
TIS_PC_ACC_PENDIND          = BIT2
TIS_PC_ACC_RQUUSE           = BIT1
TIS_PC_ACC_ESTABLISH        = BIT0

TIS_PC_STS_VALID            = BIT7
TIS_PC_STS_READY            = BIT6
TIS_PC_STS_GO               = BIT5
TIS_PC_STS_DATA             = BIT4
TIS_PC_STS_EXPECT           = BIT3
TIS_PC_STS_SELFTEST_DONE    = BIT2
TIS_PC_STS_RETRY            = BIT1

TIS_TIMEOUT_A               = (750  * 1000)
TIS_TIMEOUT_B               = (2000 * 1000)
TIS_TIMEOUT_C               = (750  * 1000)
TIS_TIMEOUT_D               = (750  * 1000)

