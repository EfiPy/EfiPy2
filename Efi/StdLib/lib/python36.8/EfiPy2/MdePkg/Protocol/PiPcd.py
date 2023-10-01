# PiPcd.py
#
# EfiPy2.MdePkg.Protocol.PiPcd
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPcdProtocolGuid = \
  EFI_GUID (0x13a3f0f6, 0x264a, 0x3ef0, ( 0xf2, 0xe0, 0xde, 0xc5, 0x12, 0x34, 0x2f, 0x34 ))

EFI_PCD_INVALID_TOKEN_NUMBER = 0

EFI_PCD_PROTOCOL_SET_SKU = CFUNCTYPE (
  VOID,
  UINTN # IN SkuId
  )

EFI_PCD_PROTOCOL_GET_8 = CFUNCTYPE (
  UINT8,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_16 = CFUNCTYPE (
  UINT16,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_32 = CFUNCTYPE (
  UINT32,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_64 = CFUNCTYPE (
  UINT64,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_POINTER = CFUNCTYPE (
  PVOID,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_BOOLEAN = CFUNCTYPE (
  BOOLEAN,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_GET_SIZE = CFUNCTYPE (
  UINTN,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN               # IN        TokenNumber
  )

EFI_PCD_PROTOCOL_SET_8 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber
  UINT8               # IN        Value
  )

EFI_PCD_PROTOCOL_SET_16 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber,
  UINT16              # IN        Value
  )

EFI_PCD_PROTOCOL_SET_32 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber,
  UINT32              # IN        Value
  )

EFI_PCD_PROTOCOL_SET_64 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber,
  UINT64              # IN        Value
  )

EFI_PCD_PROTOCOL_SET_POINTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber,
  POINTER(UINTN),     # IN OUT    *SizeOfValue,
  PVOID               # IN        *Buffer
  )

EFI_PCD_PROTOCOL_SET_BOOLEAN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST  *Guid,
  UINTN,              # IN        TokenNumber,
  BOOLEAN             # IN        Value
  )

EFI_PCD_PROTOCOL_CALLBACK = CFUNCTYPE (
  VOID,
  POINTER(EFI_GUID),  # IN CONST  *Guid, OPTIONAL
  UINTN,              # IN        CallBackToken,
  PVOID,              # IN OUT    *TokenData,
  UINTN               # IN        TokenDataSize
  )

EFI_PCD_PROTOCOL_CALLBACK_ON_SET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST  *Guid, OPTIONAL
  UINTN,                    # IN        CallBackToken,
  EFI_PCD_PROTOCOL_CALLBACK # IN        CallBackFunction
  )

EFI_PCD_PROTOCOL_CANCEL_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST  *Guid, OPTIONAL
  UINTN,                    # IN        CallBackToken,
  EFI_PCD_PROTOCOL_CALLBACK # IN        CallBackFunction
  )

EFI_PCD_PROTOCOL_GET_NEXT_TOKEN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST  *Guid, OPTIONAL
  POINTER(UINTN)            # IN        *TokenNumber
  )

EFI_PCD_PROTOCOL_GET_NEXT_TOKEN_SPACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_GUID))  # IN OUT CONST **Guid
  )

class EFI_PCD_PROTOCOL (Structure):
  _fields_ = [
    ("SetSku",            EFI_PCD_PROTOCOL_SET_SKU),
    ("Get8",              EFI_PCD_PROTOCOL_GET_8),
    ("Get16",             EFI_PCD_PROTOCOL_GET_16),
    ("Get32",             EFI_PCD_PROTOCOL_GET_32),
    ("Get64",             EFI_PCD_PROTOCOL_GET_64),
    ("GetPtr",            EFI_PCD_PROTOCOL_GET_POINTER),
    ("GetBool",           EFI_PCD_PROTOCOL_GET_BOOLEAN),
    ("GetSize",           EFI_PCD_PROTOCOL_GET_SIZE),
    ("Set8",              EFI_PCD_PROTOCOL_SET_8),
    ("Set16",             EFI_PCD_PROTOCOL_SET_16),
    ("Set32",             EFI_PCD_PROTOCOL_SET_32),
    ("Set64",             EFI_PCD_PROTOCOL_SET_64),
    ("SetPtr",            EFI_PCD_PROTOCOL_SET_POINTER),
    ("SetBool",           EFI_PCD_PROTOCOL_SET_BOOLEAN),
    ("CallbackOnSet",     EFI_PCD_PROTOCOL_CALLBACK_ON_SET),
    ("CancelCallback",    EFI_PCD_PROTOCOL_CANCEL_CALLBACK),
    ("GetNextToken",      EFI_PCD_PROTOCOL_GET_NEXT_TOKEN),
    ("GetNextTokenSpace", EFI_PCD_PROTOCOL_GET_NEXT_TOKEN_SPACE)
  ]

