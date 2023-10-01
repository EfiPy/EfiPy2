# Http.py
#
# EfiPy2.MdePkg.Protocol.Http
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiHttpServiceBindingProtocolGuid  = \
  EFI_GUID (0xbdc8e6af, 0xd9bc, 0x4379, (0xa7, 0x2a, 0xe0, 0xc4, 0xe7, 0x5d, 0xae, 0x1c ))

gEfiHttpProtocolGuid                = \
  EFI_GUID (0x7a59b29b, 0x910b, 0x4171, (0x82, 0x42, 0xa8, 0x5a, 0x0d, 0xf2, 0x5b, 0x5b ))

class EFI_HTTP_PROTOCOL (Structure):
  pass

HttpVersion10           = 0
HttpVersion11           = 1
HttpVersionUnsupported  = 2
EFI_HTTP_VERSION        = ENUM

HttpMethodGet     = 0
HttpMethodPost    = 1
HttpMethodPatch   = 2
HttpMethodOptions = 3
HttpMethodConnect = 4
HttpMethodHead    = 5
HttpMethodPut     = 6
HttpMethodDelete  = 7
HttpMethodTrace   = 8
HttpMethodMax     = 9
EFI_HTTP_METHOD   = ENUM

HTTP_STATUS_UNSUPPORTED_STATUS                  = 0
HTTP_STATUS_100_CONTINUE                        = 1
HTTP_STATUS_101_SWITCHING_PROTOCOLS             = 2
HTTP_STATUS_200_OK                              = 3
HTTP_STATUS_201_CREATED                         = 4
HTTP_STATUS_202_ACCEPTED                        = 5
HTTP_STATUS_203_NON_AUTHORITATIVE_INFORMATION   = 6
HTTP_STATUS_204_NO_CONTENT                      = 7
HTTP_STATUS_205_RESET_CONTENT                   = 8
HTTP_STATUS_206_PARTIAL_CONTENT                 = 9
HTTP_STATUS_300_MULTIPLE_CHIOCES                = 10
HTTP_STATUS_301_MOVED_PERMANENTLY               = 11
HTTP_STATUS_302_FOUND                           = 12
HTTP_STATUS_303_SEE_OTHER                       = 13
HTTP_STATUS_304_NOT_MODIFIED                    = 14
HTTP_STATUS_305_USE_PROXY                       = 15
HTTP_STATUS_307_TEMPORARY_REDIRECT              = 16
HTTP_STATUS_400_BAD_REQUEST                     = 17
HTTP_STATUS_401_UNAUTHORIZED                    = 18
HTTP_STATUS_402_PAYMENT_REQUIRED                = 19
HTTP_STATUS_403_FORBIDDEN                       = 20
HTTP_STATUS_404_NOT_FOUND                       = 21
HTTP_STATUS_405_METHOD_NOT_ALLOWED              = 22
HTTP_STATUS_406_NOT_ACCEPTABLE                  = 23
HTTP_STATUS_407_PROXY_AUTHENTICATION_REQUIRED   = 24
HTTP_STATUS_408_REQUEST_TIME_OUT                = 25
HTTP_STATUS_409_CONFLICT                        = 26
HTTP_STATUS_410_GONE                            = 27
HTTP_STATUS_411_LENGTH_REQUIRED                 = 28
HTTP_STATUS_412_PRECONDITION_FAILED             = 29
HTTP_STATUS_413_REQUEST_ENTITY_TOO_LARGE        = 30
HTTP_STATUS_414_REQUEST_URI_TOO_LARGE           = 31
HTTP_STATUS_415_UNSUPPORETD_MEDIA_TYPE          = 32
HTTP_STATUS_416_REQUESTED_RANGE_NOT_SATISFIED   = 33
HTTP_STATUS_417_EXPECTATION_FAILED              = 34
HTTP_STATUS_500_INTERNAL_SERVER_ERROR           = 35
HTTP_STATUS_501_NOT_IMIPLEMENTED                = 36
HTTP_STATUS_502_BAD_GATEWAY                     = 37
HTTP_STATUS_503_SERVICE_UNAVAILABLE             = 38
HTTP_STATUS_504_GATEWAY_TIME_OUT                = 39
HTTP_STATUS_505_HTTP_VERSION_NOT_SUPPORTED      = 40
HTTP_STATUS_308_PERMANENT_REDIRECT              = 41
EFI_HTTP_STATUS_CODE                            = ENUM

