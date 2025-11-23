# EapManagement.py
#
# EfiPy2.MdePkg.Protocol.EapManagement
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import Eap

gEfiEapManagementProtocolGuid = \
  EFI_GUID (0xbb62e663, 0x625d, 0x40b2, (0xa0, 0x88, 0xbb, 0xe8, 0x36, 0x23, 0xa2, 0x45 ))

class EFI_EAP_MANAGEMENT_PROTOCOL (Structure):
  pass

PAE_SUPPORT_AUTHENTICATOR       = 0x01
PAE_SUPPORT_SUPPLICANT          = 0x02

class EFI_EAPOL_PORT_INFO (Structure):
  _fields_ = [
    ("PortNumber",      Eap.EFI_PORT_HANDLE),
    ("ProtocolVersion", UINT8),
    ("PaeCapabilities", UINT8)
  ]

Logoff                          = 0
Disconnected                    = 1
Connecting                      = 2
Acquired                        = 3
Authenticating                  = 4
Held                            = 5
Authenticated                   = 6
MaxSupplicantPaeState           = 7
EFI_EAPOL_SUPPLICANT_PAE_STATE  = ENUM

AUTH_PERIOD_FIELD_VALID       = 0x01
HELD_PERIOD_FIELD_VALID       = 0x02
START_PERIOD_FIELD_VALID      = 0x04
MAX_START_FIELD_VALID         = 0x08

class EFI_EAPOL_SUPPLICANT_PAE_CONFIGURATION (Structure):
  _fields_ = [
    ("ValidFieldMask",  UINT8),
    ("AuthPeriod",      UINTN),
    ("HeldPeriod",      UINTN),
    ("StartPeriod",     UINTN),
    ("MaxStart",        UINTN)
  ]

class EFI_EAPOL_SUPPLICANT_PAE_STATISTICS (Structure):
  _fields_ = [
    ("EapolFramesReceived",           UINTN),
    ("EapolFramesTransmitted",        UINTN),
    ("EapolStartFramesTransmitted",   UINTN),
    ("EapolLogoffFramesTransmitted",  UINTN),
    ("EapRespIdFramesTransmitted",    UINTN),
    ("EapResponseFramesTransmitted",  UINTN),
    ("EapReqIdFramesReceived",        UINTN),
    ("EapRequestFramesReceived",      UINTN),
    ("InvalidEapolFramesReceived",    UINTN),
    ("EapLengthErrorFramesReceived",  UINTN),
    ("LastEapolFrameVersion",         UINTN),
    ("LastEapolFrameSource",          UINTN)
  ]

EFI_EAP_GET_SYSTEM_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL), # IN *This
  POINTER(BOOLEAN),                     # OUT *SystemAuthControl, 
  POINTER(EFI_EAPOL_PORT_INFO)          # OUT *PortInfo OPTIONAL
  )

EFI_EAP_SET_SYSTEM_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL), # IN  *This
  BOOLEAN                               # IN  SystemAuthControl,
  )

EFI_EAP_INITIALIZE_PORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL)  # IN  *This
  )

EFI_EAP_USER_LOGON = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL)  # IN  *This
  )

EFI_EAP_USER_LOGOFF = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL)  # IN  *This
  )

EFI_EAP_GET_SUPPLICANT_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL),           # IN     *This
  POINTER(EFI_EAPOL_SUPPLICANT_PAE_STATE),        # OUT    *CurrentState, 
  POINTER(EFI_EAPOL_SUPPLICANT_PAE_CONFIGURATION) # IN OUT *Configuration  OPTIONAL
  )

EFI_EAP_SET_SUPPLICANT_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL),           # IN *This
  POINTER(EFI_EAPOL_SUPPLICANT_PAE_CONFIGURATION) # IN *Configuration
  )

EFI_EAP_GET_SUPPLICANT_STATISTICS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_MANAGEMENT_PROTOCOL),         # IN  *This
  POINTER(EFI_EAPOL_SUPPLICANT_PAE_STATISTICS)  # OUT *Statistics
  )

EFI_EAP_MANAGEMENT_PROTOCOL._fields_ = [
    ("GetSystemConfiguration",      EFI_EAP_GET_SYSTEM_CONFIGURATION),
    ("SetSystemConfiguration",      EFI_EAP_SET_SYSTEM_CONFIGURATION),
    ("InitializePort",              EFI_EAP_INITIALIZE_PORT),
    ("UserLogon",                   EFI_EAP_USER_LOGON),
    ("UserLogoff",                  EFI_EAP_USER_LOGOFF),
    ("GetSupplicantStatus",         EFI_EAP_GET_SUPPLICANT_STATUS),
    ("SetSupplicantConfiguration",  EFI_EAP_SET_SUPPLICANT_CONFIGURATION),
    ("GetSupplicantStatistics",     EFI_EAP_GET_SUPPLICANT_STATISTICS)
  ]
