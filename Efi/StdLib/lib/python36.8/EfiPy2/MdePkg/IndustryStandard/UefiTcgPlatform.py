# UefiTcgPlatform.py
#
# EfiPy2.MdePkg.IndustryStandard.UefiTcgPlatform
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard          import *
from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL
from EfiPy2.MdePkg.Uefi.UefiSpec             import EFI_CONFIGURATION_TABLE
from EfiPy2.MdePkg.Uefi                      import UefiGpt

from EfiPy2.MdePkg.IndustryStandard          import Tpm12
from EfiPy2.MdePkg.IndustryStandard          import Tpm20

EV_PREBOOT_CERT             = 0x00000000
EV_POST_CODE                = 0x00000001
EV_NO_ACTION                = 0x00000003
EV_SEPARATOR                = 0x00000004
EV_ACTION                   = 0x00000005
EV_EVENT_TAG                = 0x00000006
EV_S_CRTM_CONTENTS          = 0x00000007
EV_S_CRTM_VERSION           = 0x00000008
EV_CPU_MICROCODE            = 0x00000009
EV_PLATFORM_CONFIG_FLAGS    = 0x0000000A
EV_TABLE_OF_DEVICES         = 0x0000000B
EV_COMPACT_HASH             = 0x0000000C
EV_NONHOST_CODE             = 0x0000000F
EV_NONHOST_CONFIG           = 0x00000010
EV_NONHOST_INFO             = 0x00000011
EV_OMIT_BOOT_DEVICE_EVENTS  = 0x00000012

EV_EFI_EVENT_BASE                 = 0x80000000
EV_EFI_VARIABLE_DRIVER_CONFIG     = EV_EFI_EVENT_BASE + 1
EV_EFI_VARIABLE_BOOT              = EV_EFI_EVENT_BASE + 2
EV_EFI_BOOT_SERVICES_APPLICATION  = EV_EFI_EVENT_BASE + 3
EV_EFI_BOOT_SERVICES_DRIVER       = EV_EFI_EVENT_BASE + 4
EV_EFI_RUNTIME_SERVICES_DRIVER    = EV_EFI_EVENT_BASE + 5
EV_EFI_GPT_EVENT                  = EV_EFI_EVENT_BASE + 6
EV_EFI_ACTION                     = EV_EFI_EVENT_BASE + 7
EV_EFI_PLATFORM_FIRMWARE_BLOB     = EV_EFI_EVENT_BASE + 8
EV_EFI_HANDOFF_TABLES             = EV_EFI_EVENT_BASE + 9
EV_EFI_PLATFORM_FIRMWARE_BLOB2    = EV_EFI_EVENT_BASE + 0xA
EV_EFI_HANDOFF_TABLES2            = EV_EFI_EVENT_BASE + 0xB
EV_EFI_HCRTM_EVENT                = EV_EFI_EVENT_BASE + 0x10
EV_EFI_VARIABLE_AUTHORITY         = EV_EFI_EVENT_BASE + 0xE0
EV_EFI_SPDM_FIRMWARE_BLOB         = EV_EFI_EVENT_BASE + 0xE1
EV_EFI_SPDM_FIRMWARE_CONFIG       = EV_EFI_EVENT_BASE + 0xE2

EFI_CALLING_EFI_APPLICATION         = b"Calling EFI Application from Boot Option"
EFI_RETURNING_FROM_EFI_APPLICATION  = b"Returning from EFI Application from Boot Option"
EFI_EXIT_BOOT_SERVICES_INVOCATION   = b"Exit Boot Services Invocation"
EFI_EXIT_BOOT_SERVICES_FAILED       = "Exit Boot Services Returned with Failure"
EFI_EXIT_BOOT_SERVICES_SUCCEEDED    = b"Exit Boot Services Returned with Success"

EV_POSTCODE_INFO_POST_CODE    = b"POST CODE"
POST_CODE_STR_LEN             = len (EV_POSTCODE_INFO_POST_CODE)

EV_POSTCODE_INFO_SMM_CODE     = b"SMM CODE"
SMM_CODE_STR_LEN             = len (EV_POSTCODE_INFO_SMM_CODE)

EV_POSTCODE_INFO_ACPI_DATA    = b"ACPI DATA"
ACPI_DATA_LEN                 = len (EV_POSTCODE_INFO_ACPI_DATA)

EV_POSTCODE_INFO_BIS_CODE     = b"BIS CODE"
BIS_CODE_LEN                  = len (EV_POSTCODE_INFO_BIS_CODE)

EV_POSTCODE_INFO_UEFI_PI      = b"UEFI PI"
UEFI_PI_LEN                   = len (EV_POSTCODE_INFO_UEFI_PI)

EV_POSTCODE_INFO_OPROM        = b"Embedded Option ROM"
OPROM_LEN                     = len (EV_POSTCODE_INFO_OPROM)

EV_POSTCODE_INFO_EMBEDDED_UEFI_DRIVER  = b"Embedded UEFI Driver"
EMBEDDED_UEFI_DRIVER_LEN               = len (EV_POSTCODE_INFO_EMBEDDED_UEFI_DRIVER)

