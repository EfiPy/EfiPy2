# UserCredential2.py
#
# EfiPy2.MdePkg.Protocol.UserCredential2
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

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation  import EFI_HII_HANDLE, \
                                                               EFI_FORM_ID,    \
                                                               EFI_IMAGE_ID,   \
                                                               EFI_STRING_ID

gEfiUserCredential2ProtocolGuid = \
  EFI_GUID (0xe98adb03, 0xb8b9, 0x4af8, ( 0xba, 0x20, 0x26, 0xe9, 0x11, 0x4c, 0xbc, 0xe5 ))

class EFI_USER_CREDENTIAL2_PROTOCOL (Structure):
  pass

EFI_CREDENTIAL2_ENROLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL), # IN  CONST *This
  EFI_USER_PROFILE_HANDLE                 # IN         User
  )

EFI_CREDENTIAL2_FORM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN  CONST *This
  POINTER(EFI_HII_HANDLE),                  #     OUT   *Hii,
  POINTER(EFI_GUID),                        #     OUT   *FormSetId,
  POINTER(EFI_FORM_ID)                      #     OUT   *FormId
  )

EFI_CREDENTIAL2_TILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST *This,
  POINTER(UINTN),                           # IN OUT   *Width,
  POINTER(UINTN),                           # IN OUT   *Height,
  POINTER(EFI_HII_HANDLE),                  # OUT      *Hii,
  POINTER(EFI_IMAGE_ID)                     # OUT      *Image
  )

EFI_CREDENTIAL2_TITLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST *This,
  POINTER(EFI_HII_HANDLE),                  # OUT      *Hii,
  POINTER(EFI_STRING_ID)                    # OUT      *String
  )

EFI_CREDENTIAL2_USER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST *This,
  EFI_USER_PROFILE_HANDLE,                  # IN       User,
  POINTER(EFI_USER_INFO_IDENTIFIER)         # OUT      *Identifier
  )

EFI_CREDENTIAL2_SELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST *This,
  POINTER(EFI_CREDENTIAL_LOGON_FLAGS)       # OUT      *AutoLogon
  )

EFI_CREDENTIAL2_DESELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL)  # IN CONST *This,
  )

EFI_CREDENTIAL2_DEFAULT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST  *This,
  POINTER(EFI_CREDENTIAL_LOGON_FLAGS)       # OUT       *AutoLogon
  )

EFI_CREDENTIAL2_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL), # IN CONST  *This,
  EFI_USER_INFO_HANDLE,                   # IN        UserInfo,
  POINTER(EFI_USER_INFO),                 # OUT       *Info,
  POINTER(UINTN)                          # IN OUT    *InfoSize
  )

EFI_CREDENTIAL2_GET_NEXT_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST  *This,
  POINTER(EFI_USER_INFO_HANDLE)             # IN OUT    *UserInfo
  )

EFI_CREDENTIAL2_DELETE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USER_CREDENTIAL2_PROTOCOL),   # IN CONST  *This,
  POINTER(EFI_USER_PROFILE_HANDLE)          # IN        User
  )

EFI_USER_CREDENTIAL2_PROTOCOL._fields_ = [
    ("Identifier",    EFI_GUID),
    ("Type",          EFI_GUID),
    ("Enroll",        EFI_CREDENTIAL2_ENROLL),
    ("Form",          EFI_CREDENTIAL2_FORM),
    ("Tile",          EFI_CREDENTIAL2_TILE),
    ("Title",         EFI_CREDENTIAL2_TITLE),
    ("User",          EFI_CREDENTIAL2_USER),
    ("Select",        EFI_CREDENTIAL2_SELECT),
    ("Deselect",      EFI_CREDENTIAL2_DESELECT),
    ("Default",       EFI_CREDENTIAL2_DEFAULT),
    ("GetInfo",       EFI_CREDENTIAL2_GET_INFO),
    ("GetNextInfo",   EFI_CREDENTIAL2_GET_NEXT_INFO),
    ("Capabilities",  EFI_CREDENTIAL_CAPABILITIES),
    ("Delete",        EFI_CREDENTIAL2_DELETE)
  ]

