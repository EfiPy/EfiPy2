# WiFi.py
#
# EfiPy2.MdePkg.Protocol.WiFi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.WiFi2 import EFI_80211_MAC_ADDRESS, EFI_80211_BSS_TYPE

gEfiWiFiProtocolGuid  = \
  EFI_GUID (0xda55bc9, 0x45f8, 0x4bb4, (0x87, 0x19, 0x52, 0x24, 0xf1, 0x8a, 0x4d, 0x45 ))

class EFI_WIRELESS_MAC_CONNECTION_PROTOCOL (Structure):
  pass

IeeePrivate           = 0
IeeePrivatewithGuest  = 1
IeeeChargeablePublic  = 2
IeeeFreePublic        = 3
IeeePersonal          = 4
IeeeEmergencyServOnly = 5
IeeeTestOrExp         = 14
IeeeWildcard          = 15
EFI_80211_ACC_NET_TYPE = ENUM

AssociateSuccess                                = 0
AssociateRefusedReasonUnspecified               = 1
AssociateRefusedCapsMismatch                    = 2
AssociateRefusedExtReason                       = 3
AssociateRefusedAPOutOfMemory                   = 4
AssociateRefusedBasicRatesMismatch              = 5
AssociateRejectedEmergencyServicesNotSupported  = 6
AssociateRefusedTemporarily                     = 7
EFI_80211_ASSOCIATE_RESULT_CODE                 = ENUM

ScanSuccess                 = 0
ScanNotSupported            = 1
EFI_80211_SCAN_RESULT_CODE  = ENUM

Ieee80211UnspecifiedReason           = 1
Ieee80211PreviousAuthenticateInvalid = 2
Ieee80211DeauthenticatedSinceLeaving = 3
Ieee80211DisassociatedDueToInactive  = 4
Ieee80211DisassociatedSinceApUnable  = 5
Ieee80211Class2FrameNonauthenticated = 6
Ieee80211Class3FrameNonassociated    = 7
Ieee80211DisassociatedSinceLeaving   = 8
EFI_80211_REASON_CODE                = ENUM

DisassociateSuccess                 = 0
DisassociateInvalidParameters       = 1
EFI_80211_DISASSOCIATE_RESULT_CODE  = ENUM

OpenSystem                      = 0
SharedKey                       = 1
FastBSSTransition               = 2
SAE                             = 3
EFI_80211_AUTHENTICATION_TYPE   = ENUM

AuthenticateSuccess                         = 0
AuthenticateRefused                         = 1
AuthenticateAnticLoggingTokenRequired       = 2
AuthenticateFiniteCyclicGroupNotSupported   = 3
AuthenticationRejected                      = 4
AuthenticateInvalidParameter                = 5
EFI_80211_AUTHENTICATE_RESULT_CODE          = ENUM

class EFI_80211_ELEMENT_HEADER (Structure):
  _fields_ = [
    ("ElementID", UINT8),
    ("Length",    UINT8)
  ]

class EFI_80211_ELEMENT_REQ (Structure):
  _fields_ = [
    ("Hdr",         EFI_80211_ELEMENT_HEADER),
    ("RequestIDs",  UINT8 * 1)
  ]

class EFI_80211_ELEMENT_SSID (Structure):
  _fields_ = [
    ("Hdr",   EFI_80211_ELEMENT_HEADER),
    ("SSId",  UINT8 * 32)
  ]

