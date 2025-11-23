# PiPeiCis.py
#
# EfiPy2.MdePkg.Pi.PiPeiCis
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi        import PiMultiPhase, PiBootMode, PiFirmwareFile, PiStatusCode, PiFirmwareVolume
from EfiPy2.MdePkg.Pi.PiMultiPhase import PI_SPECIFICATION_MAJOR_REVISION, PI_SPECIFICATION_MINOR_REVISION

EFI_PEI_FV_HANDLE   = PVOID

EFI_PEI_FILE_HANDLE = PVOID

class EFI_PEI_SERVICES (Structure):
  pass

from EfiPy2.MdePkg.Ppi.CpuIo    import EFI_PEI_CPU_IO_PPI
from EfiPy2.MdePkg.Ppi.PciCfg2  import EFI_PEI_PCI_CFG2_PPI

class EFI_PEI_NOTIFY_DESCRIPTOR (Structure):
  pass

EFI_PEIM_ENTRY_POINT2 = CFUNCTYPE (
  EFI_STATUS,
  EFI_PEI_FILE_HANDLE,               # IN       FileHandle,
  POINTER(POINTER(EFI_PEI_SERVICES)) # IN CONST **PeiServices
  )

EFI_PEIM_NOTIFY_ENTRY_POINT = CFUNCTYPE (
  EFI_STATUS,
  POINTER((EFI_PEI_SERVICES)),          # IN **PeiServices,
  POINTER(EFI_PEI_NOTIFY_DESCRIPTOR),   # IN *NotifyDescriptor,
  PVOID                                 # IN *Ppi
  )

EFI_PEI_PPI_DESCRIPTOR_PIC              = 0x00000001
EFI_PEI_PPI_DESCRIPTOR_PPI              = 0x00000010
EFI_PEI_PPI_DESCRIPTOR_NOTIFY_CALLBACK  = 0x00000020
EFI_PEI_PPI_DESCRIPTOR_NOTIFY_DISPATCH  = 0x00000040
EFI_PEI_PPI_DESCRIPTOR_NOTIFY_TYPES     = 0x00000060
EFI_PEI_PPI_DESCRIPTOR_TERMINATE_LIST   = 0x80000000

class EFI_PEI_PPI_DESCRIPTOR (Structure):
  _fields_ = [
    ("Flags",   UINTN),
    ("Guid",    POINTER(EFI_GUID)),
    ("Ppi",     PVOID)
  ]

class EFI_PEI_PPI_DESCRIPTOR (Structure):
  _fields_ = [
    ("Flags",   UINTN),
    ("Guid",    POINTER(EFI_GUID)),
    ("Notify",  EFI_PEIM_NOTIFY_ENTRY_POINT)
  ]

class EFI_PEI_DESCRIPTOR (Union):
  _fields_ = [
    ("Notify",  EFI_PEI_NOTIFY_DESCRIPTOR),
    ("Ppi",     EFI_PEI_PPI_DESCRIPTOR)
  ]

EFI_PEI_INSTALL_PPI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  POINTER(EFI_PEI_PPI_DESCRIPTOR)       # IN CONST *PpiList
  )

EFI_PEI_REINSTALL_PPI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  POINTER(EFI_PEI_PPI_DESCRIPTOR),      # IN CONST *OldPpi,
  POINTER(EFI_PEI_PPI_DESCRIPTOR)       # IN CONST *NewPpi
  )

EFI_PEI_LOCATE_PPI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),       # IN CONST **PeiServices,
  POINTER(EFI_GUID),                        # IN CONST *Guid,
  UINTN,                                    # IN       Instance,
  POINTER(POINTER(EFI_PEI_PPI_DESCRIPTOR)), # IN OUT   **PpiDescriptor OPTIONAL,
  POINTER(PVOID)                            # IN OUT   **Ppi
  )

EFI_PEI_NOTIFY_PPI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),       # IN CONST **PeiServices,
  POINTER(EFI_PEI_NOTIFY_DESCRIPTOR)        # IN CONST *NotifyList
  )

EFI_PEI_GET_BOOT_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  POINTER(PiBootMode.EFI_BOOT_MODE)     # OUT      *BootMode
  )

EFI_PEI_SET_BOOT_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  PiBootMode.EFI_BOOT_MODE              # IN       *BootMode
  )

EFI_PEI_GET_HOB_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  POINTER(PVOID)                        # OUT      **HobList
  )

EFI_PEI_CREATE_HOB = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  UINT16,                               # IN       Type,
  UINT16,                               # IN       Length,
  POINTER(PVOID)                        # IN OUT   **Hob
  )

EFI_PEI_FFS_FIND_NEXT_VOLUME2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  UINTN,                                # IN  Instance,
  POINTER(EFI_PEI_FV_HANDLE)            # OUT *VolumeHandle
  )

