# UserManager.py
#
# EfiPy2.MdePkg.Protocol.UserManager
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiUserManagerProtocolGuid             = \
  EFI_GUID (0x6fd5b00c, 0xd426, 0x4283, ( 0x98, 0x87, 0x6c, 0xf5, 0xcf, 0x1c, 0xb1, 0xfe ))

gEfiEventUserProfileChangedGuid         = \
  EFI_GUID (0xbaf1e6de, 0x209e, 0x4adb, ( 0x8d, 0x96, 0xfd, 0x8b, 0x71, 0xf3, 0xf6, 0x83 ))

EFI_USER_PROFILE_HANDLE   = PVOID
EFI_USER_INFO_HANDLE      = PVOID

EFI_USER_INFO_ATTRIBS         = UINT16
EFI_USER_INFO_STORAGE                   = 0x000F
EFI_USER_INFO_STORAGE_VOLATILE          = 0x0000
EFI_USER_INFO_STORAGE_CREDENTIAL_NV     = 0x0001
EFI_USER_INFO_STORAGE_PLATFORM_NV       = 0x0002

EFI_USER_INFO_ACCESS                    = 0x0070
EFI_USER_INFO_PUBLIC                    = 0x0010
EFI_USER_INFO_PRIVATE                   = 0x0020
EFI_USER_INFO_PROTECTED                 = 0x0030
EFI_USER_INFO_EXCLUSIVE                 = 0x0080

class EFI_USER_INFO (Structure):
  _fields_ = [
    ("Credential",  EFI_GUID),
    ("InfoType",    UINT8),
    ("Reserved1",   UINT8),
    ("InfoAttribs", EFI_USER_INFO_ATTRIBS),
    ("InfoSize",    UINT32)
  ]

gEfiUserCredentialClassUnknownGuid      = \
  EFI_GUID (0x5cf32e68, 0x7660, 0x449b, ( 0x80, 0xe6, 0x7e, 0xa3, 0x6e, 0x3, 0xf6, 0xa8 ))
gEfiUserCredentialClassPasswordGuid     = \
  EFI_GUID (0xf8e5058c, 0xccb6, 0x4714, ( 0xb2, 0x20, 0x3f, 0x7e, 0x3a, 0x64, 0xb, 0xd1 ))
gEfiUserCredentialClassSmartCardGuid    = \
  EFI_GUID (0x5f03ba33, 0x8c6b, 0x4c24, ( 0xaa, 0x2e, 0x14, 0xa2, 0x65, 0x7b, 0xd4, 0x54 ))
gEfiUserCredentialClassFingerprintGuid  = \
  EFI_GUID (0x32cba21f, 0xf308, 0x4cbc, ( 0x9a, 0xb5, 0xf5, 0xa3, 0x69, 0x9f, 0x4, 0x4a ))
gEfiUserCredentialClassHandprintGuid    = \
  EFI_GUID (0x5917ef16, 0xf723, 0x4bb9, ( 0xa6, 0x4b, 0xd8, 0xc5, 0x32, 0xf4, 0xd8, 0xb5 ))
gEfiUserCredentialClassSecureCardGuid   = \
  EFI_GUID (0x8a6b4a83, 0x42fe, 0x45d2, ( 0xa2, 0xef, 0x46, 0xf0, 0x6c, 0x7d, 0x98, 0x52 ))

EFI_CREDENTIAL_CAPABILITIES         = UINT64
EFI_CREDENTIAL_CAPABILITIES_ENROLL  = 0x0000000000000001

EFI_CREDENTIAL_LOGON_FLAGS          = UINT32
EFI_CREDENTIAL_LOGON_FLAG_AUTO                = 0x00000001
EFI_CREDENTIAL_LOGON_FLAG_DEFAULT             = 0x00000002

EFI_USER_INFO_EMPTY_RECORD                    = 0x00

EFI_USER_INFO_NAME_RECORD                     = 0x01
EFI_USER_INFO_NAME                            = PCHAR16

EFI_USER_INFO_CREATE_DATE_RECORD              = 0x02
EFI_USER_INFO_CREATE_DATE                     = EFI_TIME

EFI_USER_INFO_USAGE_DATE_RECORD               = 0x03
EFI_USER_INFO_USAGE_DATE                      = EFI_TIME

