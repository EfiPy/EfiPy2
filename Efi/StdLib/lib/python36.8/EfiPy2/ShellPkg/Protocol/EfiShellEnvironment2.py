# EfiShellEnvironment2.py
#
# EfiPy2.ShellPkg.Protocol.EfiShellEnvironment2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Protocol.SimpleFileSystem    import EFI_FILE_HANDLE
from EfiPy2.MdePkg.Guid.FileInfo                import EFI_FILE_INFO
from EfiPy2.ShellPkg.Protocol.EfiShellInterface import EFI_SHELL_INTERFACE

DEFAULT_INIT_ROW  = 1
DEFAULT_AUTO_LF   = False

SHELLENV_DUMP_PROTOCOL_INFO = CFUNCTYPE (
  VOID,
  EFI_HANDLE,   # IN  Handle
  PVOID         # IN  *Interface
  )

SHELLENV_INTERNAL_COMMAND = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,               # IN  Handle
  POINTER(EFI_SYSTEM_TABLE) # IN  *SystemTable
  )

SHELLCMD_GET_LINE_HELP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(CHAR16))  # IN OUT **Str
  )

class SHELL_FILE_ARG (Structure):
  _fields_ = [
    ("Signature",           UINT32),
    ("Link",                LIST_ENTRY),
    ("Status",              EFI_STATUS),
    ("Parent",              EFI_FILE_HANDLE),
    ("OpenMode",            UINT64),
    ("ParentName",          POINTER(CHAR16)),
    ("ParentDevicePath",    POINTER(EFI_DEVICE_PATH_PROTOCOL)),
    ("FullName",            POINTER(CHAR16)),
    ("FileName",            POINTER(CHAR16)),
    ("Handle",              EFI_FILE_HANDLE),
    ("Info",                POINTER(EFI_FILE_INFO))
  ]

SHELL_FILE_ARG_SIGNATURE  = SIGNATURE_32 ('g', 'r', 'a', 'f')

gEfiShellEnvironment2Guid                 = \
  EFI_GUID (0x47c7b221, 0xc42a, 0x11d2, (0x8e, 0x57, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

gEfiShellEnvironment2ExtGuid                 = \
  EFI_GUID (0xd2c18636, 0x40e5, 0x4eb5, (0xa3, 0x1b, 0x36, 0x69, 0x5f, 0xd4, 0x2c, 0x87 ))

EFI_SHELL_MAJOR_VER  = 0x00000001 # Major version of the EFI_SHELL_ENVIRONMENT2.
EFI_SHELL_MINOR_VER  = 0x00000000 # Minor version of the EFI_SHELL_ENVIRONMENT2.

SHELLENV_EXECUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HANDLE),  #   IN *ParentImageHandle,
  POINTER(CHAR16),      #   IN *CommandLine,
  BOOLEAN               #   IN DebugOutput
  )

SHELLENV_GET_ENV = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16)      #   IN *Name
  )

SHELLENV_GET_MAP = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16)      #   IN *Name
  )

SHELLENV_ADD_CMD = CFUNCTYPE (
  EFI_STATUS,
  SHELLENV_INTERNAL_COMMAND,   #   IN Handler,
  POINTER(CHAR16),             #   IN *Cmd,
  SHELLCMD_GET_LINE_HELP       #   IN GetLineHelp
  )

SHELLENV_ADD_PROT = CFUNCTYPE (
  VOID,
  POINTER(EFI_GUID),            #   IN *Protocol,
  SHELLENV_DUMP_PROTOCOL_INFO,  #   IN DumpToken OPTIONAL,
  SHELLENV_DUMP_PROTOCOL_INFO,  #   IN DumpInfo OPTIONAL,
  POINTER(CHAR16)               #   IN *IdString
  )

SHELLENV_GET_PROT = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(EFI_GUID),    #   IN *Protocol,
  BOOLEAN               #   IN GenId
  )

SHELLENV_CUR_DIR = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16)   #   IN *DeviceName OPTIONAL
  )

SHELLENV_FILE_META_ARG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),          #   IN      *Arg,
  POINTER(LIST_ENTRY)       #   IN OUT  *ListHead
  )

SHELLENV_FREE_FILE_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(LIST_ENTRY)   #   IN OUT *ListHead
  )

SHELLENV_NEW_SHELL = CFUNCTYPE (
  POINTER(EFI_SHELL_INTERFACE),
  EFI_HANDLE                        #   IN ImageHandle
  )

