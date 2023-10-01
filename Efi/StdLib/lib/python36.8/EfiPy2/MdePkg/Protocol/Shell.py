# Shell.py
#
# EfiPy2.MdePkg.Protocol.Shell
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Guid.FileInfo import EFI_FILE_INFO

gEfiShellProtocolGuid           = \
  EFI_GUID (0x6302d008, 0x7f9b, 0x4f30, ( 0x87, 0xac, 0x60, 0xc9, 0xfe, 0xf5, 0xda, 0x4e ))

SHELL_FILE_HANDLE = PVOID

SHELL_SUCCESS               = 0
SHELL_LOAD_ERROR            = 1
SHELL_INVALID_PARAMETER     = 2
SHELL_UNSUPPORTED           = 3
SHELL_BAD_BUFFER_SIZE       = 4
SHELL_BUFFER_TOO_SMALL      = 5
SHELL_NOT_READY             = 6
SHELL_DEVICE_ERROR          = 7
SHELL_WRITE_PROTECTED       = 8
SHELL_OUT_OF_RESOURCES      = 9
SHELL_VOLUME_CORRUPTED      = 10
SHELL_VOLUME_FULL           = 11
SHELL_NO_MEDIA              = 12
SHELL_MEDIA_CHANGED         = 13
SHELL_NOT_FOUND             = 14
SHELL_ACCESS_DENIED         = 15
SHELL_TIMEOUT               = 18
SHELL_NOT_STARTED           = 19
SHELL_ALREADY_STARTED       = 20
SHELL_ABORTED               = 21
SHELL_INCOMPATIBLE_VERSION  = 25
SHELL_SECURITY_VIOLATION    = 26
SHELL_NOT_EQUAL             = 27
SHELL_STATUS                = ENUM

class EFI_SHELL_FILE_INFO (Structure):
  _fields_ = [
    ("Link",        LIST_ENTRY),
    ("Status",      EFI_STATUS),
    ("FullName",    POINTER(CHAR16)),
    ("FileName",    POINTER(CHAR16)),
    ("Handle",      SHELL_FILE_HANDLE),
    ("Info",        POINTER(EFI_FILE_INFO))
  ]

EFI_SHELL_BATCH_IS_ACTIVE = CFUNCTYPE (
  BOOLEAN
  )

EFI_SHELL_CLOSE_FILE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE     #   IN FileHandle
  )

EFI_SHELL_CREATE_FILE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),              #   IN CONST *FileName,
  UINT64,                       #   IN       FileAttribs,
  POINTER(SHELL_FILE_HANDLE)    #   OUT      *FileHandl
  )

EFI_SHELL_DELETE_FILE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE     #   IN      FileHandl
  )

EFI_SHELL_DELETE_FILE_BY_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),              #   IN CONST *FileName
  )

EFI_SHELL_DISABLE_PAGE_BREAK = CFUNCTYPE (
  VOID
  )

EFI_SHELL_ENABLE_PAGE_BREAK = CFUNCTYPE (
  VOID
  )

EFI_SHELL_EXECUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HANDLE),      #   IN  *ParentImageHandle,
  POINTER(CHAR16),          #   IN  *CommandLine OPTIONAL,
  POINTER(POINTER(CHAR16)), #   IN  **Environment OPTIONAL,
  POINTER(EFI_STATUS)       #   OUT *StatusCode OPTIONAL
  )

EFI_SHELL_FIND_FILES = CFUNCTYPE (
  EFI_STATUS,
  CHAR16,                                #   IN CONST *FilePattern,
  POINTER(POINTER(EFI_SHELL_FILE_INFO))  #   OUT      **FileList
  )

EFI_SHELL_FIND_FILES_IN_DIR = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,                     #   IN     FileDirHandle,
  POINTER(POINTER(EFI_SHELL_FILE_INFO))  #   OUT    **FileList
  )

EFI_SHELL_FLUSH_FILE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,                     #   IN     FileDirHandle
  )

EFI_SHELL_FREE_FILE_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_SHELL_FILE_INFO))  #   IN     **FileList
  )

EFI_SHELL_GET_CUR_DIR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16)  #   IN CONST *FileSystemMapping OPTIONAL
  )

EFI_SHELL_DEVICE_NAME_FLAGS         = UINT32

# #define EFI_DEVICE_NAME_USE_COMPONENT_NAME  0x00000001
# #define EFI_DEVICE_NAME_USE_DEVICE_PATH     0x00000002
EFI_DEVICE_NAME_USE_COMPONENT_NAME  = 0x00000001
EFI_DEVICE_NAME_USE_DEVICE_PATH     = 0x00000002

EFI_SHELL_GET_DEVICE_NAME = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                  #   IN  DeviceHandle,
  EFI_SHELL_DEVICE_NAME_FLAGS, #   IN  Flags,
  POINTER(CHAR8),              #   IN  *Language,
  POINTER(POINTER(CHAR16))     #   OUT **BestDeviceName
  )

