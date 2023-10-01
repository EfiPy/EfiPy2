# HiiDatabase.py
#
# EfiPy2.MdePkg.Protocol.HiiDatabase
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import \
        EFI_HII_PACKAGE_HEADER,     \
        EFI_HII_HANDLE,             \
        EFI_HII_PACKAGE_LIST_HEADER,\
        EFI_HII_KEYBOARD_LAYOUT

gEfiHiiDatabaseProtocolGuid = \
  EFI_GUID (0xef9fc172, 0xa1b2, 0x4693, ( 0xb3, 0x27, 0x6d, 0x32, 0xfc, 0x41, 0x60, 0x42 ))

class EFI_HII_DATABASE_PROTOCOL (Structure):
  pass

EFI_HII_DATABASE_NOTIFY_TYPE  = UINTN

EFI_HII_DATABASE_NOTIFY_NEW_PACK    = 0x00000001
EFI_HII_DATABASE_NOTIFY_REMOVE_PACK = 0x00000002
EFI_HII_DATABASE_NOTIFY_EXPORT_PACK = 0x00000004
EFI_HII_DATABASE_NOTIFY_ADD_PACK    = 0x00000008

EFI_HII_DATABASE_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  UINT8,                            # IN        PackageType,
  POINTER(EFI_GUID),                # IN CONST  *PackageGuid,
  POINTER(EFI_HII_PACKAGE_HEADER),  # IN CONST  *Package,
  EFI_HII_HANDLE,                   # IN        Handle,
  EFI_HII_DATABASE_NOTIFY_TYPE      # IN        NotifyType
  )

EFI_HII_DATABASE_NEW_PACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL),   # IN CONST  *This,
  POINTER(EFI_HII_PACKAGE_LIST_HEADER), # IN CONST  *PackageList,
  EFI_HANDLE,                           # IN        DriverHandle, OPTIONAL
  POINTER(EFI_HII_HANDLE)               # OUT       *Handle
  )

EFI_HII_DATABASE_REMOVE_PACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE                        # IN        Handle
  )

EFI_HII_DATABASE_UPDATE_PACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE,                       # IN        Handle
  POINTER(EFI_HII_PACKAGE_LIST_HEADER)  # IN CONST  *PackageList
  )

EFI_HII_DATABASE_LIST_PACKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  UINT8,                              # IN        PackageType,
  POINTER(EFI_GUID),                  # IN CONST  *PackageGuid,
  POINTER(UINTN),                     # IN OUT    *HandleBufferLength,
  POINTER(EFI_HII_HANDLE)             # OUT       *Handle
  )

EFI_HII_DATABASE_EXPORT_PACKS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL),   # IN CONST  *This,
  EFI_HII_HANDLE,                       # IN        Handle,
  POINTER(UINTN),                       # IN OUT    *BufferSize,
  POINTER(EFI_HII_PACKAGE_LIST_HEADER)  # OUT       *Buffer
  )

EFI_HII_DATABASE_REGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL),   # IN CONST  *This,
  UINT8,                                # IN        PackageType,
  POINTER(EFI_GUID),                    # IN CONST  *PackageGuid,
  EFI_HII_DATABASE_NOTIFY,              # IN        PackageNotifyFn,
  EFI_HII_DATABASE_NOTIFY_TYPE,         # IN        NotifyType,
  POINTER(EFI_HANDLE)                   # OUT       *NotifyHandle
  )

EFI_HII_DATABASE_UNREGISTER_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  EFI_HANDLE                          # OUT       NotificationHandle
  )

EFI_HII_FIND_KEYBOARD_LAYOUTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  POINTER(UINT16),                    # IN OUT    *KeyGuidBufferLength,
  POINTER(EFI_GUID)                   # OUT       *KeyGuidBuffer
  )

EFI_HII_GET_KEYBOARD_LAYOUT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  POINTER(EFI_GUID),                  # IN CONST  *KeyGuid,
  POINTER(UINT16),                    # IN OUT    *KeyboardLayoutLength,
  POINTER(EFI_HII_KEYBOARD_LAYOUT)    # OUT       *KeyboardLayout
  )

EFI_HII_SET_KEYBOARD_LAYOUT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  POINTER(EFI_GUID)                   # IN CONST  *KeyGuid,
  )

EFI_HII_DATABASE_GET_PACK_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_DATABASE_PROTOCOL), # IN CONST  *This,
  EFI_HII_HANDLE,                     # IN        PackageListHandle,
  POINTER(EFI_HANDLE)                 # OUT       *DriverHandle
  )

EFI_HII_DATABASE_PROTOCOL._fields_ = [
    ("NewPackageList",          EFI_HII_DATABASE_NEW_PACK),
    ("RemovePackageList",       EFI_HII_DATABASE_REMOVE_PACK),
    ("UpdatePackageList",       EFI_HII_DATABASE_UPDATE_PACK),
    ("ListPackageLists",        EFI_HII_DATABASE_LIST_PACKS),
    ("ExportPackageLists",      EFI_HII_DATABASE_EXPORT_PACKS),
    ("RegisterPackageNotify",   EFI_HII_DATABASE_REGISTER_NOTIFY),
    ("UnregisterPackageNotify", EFI_HII_DATABASE_UNREGISTER_NOTIFY),
    ("FindKeyboardLayouts",     EFI_HII_FIND_KEYBOARD_LAYOUTS),
    ("GetKeyboardLayout",       EFI_HII_GET_KEYBOARD_LAYOUT),
    ("SetKeyboardLayout",       EFI_HII_SET_KEYBOARD_LAYOUT),
    ("GetPackageListHandle",    EFI_HII_DATABASE_GET_PACK_HANDLE)
  ]

