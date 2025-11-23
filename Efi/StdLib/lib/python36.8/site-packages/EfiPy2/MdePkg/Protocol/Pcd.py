# Pcd.py
#
# EfiPy2.MdePkg.Protocol.Pcd
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gPcdProtocolGuid  = \
  EFI_GUID (0x11b34006, 0xd85b, 0x4d0a, ( 0xa2, 0x90, 0xd5, 0xa5, 0x71, 0x31, 0xe, 0xf7 ))

PCD_INVALID_TOKEN_NUMBER  = 0

PCD_PROTOCOL_SET_SKU = CFUNCTYPE (
  VOID,
  UINTN # IN  SkuId
  )

PCD_PROTOCOL_GET8 = CFUNCTYPE (
  UINT8,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET16 = CFUNCTYPE (
  UINT16,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET32 = CFUNCTYPE (
  UINT32,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET64 = CFUNCTYPE (
  UINT64,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET_POINTER = CFUNCTYPE (
  PVOID,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET_BOOLEAN = CFUNCTYPE (
  BOOLEAN,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET_SIZE = CFUNCTYPE (
  UINTN,
  UINTN   # IN  TokenNumber
  )

PCD_PROTOCOL_GET_EX_8 = CFUNCTYPE (
  UINT8,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_16 = CFUNCTYPE (
  UINT16,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_32 = CFUNCTYPE (
  UINT32,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_64 = CFUNCTYPE (
  UINT64,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_POINTER = CFUNCTYPE (
  PVOID,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_BOOLEAN = CFUNCTYPE (
  BOOLEAN,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_GET_EX_SIZE = CFUNCTYPE (
  UINTN,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN               # IN TokenNumber
  )

PCD_PROTOCOL_SET8 = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN TokenNumber,
  UINT8             # IN Value
  )

PCD_PROTOCOL_SET16 = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN TokenNumber,
  UINT16            # IN Value
  )

PCD_PROTOCOL_SET32 = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN TokenNumber,
  UINT32            # IN Value
  )

PCD_PROTOCOL_SET64 = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN TokenNumber,
  UINT64            # IN Value
  )

PCD_PROTOCOL_SET_POINTER = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN      TokenNumber,
  POINTER(UINTN),   # IN OUT  *SizeOfBuffer,
  PVOID             # IN      *Buffer
  )

PCD_PROTOCOL_SET_BOOLEAN = CFUNCTYPE (
  EFI_STATUS,
  UINTN,            # IN  TokenNumber,
  BOOLEAN           # IN  Value
  )

PCD_PROTOCOL_SET_EX_8 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  UINT8               # IN       Value
  )

PCD_PROTOCOL_SET_EX_16 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  UINT16              # IN       Value
  )

PCD_PROTOCOL_SET_EX_32 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  UINT32              # IN       Value
  )

PCD_PROTOCOL_SET_EX_64 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  UINT64              # IN       Value
  )

PCD_PROTOCOL_SET_EX_POINTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  POINTER(UINTN),     # IN OUT   *SizeOfBuffer,
  PVOID               # IN       *Buffer
  )

PCD_PROTOCOL_SET_EX_BOOLEAN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN CONST *Guid,
  UINTN,              # IN       TokenNumber,
  BOOLEAN             # IN       Value
  )

PCD_PROTOCOL_CALLBACK = CFUNCTYPE (
  VOID,
  POINTER(EFI_GUID),        # IN CONST *CallBackGuid, OPTIONAL
  UINTN,                    # IN       CallBackToken,
  PVOID,                    # IN OUT   *TokenData,
  POINTER(UINTN),           # IN       TokenDataSize
  )

PCD_PROTOCOL_CALLBACK_ONSET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST *Guid, OPTIONAL
  UINTN,                    # IN       TokenNumber,
  PCD_PROTOCOL_CALLBACK     # IN        CallBackFunction
  )

PCD_PROTOCOL_CANCEL_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST *Guid, OPTIONAL
  UINTN,                    # IN       TokenNumber,
  PCD_PROTOCOL_CALLBACK     # IN        CallBackFunction
  )

PCD_PROTOCOL_GET_NEXT_TOKEN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        # IN CONST *Guid, OPTIONAL
  POINTER(UINTN)            # IN OUT  *TokenNumber
  )

PCD_PROTOCOL_GET_NEXT_TOKENSPACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_GUID)),   # IN CONST *Guid, OPTIONAL
  )

class PCD_PROTOCOL (Structure):
  _fields_ = [
    ("SetSku",            PCD_PROTOCOL_SET_SKU),
    ("Get8",              PCD_PROTOCOL_GET8),
    ("Get16",             PCD_PROTOCOL_GET16),
    ("Get32",             PCD_PROTOCOL_GET32),
    ("Get64",             PCD_PROTOCOL_GET64),
    ("GetPtr",            PCD_PROTOCOL_GET_POINTER),
    ("GetBool",           PCD_PROTOCOL_GET_BOOLEAN),
    ("GetSize",           PCD_PROTOCOL_GET_SIZE),
    ("Get8Ex",            PCD_PROTOCOL_GET_EX_8),
    ("Get16Ex",           PCD_PROTOCOL_GET_EX_16),
    ("Get32Ex",           PCD_PROTOCOL_GET_EX_32),
    ("Get64Ex",           PCD_PROTOCOL_GET_EX_64),
    ("GetPtrEx",          PCD_PROTOCOL_GET_EX_POINTER),
    ("GetBoolEx",         PCD_PROTOCOL_GET_EX_BOOLEAN),
    ("GetSizeEx",         PCD_PROTOCOL_GET_EX_SIZE),
    ("Set8",              PCD_PROTOCOL_SET8),
    ("Set16",             PCD_PROTOCOL_SET16),
    ("Set32",             PCD_PROTOCOL_SET32),
    ("Set64",             PCD_PROTOCOL_SET64),
    ("SetPtr",            PCD_PROTOCOL_SET_POINTER),
    ("SetBool",           PCD_PROTOCOL_SET_BOOLEAN),
    ("Set8Ex",            PCD_PROTOCOL_SET_EX_8),
    ("Set16Ex",           PCD_PROTOCOL_SET_EX_16),
    ("Set32Ex",           PCD_PROTOCOL_SET_EX_32),
    ("Set64Ex",           PCD_PROTOCOL_SET_EX_64),
    ("SetPtrEx",          PCD_PROTOCOL_SET_EX_POINTER),
    ("SetBoolEx",         PCD_PROTOCOL_SET_EX_BOOLEAN),
    ("CallbackOnSet",     PCD_PROTOCOL_CALLBACK_ONSET),
    ("CancelCallback",    PCD_PROTOCOL_CANCEL_CALLBACK),
    ("GetNextToken",      PCD_PROTOCOL_GET_NEXT_TOKEN ),
    ("GetNextTokenSpace", PCD_PROTOCOL_GET_NEXT_TOKENSPACE)
  ]

