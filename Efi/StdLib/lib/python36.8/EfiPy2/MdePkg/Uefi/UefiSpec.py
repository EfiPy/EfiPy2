# UefiSpec.py
#
# EfiPy2.MdePkg.Uefi.UefiSpec
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.Uefi.UefiBaseType       import *
from EfiPy2.MdePkg.Uefi.UefiMultiPhase     import *
from EfiPy2.MdePkg.Protocol.SimpleTextIn   import EFI_SIMPLE_TEXT_INPUT_PROTOCOL
from EfiPy2.MdePkg.Protocol.SimpleTextOut  import EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL
from EfiPy2.MdePkg.Protocol.DevicePath     import EFI_DEVICE_PATH_PROTOCOL

AllocateAnyPages    = 0
AllocateMaxAddress  = 1
AllocateAddress     = 2
MaxAllocateType     = 3
EFI_ALLOCATE_TYPE = ENUM

EFI_TIME_ADJUST_DAYLIGHT  = 0x01
EFI_TIME_IN_DAYLIGHT      = 0x02

EFI_UNSPECIFIED_TIMEZONE  = 0x07FF

EFI_MEMORY_UC   = 0x0000000000000001
EFI_MEMORY_WC   = 0x0000000000000002
EFI_MEMORY_WT   = 0x0000000000000004
EFI_MEMORY_WB   = 0x0000000000000008
EFI_MEMORY_UCE  = 0x0000000000000010

EFI_MEMORY_WP               = 0x0000000000001000
EFI_MEMORY_RP               = 0x0000000000002000
EFI_MEMORY_XP               = 0x0000000000004000
EFI_MEMORY_RO               = 0x0000000000020000

EFI_MEMORY_NV               = 0x0000000000008000
EFI_MEMORY_MORE_RELIABLE    = 0x0000000000010000
EFI_MEMORY_RUNTIME          = 0x8000000000000000

EFI_MEMORY_DESCRIPTOR_VERSION = 1

class EFI_MEMORY_DESCRIPTOR (Structure):
  _fields_ = [
    ("Type",            UINT32),
    ("PhysicalStart",   EFI_PHYSICAL_ADDRESS),
    ("VirtualStart",    EFI_VIRTUAL_ADDRESS),
    ("NumberOfPages",   UINT64),
    ("Attribute",       UINT64)
    ]

EFI_ALLOCATE_PAGES = CFUNCTYPE (
  EFI_STATUS,
  EFI_ALLOCATE_TYPE,             # IN     Type
  EFI_MEMORY_TYPE,               # IN     MemoryType
  UINTN,                         # IN     Pages
  POINTER(EFI_PHYSICAL_ADDRESS)  # IN OUT *Memory
  )

EFI_FREE_PAGES = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN Memory
  UINTN                 # IN Pages
  )

EFI_GET_MEMORY_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINTN),                 # IN OUT *MemoryMapSize
  POINTER(EFI_MEMORY_DESCRIPTOR), # IN OUT *MemoryMap
  POINTER(UINTN),                 # OUT    *MapKey
  POINTER(UINTN),                 # OUT    *DescriptorSize
  POINTER(UINT32)                 # OUT    *DescriptorVersion
  )

EFI_ALLOCATE_POOL = CFUNCTYPE (
  EFI_STATUS,
  EFI_MEMORY_TYPE,  # IN  PoolType
  UINTN,            # IN  Size
  POINTER(PVOID)    # OUT **Buffer
  )

EFI_FREE_POOL = CFUNCTYPE (
  EFI_STATUS,
  PVOID                 # IN *Buffer
  )

EFI_SET_VIRTUAL_ADDRESS_MAP = CFUNCTYPE (
  EFI_STATUS,
  UINTN,                         # IN MemoryMapSize
  UINTN,                         # IN DescriptorSize
  UINT32,                        # IN DescriptorVersion
  POINTER(EFI_MEMORY_DESCRIPTOR) # IN *VirtualMap
  )

EFI_CONNECT_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                        # IN ControllerHandle
  POINTER(EFI_HANDLE),               # IN *DriverImageHandle,   OPTIONAL
  POINTER(EFI_DEVICE_PATH_PROTOCOL), # IN *RemainingDevicePath, OPTIONAL
  BOOLEAN                            # IN Recursive
  )

