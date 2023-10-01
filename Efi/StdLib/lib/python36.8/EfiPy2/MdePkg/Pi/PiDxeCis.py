# PiDxeCis.py
#
# EfiPy2.MdePkg.Pi.PiDxeCis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

EfiGcdMemoryTypeNonExistent = 0
EfiGcdMemoryTypeReserved = 1
EfiGcdMemoryTypeSystemMemory = 2
EfiGcdMemoryTypeMemoryMappedIo = 3
EfiGcdMemoryTypePersistentMemory = 4
EfiGcdMemoryTypeMoreReliable = 5
EfiGcdMemoryTypeMaximum      = 6
EFI_GCD_MEMORY_TYPE         = ENUM

EfiGcdIoTypeNonExistent = 0
EfiGcdIoTypeReserved = 1
EfiGcdIoTypeIo = 2
EfiGcdIoTypeMaximum = 3
EFI_GCD_IO_TYPE     = ENUM

EfiGcdAllocateAnySearchBottomUp = 1
EfiGcdAllocateMaxAddressSearchBottomUp = 2
EfiGcdAllocateAddress = 3
EfiGcdAllocateAnySearchTopDown = 4
EfiGcdAllocateMaxAddressSearchTopDown = 5
EfiGcdMaxAllocateType = 6
EFI_GCD_ALLOCATE_TYPE = ENUM

class EFI_GCD_MEMORY_SPACE_DESCRIPTOR (Structure):
  _fields_ = [
    ("BaseAddress",   EFI_PHYSICAL_ADDRESS),
    ("Length",        UINT64),
    ("Capabilities",  UINT64),
    ("Attributes",    UINT64),
    ("GcdMemoryType", EFI_GCD_MEMORY_TYPE),
    ("ImageHandle",   EFI_HANDLE),
    ("DeviceHandle",  EFI_HANDLE)
  ]

class EFI_GCD_IO_SPACE_DESCRIPTOR (Structure):
  _fields_ = [
    ("BaseAddress",   EFI_PHYSICAL_ADDRESS),
    ("Length",        UINT64),
    ("GcdIoType",     EFI_GCD_IO_TYPE),
    ("ImageHandle",   EFI_HANDLE),
    ("DeviceHandle",  EFI_HANDLE)
  ]

EFI_ADD_MEMORY_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_GCD_MEMORY_TYPE,  # IN GcdMemoryType,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64,               # IN Length,
  UINT64                # IN Capabilities
  )

EFI_ALLOCATE_MEMORY_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_GCD_ALLOCATE_TYPE,              # IN     GcdAllocateType,
  EFI_GCD_MEMORY_TYPE,                # IN     GcdMemoryType,
  UINTN,                              # IN     Alignment,
  UINT64,                             # IN     Length,
  POINTER(EFI_PHYSICAL_ADDRESS),      # IN OUT *BaseAddress,
  EFI_HANDLE,                         # IN     ImageHandle,
  EFI_HANDLE                          # IN     DeviceHandle OPTIONAL
  )

EFI_FREE_MEMORY_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64                # IN Length
  )

EFI_REMOVE_MEMORY_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64                # IN Length
  )

EFI_GET_MEMORY_SPACE_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS,                     # IN    BaseAddress,
  POINTER(EFI_GCD_MEMORY_SPACE_DESCRIPTOR)  # OUT  *Descriptor
  )

EFI_SET_MEMORY_SPACE_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64,               # IN Length,
  UINT64                # IN Attributes
  )

EFI_SET_MEMORY_SPACE_CAPABILITIES = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64,               # IN Length,
  UINT64                # IN Capabilities
  )

EFI_GET_MEMORY_SPACE_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINTN),                                   # OUT *NumberOfDescriptors,
  POINTER(POINTER(EFI_GCD_MEMORY_SPACE_DESCRIPTOR)) # OUT **MemorySpaceMap
  )

EFI_ADD_IO_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_GCD_IO_TYPE,      # IN GcdIoType,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64                # IN Length
  )

