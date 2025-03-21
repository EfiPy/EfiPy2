# Smbios.py
#
# EfiPy2.MdePkg.Protocol.Smbios
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard import SmBios

gEfiSmbiosProtocolGuid    = \
  EFI_GUID (0x3583ff6, 0xcb36, 0x4940, ( 0x94, 0x7e, 0xb9, 0xb3, 0x9f, 0x4a, 0xfa, 0xf7 ))

EFI_SMBIOS_TYPE_BIOS_INFORMATION                      = SmBios.SMBIOS_TYPE_BIOS_INFORMATION
EFI_SMBIOS_TYPE_SYSTEM_INFORMATION                    = SmBios.SMBIOS_TYPE_SYSTEM_INFORMATION
EFI_SMBIOS_TYPE_BASEBOARD_INFORMATION                 = SmBios.SMBIOS_TYPE_BASEBOARD_INFORMATION
EFI_SMBIOS_TYPE_SYSTEM_ENCLOSURE                      = SmBios.SMBIOS_TYPE_SYSTEM_ENCLOSURE
EFI_SMBIOS_TYPE_PROCESSOR_INFORMATION                 = SmBios.SMBIOS_TYPE_PROCESSOR_INFORMATION
EFI_SMBIOS_TYPE_MEMORY_CONTROLLER_INFORMATION         = SmBios.SMBIOS_TYPE_MEMORY_CONTROLLER_INFORMATION
EFI_SMBIOS_TYPE_MEMORY_MODULE_INFORMATON              = SmBios.SMBIOS_TYPE_MEMORY_MODULE_INFORMATON
EFI_SMBIOS_TYPE_CACHE_INFORMATION                     = SmBios.SMBIOS_TYPE_CACHE_INFORMATION
EFI_SMBIOS_TYPE_PORT_CONNECTOR_INFORMATION            = SmBios.SMBIOS_TYPE_PORT_CONNECTOR_INFORMATION
EFI_SMBIOS_TYPE_SYSTEM_SLOTS                          = SmBios.SMBIOS_TYPE_SYSTEM_SLOTS
EFI_SMBIOS_TYPE_ONBOARD_DEVICE_INFORMATION            = SmBios.SMBIOS_TYPE_ONBOARD_DEVICE_INFORMATION
EFI_SMBIOS_TYPE_OEM_STRINGS                           = SmBios.SMBIOS_TYPE_OEM_STRINGS
EFI_SMBIOS_TYPE_SYSTEM_CONFIGURATION_OPTIONS          = SmBios.SMBIOS_TYPE_SYSTEM_CONFIGURATION_OPTIONS
EFI_SMBIOS_TYPE_BIOS_LANGUAGE_INFORMATION             = SmBios.SMBIOS_TYPE_BIOS_LANGUAGE_INFORMATION
EFI_SMBIOS_TYPE_GROUP_ASSOCIATIONS                    = SmBios.SMBIOS_TYPE_GROUP_ASSOCIATIONS
EFI_SMBIOS_TYPE_SYSTEM_EVENT_LOG                      = SmBios.SMBIOS_TYPE_SYSTEM_EVENT_LOG
EFI_SMBIOS_TYPE_PHYSICAL_MEMORY_ARRAY                 = SmBios.SMBIOS_TYPE_PHYSICAL_MEMORY_ARRAY
EFI_SMBIOS_TYPE_MEMORY_DEVICE                         = SmBios.SMBIOS_TYPE_MEMORY_DEVICE
EFI_SMBIOS_TYPE_32BIT_MEMORY_ERROR_INFORMATION        = SmBios.SMBIOS_TYPE_32BIT_MEMORY_ERROR_INFORMATION
EFI_SMBIOS_TYPE_MEMORY_ARRAY_MAPPED_ADDRESS           = SmBios.SMBIOS_TYPE_MEMORY_ARRAY_MAPPED_ADDRESS
EFI_SMBIOS_TYPE_MEMORY_DEVICE_MAPPED_ADDRESS          = SmBios.SMBIOS_TYPE_MEMORY_DEVICE_MAPPED_ADDRESS
EFI_SMBIOS_TYPE_BUILT_IN_POINTING_DEVICE              = SmBios.SMBIOS_TYPE_BUILT_IN_POINTING_DEVICE
EFI_SMBIOS_TYPE_PORTABLE_BATTERY                      = SmBios.SMBIOS_TYPE_PORTABLE_BATTERY
EFI_SMBIOS_TYPE_SYSTEM_RESET                          = SmBios.SMBIOS_TYPE_SYSTEM_RESET
EFI_SMBIOS_TYPE_HARDWARE_SECURITY                     = SmBios.SMBIOS_TYPE_HARDWARE_SECURITY
EFI_SMBIOS_TYPE_SYSTEM_POWER_CONTROLS                 = SmBios.SMBIOS_TYPE_SYSTEM_POWER_CONTROLS
EFI_SMBIOS_TYPE_VOLTAGE_PROBE                         = SmBios.SMBIOS_TYPE_VOLTAGE_PROBE
EFI_SMBIOS_TYPE_COOLING_DEVICE                        = SmBios.SMBIOS_TYPE_COOLING_DEVICE
EFI_SMBIOS_TYPE_TEMPERATURE_PROBE                     = SmBios.SMBIOS_TYPE_TEMPERATURE_PROBE
EFI_SMBIOS_TYPE_ELECTRICAL_CURRENT_PROBE              = SmBios.SMBIOS_TYPE_ELECTRICAL_CURRENT_PROBE
EFI_SMBIOS_TYPE_OUT_OF_BAND_REMOTE_ACCESS             = SmBios.SMBIOS_TYPE_OUT_OF_BAND_REMOTE_ACCESS
EFI_SMBIOS_TYPE_BOOT_INTEGRITY_SERVICE                = SmBios.SMBIOS_TYPE_BOOT_INTEGRITY_SERVICE
EFI_SMBIOS_TYPE_SYSTEM_BOOT_INFORMATION               = SmBios.SMBIOS_TYPE_SYSTEM_BOOT_INFORMATION
EFI_SMBIOS_TYPE_64BIT_MEMORY_ERROR_INFORMATION        = SmBios.SMBIOS_TYPE_64BIT_MEMORY_ERROR_INFORMATION
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE                     = SmBios.SMBIOS_TYPE_MANAGEMENT_DEVICE
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE_COMPONENT           = SmBios.SMBIOS_TYPE_MANAGEMENT_DEVICE_COMPONENT
EFI_SMBIOS_TYPE_MANAGEMENT_DEVICE_THRESHOLD_DATA      = SmBios.SMBIOS_TYPE_MANAGEMENT_DEVICE_THRESHOLD_DATA
EFI_SMBIOS_TYPE_MEMORY_CHANNEL                        = SmBios.SMBIOS_TYPE_MEMORY_CHANNEL
EFI_SMBIOS_TYPE_IPMI_DEVICE_INFORMATION               = SmBios.SMBIOS_TYPE_IPMI_DEVICE_INFORMATION
EFI_SMBIOS_TYPE_SYSTEM_POWER_SUPPLY                   = SmBios.SMBIOS_TYPE_SYSTEM_POWER_SUPPLY
EFI_SMBIOS_TYPE_ADDITIONAL_INFORMATION                = SmBios.SMBIOS_TYPE_ADDITIONAL_INFORMATION
EFI_SMBIOS_TYPE_ONBOARD_DEVICES_EXTENDED_INFORMATION  = SmBios.SMBIOS_TYPE_ONBOARD_DEVICES_EXTENDED_INFORMATION
EFI_SMBIOS_TYPE_MANAGEMENT_CONTROLLER_HOST_INTERFACE  = SmBios.SMBIOS_TYPE_MANAGEMENT_CONTROLLER_HOST_INTERFACE
EFI_SMBIOS_TYPE_TPM_DEVICE                            = SmBios.SMBIOS_TYPE_TPM_DEVICE
EFI_SMBIOS_TYPE_PROCESSOR_ADDITIONAL_INFORMATION      = SmBios.SMBIOS_TYPE_PROCESSOR_ADDITIONAL_INFORMATION
EFI_SMBIOS_TYPE_FIRMWARE_INVENTORY_INFORMATION        = SmBios.SMBIOS_TYPE_FIRMWARE_INVENTORY_INFORMATION
EFI_SMBIOS_TYPE_STRING_PROPERTY_INFORMATION           = SmBios.SMBIOS_TYPE_STRING_PROPERTY_INFORMATION
EFI_SMBIOS_TYPE_INACTIVE                              = SmBios.SMBIOS_TYPE_INACTIVE
EFI_SMBIOS_TYPE_END_OF_TABLE                          = SmBios.SMBIOS_TYPE_END_OF_TABLE
EFI_SMBIOS_OEM_BEGIN                                  = SmBios.SMBIOS_OEM_BEGIN
EFI_SMBIOS_OEM_END                                    = SmBios.SMBIOS_OEM_END