EFI_DISCONNECT_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE, # IN ControllerHandle
  EFI_HANDLE, # IN DriverImageHandle, OPTIONAL
  EFI_HANDLE  # IN ChildHandle        OPTIONAL
  )

EFI_OPTIONAL_PTR     = 0x00000001

EFI_CONVERT_POINTER = CFUNCTYPE (
  UINTN,          # IN     DebugDisposition
  POINTER(PVOID)  # IN OUT **Address 
  )

EVT_TIMER                         = 0x80000000
EVT_RUNTIME                       = 0x40000000
EVT_NOTIFY_WAIT                   = 0x00000100
EVT_NOTIFY_SIGNAL                 = 0x00000200

EVT_SIGNAL_EXIT_BOOT_SERVICES     = 0x00000201
EVT_SIGNAL_VIRTUAL_ADDRESS_CHANGE = 0x60000202

EVT_RUNTIME_CONTEXT               = 0x20000000

EFI_EVENT_NOTIFY = CFUNCTYPE (
  VOID,
  EFI_EVENT,         # IN Event
  PVOID              # IN *Context
  )

EFI_CREATE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  UINT32,            # IN  Type
  EFI_TPL,           # IN  NotifyTpl
  EFI_EVENT_NOTIFY,  # IN  NotifyFunction
  PVOID,             # IN  *NotifyContext
  POINTER(EFI_EVENT) # OUT *Event
  )

EFI_CREATE_EVENT_EX = CFUNCTYPE (
  EFI_STATUS,
  UINT32,            #   IN       Type
  EFI_TPL,           #   IN       NotifyTpl
  EFI_EVENT_NOTIFY,  #   IN       NotifyFunction OPTIONAL
  PVOID,             #   IN CONST *NotifyContext OPTIONAL
  POINTER(EFI_GUID), #   IN CONST *EventGroup    OPTIONAL
  POINTER(EFI_EVENT) #   OUT      *Event
  )

EFI_TIMER_DELAY = ENUM

TimerCancel   = 0
TimerPeriodic = 1
TimerRelative = 2

EFI_SET_TIMER = CFUNCTYPE (
  EFI_STATUS,
  EFI_EVENT,            # IN Event
  EFI_TIMER_DELAY,      # IN Type
  UINT64                # IN TriggerTime
  )

EFI_SIGNAL_EVENT = CFUNCTYPE (
  EFI_STATUS,
  EFI_EVENT          # IN Event
  )

EFI_WAIT_FOR_EVENT = CFUNCTYPE (
  EFI_STATUS,
  UINTN,               # IN  NumberOfEvents
  POINTER(EFI_EVENT),  # IN  *Event
  POINTER(UINTN)       # OUT *Index
  )

EFI_CLOSE_EVENT = CFUNCTYPE (
  EFI_STATUS,
  EFI_EVENT           # IN Event
  )

EFI_CHECK_EVENT = CFUNCTYPE (
  EFI_STATUS,
  EFI_EVENT           # IN Event
  )
TPL_APPLICATION       = 4
TPL_CALLBACK          = 8
TPL_NOTIFY            = 16
TPL_HIGH_LEVEL        = 31

EFI_RAISE_TPL = CFUNCTYPE (
  EFI_TPL,
  EFI_TPL               # IN NewTpl
  )

EFI_RESTORE_TPL = CFUNCTYPE (
  VOID,
  EFI_TPL             # IN OldTpl
  )

EFI_GET_VARIABLE = CFUNCTYPE (
  EFI_STATUS,
  PCHAR16,           # IN     *VariableName
  POINTER(EFI_GUID), # IN     *VendorGuid
  POINTER(UINT32),   # OUT    *Attributes,    OPTIONAL
  POINTER(UINTN),    # IN OUT *DataSize
  PVOID              # OUT    *Data
  )

EFI_GET_NEXT_VARIABLE_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINTN),    # IN OUT *VariableNameSize
  PCHAR16,           # IN OUT *VariableName
  POINTER(EFI_GUID)  # IN OUT *VendorGuid
  )

EFI_SET_VARIABLE = CFUNCTYPE (
  EFI_STATUS,
  PCHAR16,           # IN *VariableName
  POINTER(EFI_GUID), # IN *VendorGuid
  UINT32,            # IN Attributes
  UINTN,             # IN DataSize
  PVOID              # IN *Data
  )

