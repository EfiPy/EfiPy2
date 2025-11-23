# RestEx.py
#
# EfiPy2.MdePkg.Protocol.RestEx
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.Http import EFI_HTTP_MESSAGE, EFI_HTTP_CONFIG_DATA

gEfiRestExServiceBindingProtocolGuid           = \
  EFI_GUID (0x456bbe01, 0x99d0, 0x45ea, (0xbb, 0x5f, 0x16, 0xd8, 0x4b, 0xed, 0xc5, 0x59 ))

gEfiRestExProtocolGuid           = \
  EFI_GUID (0x55648b91, 0xe7d, 0x40a3, (0xa9, 0xb3, 0xa8, 0x15, 0xd7, 0xea, 0xdf, 0x97 ))

class EFI_REST_EX_PROTOCOL (Structure):
  pass

class EFI_REST_EX_SERVICE_INFO_VER (Structure):
  _fields_ = [
    ("Major", UINT8),
    ("Minor", UINT8)
  ]

class EFI_REST_EX_SERVICE_INFO_HEADER (Structure):
  _fields_ = [
    ("Length",              UINT32),
    ("RestServiceInfoVer",  EFI_REST_EX_SERVICE_INFO_VER)
  ]

EfiRestExServiceUnspecific  = 1
EfiRestExServiceRedfish     = 2
EfiRestExServiceOdata       = 2
EfiRestExServiceVendorSpecific = 0xff
EfiRestExServiceTypeMax        = 0x100
EFI_REST_EX_SERVICE_TYPE       = ENUM

EfiRestExServiceInBandAccess    = 1
EfiRestExServiceOutOfBandAccess = 2
EfiRestExServiceModeMax         = 3
EFI_REST_EX_SERVICE_ACCESS_MODE = ENUM

EfiRestExConfigHttp         = 1
EfiRestExConfigUnspecific   = 2
EfiRestExConfigTypeMax      = 3
EFI_REST_EX_CONFIG_TYPE     = ENUM

class EFI_REST_EX_SERVICE_INFO_V_1_0 (Structure):
  _fields_ = [
    ("EfiRestExServiceInfoHeader",  EFI_REST_EX_SERVICE_INFO_HEADER),
    ("RestServiceType",             EFI_REST_EX_SERVICE_TYPE),
    ("RestServiceAccessMode",       EFI_REST_EX_SERVICE_ACCESS_MODE),
    ("VendorRestServiceName",       EFI_GUID),
    ("VendorSpecificDataLength",    UINT32),
    ("VendorSpecifcData",           POINTER(UINT8)),
    ("RestExConfigType",            EFI_REST_EX_CONFIG_TYPE),
    ("RestExConfigDataLength",      UINT8)
  ]

class EFI_REST_EX_SERVICE_INFO (Union):
  _fields_ = [
    ("EfiRestExServiceInfoHeader",  EFI_REST_EX_SERVICE_INFO_HEADER),
    ("EfiRestExServiceInfoV10",     EFI_REST_EX_SERVICE_INFO_V_1_0)
  ]

class EFI_REST_EX_HTTP_CONFIG_DATA (Structure):
  _fields_ = [
    ("HttpConfigData",      EFI_HTTP_CONFIG_DATA),
    ("SendReceiveTimeout",  UINT32)
  ]

EFI_REST_EX_CONFIG_DATA = POINTER(UINT8)

class EFI_REST_EX_TOKEN (Structure):
  _fields_ = [
    ("Event",           EFI_EVENT),
    ("Status",          EFI_STATUS),
    ("ResponseMessage", POINTER(EFI_HTTP_MESSAGE))
  ]

EFI_REST_SEND_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    # IN    *This,
  POINTER(EFI_HTTP_MESSAGE),        # IN    *RequestMessage,
  POINTER(EFI_HTTP_MESSAGE)         # OUT   *ResponseMessage
  )

EFI_REST_GET_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    # IN    *This,
  POINTER(EFI_TIME)                 # OUT   *Time
  )

EFI_REST_EX_GET_SERVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),                # IN    *This,
  POINTER(POINTER(EFI_REST_EX_SERVICE_INFO))    # OUT   **RestExServiceInfo
  )

EFI_REST_EX_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    # IN    *This,
  POINTER(EFI_REST_EX_SERVICE_INFO) # OUT   *RestExConfigData
  )

EFI_REST_EX_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    # IN    *This,
  EFI_REST_EX_CONFIG_DATA           # IN    RestExConfigData
  )

EFI_REST_EX_ASYNC_SEND_RECEIVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    #   IN    *This,
  POINTER(EFI_HTTP_MESSAGE),        #   IN    *RequestMessage OPTIONAL,
  POINTER(EFI_REST_EX_TOKEN),       #   IN    *RestExToken,
  POINTER(UINTN)                    #   IN    *TimeOutInMilliSeconds OPTIONAL
  )

EFI_REST_EX_EVENT_SERVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_EX_PROTOCOL),    #   IN    *This,
  POINTER(EFI_HTTP_MESSAGE),        #   IN    *RequestMessage OPTIONAL,
  POINTER(EFI_REST_EX_TOKEN)        #   IN    *RestExToken
  )

EFI_REST_EX_PROTOCOL._fields_ = [
    ("SendReceive",     EFI_REST_SEND_RECEIVE),
    ("GetServiceTime",  EFI_REST_GET_TIME),
    ("GetService",      EFI_REST_EX_GET_SERVICE),
    ("GetModeData",     EFI_REST_EX_GET_MODE_DATA),
    ("Configure",       EFI_REST_EX_CONFIGURE),
    ("AyncSendReceive", EFI_REST_EX_ASYNC_SEND_RECEIVE),
    ("EventService",    EFI_REST_EX_EVENT_SERVICE)
  ]