class EFI_HTTPv4_ACCESS_POINT (Structure):
  _fields_ = [
    ("UseDefaultAddress", BOOLEAN),
    ("LocalAddress",      EFI_IPv4_ADDRESS),
    ("LocalSubnet",       EFI_IPv4_ADDRESS),
    ("LocalPort",         UINT16)
  ]

class EFI_HTTPv6_ACCESS_POINT (Structure):
  _fields_ = [
    ("LocalAddress", EFI_IPv6_ADDRESS),
    ("LocalPort",    UINT16)
  ]

class EFI_HTTP_CONFIG_DATA_AccessPoint (Union):
  _fields_ = [
    ("IPv4Node",  POINTER(EFI_HTTPv4_ACCESS_POINT)),
    ("IPv6Node",  POINTER(EFI_HTTPv6_ACCESS_POINT))
  ]

class EFI_HTTP_CONFIG_DATA (Structure):
  _fields_ = [
    ("HttpVersion",         EFI_HTTP_VERSION),
    ("TimeOutMillisec",     UINT32),
    ("LocalAddressIsIPv6",  BOOLEAN),
    ("AccessPoint",         EFI_HTTP_CONFIG_DATA_AccessPoint)
  ]

class EFI_HTTP_REQUEST_DATA (Structure):
  _fields_ = [
    ("Method",  EFI_HTTP_METHOD),
    ("Url",     PCHAR16)
  ]

class EFI_HTTP_RESPONSE_DATA (Structure):
  _fields_ = [
    ("StatusCode",  EFI_HTTP_STATUS_CODE)
  ]

class EFI_HTTP_HEADER (Structure):
  _fields_ = [
    ("FieldName",   PCHAR8),
    ("FieldValue",  PCHAR8)
  ]

class EFI_HTTP_MESSAGE_Data (Union):
  _fields_ = [
    ("Request",   POINTER(EFI_HTTP_REQUEST_DATA)),
    ("Response",  POINTER(EFI_HTTP_RESPONSE_DATA))
  ]

class EFI_HTTP_MESSAGE (Structure):
  _fields_ = [
    ("Data",        EFI_HTTP_MESSAGE_Data),
    ("HeaderCount", UINTN),
    ("Headers",     POINTER(EFI_HTTP_HEADER)),
    ("BodyLength",  UINTN),
    ("Body",        PVOID)
  ]

class EFI_HTTP_TOKEN (Structure):
  _fields_ = [
    ("Event",    EFI_EVENT),
    ("Status",   EFI_STATUS),
    ("Message",  POINTER(EFI_HTTP_MESSAGE))
  ]

EFI_HTTP_GET_MODE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL),     # IN CONST  *This,
  POINTER(EFI_HTTP_CONFIG_DATA)   # OUT       *HttpConfigData
  )

EFI_HTTP_CONFIGURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL),     # IN *This,
  POINTER(EFI_HTTP_CONFIG_DATA)   # IN *HttpConfigData
  )

EFI_HTTP_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL), # IN *This,
  POINTER(EFI_HTTP_TOKEN)     # IN *Token
  )

EFI_HTTP_CANCEL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL), # IN *This,
  POINTER(EFI_HTTP_TOKEN)     # IN *Token
  )

EFI_HTTP_RESPONSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL), # IN *This,
  POINTER(EFI_HTTP_TOKEN)     # IN *Token
  )

EFI_HTTP_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HTTP_PROTOCOL)  # IN *This,
  )

EFI_HTTP_PROTOCOL._fields_ = [
    ("GetModeData", EFI_HTTP_GET_MODE_DATA),
    ("Configure",   EFI_HTTP_CONFIGURE),
    ("Request",     EFI_HTTP_REQUEST),
    ("Cancel",      EFI_HTTP_CANCEL),
    ("Response",    EFI_HTTP_RESPONSE),
    ("Poll",        EFI_HTTP_POLL)
  ]

