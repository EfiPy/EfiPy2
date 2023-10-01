# PiHob.py
#
# EfiPy2.MdePkg.Pi.PiHob
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2                      import *
from EfiPy2.MdePkg.Pi.PiBootMode import EFI_BOOT_MODE

EFI_HOB_TYPE_HANDOFF              = 0x0001
EFI_HOB_TYPE_MEMORY_ALLOCATION    = 0x0002
EFI_HOB_TYPE_RESOURCE_DESCRIPTOR  = 0x0003
EFI_HOB_TYPE_GUID_EXTENSION       = 0x0004
EFI_HOB_TYPE_FV                   = 0x0005
EFI_HOB_TYPE_CPU                  = 0x0006
EFI_HOB_TYPE_MEMORY_POOL          = 0x0007
EFI_HOB_TYPE_FV2                  = 0x0009
EFI_HOB_TYPE_LOAD_PEIM_UNUSED     = 0x000A
EFI_HOB_TYPE_UEFI_CAPSULE         = 0x000B
EFI_HOB_TYPE_FV3                  = 0x000C
EFI_HOB_TYPE_UNUSED               = 0xFFFE
EFI_HOB_TYPE_END_OF_HOB_LIST      = 0xFFFF

class EFI_HOB_GENERIC_HEADER (Structure):
  _fields_ = [
    ("HobType",   UINT16),
    ("HobLength", UINT16),
    ("Reserved",  UINT32)
  ]

EFI_HOB_HANDOFF_TABLE_VERSION = 0x0009

class EFI_HOB_HANDOFF_INFO_TABLE (Structure):
  _fields_ = [
    ("Header",              EFI_HOB_GENERIC_HEADER),
    ("Version",             UINT32),
    ("BootMode",            EFI_BOOT_MODE),
    ("EfiMemoryTop",        EFI_PHYSICAL_ADDRESS),
    ("EfiMemoryBottom",     EFI_PHYSICAL_ADDRESS),
    ("EfiFreeMemoryTop",    EFI_PHYSICAL_ADDRESS),
    ("EfiFreeMemoryBottom", EFI_PHYSICAL_ADDRESS),
    ("EfiEndOfHobList",     EFI_PHYSICAL_ADDRESS)
  ]

class EFI_HOB_MEMORY_ALLOCATION_HEADER (Structure):
  _fields_ = [
    ("Name",              EFI_GUID),
    ("MemoryBaseAddress", EFI_PHYSICAL_ADDRESS),
    ("MemoryLength",      UINT64),
    ("MemoryType",        EFI_MEMORY_TYPE),
    ("Reserved",          UINT8 * 4)
  ]

class EFI_HOB_MEMORY_ALLOCATION (Structure):
  _fields_ = [
    ("Header",          EFI_HOB_GENERIC_HEADER),
    ("AllocDescriptor", EFI_HOB_MEMORY_ALLOCATION_HEADER)
  ]

class EFI_HOB_MEMORY_ALLOCATION_STACK (Structure):
  _fields_ = [
    ("Header",          EFI_HOB_GENERIC_HEADER),
    ("AllocDescriptor", EFI_HOB_MEMORY_ALLOCATION_HEADER)
  ]

class EFI_HOB_MEMORY_ALLOCATION_BSP_STORE (Structure):
  _fields_ = [
    ("Header",          EFI_HOB_GENERIC_HEADER),
    ("AllocDescriptor", EFI_HOB_MEMORY_ALLOCATION_HEADER)
  ]

class EFI_HOB_MEMORY_ALLOCATION_MODULE (Structure):
  _fields_ = [
    ("Header",                  EFI_HOB_GENERIC_HEADER),
    ("MemoryAllocationHeader",  EFI_HOB_MEMORY_ALLOCATION_HEADER),
    ("ModuleName",              EFI_GUID),
    ("EntryPoint",              EFI_PHYSICAL_ADDRESS)
  ]

EFI_RESOURCE_TYPE                       = UINT32

EFI_RESOURCE_SYSTEM_MEMORY          = 0x00000000
EFI_RESOURCE_MEMORY_MAPPED_IO       = 0x00000001
EFI_RESOURCE_IO                     = 0x00000002
EFI_RESOURCE_FIRMWARE_DEVICE        = 0x00000003
EFI_RESOURCE_MEMORY_MAPPED_IO_PORT  = 0x00000004
EFI_RESOURCE_MEMORY_RESERVED        = 0x00000005
EFI_RESOURCE_IO_RESERVED            = 0x00000006

EFI_RESOURCE_MAX_MEMORY_TYPE        = 0x00000008

EFI_RESOURCE_ATTRIBUTE_TYPE             = UINT32

EFI_RESOURCE_ATTRIBUTE_PRESENT                  = 0x00000001
EFI_RESOURCE_ATTRIBUTE_INITIALIZED              = 0x00000002
EFI_RESOURCE_ATTRIBUTE_TESTED                   = 0x00000004
EFI_RESOURCE_ATTRIBUTE_READ_PROTECTED           = 0x00000080

EFI_RESOURCE_ATTRIBUTE_WRITE_PROTECTED          = 0x00000100
EFI_RESOURCE_ATTRIBUTE_EXECUTION_PROTECTED      = 0x00000200
EFI_RESOURCE_ATTRIBUTE_PERSISTENT               = 0x00800000