SHELLENV_BATCH_IS_ACTIVE = CFUNCTYPE (
  BOOLEAN
  )

SHELLENV_FREE_RESOURCES = CFUNCTYPE (
  VOID
  )

SHELLENV_ENABLE_PAGE_BREAK = CFUNCTYPE (
  VOID,
  INT32,     #   IN StartRow,
  BOOLEAN    #   IN AutoWrap
  )

SHELLENV_DISABLE_PAGE_BREAK = CFUNCTYPE (
  VOID
  )

SHELLENV_GET_PAGE_BREAK = CFUNCTYPE (
  BOOLEAN
  )

SHELLENV_SET_KEY_FILTER = CFUNCTYPE (
  VOID,
  UINT32      #   IN KeyFilter
  )

SHELLENV_GET_KEY_FILTER = CFUNCTYPE (
  UINT32
  )

SHELLENV_GET_EXECUTION_BREAK = CFUNCTYPE (
  BOOLEAN
  )

SHELLENV_INCREMENT_SHELL_NESTING_LEVEL = CFUNCTYPE (
  VOID
  )

SHELLENV_DECREMENT_SHELL_NESTING_LEVEL = CFUNCTYPE (
  VOID
  )

SHELLENV_IS_ROOT_SHELL = CFUNCTYPE (
  BOOLEAN
  )

SHELLENV_CLOSE_CONSOLE_PROXY = CFUNCTYPE (
  VOID,
  EFI_HANDLE,                                       #   IN     ConInHandle,
  POINTER(POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL)), #   IN OUT **ConIn,
  EFI_HANDLE,                                       #   IN     ConOutHandle,
  POINTER(POINTER(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)) #   IN OUT **ConOut
  )

INIT_HANDLE_ENUMERATOR = CFUNCTYPE (
  VOID
  )

NEXT_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_HANDLE))  #   IN OUT **Handle
  )

SKIP_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  UINTN         # IN  SkipNum
  )

RESET_HANDLE_ENUMERATOR = CFUNCTYPE (
  UINTN,
  UINTN         # IN  EnumIndex
  )

CLOSE_HANDLE_ENUMERATOR = CFUNCTYPE (
  UINTN
  )

GET_NUM = CFUNCTYPE (
  UINTN
  )

class HANDLE_ENUMERATOR (Structure):
  _fields_ = [
    ("Init",    INIT_HANDLE_ENUMERATOR ),
    ("Next",    NEXT_HANDLE),
    ("Skip",    SKIP_HANDLE),
    ("Reset",   RESET_HANDLE_ENUMERATOR),
    ("Close",   CLOSE_HANDLE_ENUMERATOR),
    ("GetNum",  GET_NUM)
  ]

PROTOCOL_INFO_SIGNATURE  = SIGNATURE_32 ('s', 'p', 'i', 'n')

class PROTOCOL_INFO (Structure):
  _fields_ = [
    ("Signature",    UINTN),
    ("Link",         LIST_ENTRY),
    ("ProtocolId",   EFI_GUID),
    ("IdString",     POINTER(CHAR16)),
    ("DumpToken",    SHELLENV_DUMP_PROTOCOL_INFO),
    ("DumpInfo",     SHELLENV_DUMP_PROTOCOL_INFO),
    ("NoHandles",    UINTN),
    ("Handles",      POINTER(EFI_HANDLE))
  ]

INIT_PROTOCOL_INFO_ENUMERATOR = CFUNCTYPE (
  VOID
  )

NEXT_PROTOCOL_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(PROTOCOL_INFO))   #   IN OUT **ProtocolInfo
  )

SKIP_PROTOCOL_INFO = CFUNCTYPE (
  EFI_STATUS,
  UINTN                         #   IN SkipNum
  )

RESET_PROTOCOL_INFO_ENUMERATOR = CFUNCTYPE (
  VOID
  )

CLOSE_PROTOCOL_INFO_ENUMERATOR = CFUNCTYPE (
  VOID
  )

class PROTOCOL_INFO_ENUMERATOR (Structure):
  _fields_ = [
    ("Init",    INIT_PROTOCOL_INFO_ENUMERATOR),
    ("Next",    NEXT_PROTOCOL_INFO),
    ("Skip",    SKIP_PROTOCOL_INFO),
    ("Reset",   RESET_PROTOCOL_INFO_ENUMERATOR),
    ("Close",   CLOSE_PROTOCOL_INFO_ENUMERATOR)
  ]