class EFI_TIME_CAPABILITIES (Structure):
  _fields_ = [
    ("Resolution",      UINT32),
    ("Accuracy",        UINT32),
    ("SetsToZero",      BOOLEAN)
    ]

EFI_GET_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIME),             # OUT *Time
  POINTER(EFI_TIME_CAPABILITIES) # OUT *Capabilities OPTIONAL
  )

EFI_SET_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TIME)      # IN *Time
  )

EFI_GET_WAKEUP_TIME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(BOOLEAN), # OUT *Enabled
  POINTER(BOOLEAN), # OUT *Pending
  POINTER(EFI_TIME) # OUT *Time
  )

EFI_SET_WAKEUP_TIME = CFUNCTYPE (
  EFI_STATUS,
  BOOLEAN,          # IN Enable
  POINTER(EFI_TIME) # IN *Time   OPTIONAL
  )

EFI_IMAGE_LOAD = CFUNCTYPE (
  EFI_STATUS,
  BOOLEAN,                           # IN  BootPolicy
  EFI_HANDLE,                        # IN  ParentImageHandle
  POINTER(EFI_DEVICE_PATH_PROTOCOL), # IN  *DevicePath
  PVOID,                             # IN  *SourceBuffer OPTIONAL
  UINTN,                             # IN  SourceSize
  POINTER(EFI_HANDLE)                # OUT *ImageHandle
  )

EFI_IMAGE_START = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,         # IN  ImageHandle
  POINTER(UINTN),     # OUT *ExitDataSize
  POINTER(PCHAR16)    # OUT **ExitData    OPTIONAL
  )

EFI_EXIT = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                # IN ImageHandle
  EFI_STATUS,                # IN ExitStatus
  UINTN,                     # IN ExitDataSize
  PCHAR16                    # IN *ExitData     OPTIONAL
  )

EFI_IMAGE_UNLOAD = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE         # IN ImageHandle
  )

EFI_EXIT_BOOT_SERVICES = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,  # IN ImageHandle
  UINTN        # IN MapKey
  )

EFI_STALL = CFUNCTYPE (
  EFI_STATUS,
  UINTN                     # IN Microseconds
  )

EFI_SET_WATCHDOG_TIMER = CFUNCTYPE (
  EFI_STATUS,
  UINTN,       # IN Timeout
  UINT64,      # IN WatchdogCode
  UINTN,       # IN DataSize
  PCHAR16      # IN *WatchdogData OPTIONAL
  )

EFI_RESET_SYSTEM = CFUNCTYPE (
  VOID,
  EFI_RESET_TYPE,    # IN ResetType
  EFI_STATUS,        # IN ResetStatus
  UINTN,             # IN DataSize
  PVOID              # IN *ResetData OPTIONAL
  )

EFI_GET_NEXT_MONOTONIC_COUNT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINT64)  # OUT *Count
  )

EFI_GET_NEXT_HIGH_MONO_COUNT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(UINT32)  # OUT *HighCount
  )

EFI_CALCULATE_CRC32 = CFUNCTYPE (
  EFI_STATUS,
  PVOID,          # IN  *Data
  UINTN,          # IN  DataSize
  POINTER(UINT32) # OUT *Crc32
  )

EFI_COPY_MEM = CFUNCTYPE (
  VOID,
  PVOID,                 # IN *Destination
  PVOID,                 # IN *Source
  UINTN                  # IN Length
  )

EFI_SET_MEM = CFUNCTYPE (
  VOID,
  PVOID,                  # IN *Buffer
  UINTN,                  # IN Size
  UINT8                   # IN Value
  )

EFI_NATIVE_INTERFACE = 0
EFI_INTERFACE_TYPE = ENUM

EFI_INSTALL_PROTOCOL_INTERFACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HANDLE), # IN OUT *Handle
  POINTER(EFI_GUID),   # IN     *Protocol
  EFI_INTERFACE_TYPE,  # IN     InterfaceType
  PVOID                # IN     *Interface
  )

EFI_INSTALL_MULTIPLE_PROTOCOL_INTERFACES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HANDLE)  # IN OUT *Handle
  )

EFI_REINSTALL_PROTOCOL_INTERFACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,        # IN Handle
  POINTER(EFI_GUID), # IN *Protocol
  PVOID,             # IN *OldInterface
  PVOID              # IN *NewInterface
  )