EFI_SHELL_GET_DEVICE_PATH_FROM_MAP = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(CHAR16)                   #   IN CONST  *Mapping
  )

EFI_SHELL_GET_DEVICE_PATH_FROM_FILE_PATH = CFUNCTYPE (
  POINTER(EFI_DEVICE_PATH_PROTOCOL),
  POINTER(CHAR16)                   #   IN CONST  *Path
  )

EFI_SHELL_GET_ENV = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16)       #   IN CONST *Name OPTIONAL
  )

EFI_SHELL_GET_ENV_EX = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16),  #   IN CONST *Name OPTIONAL
  POINTER(UINT32)   #   OUT      *Attributes OPTIONAL
  )

EFI_SHELL_GET_FILE_INFO = CFUNCTYPE (
  POINTER(EFI_FILE_INFO),
  SHELL_FILE_HANDLE         #   IN  FileHandle
  )

EFI_SHELL_GET_FILE_PATH_FROM_DEVICE_PATH = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(EFI_DEVICE_PATH_PROTOCOL)     #   IN CONST  *Path
  )

EFI_SHELL_GET_FILE_POSITION = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,    #   IN  FileHandle,
  POINTER(UINT64)       #   OUT *Position
  )

EFI_SHELL_GET_FILE_SIZE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,    #   IN  FileHandle,
  POINTER(UINT64)       #   OUT *Size
  )

EFI_SHELL_GET_GUID_FROM_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),      #   IN  CONST *GuidName,
  POINTER(EFI_GUID)     #   OUT       *Guid
  )

EFI_SHELL_GET_GUID_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),        #   IN  CONST *Guid,
  POINTER(POINTER(CHAR16))  #   OUT CONST **GuidName
  )

EFI_SHELL_GET_HELP_TEXT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),          #   IN CONST *Command,
  POINTER(CHAR16),          #   IN CONST *Sections OPTIONAL,
  POINTER(POINTER(CHAR16))  #   OUT      **HelpText
  )

EFI_SHELL_GET_MAP_FROM_DEVICE_PATH = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(POINTER(EFI_DEVICE_PATH_PROTOCOL))  #   IN OUT  **DevicePath
  )

EFI_SHELL_GET_PAGE_BREAK = CFUNCTYPE (
  BOOLEAN
  )

EFI_SHELL_IS_ROOT_SHELL = CFUNCTYPE (
  BOOLEAN
  )

EFI_SHELL_OPEN_FILE_BY_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),              #   IN CONST    *FileName,
  POINTER(SHELL_FILE_HANDLE),   #   OUT         *FileHandle,
  UINT64                        #   IN          OpenMode
  )

EFI_SHELL_OPEN_FILE_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),                      #   IN      *Path,
  UINT64,                               #   IN      OpenMode,
  POINTER(POINTER(EFI_SHELL_FILE_INFO)) #   IN OUT  **FileList
  )

EFI_SHELL_OPEN_ROOT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    #   IN  *DevicePath,
  POINTER(SHELL_FILE_HANDLE)            #   OUT *FileHandle
  )

EFI_SHELL_OPEN_ROOT_BY_HANDLE = CFUNCTYPE (
  EFI_STATUS,
  EFI_HANDLE,                   #   IN  DeviceHandle,
  POINTER(SHELL_FILE_HANDLE)    #   OUT *FileHandle
  )

EFI_SHELL_READ_FILE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE, #   IN     FileHandle,
  POINTER(UINTN),    #   IN OUT *ReadSize,
  PVOID              #   IN OUT *Buffer
  )

EFI_SHELL_REGISTER_GUID_NAME = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID), #   IN CONST *Guid,
  POINTER(CHAR16)    #   IN CONST *GuidName
  )

EFI_SHELL_REMOVE_DUP_IN_FILE_LIST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(POINTER(EFI_SHELL_FILE_INFO)) #   IN  **FileList
  )

EFI_SHELL_SET_ALIAS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),  #   IN CONST *Command,
  POINTER(CHAR16),  #   IN CONST *Alias,
  BOOLEAN,          #   IN       Replace,
  BOOLEAN           #   IN       Volatile
  )

EFI_SHELL_GET_ALIAS = CFUNCTYPE (
  POINTER(CHAR16),
  POINTER(CHAR16),  #   IN  CONST *Alias,
  POINTER(BOOLEAN)  #   OUT       *Volatile OPTIONAL
  )

EFI_SHELL_SET_CUR_DIR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),  #   IN CONST *FileSystem OPTIONAL,
  POINTER(CHAR16)   #   IN CONST *Dir
  )

EFI_SHELL_SET_ENV = CFUNCTYPE (
  EFI_STATUS,
  POINTER(CHAR16),  #   IN CONST *Name,
  POINTER(CHAR16),  #   IN CONST *Value,
  BOOLEAN           #   IN       Volatile
  )