class EFI_80211_SCAN_DATA (Structure):
  _fields_ = [
    ("BSSType",             EFI_80211_BSS_TYPE), 
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("SSIdLen",             UINT8),
    ("SSId",                POINTER(UINT8)),
    ("PassiveMode",         BOOLEAN),
    ("ProbeDelay",          UINT32),
    ("ChannelList",         POINTER(UINT32)),
    ("MinChannelTime",      UINT32),
    ("MaxChannelTime",      UINT32),
    ("RequestInformation",  POINTER(EFI_80211_ELEMENT_REQ)),
    ("SSIDList",            POINTER(EFI_80211_ELEMENT_SSID)),
    ("AccessNetworkType",   EFI_80211_ACC_NET_TYPE),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_COUNTRY_TRIPLET_SUBBAND (Structure):
  _fields_ = [
    ("FirstChannelNum",  UINT8),
    ("NumOfChannels",    UINT8),
    ("MaxTxPowerLevel",  UINT8)
  ]

class EFI_80211_COUNTRY_TRIPLET_OPERATE (Structure):
  _fields_ = [
    ("OperatingExtId",  UINT8),
    ("OperatingClass",  UINT8),
    ("CoverageClass",   UINT8)
  ]

class EFI_80211_COUNTRY_TRIPLET (Union):
  _fields_ = [
    ("Subband",   EFI_80211_COUNTRY_TRIPLET_SUBBAND),
    ("Operating", EFI_80211_COUNTRY_TRIPLET_OPERATE)
  ]

class EFI_80211_ELEMENT_COUNTRY (Structure):
  _fields_ = [
    ("Hdr",             EFI_80211_ELEMENT_HEADER),
    ("CountryStr",      UINT8 * 3),
    ("CountryTriplet",  EFI_80211_COUNTRY_TRIPLET * 1)
  ]

class EFI_80211_ELEMENT_DATA_RSN (Structure):
  _fields_ = [
    ("Version",                       UINT16),
    ("GroupDataCipherSuite",          UINT32)
    # ("PairwiseCipherSuiteCount",      UINT16),
    # ("PairwiseCipherSuiteList",       UINT32 * PairwiseCipherSuiteCount),
    # ("AKMSuiteCount",                 UINT16),
    # ("AKMSuiteList",                  UINT32 * AKMSuiteCount),
    # ("RSNCapabilities",               UINT16),
    # ("PMKIDCount",                    UINT16),
    # ("PMKIDList",                     (UINT8 * PMKIDCount) * 16),
    # ("GroupManagementCipherSuite",    UINT32)
  ]

class EFI_80211_ELEMENT_RSN (Structure):
  _fields_ = [
    ("Hdr",   EFI_80211_ELEMENT_HEADER),
    ("Data",  POINTER(EFI_80211_ELEMENT_DATA_RSN))
  ]

class EFI_80211_ELEMENT_EXT_CAP (Structure):
  _fields_ = [
    ("Hdr",           EFI_80211_ELEMENT_HEADER),
    ("Capabilities",  UINT8 * 1)
  ]

class EFI_80211_BSS_DESCRIPTION (Structure):
  _fields_ = [
    ("BSSId",                     EFI_80211_MAC_ADDRESS),
    ("SSId",                      POINTER(UINT8)),
    ("SSIdLen",                   UINT8),
    ("BSSType",                   EFI_80211_BSS_TYPE),
    ("BeaconPeriod",              UINT16),
    ("Timestamp",                 UINT64),
    ("CapabilityInfo",            UINT16),
    ("BSSBasicRateSet",           POINTER(UINT8)),
    ("OperationalRateSet",        POINTER(UINT8)),
    ("Country",                   POINTER(EFI_80211_ELEMENT_COUNTRY)),
    ("RSN",                       EFI_80211_ELEMENT_RSN),
    ("RSSI",                      UINT8),
    ("RCPIMeasurement",           UINT8),
    ("RSNIMeasurement",           UINT8),
    ("RequestedElements",         POINTER(UINT8)),
    ("BSSMembershipSelectorSet",  POINTER(UINT8)),
    ("ExtCapElement",             POINTER(EFI_80211_ELEMENT_EXT_CAP))
  ]

class EFI_80211_SUBELEMENT_INFO (Structure):
  _fields_ = [
    ("SubElementID",  UINT8),
    ("Length",        UINT8),
    ("Data",          UINT8 * 1)
  ]

class EFI_80211_MULTIPLE_BSSID (Structure):
  _fields_ = [
    ("Hdr",         EFI_80211_ELEMENT_HEADER),
    ("Indicator",   UINT8),
    ("SubElement",  EFI_80211_SUBELEMENT_INFO * 1)
  ]

class EFI_80211_BSS_DESP_PILOT (Structure):
  _fields_ = [
    ("BSSId",           EFI_80211_MAC_ADDRESS),
    ("BSSType",         EFI_80211_BSS_TYPE),
    ("ConCapInfo",      UINT8),
    ("ConCountryStr",   UINT8 * 2),
    ("OperatingClass",  UINT8),
    ("Channel",         UINT8),
    ("Interval",        UINT8),
    ("MultipleBSSID",   POINTER(EFI_80211_MULTIPLE_BSSID)),
    ("RCPIMeasurement", UINT8),
    ("RSNIMeasurement", UINT8)
  ]

class EFI_80211_SCAN_RESULT (Structure):
  _fields_ = [
    ("NumOfBSSDesp",          UINTN),
    ("BSSDespSet",            POINTER(POINTER(EFI_80211_BSS_DESCRIPTION))),
    ("NumofBSSDespFromPilot", UINTN),
    ("BSSDespFromPilotSet",   POINTER(POINTER(EFI_80211_BSS_DESP_PILOT))),
    ("VendorSpecificInfo",    POINTER(UINT8))
  ]

class EFI_80211_SCAN_DATA_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("Data",        POINTER(EFI_80211_SCAN_DATA)),
    ("ResultCode",  EFI_80211_SCAN_RESULT_CODE),
    ("Result",      POINTER(EFI_80211_SCAN_RESULT))
  ]

class EFI_80211_ELEMENT_SUPP_CHANNEL_TUPLE (Structure):
  _fields_ = [
    ("FirstChannelNumber",  UINT8),
    ("NumberOfChannels",    UINT8)
  ]

class EFI_80211_ELEMENT_SUPP_CHANNEL (Structure):
  _fields_ = [
    ("Hdr",     EFI_80211_ELEMENT_HEADER),
    ("Subband", EFI_80211_ELEMENT_SUPP_CHANNEL_TUPLE * 1)
  ]

