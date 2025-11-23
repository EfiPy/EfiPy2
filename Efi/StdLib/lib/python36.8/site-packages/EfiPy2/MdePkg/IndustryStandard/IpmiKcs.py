# IpmiKcs.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiKcs
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import *

IPMI_KCS_STATUS_REGISTER_OFFSET    = 1
IPMI_KCS_COMMAND_REGISTER_OFFSET   = 1
IPMI_KCS_DATA_OUT_REGISTER_OFFSET  = 0
IPMI_KCS_DATA_IN_REGISTER_OFFSET   = 0

IPMI_KCS_OBF           = BIT0
IPMI_KCS_IBF           = BIT1
IPMI_KCS_SMS_ATN       = BIT2
IPMI_KCS_COMMAND_DATA  = BIT3
IPMI_KCS_OEM1          = BIT4
IPMI_KCS_OEM2          = BIT5
IPMI_KCS_S0            = BIT6
IPMI_KCS_S1            = BIT7

IPMI_KCS_CONTROL_CODE_GET_STATUS_ABORT  = 0x60
IPMI_KCS_CONTROL_CODE_WRITE_START       = 0x61
IPMI_KCS_CONTROL_CODE_WRITE_END         = 0x62
IPMI_KCS_CONTROL_CODE_READ              = 0x68

IPMI_KCS_STATUS_NO_ERROR      = 0x00
IPMI_KCS_STATUS_ABORT         = 0x01
IPMI_KCS_STATUS_ILLEGAL       = 0x02
IPMI_KCS_STATUS_LENGTH_ERROR  = 0x06
IPMI_KCS_STATUS_UNSPECIFIED   = 0xFF

IpmiKcsIdleState  = 0
IpmiKcsReadState  = 1
IpmiKcsWriteState = 2
IpmiKcsErrorState = 3
IPMI_KCS_STATE = ENUM

class IPMI_KCS_REQUEST_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NetFunc", UINT8),
    ("Command", UINT8),
    ("Data",    UINT8 * 1)
    ]

class IPMI_KCS_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NetFunc", UINT8),
    ("Command", UINT8)
    ]