EFI_USER_INFO_USAGE_COUNT_RECORD              = 0x04
EFI_USER_INFO_USAGE_COUNT                     = UINT64

EFI_USER_INFO_IDENTIFIER_RECORD               = 0x05
EFI_USER_INFO_IDENTIFIER                      = UINT8 * 16

EFI_USER_INFO_CREDENTIAL_TYPE_RECORD          = 0x06
EFI_USER_INFO_CREDENTIAL_TYPE                 = EFI_GUID

EFI_USER_INFO_CREDENTIAL_TYPE_NAME_RECORD     = 0x07
EFI_USER_INFO_CREDENTIAL_TYPE_NAME            = PCHAR16

EFI_USER_INFO_CREDENTIAL_PROVIDER_RECORD      = 0x08
EFI_USER_INFO_CREDENTIAL_PROVIDER             = EFI_GUID

EFI_USER_INFO_CREDENTIAL_PROVIDER_NAME_RECORD = 0x09
EFI_USER_INFO_CREDENTIAL_PROVIDER_NAME        = PCHAR16

EFI_USER_INFO_PKCS11_RECORD                   = 0x0A

EFI_USER_INFO_CBEFF_RECORD                    = 0x0B
EFI_USER_INFO_CBEFF                           = PVOID

EFI_USER_INFO_FAR_RECORD                      = 0x0C
EFI_USER_INFO_FAR                             = UINT8

EFI_USER_INFO_RETRY_RECORD                    = 0x0D
EFI_USER_INFO_RETRY                           = UINT8

EFI_USER_INFO_ACCESS_POLICY_RECORD            = 0x0E

class EFI_USER_INFO_ACCESS_CONTROL (Structure):
  _fields_ = [
    ("Type",  UINT32),
    ("Size",  UINT32)
  ]

EFI_USER_INFO_ACCESS_POLICY                   = EFI_USER_INFO_ACCESS_CONTROL

EFI_USER_INFO_ACCESS_FORBID_LOAD              = 0x00000001

EFI_USER_INFO_ACCESS_PERMIT_LOAD              = 0x00000002
EFI_USER_INFO_ACCESS_ENROLL_SELF              = 0x00000003
EFI_USER_INFO_ACCESS_ENROLL_OTHERS            = 0x00000004
EFI_USER_INFO_ACCESS_MANAGE                   = 0x00000005
EFI_USER_INFO_ACCESS_SETUP                    = 0x00000006

gEfiUserInfoAccessSetupAdminGuid        = \
  EFI_GUID (0x85b75607, 0xf7ce, 0x471e, ( 0xb7, 0xe4, 0x2a, 0xea, 0x5f, 0x72, 0x32, 0xee ))
gEfiUserInfoAccessSetupNormalGuid       = \
  EFI_GUID (0x1db29ae0, 0x9dcb, 0x43bc, ( 0x8d, 0x87, 0x5d, 0xa1, 0x49, 0x64, 0xdd, 0xe2 ))
gEfiUserInfoAccessSetupRestrictedGuid   = \
  EFI_GUID (0xbdb38125, 0x4d63, 0x49f4,  ( 0x82, 0x12, 0x61, 0xcf, 0x5a, 0x19, 0xa, 0xf8 ))

EFI_USER_INFO_ACCESS_FORBID_CONNECT           = 0x00000007

EFI_USER_INFO_ACCESS_PERMIT_CONNECT           = 0x00000008

EFI_USER_INFO_ACCESS_BOOT_ORDER               = 0x00000009
EFI_USER_INFO_ACCESS_BOOT_ORDER_HDR           = UINT32

EFI_USER_INFO_ACCESS_BOOT_ORDER_MASK          = 0x0000000F

EFI_USER_INFO_ACCESS_BOOT_ORDER_INSERT        = 0x00000000

EFI_USER_INFO_ACCESS_BOOT_ORDER_APPEND        = 0x00000001

EFI_USER_INFO_ACCESS_BOOT_ORDER_REPLACE       = 0x00000002

EFI_USER_INFO_ACCESS_BOOT_ORDER_NODEFAULT     = 0x00000010

EFI_USER_INFO_IDENTITY_POLICY_RECORD          = 0x0F