GET_DEVICE_NAME = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,               #   IN      DeviceHandle,
  BOOLEAN,                  #   IN      UseComponentName,
  BOOLEAN,                  #   IN      UseDevicePath,
  POINTER(CHAR8),           #   IN      *Language,
  POINTER(POINTER(CHAR16)), #   IN OUT  **BestDeviceName,
  POINTER(EFI_STATUS),      #   OUT     *ConfigurationStatus,
  POINTER(EFI_STATUS),      #   OUT     *DiagnosticsStatus,
  BOOLEAN,                  #   IN      Display,
  UINTN                     #   IN      Indent
  )

GET_SHELL_MODE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(CHAR16))  #   OUT  **Mode
  )

SHELLENV_NAME_TO_PATH = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(CHAR16)                       #   IN  *Path
  )

SHELLENV_GET_FS_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    #   IN  *DevPath,
  BOOLEAN,                              #   IN  ConsistMapping,
  POINTER(POINTER(CHAR16))              #   OUT **Name
  )

SHELLENV_FILE_META_ARG_NO_WILDCARD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),      #   IN      *Arg,
  POINTER(LIST_ENTRY)   #   IN OUT  *ListHead
  )

SHELLENV_DEL_DUP_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(LIST_ENTRY)   #   IN *ListHead
  )

SHELLENV_GET_FS_DEVICE_PATH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),                              #   IN  *Name,
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))    #   OUT **DevPath
  )

class EFI_SHELL_ENVIRONMENT2 (Structure):
  _fields_ = [
    ("Execute",                     SHELLENV_EXECUTE),
    ("GetEnv",                      SHELLENV_GET_ENV),
    ("GetMap",                      SHELLENV_GET_MAP),
    ("AddCmd",                      SHELLENV_ADD_CMD),
    ("AddProt",                     SHELLENV_ADD_PROT),
    ("GetProt",                     SHELLENV_GET_PROT),
    ("CurDir",                      SHELLENV_CUR_DIR),
    ("FileMetaArg",                 SHELLENV_FILE_META_ARG),
    ("FreeFileList",                SHELLENV_FREE_FILE_LIST),
    ("NewShell",                    SHELLENV_NEW_SHELL),
    ("BatchIsActive",               SHELLENV_BATCH_IS_ACTIVE),
    ("FreeResources",               SHELLENV_FREE_RESOURCES),
    ("SESGuid",                     EFI_GUID),
    ("MajorVersion",                UINT32),
    ("MinorVersion",                UINT32),
    ("EnablePageBreak",             SHELLENV_ENABLE_PAGE_BREAK),
    ("DisablePageBreak",            SHELLENV_DISABLE_PAGE_BREAK),
    ("GetPageBreak",                SHELLENV_GET_PAGE_BREAK),
    ("SetKeyFilter",                SHELLENV_SET_KEY_FILTER),
    ("GetKeyFilter",                SHELLENV_GET_KEY_FILTER),
    ("GetExecutionBreak",           SHELLENV_GET_EXECUTION_BREAK),
    ("IncrementShellNestingLevel",  SHELLENV_INCREMENT_SHELL_NESTING_LEVEL),
    ("DecrementShellNestingLevel",  SHELLENV_DECREMENT_SHELL_NESTING_LEVEL),
    ("IsRootShell",                 SHELLENV_IS_ROOT_SHELL),
    ("CloseConsoleProxy",           SHELLENV_CLOSE_CONSOLE_PROXY),
    ("HandleEnumerator",            HANDLE_ENUMERATOR),
    ("ProtocolInfoEnumerator",      PROTOCOL_INFO_ENUMERATOR),
    ("GetDeviceName",               GET_DEVICE_NAME),
    ("GetShellMode",                GET_SHELL_MODE),
    ("NameToPath",                  SHELLENV_NAME_TO_PATH),
    ("GetFsName",                   SHELLENV_GET_FS_NAME),
    ("FileMetaArgNoWildCard",       SHELLENV_FILE_META_ARG_NO_WILDCARD),
    ("DelDupFileArg",               SHELLENV_DEL_DUP_FILE),
    ("GetFsDevicePath",             SHELLENV_GET_FS_DEVICE_PATH)
  ]