EFI_ALLOCATE_IO_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_GCD_ALLOCATE_TYPE,              # IN     GcdAllocateType,
  EFI_GCD_IO_TYPE,                    # IN     GcdIoType,
  UINTN,                              # IN     Alignment,
  UINT64,                             # IN     Length,
  POINTER(EFI_PHYSICAL_ADDRESS),      # IN OUT *BaseAddress,
  EFI_HANDLE,                         # IN     ImageHandle,
  EFI_HANDLE                          # IN     DeviceHandle OPTIONAL
  )

EFI_FREE_IO_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64                # IN Length
  )

EFI_REMOVE_IO_SPACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN BaseAddress,
  UINT64                # IN Length
  )

EFI_GET_IO_SPACE_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS,                 # IN  BaseAddress,
  POINTER(EFI_GCD_IO_SPACE_DESCRIPTOR)  # OUT *Descriptor
  )

EFI_GET_IO_SPACE_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINTN),                               # OUT *NumberOfDescriptors,
  POINTER(POINTER(EFI_GCD_IO_SPACE_DESCRIPTOR)) # OUT **IoSpaceMap
  )

EFI_DISPATCH = CFUNCTYPE (
  EFI_STATUS
  )

EFI_SCHEDULE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,       # IN FirmwareVolumeHandle,
  POINTER(EFI_GUID) # IN CONST *FileName
  )

EFI_TRUST = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,       # IN FirmwareVolumeHandle,
  POINTER(EFI_GUID) # IN CONST *FileName
  )

EFI_PROCESS_FIRMWARE_VOLUME = CFUNCTYPE (
  EFI_STATUS,
  PVOID,              # IN CONST  *FirmwareVolumeHeader,
  UINTN,              # IN        Size,
  POINTER(EFI_HANDLE) # OUT       *FirmwareVolumeHandle
  )

DXE_SERVICES_SIGNATURE            = 0x565245535f455844
DXE_SPECIFICATION_MAJOR_REVISION  = 1
DXE_SPECIFICATION_MINOR_REVISION  = 70
DXE_SERVICES_REVISION             = (DXE_SPECIFICATION_MAJOR_REVISION<<16) | (DXE_SPECIFICATION_MINOR_REVISION)

class DXE_SERVICES (Structure):
  _fields_ = [
    ("Hdr",                         EFI_TABLE_HEADER),
    ("AddMemorySpace",              EFI_ADD_MEMORY_SPACE),
    ("AllocateMemorySpace",         EFI_ALLOCATE_MEMORY_SPACE),
    ("FreeMemorySpace",             EFI_FREE_MEMORY_SPACE),
    ("RemoveMemorySpace",           EFI_REMOVE_MEMORY_SPACE),
    ("GetMemorySpaceDescriptor",    EFI_GET_MEMORY_SPACE_DESCRIPTOR),
    ("SetMemorySpaceAttributes",    EFI_SET_MEMORY_SPACE_ATTRIBUTES),
    ("GetMemorySpaceMap",           EFI_GET_MEMORY_SPACE_MAP),
    ("AddIoSpace",                  EFI_ADD_IO_SPACE),
    ("AllocateIoSpace",             EFI_ALLOCATE_IO_SPACE),
    ("FreeIoSpace",                 EFI_FREE_IO_SPACE),
    ("RemoveIoSpace",               EFI_REMOVE_IO_SPACE),
    ("GetIoSpaceDescriptor",        EFI_GET_IO_SPACE_DESCRIPTOR),
    ("GetIoSpaceMap",               EFI_GET_IO_SPACE_MAP),
    ("Dispatch",                    EFI_DISPATCH),
    ("Schedule",                    EFI_SCHEDULE),
    ("Trust",                       EFI_TRUST),
    ("ProcessFirmwareVolume",       EFI_PROCESS_FIRMWARE_VOLUME),
    ("SetMemorySpaceCapabilities",  EFI_SET_MEMORY_SPACE_CAPABILITIES)
  ]

EFI_DXE_SERVICES  = DXE_SERVICES