EFI_UNINSTALL_PROTOCOL_INTERFACE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,        # IN Handle
  POINTER(EFI_GUID), # IN *Protocol
  PVOID              # IN *Interface
  )

EFI_UNINSTALL_MULTIPLE_PROTOCOL_INTERFACES = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE   # IN Handle
  )

EFI_HANDLE_PROTOCOL = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,         # IN  Handle
  POINTER(EFI_GUID),  # IN  *Protocol
  POINTER(PVOID)      # OUT **Interface
  )

EFI_OPEN_PROTOCOL_BY_HANDLE_PROTOCOL  = 0x00000001
EFI_OPEN_PROTOCOL_GET_PROTOCOL        = 0x00000002
EFI_OPEN_PROTOCOL_TEST_PROTOCOL       = 0x00000004
EFI_OPEN_PROTOCOL_BY_CHILD_CONTROLLER = 0x00000008
EFI_OPEN_PROTOCOL_BY_DRIVER           = 0x00000010
EFI_OPEN_PROTOCOL_EXCLUSIVE           = 0x00000020

EFI_OPEN_PROTOCOL = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,       # IN  Handle
  POINTER(EFI_GUID),# IN  *Protocol
  POINTER(PVOID),   # OUT **Interface, OPTIONAL
  EFI_HANDLE,       # IN  AgentHandle
  EFI_HANDLE,       # IN  ControllerHandle
  UINT32            # IN  Attributes
  )

EFI_CLOSE_PROTOCOL = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,        # IN Handle
  POINTER(EFI_GUID), # IN *Protocol
  EFI_HANDLE,        # IN AgentHandle
  EFI_HANDLE         # IN ControllerHandle
  )

class EFI_OPEN_PROTOCOL_INFORMATION_ENTRY (Structure):
  _fields_ = [
    ("AgentHandle",       EFI_HANDLE),
    ("ControllerHandle",  EFI_HANDLE),
    ("Attributes",        UINT32),
    ("OpenCount",         UINT32)
    ]

EFI_OPEN_PROTOCOL_INFORMATION = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                                             # IN  Handle
  POINTER(EFI_GUID),                                      # IN  *Protocol
  POINTER(POINTER(EFI_OPEN_PROTOCOL_INFORMATION_ENTRY)),  # OUT **EntryBuffer
  POINTER(UINTN)                                          # OUT *EntryCount
  )

EFI_PROTOCOLS_PER_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                          # IN  Handle
  POINTER(POINTER(POINTER(EFI_GUID))), # OUT ***ProtocolBuffer
  POINTER(UINTN)                       # OUT *ProtocolBufferCount
  )

EFI_REGISTER_PROTOCOL_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID), # IN  *Protocol
  EFI_EVENT,         # IN  Event
  POINTER(PVOID)     # OUT **Registration
  )

AllHandles        = 0
ByRegisterNotify  = 1
ByProtocol        = 2
EFI_LOCATE_SEARCH_TYPE = ENUM

EFI_LOCATE_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  EFI_LOCATE_SEARCH_TYPE, # IN     SearchType
  POINTER(EFI_GUID),      # IN     *Protocol,    OPTIONAL
  PVOID,                  # IN     *SearchKey,   OPTIONAL
  POINTER(UINTN),         # IN OUT *BufferSize
  POINTER(EFI_HANDLE)     # OUT    *Buffer
  )

EFI_LOCATE_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),                           #   IN     *Protocol
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL)),  #   IN OUT **DevicePath
  POINTER(EFI_HANDLE)                          #   OUT    *Device
  )

EFI_INSTALL_CONFIGURATION_TABLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN *Guid
  PVOID               # IN *Table
  )

EFI_LOCATE_HANDLE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  EFI_LOCATE_SEARCH_TYPE,      # IN     SearchType
  POINTER(EFI_GUID),           # IN     *Protocol,      OPTIONAL
  PVOID,                       # IN     *SearchKey,     OPTIONAL
  POINTER(UINTN),              # IN OUT *NoHandles
  POINTER(POINTER(EFI_HANDLE)) # OUT    **Buffer
  )

EFI_LOCATE_PROTOCOL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),  # IN  *Protocol
  PVOID,              # IN  *Registration, OPTIONAL
  POINTER(PVOID)      # OUT **Interface
  )