EFI_RESOURCE_ATTRIBUTE_SINGLE_BIT_ECC           = 0x00000008
EFI_RESOURCE_ATTRIBUTE_MULTIPLE_BIT_ECC         = 0x00000010
EFI_RESOURCE_ATTRIBUTE_ECC_RESERVED_1           = 0x00000020
EFI_RESOURCE_ATTRIBUTE_ECC_RESERVED_2           = 0x00000040
EFI_RESOURCE_ATTRIBUTE_UNCACHEABLE              = 0x00000400
EFI_RESOURCE_ATTRIBUTE_WRITE_COMBINEABLE        = 0x00000800
EFI_RESOURCE_ATTRIBUTE_WRITE_THROUGH_CACHEABLE  = 0x00001000
EFI_RESOURCE_ATTRIBUTE_WRITE_BACK_CACHEABLE     = 0x00002000
EFI_RESOURCE_ATTRIBUTE_16_BIT_IO                = 0x00004000
EFI_RESOURCE_ATTRIBUTE_32_BIT_IO                = 0x00008000
EFI_RESOURCE_ATTRIBUTE_64_BIT_IO                = 0x00010000
EFI_RESOURCE_ATTRIBUTE_UNCACHED_EXPORTED        = 0x00020000
EFI_RESOURCE_ATTRIBUTE_READ_PROTECTABLE         = 0x00100000

EFI_RESOURCE_ATTRIBUTE_WRITE_PROTECTABLE        = 0x00200000
EFI_RESOURCE_ATTRIBUTE_EXECUTION_PROTECTABLE    = 0x00400000
EFI_RESOURCE_ATTRIBUTE_PERSISTABLE              = 0x01000000

EFI_RESOURCE_ATTRIBUTE_READ_ONLY_PROTECTED      = 0x00040000
EFI_RESOURCE_ATTRIBUTE_READ_ONLY_PROTECTABLE    = 0x00800000

EFI_RESOURCE_ATTRIBUTE_MORE_RELIABLE            = 0x02000000

class EFI_HOB_RESOURCE_DESCRIPTOR (Structure):
  _fields_ = [
    ("Header",            EFI_HOB_GENERIC_HEADER),
    ("Owner",             EFI_GUID),
    ("ResourceType",      EFI_RESOURCE_TYPE),
    ("ResourceAttribute", EFI_RESOURCE_ATTRIBUTE_TYPE),
    ("PhysicalStart",     EFI_PHYSICAL_ADDRESS),
    ("ResourceLength",    UINT64)
  ]

class EFI_HOB_GUID_TYPE (Structure):
  _fields_ = [
    ("Header",  EFI_HOB_GENERIC_HEADER),
    ("Name",    EFI_GUID)
  ]

class EFI_HOB_FIRMWARE_VOLUME (Structure):
  _fields_ = [
    ("Header",      EFI_HOB_GENERIC_HEADER),
    ("BaseAddress", EFI_PHYSICAL_ADDRESS),
    ("Length",      UINT64)
  ]

class EFI_HOB_FIRMWARE_VOLUME2 (Structure):
  _fields_ = [
    ("Header",      EFI_HOB_GENERIC_HEADER),
    ("BaseAddress", EFI_PHYSICAL_ADDRESS),
    ("Length",      UINT64),
    ("FvName",      EFI_GUID),
    ("FileName",    EFI_GUID)
  ]

class EFI_HOB_FIRMWARE_VOLUME3 (Structure):
  _fields_ = [
    ("Header",                  EFI_HOB_GENERIC_HEADER),
    ("BaseAddress",             EFI_PHYSICAL_ADDRESS),
    ("Length",                  UINT64),
    ("AuthenticationStatus",    UINT32),
    ("ExtractedFv",             BOOLEAN),
    ("FvName",                  EFI_GUID),
    ("FileName",                EFI_GUID)
  ]

class EFI_HOB_CPU (Structure):
  _fields_ = [
    ("Header",            EFI_HOB_GENERIC_HEADER),
    ("SizeOfMemorySpace", UINT8),
    ("SizeOfIoSpace",     UINT8),
    ("Reserved",          UINT8 * 6)
  ]

class EFI_HOB_MEMORY_POOL (Structure):
  _fields_ = [
    ("Header",  EFI_HOB_GENERIC_HEADER)
  ]

class EFI_HOB_UEFI_CAPSULE (Structure):
  _fields_ = [
    ("Header",      EFI_HOB_GENERIC_HEADER),
    ("BaseAddress", EFI_PHYSICAL_ADDRESS),
    ("Length",      UINT64)
  ]

class EFI_PEI_HOB_POINTERS (Union):
  _fields_ = [
    ("Header",                    POINTER(EFI_HOB_GENERIC_HEADER)),
    ("HandoffInformationTable",   POINTER(EFI_HOB_HANDOFF_INFO_TABLE)),
    ("MemoryAllocation",          POINTER(EFI_HOB_MEMORY_ALLOCATION)),
    ("MemoryAllocationBspStore",  POINTER(EFI_HOB_MEMORY_ALLOCATION_BSP_STORE)),
    ("MemoryAllocationStack",     POINTER(EFI_HOB_MEMORY_ALLOCATION_STACK )),
    ("MemoryAllocationModule",    POINTER(EFI_HOB_MEMORY_ALLOCATION_MODULE)),
    ("ResourceDescriptor",        POINTER(EFI_HOB_RESOURCE_DESCRIPTOR)),
    ("Guid",                      POINTER(EFI_HOB_GUID_TYPE)),
    ("FirmwareVolume",            POINTER(EFI_HOB_FIRMWARE_VOLUME )),
    ("FirmwareVolume2",           POINTER(EFI_HOB_FIRMWARE_VOLUME2)),
    ("FirmwareVolume3",           POINTER(EFI_HOB_FIRMWARE_VOLUME3)),
    ("Cpu",                       POINTER(EFI_HOB_CPU)),
    ("Pool",                      POINTER(EFI_HOB_MEMORY_POOL)),
    ("Capsule",                   POINTER(EFI_HOB_UEFI_CAPSULE)),
    ("Raw",                       POINTER(UINT8))
  ]