class EFI_USER_INFO_IDENTITY_POLICY (Structure):
  _fields_ = [
    ("Type",    UINT32),
    ("Length",  UINT32)
  ]

EFI_USER_INFO_IDENTITY_FALSE                  = 0x00
EFI_USER_INFO_IDENTITY_TRUE                   = 0x01
EFI_USER_INFO_IDENTITY_CREDENTIAL_TYPE        = 0x02
EFI_USER_INFO_IDENTITY_CREDENTIAL_PROVIDER    = 0x03
EFI_USER_INFO_IDENTITY_NOT                    = 0x10
EFI_USER_INFO_IDENTITY_AND                    = 0x11
EFI_USER_INFO_IDENTITY_OR                     = 0x12

EFI_USER_INFO_GUID_RECORD                     = 0xFF
EFI_USER_INFO_GUID                            = EFI_GUID

class EFI_USER_INFO_TABLE (Structure):
  _fields_ = [
    ("Size",    UINT64)
  ]

class EFI_USER_MANAGER_PROTOCOL (Structure):
  pass

EFI_USER_PROFILE_CREATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_USER_PROFILE_HANDLE)    # OUT       *User
  )

EFI_USER_PROFILE_DELETE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  EFI_USER_PROFILE_HANDLE             # IN        User
  )

EFI_USER_PROFILE_GET_NEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_USER_PROFILE_HANDLE)    # IN  OUT   *User
  )

EFI_USER_PROFILE_CURRENT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_USER_PROFILE_HANDLE)    # OUT       *CurrentUser
  )

EFI_USER_PROFILE_IDENTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_USER_PROFILE_HANDLE)    # OUT       *User
  )

EFI_USER_PROFILE_FIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_USER_PROFILE_HANDLE),   # IN OUT    *User
  POINTER(EFI_USER_INFO_HANDLE),      # IN OUT    *UserInfo OPTIONAL,
  POINTER(EFI_USER_INFO),             # IN CONST  *Info,
  UINTN                               # IN        InfoSize
  )

EFI_USER_PROFILE_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN  CONST *This
  POINTER(EFI_HANDLE)                 # IN        Changed
  )

EFI_USER_PROFILE_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN CONST  *This
  EFI_USER_PROFILE_HANDLE,            # IN        User
  EFI_USER_INFO_HANDLE,               # IN        UserInfo,
  POINTER(EFI_USER_INFO),             # OUT       *Info,
  POINTER(UINTN)                      # IN OUT    *InfoSize
  )

EFI_USER_PROFILE_SET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN CONST  *This
  EFI_USER_PROFILE_HANDLE,            # IN        User,
  POINTER(EFI_USER_INFO_HANDLE),      # IN OUT    *UserInfo,
  POINTER(EFI_USER_INFO),             # IN CONST  *Info,
  UINTN                               # IN        InfoSize
  )

EFI_USER_PROFILE_DELETE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN CONST  *This
  EFI_USER_PROFILE_HANDLE,            # IN        User,
  EFI_USER_INFO_HANDLE                # IN        UserInfo
  )

EFI_USER_PROFILE_GET_NEXT_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_MANAGER_PROTOCOL), # IN CONST  *This
  EFI_USER_PROFILE_HANDLE,            # IN        User,
  POINTER(EFI_USER_INFO_HANDLE)       # IN OUT    *UserInfo
  )

EFI_USER_MANAGER_PROTOCOL._fields_ = [
    ("Create",      EFI_USER_PROFILE_CREATE),
    ("Delete",      EFI_USER_PROFILE_DELETE),
    ("GetNext",     EFI_USER_PROFILE_GET_NEXT),
    ("Current",     EFI_USER_PROFILE_CURRENT),
    ("Identify",    EFI_USER_PROFILE_IDENTIFY),
    ("Find",        EFI_USER_PROFILE_FIND),
    ("Notify",      EFI_USER_PROFILE_NOTIFY),
    ("GetInfo",     EFI_USER_PROFILE_GET_INFO),
    ("SetInfo",     EFI_USER_PROFILE_SET_INFO),
    ("DeleteInfo",  EFI_USER_PROFILE_DELETE_INFO),
    ("GetNextInfo", EFI_USER_PROFILE_GET_NEXT_INFO)
  ]