class EFI_CAPSULE_BLOCK_DESCRIPTOR (Structure):

  class _union (Union):

    _fields_ = [
      ("DataBlock",           EFI_PHYSICAL_ADDRESS),
      ("ContinuationPointer", EFI_PHYSICAL_ADDRESS)
      ]

  _fields_ = [
    ("Length",    UINT64),
    ("Union",     _union)
    ]

class EFI_CAPSULE_HEADER (Structure):
  _fields_ = [
    ("CapsuleGuid",       EFI_GUID),
    ("HeaderSize",        UINT32),
    ("Flags",             UINT32),
    ("CapsuleImageSize",  UINT32)
    ]


class EFI_CAPSULE_TABLE (Structure):
  _fields_ = [
    ("CapsuleArrayNumber",  UINT32),
    ("CapsulePtr",          PVOID)
    ]

CAPSULE_FLAGS_PERSIST_ACROSS_RESET          = 0x00010000
CAPSULE_FLAGS_POPULATE_SYSTEM_TABLE         = 0x00020000
CAPSULE_FLAGS_INITIATE_RESET                = 0x00040000

EFI_UPDATE_CAPSULE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_CAPSULE_HEADER)),  # IN **CapsuleHeaderArray
  UINTN,                                 # IN CapsuleCount
  EFI_PHYSICAL_ADDRESS                   # IN ScatterGatherList   OPTIONAL
  )

EFI_QUERY_CAPSULE_CAPABILITIES = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_CAPSULE_HEADER)),  # IN  **CapsuleHeaderArray
  UINTN,                                 # IN  CapsuleCount
  POINTER(UINT64),                       # OUT *MaximumCapsuleSize
  POINTER(EFI_RESET_TYPE)                # OUT *ResetType
  )

EFI_QUERY_VARIABLE_INFO = CFUNCTYPE (
  EFI_STATUS,
  UINT32,           # IN  Attributes
  POINTER(UINT64),  # OUT *MaximumVariableStorageSize
  POINTER(UINT64),  # OUT *RemainingVariableStorageSize
  POINTER(UINT64)   # OUT *MaximumVariableSize
  )

EFI_OS_INDICATIONS_BOOT_TO_FW_UI                    = 0x0000000000000001
EFI_OS_INDICATIONS_TIMESTAMP_REVOCATION             = 0x0000000000000002
EFI_OS_INDICATIONS_FILE_CAPSULE_DELIVERY_SUPPORTED  = 0x0000000000000004
EFI_OS_INDICATIONS_FMP_CAPSULE_SUPPORTED            = 0x0000000000000008
EFI_OS_INDICATIONS_CAPSULE_RESULT_VAR_SUPPORTED     = 0x0000000000000010

EFI_SYSTEM_TABLE_SIGNATURE      = SIGNATURE_64 ('I','B','I',' ','S','Y','S','T')
EFI_2_50_SYSTEM_TABLE_REVISION  = (2 << 16) | (50)
EFI_2_40_SYSTEM_TABLE_REVISION  = (2 << 16) | (40)
EFI_2_31_SYSTEM_TABLE_REVISION  = (2 << 16) | (31)
EFI_2_30_SYSTEM_TABLE_REVISION  = (2 << 16) | (30)
EFI_2_20_SYSTEM_TABLE_REVISION  = (2 << 16) | (20)
EFI_2_10_SYSTEM_TABLE_REVISION  = (2 << 16) | (10)
EFI_2_00_SYSTEM_TABLE_REVISION  = (2 << 16) | (00)
EFI_1_10_SYSTEM_TABLE_REVISION  = (1 << 16) | (10)
EFI_1_02_SYSTEM_TABLE_REVISION  = (1 << 16) | ( 2)
EFI_SYSTEM_TABLE_REVISION       = EFI_2_50_SYSTEM_TABLE_REVISION
EFI_SPECIFICATION_VERSION       = EFI_SYSTEM_TABLE_REVISION

