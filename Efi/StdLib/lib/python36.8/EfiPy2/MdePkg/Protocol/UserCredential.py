# UserCredential.py
#
# EfiPy2.MdePkg.Protocol.UserCredential
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.UserManager                 import EFI_USER_PROFILE_HANDLE,     \
                                                               EFI_USER_INFO_IDENTIFIER,    \
                                                               EFI_CREDENTIAL_LOGON_FLAGS,  \
                                                               EFI_USER_INFO_HANDLE,        \
                                                               EFI_USER_INFO,               \
                                                               EFI_CREDENTIAL_CAPABILITIES

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation  import  EFI_HII_HANDLE, \
                                                                EFI_FORM_ID,    \
                                                                EFI_IMAGE_ID,   \
                                                                EFI_STRING_ID

gEfiUserCredentialProtocolGuid  = \
  EFI_GUID (0x71ee5e94, 0x65b9, 0x45d5, ( 0x82, 0x1a, 0x3a, 0x4d, 0x86, 0xcf, 0xe6, 0xbe ))

class EFI_USER_CREDENTIAL_PROTOCOL (Structure):
  pass

EFI_CREDENTIAL_ENROLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),  # IN  CONST *This
  EFI_USER_PROFILE_HANDLE                 # IN         User
  )

EFI_CREDENTIAL_FORM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN  CONST *This
  POINTER(EFI_HII_HANDLE),                  #     OUT   *Hii,
  POINTER(EFI_GUID),                        #     OUT   *FormSetId,
  POINTER(EFI_FORM_ID)                      #     OUT   *FormId
  )

EFI_CREDENTIAL_TILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST *This,
  POINTER(UINTN),                           # IN OUT   *Width,
  POINTER(UINTN),                           # IN OUT   *Height,
  POINTER(EFI_HII_HANDLE),                  # OUT      *Hii,
  POINTER(EFI_IMAGE_ID)                     # OUT      *Image
  )

EFI_CREDENTIAL_TITLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST *This,
  POINTER(EFI_HII_HANDLE),                  # OUT      *Hii,
  POINTER(EFI_STRING_ID)                    # OUT      *String
  )

EFI_CREDENTIAL_USER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST *This,
  EFI_USER_PROFILE_HANDLE,                  # IN       User,
  POINTER(EFI_USER_INFO_IDENTIFIER)         # OUT      *Identifier
  )

EFI_CREDENTIAL_SELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST *This,
  POINTER(EFI_CREDENTIAL_LOGON_FLAGS)       # OUT      *AutoLogon
  )

EFI_CREDENTIAL_DESELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL) # IN CONST *This,
  )

EFI_CREDENTIAL_DEFAULT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST  *This,
  POINTER(EFI_CREDENTIAL_LOGON_FLAGS)       # OUT       *AutoLogon
  )

EFI_CREDENTIAL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),  # IN CONST  *This,
  EFI_USER_INFO_HANDLE,                   # IN        UserInfo,
  POINTER(EFI_USER_INFO),                 # OUT       *Info,
  POINTER(UINTN)                          # IN OUT    *InfoSize
  )

EFI_CREDENTIAL_GET_NEXT_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL_PROTOCOL),    # IN CONST  *This,
  POINTER(EFI_USER_INFO_HANDLE)             # IN OUT    *UserInfo
  )

EFI_USER_CREDENTIAL_PROTOCOL._fields_ = [
    ("Identifier",    EFI_GUID),
    ("Type",          EFI_GUID),
    ("Enroll",        EFI_CREDENTIAL_ENROLL),
    ("Form",          EFI_CREDENTIAL_FORM),
    ("Tile",          EFI_CREDENTIAL_TILE),
    ("Title",         EFI_CREDENTIAL_TITLE),
    ("User",          EFI_CREDENTIAL_USER),
    ("Select",        EFI_CREDENTIAL_SELECT),
    ("Deselect",      EFI_CREDENTIAL_DESELECT),
    ("Default",       EFI_CREDENTIAL_DEFAULT),
    ("GetInfo",       EFI_CREDENTIAL_GET_INFO),
    ("GetNextInfo",   EFI_CREDENTIAL_GET_NEXT_INFO),
    ("Capabilities",  EFI_CREDENTIAL_CAPABILITIES)
  ]

