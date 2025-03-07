# Pldm.py
#
# EfiPy2.MdePkg.IndustryStandard.Pldm
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

PLDM_MESSAGE_HEADER_VERSION  = 0

class PLDM_MESSAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InstanceId",          UINT8, 5),
    ("Reserved",            UINT8, 1),
    ("DatagramBit",         UINT8, 1),
    ("RequestBit",          UINT8, 1),
    ("PldmType",            UINT8, 6),
    ("HeaderVersion",       UINT8, 2),
    ("PldmTypeCommandCode", UINT8)
    ]

PLDM_REQUEST_HEADER = PLDM_MESSAGE_HEADER

PLDM_MESSAGE_HEADER_IS_REQUEST        = 1
PLDM_MESSAGE_HEADER_IS_RESPONSE       = 0
PLDM_MESSAGE_HEADER_IS_DATAGRAM       = 1
PLDM_MESSAGE_HEADER_INSTANCE_ID_MASK  = 0x1f

class PLDM_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PldmHeader",          PLDM_MESSAGE_HEADER),
    ("PldmCompletionCode",  UINT8)
  ]

PLDM_HEADER_VERSION  = 0x00

PLDM_COMPLETION_CODE_SUCCESS                     = 0x00
PLDM_COMPLETION_CODE_ERROR                       = 0x01
PLDM_COMPLETION_CODE_ERROR_INVALID_DATA          = 0x02
PLDM_COMPLETION_CODE_ERROR_INVALID_LENGTH        = 0x03
PLDM_COMPLETION_CODE_ERROR_NOT_READY             = 0x04
PLDM_COMPLETION_CODE_ERROR_UNSUPPORTED_PLDM_CMD  = 0x05
PLDM_COMPLETION_CODE_ERROR_INVALID_PLDM_TYPE     = 0x20
PLDM_COMPLETION_CODE_SPECIFIC_START              = 0x80
PLDM_COMPLETION_CODE_SPECIFIC_END                = 0xff

PLDM_TYPE_MESSAGE_CONTROL_AND_DISCOVERY    = 0x00
PLDM_TYPE_SMBIOS                           = 0x01
PLDM_TYPE_PLATFORM_MONITORING_AND_CONTROL  = 0x02
PLDM_TYPE_BIOS_CONTROL_AND_CONFIGURATION   = 0x03

PLDM_TRANSFER_FLAG_START          = 0x01
PLDM_TRANSFER_FLAG_MIDDLE         = 0x02
PLDM_TRANSFER_FLAG_END            = 0x04
PLDM_TRANSFER_FLAG_START_AND_END  = 0x05

PLDM_TRANSFER_OPERATION_FLAG_GET_NEXT_PART   = 0x00
PLDM_TRANSFER_OPERATION_FLAG_GET_FIRST_PART  = 0x01