EFI_SMBIOS_STRING       = SmBios.SMBIOS_TABLE_STRING
EFI_SMBIOS_TYPE         = SmBios.SMBIOS_TYPE
EFI_SMBIOS_HANDLE       = SmBios.SMBIOS_HANDLE
EFI_SMBIOS_TABLE_HEADER = SmBios.SMBIOS_STRUCTURE
class EFI_SMBIOS_PROTOCOL (Structure):
  pass

EFI_SMBIOS_ADD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN      *This
  EFI_HANDLE,                           # IN      ProducerHandle OPTIONAL,
  POINTER(EFI_SMBIOS_HANDLE),           # IN OUT  *SmbiosHandle,
  POINTER(EFI_SMBIOS_TABLE_HEADER)      # IN      *Record
  )

EFI_SMBIOS_UPDATE_STRING = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN *This
  POINTER(EFI_SMBIOS_HANDLE),           # IN *SmbiosHandle,
  POINTER(UINTN),                       # IN *StringNumber,
  PCHAR8                                # IN *String
  )

EFI_SMBIOS_REMOVE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),         # IN *This
  EFI_SMBIOS_HANDLE                     # IN SmbiosHandle
  )

EFI_SMBIOS_GET_NEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SMBIOS_PROTOCOL),               # IN  *This
  POINTER(EFI_SMBIOS_HANDLE),                 # IN  *SmbiosHandle,
  POINTER(EFI_SMBIOS_TYPE),                   # IN  *Type              OPTIONAL,
  POINTER(POINTER(EFI_SMBIOS_TABLE_HEADER)),  # OUT **Record,
  POINTER(EFI_HANDLE)                         # OUT *ProducerHandle    OPTIONAL
  )

EFI_SMBIOS_PROTOCOL._fields_ = [
    ("Add",           EFI_SMBIOS_ADD),
    ("UpdateString",  EFI_SMBIOS_UPDATE_STRING),
    ("Remove",        EFI_SMBIOS_REMOVE),
    ("GetNext",       EFI_SMBIOS_GET_NEXT),
    ("MajorVersion",  UINT8),
    ("MinorVersion",  UINT8)
  ]