EFI_PEI_FFS_FIND_NEXT_FILE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  PiFirmwareFile.EFI_FV_FILETYPE,       # IN       SearchType,
  EFI_PEI_FV_HANDLE,                    # IN CONST FvHandle,
  POINTER(EFI_PEI_FILE_HANDLE)          # IN OUT   *FileHandle
  )

EFI_PEI_FFS_FIND_SECTION_DATA2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  PiFirmwareFile.EFI_SECTION_TYPE,      # IN       SectionType,
  EFI_PEI_FILE_HANDLE,                  # IN       FileHandle,
  POINTER(PVOID)                        # OUT      **SectionData
  )

EFI_PEI_FFS_FIND_SECTION_DATA3 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  PiFirmwareFile.EFI_SECTION_TYPE,      # IN       SectionType,
  UINTN,                                # IN       SectionInstance,
  EFI_PEI_FILE_HANDLE,                  # IN       FileHandle,
  POINTER(PVOID),                       # OUT      **SectionData
  POINTER(UINT32)                       # OUT      *AuthenticationStatus
  )

EFI_PEI_INSTALL_PEI_MEMORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  EFI_PHYSICAL_ADDRESS,                 # IN       MemoryBegin,
  UINT64,                               # IN       MemoryLength
  )

EFI_PEI_ALLOCATE_PAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  EFI_MEMORY_TYPE,                      # IN       MemoryType,
  UINTN,                                # IN       Pages,
  POINTER(EFI_PHYSICAL_ADDRESS)         # OUT      *Memory
  )

EFI_PEI_FREE_PAGES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  EFI_PHYSICAL_ADDRESS,                 # IN       Memory,
  UINTN                                 # IN       Pages
  )

EFI_PEI_ALLOCATE_POOL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN CONST **PeiServices,
  UINTN,                                # IN       Size,
  POINTER(PVOID)                        # OUT      **Buffer
  )

EFI_PEI_COPY_MEM = CFUNCTYPE (
  None,
  PVOID,    # IN    *Destination,
  PVOID,    # IN    *Source,
  UINTN     # IN    Size
  )

EFI_PEI_SET_MEM = CFUNCTYPE (
  None,
  PVOID,    # IN    *Buffer,
  UINTN,    # IN    Size,
  UINT8     # IN    Value
  )

EFI_PEI_REPORT_STATUS_CODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES)),         # IN CONST **PeiServices,
  PiStatusCode.EFI_STATUS_CODE_TYPE,          # IN       Type,
  PiStatusCode.EFI_STATUS_CODE_VALUE,         # IN       Value,
  UINT32,                                     # IN       Instance,
  POINTER(EFI_GUID),                          # IN CONST *CallerId OPTIONAL,
  POINTER(PiStatusCode.EFI_STATUS_CODE_DATA)  # IN CONST *Data OPTIONAL
  )

EFI_PEI_RESET_SYSTEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_PEI_SERVICES))    # IN CONST **PeiServices,
  )

EFI_PEI_RESET2_SYSTEM = CFUNCTYPE (
  None,
  EFI_RESET_TYPE,                       # IN ResetType,
  EFI_STATUS,                           # IN ResetStatus,
  UINTN,                                # IN DataSize,
  PVOID                                 # IN *ResetData OPTIONAL
  )

EFI_PEI_FFS_FIND_BY_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),              # IN  CONST *FileName,
  EFI_PEI_FV_HANDLE,              # IN        VolumeHandle,
  POINTER(EFI_PEI_FILE_HANDLE)    # OUT       *FileHandle
  )

class EFI_FV_FILE_INFO (Structure):
  _fields_ = [
    ("FileName",        EFI_GUID),
    ("FileType",        PiFirmwareFile.EFI_FV_FILETYPE),
    ("FileAttributes",  PiFirmwareVolume.EFI_FV_FILE_ATTRIBUTES),
    ("Buffer",          PVOID),
    ("BufferSize",      UINT32)
  ]

class EFI_FV_FILE_INFO2 (Structure):
  _fields_ = [
    ("FileName",                EFI_GUID),
    ("FileType",                PiFirmwareFile.EFI_FV_FILETYPE),
    ("FileAttributes",          PiFirmwareVolume.EFI_FV_FILE_ATTRIBUTES),
    ("Buffer",                  PVOID),
    ("BufferSize",              UINT32),
    ("AuthenticationStatus",    UINT32)
  ]

EFI_PEI_FFS_GET_FILE_INFO = CFUNCTYPE (
  EFI_STATUS,
  EFI_PEI_FILE_HANDLE,            # IN  FileHandle,
  POINTER(EFI_FV_FILE_INFO),      # OUT *FileInfo
  )

EFI_PEI_FFS_GET_FILE_INFO2 = CFUNCTYPE (
  EFI_STATUS,
  EFI_PEI_FILE_HANDLE,            # IN  FileHandle,
  POINTER(EFI_FV_FILE_INFO2),     # OUT *FileInfo
  )