EFI_RUNTIME_SERVICES_SIGNATURE  = SIGNATURE_64 ('R','U','N','T','S','E','R','V')
class EFI_RUNTIME_SERVICES (Structure):
  _fields_ = [
    ("Hdr",                       EFI_TABLE_HEADER),
    ("GetTime",                   EFI_GET_TIME),
    ("SetTime",                   EFI_SET_TIME),
    ("GetWakeupTime",             EFI_GET_WAKEUP_TIME),
    ("SetWakeupTime",             EFI_SET_WAKEUP_TIME),
    ("SetVirtualAddressMap",      EFI_SET_VIRTUAL_ADDRESS_MAP),
    ("ConvertPointer",            EFI_CONVERT_POINTER),
    ("GetVariable",               EFI_GET_VARIABLE),
    ("GetNextVariableName",       EFI_GET_NEXT_VARIABLE_NAME),
    ("SetVariable",               EFI_SET_VARIABLE),
    ("GetNextHighMonotonicCount", EFI_GET_NEXT_HIGH_MONO_COUNT),
    ("ResetSystem",               EFI_RESET_SYSTEM),
    ("UpdateCapsule",             EFI_UPDATE_CAPSULE),
    ("QueryCapsuleCapabilities",  EFI_QUERY_CAPSULE_CAPABILITIES),
    ("QueryVariableInfo",         EFI_QUERY_VARIABLE_INFO)
    ]

EFI_BOOT_SERVICES_SIGNATURE   = SIGNATURE_64 ('B','O','O','T','S','E','R','V')

EFI_RUNTIME_SERVICES_REVISION   = EFI_SPECIFICATION_VERSION

class EFI_BOOT_SERVICES (Structure):
  _fields_ = [
    ("Hdr",                       EFI_TABLE_HEADER),
    ("RaiseTPL",                  EFI_RAISE_TPL),
    ("RestoreTPL",                EFI_RESTORE_TPL),
    ("AllocatePages",             EFI_ALLOCATE_PAGES),
    ("FreePages",                 EFI_FREE_PAGES),
    ("GetMemoryMap",              EFI_GET_MEMORY_MAP),
    ("AllocatePool",              EFI_ALLOCATE_POOL),
    ("FreePool",                  EFI_FREE_POOL),
    ("CreateEvent",               EFI_CREATE_EVENT),
    ("SetTimer",                  EFI_SET_TIMER),
    ("WaitForEvent",              EFI_WAIT_FOR_EVENT),
    ("SignalEvent",               EFI_SIGNAL_EVENT),
    ("CloseEvent",                EFI_CLOSE_EVENT),
    ("CheckEvent",                EFI_CHECK_EVENT),
    ("InstallProtocolInterface",  EFI_INSTALL_PROTOCOL_INTERFACE),
    ("ReinstallProtocolInterface",EFI_REINSTALL_PROTOCOL_INTERFACE),
    ("UninstallProtocolInterface",EFI_UNINSTALL_PROTOCOL_INTERFACE),
    ("HandleProtocol",            EFI_HANDLE_PROTOCOL),
    ("Reserved",                  PVOID),
    ("RegisterProtocolNotify",    EFI_REGISTER_PROTOCOL_NOTIFY),
    ("LocateHandle",              EFI_LOCATE_HANDLE),
    ("LocateDevicePath",          EFI_LOCATE_DEVICE_PATH),
    ("InstallConfigurationTable", EFI_INSTALL_CONFIGURATION_TABLE),
    ("LoadImage",                 EFI_IMAGE_LOAD),
    ("StartImage",                EFI_IMAGE_START),
    ("Exit",                      EFI_EXIT),
    ("UnloadImage",               EFI_IMAGE_UNLOAD),
    ("ExitBootServices",          EFI_EXIT_BOOT_SERVICES),
    ("GetNextMonotonicCount",     EFI_GET_NEXT_MONOTONIC_COUNT),
    ("Stall",                     EFI_STALL),
    ("SetWatchdogTimer",          EFI_SET_WATCHDOG_TIMER),
    ("ConnectController",         EFI_CONNECT_CONTROLLER),
    ("DisconnectController",      EFI_DISCONNECT_CONTROLLER),
    ("OpenProtocol",              EFI_OPEN_PROTOCOL),
    ("CloseProtocol",             EFI_CLOSE_PROTOCOL),
    ("OpenProtocolInformation",   EFI_OPEN_PROTOCOL_INFORMATION),
    ("ProtocolsPerHandle",        EFI_PROTOCOLS_PER_HANDLE),
    ("LocateHandleBuffer",        EFI_LOCATE_HANDLE_BUFFER),
    ("LocateProtocol",            EFI_LOCATE_PROTOCOL),
    ("InstallMultipleProtocolInterfaces",   EFI_INSTALL_MULTIPLE_PROTOCOL_INTERFACES),
    ("UninstallMultipleProtocolInterfaces", EFI_UNINSTALL_MULTIPLE_PROTOCOL_INTERFACES),
    ("CalculateCrc32",            EFI_CALCULATE_CRC32),
    ("CopyMem",                   EFI_COPY_MEM),
    ("SetMem",                    EFI_SET_MEM),
    ("CreateEventEx",             EFI_CREATE_EVENT_EX)
    ]

