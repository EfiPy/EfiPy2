# PldmSmbiosTransfer.py
#
# EfiPy2.MdePkg.IndustryStandard.PldmSmbiosTransfer
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.Pldm import *

PLDM_GET_SMBIOS_STRUCTURE_TABLE_METADATA_COMMAND_CODE  = 0x01
PLDM_SET_SMBIOS_STRUCTURE_TABLE_METADATA_COMMAND_CODE  = 0x02
PLDM_GET_SMBIOS_STRUCTURE_TABLE_COMMAND_CODE           = 0x03
PLDM_SET_SMBIOS_STRUCTURE_TABLE_COMMAND_CODE           = 0x04
PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_COMMAND_CODE         = 0x05
PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_COMMAND_CODE       = 0x06

PLDM_COMPLETION_CODE_INVALID_DATA_TRANSFER_HANDLE        = 0x80
PLDM_COMPLETION_CODE_INVALID_TRANSFER_OPERATION_FLAG     = 0x81
PLDM_COMPLETION_CODE_INVALID_TRANSFER_FLAG               = 0x82
PLDM_COMPLETION_CODE_NO_SMBIOS_STRUCTURE_TABLE_METADATA  = 0x83
PLDM_COMPLETION_CODE_INVALID_DATA_INTEGRITY_CHECK        = 0x84
PLDM_COMPLETION_CODE_SMBIOS_STRUCTURE_TABLE_UNAVAILABLE  = 0x85

class PLDM_SMBIOS_STRUCTURE_TABLE_METADATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SmbiosMajorVersion",                      UINT8 ),
    ("SmbiosMinorVersion",                      UINT8 ),
    ("MaximumStructureSize",                    UINT16),
    ("SmbiosStructureTableLength",              UINT16),
    ("NumberOfSmbiosStructures",                UINT16),
    ("SmbiosStructureTableIntegrityChecksum",   UINT32)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_TABLE_METADATA_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",                  PLDM_RESPONSE_HEADER),
    ("SmbiosStructureTableMetadata",    PLDM_SMBIOS_STRUCTURE_TABLE_METADATA)
  ]

class PLDM_SET_SMBIOS_STRUCTURE_TABLE_METADATA_REQUEST_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestHeader",                   PLDM_REQUEST_HEADER),
    ("SmbiosStructureTableMetadata",    PLDM_SMBIOS_STRUCTURE_TABLE_METADATA)
  ]

class PLDM_SET_SMBIOS_STRUCTURE_TABLE_METADATA_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",  PLDM_RESPONSE_HEADER)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_TABLE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataTransferHandle",      UINT32),
    ("TransferOperationFlag",   UINT8)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_TABLE_REQUEST_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestHeader",                   PLDM_REQUEST_HEADER),
    ("GetSmbiosStructureTableRequest",  PLDM_GET_SMBIOS_STRUCTURE_TABLE_REQUEST)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_TABLE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NextDataTransferHandle",  UINT32),
    ("TransferFlag",            UINT8),
    ("Table",                   UINT8 * 0)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_TABLE_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",                  PLDM_RESPONSE_HEADER),
    ("GetSmbiosStructureTableResponse", PLDM_GET_SMBIOS_STRUCTURE_TABLE_RESPONSE)
  ]

class PLDM_SET_SMBIOS_STRUCTURE_TABLE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataTransferHandle",  UINT32),
    ("TransferFlag",        UINT8),
    ("Table",               UINT8 * 0)
  ]

class PLDM_SET_SMBIOS_STRUCTURE_TABLE_REQUEST_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestHeader",                   PLDM_REQUEST_HEADER),
    ("SetSmbiosStructureTableRequest",  PLDM_SET_SMBIOS_STRUCTURE_TABLE_REQUEST)
  ]

class PLDM_SET_SMBIOS_STRUCTURE_TABLE_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",          PLDM_RESPONSE_HEADER),
    ("NextDataTransferHandle",  UINT32)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataTransferHandle",      UINT32),
    ("TransferOperationFlag",   UINT8),
    ("Type",                    UINT8),
    ("StructureInstanceId",     UINT16)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_REQUEST_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestHeader",                   PLDM_REQUEST_HEADER),
    ("GetSmbiosStructureByTypeRequest", PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_REQUEST)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NextDataTransferHandle",  UINT32),
    ("TransferFlag",            UINT8),
    ("Table",                   UINT8 * 0)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",                      PLDM_RESPONSE_HEADER),
    ("GetSmbiosStructureByTypeResponse",    PLDM_GET_SMBIOS_STRUCTURE_BY_TYPE_RESPONSE)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataTransferHandle",      UINT32),
    ("TransferOperationFlag",   UINT8),
    ("Handle",                  UINT16)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_REQUEST_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestHeader",                       PLDM_REQUEST_HEADER),
    ("GetSmbiosStructureByHandleRequest",   PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_REQUEST)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NextDataTransferHandle",  UINT32),
    ("TransferFlag",            UINT8),
    ("Table",                   UINT8 * 0)
  ]

class PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_RESPONSE_FORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ResponseHeader",                      PLDM_RESPONSE_HEADER),
    ("GetSmbiosStructureByTypeResponse",    PLDM_GET_SMBIOS_STRUCTURE_BY_HANDLE_RESPONSE)
  ]