class EFI_FV_INFO (Structure):
  _fields_ = [
    ("FvAttributes",    PiFirmwareVolume.EFI_FVB_ATTRIBUTES_2),
    ("FvFormat",        EFI_GUID),
    ("FvName",          EFI_GUID),
    ("*FvStart",        PVOID),
    ("FvSize",          UINT64)
  ]

EFI_PEI_FFS_GET_VOLUME_INFO = CFUNCTYPE (
  EFI_STATUS,
  EFI_PEI_FV_HANDLE,              # IN  VolumeHandle,
  POINTER(EFI_FV_INFO),           # OUT *VolumeInfo
  )

EFI_PEI_REGISTER_FOR_SHADOW = CFUNCTYPE (
  EFI_STATUS,
  EFI_PEI_FILE_HANDLE             # IN  FileHandle
  )

PEI_SPECIFICATION_MAJOR_REVISION  = PI_SPECIFICATION_MAJOR_REVISION
PEI_SPECIFICATION_MINOR_REVISION  = PI_SPECIFICATION_MINOR_REVISION

PEI_SERVICES_SIGNATURE  = 0x5652455320494550

PEI_SERVICES_REVISION  = ((PEI_SPECIFICATION_MAJOR_REVISION<<16) | (PEI_SPECIFICATION_MINOR_REVISION))

EFI_PEI_SERVICES._fields_ = [
    ("Hdr",                 EFI_TABLE_HEADER),
    ("InstallPpi",          EFI_PEI_INSTALL_PPI),
    ("ReInstallPpi",        EFI_PEI_REINSTALL_PPI),
    ("LocatePpi",           EFI_PEI_LOCATE_PPI),
    ("NotifyPpi",           EFI_PEI_NOTIFY_PPI),
    ("GetBootMode",         EFI_PEI_GET_BOOT_MODE),
    ("SetBootMode",         EFI_PEI_SET_BOOT_MODE),
    ("GetHobList",          EFI_PEI_GET_HOB_LIST),
    ("CreateHob",           EFI_PEI_CREATE_HOB),
    ("FfsFindNextVolume",   EFI_PEI_FFS_FIND_NEXT_VOLUME2),
    ("FfsFindNextFile",     EFI_PEI_FFS_FIND_NEXT_FILE2),
    ("FfsFindSectionData",  EFI_PEI_FFS_FIND_SECTION_DATA2),
    ("InstallPeiMemory",    EFI_PEI_INSTALL_PEI_MEMORY),
    ("AllocatePages",       EFI_PEI_ALLOCATE_PAGES),
    ("AllocatePool",        EFI_PEI_ALLOCATE_POOL),
    ("CopyMem",             EFI_PEI_COPY_MEM),
    ("SetMem",              EFI_PEI_SET_MEM),
    ("ReportStatusCode",    EFI_PEI_REPORT_STATUS_CODE),
    ("ResetSystem",         EFI_PEI_RESET_SYSTEM),
    ("CpuIo",               POINTER(EFI_PEI_CPU_IO_PPI)),
    ("PciCfg",              POINTER(EFI_PEI_PCI_CFG2_PPI)),
    ("FfsFindFileByName",   EFI_PEI_FFS_FIND_BY_NAME),
    ("FfsGetFileInfo",      EFI_PEI_FFS_GET_FILE_INFO),
    ("FfsGetVolumeInfo",    EFI_PEI_FFS_GET_VOLUME_INFO),
    ("RegisterForShadow",   EFI_PEI_REGISTER_FOR_SHADOW),
    ("FindSectionData3",    EFI_PEI_FFS_FIND_SECTION_DATA3),
    ("FfsGetFileInfo2",     EFI_PEI_FFS_GET_FILE_INFO2),
    ("ResetSystem2",        EFI_PEI_RESET2_SYSTEM),
    ("FreePages",           EFI_PEI_FREE_PAGES)
  ]

class EFI_SEC_PEI_HAND_OFF (Structure):
  _fields_ = [
    ("DataSize",                UINT16),
    ("BootFirmwareVolumeBase",  PVOID),
    ("BootFirmwareVolumeSize",  UINTN),
    ("TemporaryRamBase",        PVOID),
    ("TemporaryRamSize",        UINTN),
    ("PeiTemporaryRamBase",     PVOID),
    ("PeiTemporaryRamSize",     UINTN),
    ("StackBase",               PVOID),
    ("StackSize",               UINTN)
  ]

EFI_PEI_CORE_ENTRY_POINT = CFUNCTYPE (
  None,
  POINTER(EFI_SEC_PEI_HAND_OFF),    # IN CONST  *SecCoreData,
  POINTER(EFI_PEI_PPI_DESCRIPTOR)   # IN CONST  *PpiList
  )

