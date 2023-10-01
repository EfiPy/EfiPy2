# RestJsonStructure.py
#
# EfiPy2.MdePkg.Protocol.RestJsonStructure
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

EFI_REST_JSON_STRUCTURE_PROTOCOL_GUID           = \
  EFI_GUID (0xa9a048f6, 0x48a0, 0x4714, (0xb7, 0xda, 0xa9, 0xad,0x87, 0xd4, 0xda, 0xc9 ))

class EFI_REST_JSON_STRUCTURE_PROTOCOL (Structure):
  pass

EFI_REST_JSON_RESOURCE_TYPE_DATATYPE = POINTER(CHAR8)

class EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE (Structure):
  _fields_ = [
    ("ResourceTypeName",    POINTER(CHAR8)),
    ("MajorVersion",        POINTER(CHAR8)),
    ("MinorVersion",        POINTER(CHAR8)),
    ("ErrataVersion",       POINTER(CHAR8))
  ]

class EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER (Structure):
  _fields_ = [
    ("NameSpace",   EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE),
    ("DataType",    EFI_REST_JSON_RESOURCE_TYPE_DATATYPE)
  ]

class EFI_REST_JSON_STRUCTURE_SUPPORTED (Structure):
  _fields_ = [
    ("NextSupportedRsrcInterp", LIST_ENTRY),
    ("RestResourceInterp",      EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER)
  ]

class EFI_REST_JSON_STRUCTURE_HEADER (Structure):
  _fields_ = [
    ("JsonRsrcIdentifier",      EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER),
    ("JsonStructurePointer",    PVOID)
  ]

EFI_REST_JSON_STRUCTURE_TO_STRUCTURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER),  #   IN  *JsonRsrcIdentifier OPTIONAL,
  POINTER(CHAR8),                                   #   IN  *ResourceJsonText,
  POINTER(POINTER(EFI_REST_JSON_STRUCTURE_HEADER))  #   OUT **JsonStructure
  )

EFI_REST_JSON_STRUCTURE_TO_JSON = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_STRUCTURE_HEADER),          #   IN  *JsonStructureHeader,
  POINTER(POINTER(CHAR8))                           #   OUT **ResourceJsonText
  )

EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_STRUCTURE_HEADER)           #   IN  *JsonStructureHeader
  )

EFI_REST_JSON_STRUCTURE_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),    #   IN *This
  POINTER(EFI_REST_JSON_STRUCTURE_SUPPORTED),   #   IN *JsonStructureSupported,
  EFI_REST_JSON_STRUCTURE_TO_STRUCTURE,         #   IN ToStructure,
  EFI_REST_JSON_STRUCTURE_TO_JSON,              #   IN ToJson,
  EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE     #   IN DestroyStructure
  )

EFI_REST_JSON_STRUCTURE_PROTOCOL._fields_ = [
    ("Register",            EFI_REST_JSON_STRUCTURE_REGISTER),
    ("ToStructure",         EFI_REST_JSON_STRUCTURE_TO_STRUCTURE),
    ("ToJson",              EFI_REST_JSON_STRUCTURE_TO_JSON),
    ("DestoryStructure",    EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE)
  ]