FIRMWARE_DEBUGGER_EVENT_STRING      = b"UEFI Debug Mode"
FIRMWARE_DEBUGGER_EVENT_STRING_LEN  = len (FIRMWARE_DEBUGGER_EVENT_STRING)

TCG_EVENTTYPE = UINT32
TCG_PCRINDEX  = Tpm12.TPM_PCRINDEX
TCG_DIGEST    = Tpm12.TPM_DIGEST

class TCG_PCR_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digest",    TCG_DIGEST),
    ("EventSize", UINT32),
    ("Event",     UINT8 * 1)
  ]

TSS_EVENT_DATA_MAX_SIZE   = 256

class TCG_PCR_EVENT_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digest",    TCG_DIGEST),
    ("EventSize", UINT32),
  ]

class EFI_PLATFORM_FIRMWARE_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlobBase",    EFI_PHYSICAL_ADDRESS),
    ("BlobLength",  UINT64)
  ]

class UEFI_PLATFORM_FIRMWARE_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlobBase",    EFI_PHYSICAL_ADDRESS),
    ("BlobLength",  UINT64)
  ]

class UEFI_PLATFORM_FIRMWARE_BLOB2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlobDescriptionSize", UINT8)
    # ("BlobDescription",     UINT8 * BlobDescriptionSize),
    # ("BlobBase",            EFI_PHYSICAL_ADDRESS),
    # ("BlobLength",          UINT64)
  ]

class EFI_IMAGE_LOAD_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ImageLocationInMemory", EFI_PHYSICAL_ADDRESS),
    ("ImageLengthInMemory",   UINTN),
    ("ImageLinkTimeAddress",  UINTN),
    ("LengthOfDevicePath",    UINTN),
    ("DevicePath",            EFI_DEVICE_PATH_PROTOCOL * 1)
  ]

class UEFI_IMAGE_LOAD_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ImageLocationInMemory",   EFI_PHYSICAL_ADDRESS),
    ("ImageLengthInMemory",     UINT64),
    ("ImageLinkTimeAddress",    UINT64),
    ("LengthOfDevicePath",      UINT64),
    ("DevicePath",              EFI_DEVICE_PATH_PROTOCOL * 1)
  ]

class EFI_HANDOFF_TABLE_POINTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfTables",  UINTN),
    ("TableEntry",      EFI_CONFIGURATION_TABLE * 1)
  ]

class UEFI_HANDOFF_TABLE_POINTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumberOfTables",  UINT64),
    ("TableEntry",      EFI_CONFIGURATION_TABLE * 1)
  ]

class UEFI_HANDOFF_TABLE_POINTERS2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TableDescriptionSize",    UINT8)
    # ("TableDescription",        UINT8 * TableDescriptionSize),
    # ("NumberOfTables",          UINT64),
    # ("TableEntry",              EFI_CONFIGURATION_TABLE * 1),
  ]

class EFI_VARIABLE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VariableName",        EFI_GUID),
    ("UnicodeNameLength",   UINTN),
    ("VariableDataLength",  UINTN),
    ("UnicodeName",         CHAR16 * 1),
    ("VariableData",        INT8 * 1)
  ]

class UEFI_VARIABLE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VariableName",        EFI_GUID),
    ("UnicodeNameLength",   UINT64),
    ("VariableDataLength",  UINT64),
    ("UnicodeName",         CHAR16 * 1),
    ("VariableData",        INT8 * 1)
  ]

class EFI_VARIABLE_DATA_TREE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VariableName",        EFI_GUID),
    ("UnicodeNameLength",   UINT64),
    ("VariableDataLength",  UINT64),
    ("UnicodeName",         CHAR16 * 1),
    ("VariableData",        INT8 * 1)
  ]

class EFI_GPT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EfiPartitionHeader",  UefiGpt.EFI_PARTITION_TABLE_HEADER),
    ("NumberOfPartitions",  UINTN),
    ("Partitions",          UefiGpt.EFI_PARTITION_ENTRY * 1)
  ]

class UEFI_GPT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EfiPartitionHeader",  UefiGpt.EFI_PARTITION_TABLE_HEADER),
    ("NumberOfPartitions",  UINT64),
    ("Partitions",          UefiGpt.EFI_PARTITION_ENTRY * 1)
  ]

TCG_DEVICE_SECURITY_EVENT_DATA_SIGNATURE  = b"SPDM Device Sec"
TCG_DEVICE_SECURITY_EVENT_DATA_VERSION    = 1

TCG_DEVICE_SECURITY_EVENT_DATA_DEVICE_TYPE_NULL  = 0
TCG_DEVICE_SECURITY_EVENT_DATA_DEVICE_TYPE_PCI   = 1
TCG_DEVICE_SECURITY_EVENT_DATA_DEVICE_TYPE_USB   = 2

class TCG_DEVICE_SECURITY_EVENT_DATA_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",   UINT8 * 16),
    ("Version",     UINT16),
    ("Length",      UINT16),
    ("SpdmHashAlgo",UINT32),
    ("DeviceType",  UINT32)
    # ("SpdmMeasurementBlock",  SPDM_MEASUREMENT_BLOCK)
  ]