class EFI_CONFIGURATION_TABLE (Structure):
  _fields_ = [
    ("VendorGuid",      EFI_GUID),
    ("VendorTable",     PVOID)
    ]

class EFI_SYSTEM_TABLE (Structure):
  _fields_ = [
    ("Hdr",                       EFI_TABLE_HEADER),
    ("FirmwareVendor",            PCHAR16),
    ("FirmwareRevision",          UINT32),
    ("ConsoleInHandle",           EFI_HANDLE),
    ("ConIn",                     POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL)),
    ("ConsoleOutHandle",          EFI_HANDLE),
    ("ConOut",                    POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)),
    ("StandardErrorHandle",       EFI_HANDLE),
    ("StdErr",                    POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)),
    ("RuntimeServices",           POINTER(EFI_RUNTIME_SERVICES)),
    ("BootServices",              POINTER(EFI_BOOT_SERVICES)),
    ("NumberOfTableEntries",      UINTN),
    ("ConfigurationTable",        POINTER(EFI_CONFIGURATION_TABLE))
    ]

EFI_IMAGE_ENTRY_POINT = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,               # IN ImageHandle,
  POINTER(EFI_SYSTEM_TABLE) # IN *SystemTable
  )

class EFI_LOAD_OPTION (Structure):
  _pack_          = 1
  _fields_ = [
    ("Attributes",          UINT32),
    ("FilePathListLength",  UINT16)
    # ("Description",       CHAR16 * N)
    # ("FilePathList",      EFI_DEVICE_PATH_PROTOCOL * N)
    # ("OptionalData",      UINT8 * N)
    ]

LOAD_OPTION_ACTIVE              = 0x00000001
LOAD_OPTION_FORCE_RECONNECT     = 0x00000002
LOAD_OPTION_HIDDEN              = 0x00000008
LOAD_OPTION_CATEGORY            = 0x00001F00
LOAD_OPTION_CATEGORY_BOOT       = 0x00000000
LOAD_OPTION_CATEGORY_APP        = 0x00000100
EFI_BOOT_OPTION_SUPPORT_KEY     = 0x00000001
EFI_BOOT_OPTION_SUPPORT_APP     = 0x00000002
EFI_BOOT_OPTION_SUPPORT_SYSPREP = 0x00000010
EFI_BOOT_OPTION_SUPPORT_COUNT   = 0x00000300

class EFI_BOOT_KEY_DATA_Options (Structure):
  _fields_ = [
    ("Revision",        UINT32, 8),
    ("ShiftPressed",    UINT32, 1),
    ("ControlPressed",  UINT32, 1),
    ("AltPressed",      UINT32, 1),
    ("LogoPressed",     UINT32, 1),
    ("MenuPressed",     UINT32, 1),
    ("SysReqPressed",   UINT32, 1),
    ("Reserved",        UINT32, 16),
    ("InputKeyCount",   UINT32, 2)
    ]

class EFI_BOOT_KEY_DATA (Union):
  _fields_ = [
    ("Options",     EFI_BOOT_KEY_DATA_Options),
    ("PackedValue", UINT32)
    ]

class EFI_KEY_OPTION (Structure):
  _pack_          = 1
  _fields_ = [
    ("KeyData",         EFI_BOOT_KEY_DATA),
    ("BootOptionCrc",   UINT32),
    ("BootOption",      UINT16)
    # ("Keys",          EFI_INPUT_KEY * N)
    ]

from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_IA32
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_X64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_ARM
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_AARCH64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_RISCV64
from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME_LOONGARCH64

from _EfiPy2 import EFI_REMOVABLE_MEDIA_FILE_NAME

EFI_CAPSULE_FILE_DIRECTORY = "\\EFI\\UpdateCapsule\\"
