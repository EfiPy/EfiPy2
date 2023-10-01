# IpmiNetFnSensorEvent.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnSensorEvent
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

IPMI_NETFN_SENSOR_EVENT = 0x04

IPMI_SENSOR_PLATFORM_EVENT_MESSAGE   = 0x02

class IPMI_PLATFORM_EVENT_MESSAGE_DATA_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("GeneratorId",  UINT8),
    ("EvMRevision",  UINT8),
    ("SensorType",   UINT8),
    ("SensorNumber", UINT8),
    ("EventDirType", UINT8),
    ("OEMEvData1",   UINT8),
    ("OEMEvData2",   UINT8),
    ("OEMEvData3",   UINT8)
  ]
