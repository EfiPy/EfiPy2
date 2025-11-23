# IpmiNetFnSensorEvent.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnSensorEvent
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2025 MaxWu efipy.core@gmail.com
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
IPMI_SENSOR_SET_SENSOR_THRESHOLDS  = 0x26

class SENSOR_BITS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LowerNonCriticalThreshold",     UINT8, 1),
    ("LowerCriticalThreshold",        UINT8, 1),
    ("LowerNonRecoverableThreshold",  UINT8, 1),
    ("UpperNonCriticalThreshold",     UINT8, 1),
    ("UpperCriticalThreshold",        UINT8, 1),
    ("UpperNonRecoverableThreshold",  UINT8, 1),
    ("Reserved",                      UINT8, 2)
  ]

class SENSOR_BITS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",  SENSOR_BITS_Bits),
    ("Uint8", UINT8)
  ]

class IPMI_SENSOR_SET_SENSOR_THRESHOLD_REQUEST_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SensorNumber",                  UINT8),
    ("SetBitEnable",                  SENSOR_BITS),
    ("LowerNonCriticalThreshold",     UINT8),
    ("LowerCriticalThreshold",        UINT8),
    ("LowerNonRecoverableThreshold",  UINT8),
    ("UpperNonCriticalThreshold",     UINT8),
    ("UpperCriticalThreshold",        UINT8),
    ("UpperNonRecoverableThreshold",  UINT8)
  ]

IPMI_SENSOR_GET_SENSOR_THRESHOLDS  = 0x27

class IPMI_SENSOR_GET_SENSOR_THRESHOLD_RESPONSE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("GetBitEnable",                SENSOR_BITS),
    ("LowerNonCriticalThreshold",   UINT8),
    ("LowerCriticalThreshold",      UINT8),
    ("LowerNonRecoverableThreshold",UINT8),
    ("UpperNonCriticalThreshold",   UINT8),
    ("UpperCriticalThreshold",      UINT8),
    ("UpperNonRecoverableThreshold",UINT8)
  ]