TCG_DEVICE_SECURITY_EVENT_DATA_PCI_CONTEXT_VERSION  = 0

class TCG_DEVICE_SECURITY_EVENT_DATA_PCI_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",             UINT16),
    ("Length",              UINT16),
    ("VendorId",            UINT16),
    ("DeviceId",            UINT16),
    ("RevisionID",          UINT8),
    ("ClassCode",           UINT8 * 3),
    ("SubsystemVendorID",   UINT16),
    ("SubsystemID",         UINT16)
  ]

TCG_DEVICE_SECURITY_EVENT_DATA_USB_CONTEXT_VERSION  = 0

class TCG_DEVICE_SECURITY_EVENT_DATA_USB_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",             UINT16),
    ("Length",              UINT16),

    # ("DeviceDescriptor",        UINT8 * DescLen),
    # ("BodDescriptor",           UINT8 * DescLen),
    # ("ConfigurationDescriptor",(UINT8 * NumOfConfiguration) * DescLen)
  ]

class TCG_PCR_EVENT2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digest",    Tpm20.TPML_DIGEST_VALUES),
    ("EventSize", UINT32),
    ("Event",     UINT8 * 1)
  ]

class TCG_PCR_EVENT2_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PCRIndex",  TCG_PCRINDEX),
    ("EventType", TCG_EVENTTYPE),
    ("Digests",   Tpm20.TPML_DIGEST_VALUES),
    ("EventSize", UINT32)
  ]

class TCG_EfiSpecIdEventAlgorithmSize (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmId", UINT16),
    ("digestSize",  UINT16)
  ]

TCG_EfiSpecIDEventStruct_SIGNATURE_02  = b"Spec ID Event02"
TCG_EfiSpecIDEventStruct_SIGNATURE_03  = b"Spec ID Event03"

TCG_EfiSpecIDEventStruct_SPEC_VERSION_MAJOR_TPM12  = 1
TCG_EfiSpecIDEventStruct_SPEC_VERSION_MINOR_TPM12  = 2
TCG_EfiSpecIDEventStruct_SPEC_ERRATA_TPM12         = 2

TCG_EfiSpecIDEventStruct_SPEC_VERSION_MAJOR_TPM2   = 2
TCG_EfiSpecIDEventStruct_SPEC_VERSION_MINOR_TPM2   = 0
TCG_EfiSpecIDEventStruct_SPEC_ERRATA_TPM2          = 0
TCG_EfiSpecIDEventStruct_SPEC_ERRATA_TPM2_REV_105  = 105

class TCG_EfiSpecIDEventStruct (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("signature",           UINT8 * 16),
    ("platformClass",       UINT32),
    ("specVersionMinor",    UINT8),
    ("specVersionMajor",    UINT8),
    ("specErrata",          UINT8),
    ("uintnSize",           UINT8)
    # ("numberOfAlgorithms",  UINT32),
    # ("digestSize",          TCG_EfiSpecIdEventAlgorithmSize * numberOfAlgorithms),
    # ("vendorInfoSize",      UINT8),
    # ("vendorInfo",          UINT8 * vendorInfoSize)
  ]

class TCG_PCClientTaggedEvent (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("taggedEventID",       UINT32),
    ("taggedEventDataSize", UINT32)
    # ("taggedEventData",     UINT8 * taggedEventDataSize)
  ]

TCG_Sp800_155_PlatformId_Event_SIGNATURE   = b"SP800-155 Event"
TCG_Sp800_155_PlatformId_Event2_SIGNATURE  = b"SP800-155 Event2"

class TCG_Sp800_155_PlatformId_Event2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",               UINT8 * 16),
    ("VendorId",                UINT32),
    ("ReferenceManifestGuid",   EFI_GUID)
    # ("PlatformManufacturerStrSize",   UINT8),
    # ("PlatformManufacturerStr",       UINT8 * PlatformManufacturerStrSize),
    # ("PlatformModelSize",             UINT8),
    # ("PlatformModel",                 UINT8 * PlatformModelSize),
    # ("PlatformVersionSize",           UINT8),
    # ("PlatformVersion",               UINT8 * PlatformVersionSize),
    # ("PlatformModelSize",             UINT8),
    # ("PlatformModel",                 UINT8 * PlatformModelSize),
    # ("FirmwareManufacturerStrSize",   UINT8),
    # ("FirmwareManufacturerStr",       UINT8 * FirmwareManufacturerStrSize),
    # ("FirmwareManufacturerId",        UINT32),
    # ("FirmwareVersion",               UINT8),
    # ("FirmwareVersion",               UINT8 * FirmwareVersionSize)
  ]

TCG_EfiStartupLocalityEvent_SIGNATURE  = b"StartupLocality"
LOCALITY_0_INDICATOR  = 0x00
LOCALITY_3_INDICATOR  = 0x03

class TCG_EfiStartupLocalityEvent (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT8 * 16),
    ("StartupLocality", UINT8)
  ]

