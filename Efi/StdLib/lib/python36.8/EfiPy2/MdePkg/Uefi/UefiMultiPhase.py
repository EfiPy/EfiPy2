# UefiMultiPhase.py
#
# EfiPy2.MdePkg.Uefi.UefiMultiPhase
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.Uefi.UefiBaseType   import *
from EfiPy2.MdePkg.Guid.WinCertificate import WIN_CERTIFICATE_UEFI_GUID

EfiReservedMemoryType       =  0
EfiLoaderCode               =  1
EfiLoaderData               =  2
EfiBootServicesCode         =  3
EfiBootServicesData         =  4
EfiRuntimeServicesCode      =  5
EfiRuntimeServicesData      =  6
EfiConventionalMemory       =  7
EfiUnusableMemory           =  8
EfiACPIReclaimMemory        =  9
EfiACPIMemoryNVS            = 10
EfiMemoryMappedIO           = 11
EfiMemoryMappedIOPortSpace  = 12
EfiPalCode                  = 13
EfiPersistentMemory         = 14
EfiMaxMemoryType            = 15
EFI_MEMORY_TYPE = ENUM

EfiResetCold                =  0
EfiResetWarm                =  1
EfiResetShutdown            =  2
EfiResetPlatformSpecific    =  3
EFI_RESET_TYPE = ENUM

class EFI_TABLE_HEADER (Structure):
  _fields_ = [
    ("Signature",   UINT64),
    ("Revision",    UINT32),
    ("HeaderSize",  UINT32),
    ("CRC32",       UINT32),
    ("Reserved",    UINT32)
    ]

EFI_VARIABLE_NON_VOLATILE                            = 0x00000001
EFI_VARIABLE_BOOTSERVICE_ACCESS                      = 0x00000002
EFI_VARIABLE_RUNTIME_ACCESS                          = 0x00000004

EFI_VARIABLE_HARDWARE_ERROR_RECORD                   = 0x00000008

EFI_VARIABLE_AUTHENTICATED_WRITE_ACCESS              = 0x00000010
EFI_VARIABLE_TIME_BASED_AUTHENTICATED_WRITE_ACCESS   = 0x00000020
EFI_VARIABLE_APPEND_WRITE                            = 0x00000040

class EFI_VARIABLE_AUTHENTICATION (Structure):
  _fields_ = [
    ("MonotonicCount",   UINT64),
    ("AuthInfo",         WIN_CERTIFICATE_UEFI_GUID)
    ]

class EFI_VARIABLE_AUTHENTICATION_2 (Structure):
  _fields_ = [
    ("TimeStamp",   EFI_TIME),
    ("AuthInfo",    WIN_CERTIFICATE_UEFI_GUID)
    ]