class EFI_80211_ASSOCIATE_DATA (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("CapabilityInfo",      UINT16),
    ("FailureTimeout",      UINT32),
    ("ListenInterval",      UINT32),
    ("Channels",            POINTER(EFI_80211_ELEMENT_SUPP_CHANNEL)),
    ("RSN",                 EFI_80211_ELEMENT_RSN),
    ("ExtCapElement",       POINTER(EFI_80211_ELEMENT_EXT_CAP)),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_ELEMENT_TIMEOUT_VAL (Structure):
  _fields_ = [
    ("Hdr",   EFI_80211_ELEMENT_HEADER),
    ("Type",  UINT8),
    ("Value", UINT32)
  ]

class EFI_80211_ASSOCIATE_RESULT (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("CapabilityInfo",      UINT16),
    ("AssociationID",       UINT16),
    ("RCPIValue",           UINT8),
    ("RSNIValue",           UINT8),
    ("ExtCapElement",       POINTER(EFI_80211_ELEMENT_EXT_CAP)),
    ("TimeoutInterval",     EFI_80211_ELEMENT_TIMEOUT_VAL),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_ASSOCIATE_DATA_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("Data",        POINTER(EFI_80211_ASSOCIATE_DATA)),
    ("ResultCode",  EFI_80211_ASSOCIATE_RESULT_CODE),
    ("Result",      POINTER(EFI_80211_ASSOCIATE_RESULT))
  ]

class EFI_80211_DISASSOCIATE_DATA (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("ReasonCode",          EFI_80211_REASON_CODE),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_DISASSOCIATE_DATA_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("Data",        POINTER(EFI_80211_DISASSOCIATE_DATA)),
    ("ResultCode",  EFI_80211_DISASSOCIATE_RESULT_CODE)
  ]

class EFI_80211_AUTHENTICATE_DATA (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("AuthType",            EFI_80211_AUTHENTICATION_TYPE),
    ("FailureTimeout",      UINT32),
    ("FTContent",           POINTER(UINT8)),
    ("SAEContent",          POINTER(UINT8)),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_AUTHENTICATE_RESULT (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("FTContent",           POINTER(UINT8)),
    ("SAEContent",          POINTER(UINT8)),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_AUTHENTICATE_DATA_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("Data",        POINTER(EFI_80211_AUTHENTICATE_DATA)),
    ("ResultCode",  EFI_80211_AUTHENTICATE_RESULT_CODE),
    ("Result",      POINTER(EFI_80211_AUTHENTICATE_RESULT))
  ]

class EFI_80211_DEAUTHENTICATE_DATA (Structure):
  _fields_ = [
    ("BSSId",               EFI_80211_MAC_ADDRESS),
    ("ReasonCode",          EFI_80211_REASON_CODE),
    ("VendorSpecificInfo",  POINTER(UINT8))
  ]

class EFI_80211_DEAUTHENTICATE_DATA_TOKEN (Structure):
  _fields_ = [
    ("Event",   EFI_EVENT),
    ("Status",  EFI_STATUS),
    ("Data",    POINTER(EFI_80211_DEAUTHENTICATE_DATA))
  ]

EFI_WIRELESS_MAC_CONNECTION_SCAN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_PROTOCOL),  # IN  *This
  POINTER(EFI_80211_SCAN_DATA_TOKEN)              # IN  *Data
  )

EFI_WIRELESS_MAC_CONNECTION_ASSOCIATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_PROTOCOL),  # IN  *This
  POINTER(EFI_80211_ASSOCIATE_DATA_TOKEN)         # IN  *Data
  )

EFI_WIRELESS_MAC_CONNECTION_DISASSOCIATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_PROTOCOL),  # IN  *This
  POINTER(EFI_80211_DISASSOCIATE_DATA_TOKEN)      # IN  *Data
  )

EFI_WIRELESS_MAC_CONNECTION_AUTHENTICATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_PROTOCOL),  # IN  *This
  POINTER(EFI_80211_AUTHENTICATE_DATA_TOKEN)      # IN  *Data
  )

EFI_WIRELESS_MAC_CONNECTION_DEAUTHENTICATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_WIRELESS_MAC_CONNECTION_PROTOCOL),  # IN  *This
  POINTER(EFI_80211_DEAUTHENTICATE_DATA_TOKEN)    # IN  *Data
  )

EFI_WIRELESS_MAC_CONNECTION_PROTOCOL._fields_ = [
    ("Scan",            EFI_WIRELESS_MAC_CONNECTION_SCAN),
    ("Associate",       EFI_WIRELESS_MAC_CONNECTION_ASSOCIATE),
    ("Disassociate",    EFI_WIRELESS_MAC_CONNECTION_DISASSOCIATE),
    ("Authenticate",    EFI_WIRELESS_MAC_CONNECTION_AUTHENTICATE),
    ("Deauthenticate",  EFI_WIRELESS_MAC_CONNECTION_DEAUTHENTICATE)
  ]

