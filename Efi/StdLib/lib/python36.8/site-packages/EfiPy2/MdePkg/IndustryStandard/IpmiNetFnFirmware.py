# IpmiNetFnFirmware.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnFirmware
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

IPMI_NETFN_FIRMWARE  = 0x08

IPMI_GET_BMC_EXECUTION_CONTEXT  = 0x23

class IPMI_MSG_GET_BMC_EXEC_RSP (Structure):
  _fields_ = [
    ("CurrentExecutionContext", UINT8),
    ("PartitionPointer",        UINT8)
  ]

IPMI_BMC_IN_FORCED_UPDATE_MODE  = 0x11