EFI_SHELL_SET_FILE_INFO = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,        #   IN       FileHandle,
  POINTER(EFI_FILE_INFO)    #   IN CONST *FileInfo
  )

EFI_SHELL_SET_FILE_POSITION = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,        #   IN       FileHandle,
  UINT64                    #   IN       Position
  )

EFI_SHELL_SET_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEVICE_PATH_PROTOCOL),    #   IN CONST *DevicePath,
  POINTER(CHAR16)                       #   IN CONST *Mapping
  )

EFI_SHELL_WRITE_FILE = CFUNCTYPE (
  EFI_STATUS,
  SHELL_FILE_HANDLE,  #   IN      FileHandle,
  POINTER(UINTN),     #   IN OUT  *BufferSize,
  PVOID               #   IN      *Buffer
  )

class EFI_SHELL_PROTOCOL (Structure):
  _fields_ = [
    ("Execute",                     EFI_SHELL_EXECUTE),
    ("GetEnv",                      EFI_SHELL_GET_ENV),
    ("SetEnv",                      EFI_SHELL_SET_ENV),
    ("GetAlias",                    EFI_SHELL_GET_ALIAS),
    ("SetAlias",                    EFI_SHELL_SET_ALIAS),
    ("GetHelpText",                 EFI_SHELL_GET_HELP_TEXT),
    ("GetDevicePathFromMap",        EFI_SHELL_GET_DEVICE_PATH_FROM_MAP),
    ("GetMapFromDevicePath",        EFI_SHELL_GET_MAP_FROM_DEVICE_PATH),
    ("GetDevicePathFromFilePath",   EFI_SHELL_GET_DEVICE_PATH_FROM_FILE_PATH),
    ("GetFilePathFromDevicePath",   EFI_SHELL_GET_FILE_PATH_FROM_DEVICE_PATH),
    ("SetMap",                      EFI_SHELL_SET_MAP),
    ("GetCurDir",                   EFI_SHELL_GET_CUR_DIR),
    ("SetCurDir",                   EFI_SHELL_SET_CUR_DIR),
    ("OpenFileList",                EFI_SHELL_OPEN_FILE_LIST),
    ("FreeFileList",                EFI_SHELL_FREE_FILE_LIST),
    ("RemoveDupInFileList",         EFI_SHELL_REMOVE_DUP_IN_FILE_LIST),
    ("BatchIsActive",               EFI_SHELL_BATCH_IS_ACTIVE),
    ("IsRootShell",                 EFI_SHELL_IS_ROOT_SHELL),
    ("EnablePageBreak",             EFI_SHELL_ENABLE_PAGE_BREAK),
    ("DisablePageBreak",            EFI_SHELL_DISABLE_PAGE_BREAK),
    ("GetPageBreak",                EFI_SHELL_GET_PAGE_BREAK),
    ("GetDeviceName",               EFI_SHELL_GET_DEVICE_NAME),
    ("GetFileInfo",                 EFI_SHELL_GET_FILE_INFO),
    ("SetFileInfo",                 EFI_SHELL_SET_FILE_INFO),
    ("OpenFileByName",              EFI_SHELL_OPEN_FILE_BY_NAME),
    ("CloseFile",                   EFI_SHELL_CLOSE_FILE),
    ("CreateFile",                  EFI_SHELL_CREATE_FILE),
    ("ReadFile",                    EFI_SHELL_READ_FILE),
    ("WriteFile",                   EFI_SHELL_WRITE_FILE),
    ("DeleteFile",                  EFI_SHELL_DELETE_FILE),
    ("DeleteFileByName",            EFI_SHELL_DELETE_FILE_BY_NAME),
    ("GetFilePosition",             EFI_SHELL_GET_FILE_POSITION),
    ("SetFilePosition",             EFI_SHELL_SET_FILE_POSITION),
    ("FlushFile",                   EFI_SHELL_FLUSH_FILE),
    ("FindFiles",                   EFI_SHELL_FIND_FILES),
    ("FindFilesInDir",              EFI_SHELL_FIND_FILES_IN_DIR),
    ("GetFileSize",                 EFI_SHELL_GET_FILE_SIZE),
    ("OpenRoot",                    EFI_SHELL_OPEN_ROOT),
    ("OpenRootByHandle",            EFI_SHELL_OPEN_ROOT_BY_HANDLE),
    ("ExecutionBreak",              EFI_EVENT),
    ("MajorVersion",                UINT32),
    ("MinorVersion",                UINT32),
    ("RegisterGuidName",            EFI_SHELL_REGISTER_GUID_NAME),
    ("GetGuidName",                 EFI_SHELL_GET_GUID_NAME),
    ("GetGuidFromName",             EFI_SHELL_GET_GUID_FROM_NAME),
    ("GetEnvEx",                    EFI_SHELL_GET_ENV_EX)
  ]
