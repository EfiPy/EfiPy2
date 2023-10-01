# SimpleFileSystem.py
#
# EfiPy2.MdePkg.Protocol.SimpleFileSystem
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

gEfiSimpleFileSystemProtocolGuid = EFI_GUID( 0x964e5b22, 0x6459, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

class EFI_SIMPLE_FILE_SYSTEM_PROTOCOL (Structure):
  pass

class EFI_FILE_PROTOCOL (Structure):
  pass

EFI_FILE_HANDLE = POINTER (EFI_FILE_PROTOCOL)

EFI_FILE_IO_INTERFACE = EFI_SIMPLE_FILE_SYSTEM_PROTOCOL
EFI_FILE              = EFI_FILE_PROTOCOL

EFI_SIMPLE_FILE_SYSTEM_PROTOCOL_OPEN_VOLUME = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_SIMPLE_FILE_SYSTEM_PROTOCOL),  # IN  *This
  POINTER(POINTER(EFI_FILE_PROTOCOL))         # OUT **Root
  )

EFI_SIMPLE_FILE_SYSTEM_PROTOCOL_REVISION  = 0x00010000

EFI_FILE_IO_INTERFACE_REVISION  = EFI_SIMPLE_FILE_SYSTEM_PROTOCOL_REVISION

EFI_SIMPLE_FILE_SYSTEM_PROTOCOL._fields_ = [
  ("Revision",    UINT64),
  ("OpenVolume",  EFI_SIMPLE_FILE_SYSTEM_PROTOCOL_OPEN_VOLUME)
  ]

EFI_FILE_OPEN = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN  *This
  POINTER(POINTER(EFI_FILE_PROTOCOL)),  # OUT **NewHandle
  PCHAR16,                              # IN  *FileName
  UINT64,                               # IN  OpenMode
  UINT64                                # IN  Attributes
  )

EFI_FILE_MODE_READ    = 0x0000000000000001
EFI_FILE_MODE_WRITE   = 0x0000000000000002
EFI_FILE_MODE_CREATE  = 0x8000000000000000

EFI_FILE_READ_ONLY  = 0x0000000000000001
EFI_FILE_HIDDEN     = 0x0000000000000002
EFI_FILE_SYSTEM     = 0x0000000000000004
EFI_FILE_RESERVED   = 0x0000000000000008
EFI_FILE_DIRECTORY  = 0x0000000000000010
EFI_FILE_ARCHIVE    = 0x0000000000000020
EFI_FILE_VALID_ATTR = 0x0000000000000037

EFI_FILE_CLOSE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL)           # IN  *This
  )

EFI_FILE_DELETE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL)           # IN  *This
  )

EFI_FILE_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (UINTN),                      # IN OUT *BufferSize
  PVOID                                 # OUT    *Buffer
  )

EFI_FILE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (UINTN),                      # IN OUT *BufferSize
  PVOID                                 # IN     *Buffer
  )

EFI_FILE_SET_POSITION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN *This
  UINT64                                # IN Position
  )

EFI_FILE_GET_POSITION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN  *This
  POINTER (UINT64)                      # OUT *Position
  )

EFI_FILE_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (EFI_GUID),                   # IN     *InformationType
  POINTER (UINTN),                      # IN OUT *BufferSize
  PVOID                                 # OUT    *Buffer
  )

EFI_FILE_SET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN *This
  POINTER (EFI_GUID),                   # IN *InformationType
  UINTN,                                # IN BufferSize
  PVOID                                 # IN *Buffer
  )

EFI_FILE_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL)           # IN *This
  )

class EFI_FILE_IO_TOKEN (Structure):
  _fields_ = [
    ("Event",       EFI_EVENT),
    ("Status",      EFI_STATUS),
    ("BufferSize",  UINTN),
    ("Buffer",      PVOID)
    ]

EFI_FILE_OPEN_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (POINTER (EFI_FILE_PROTOCOL)),# OUT    **NewHandle
  PCHAR16,                              # IN     *FileName
  UINT64,                               # IN     OpenMode
  UINT64,                               # IN     Attributes
  POINTER (EFI_FILE_IO_TOKEN)           # IN OUT *Token
  )

EFI_FILE_READ_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (EFI_FILE_IO_TOKEN)           # IN OUT *Token
  )

EFI_FILE_WRITE_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (EFI_FILE_IO_TOKEN)           # IN OUT *Token
  )

EFI_FILE_FLUSH_EX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_FILE_PROTOCOL),          # IN     *This
  POINTER (EFI_FILE_IO_TOKEN)           # IN OUT *Token
  )

EFI_FILE_PROTOCOL_REVISION        = 0x00010000
EFI_FILE_PROTOCOL_REVISION2       = 0x00020000
EFI_FILE_PROTOCOL_LATEST_REVISION = EFI_FILE_PROTOCOL_REVISION2

EFI_FILE_REVISION   = EFI_FILE_PROTOCOL_REVISION

EFI_FILE_PROTOCOL._fields_ = [
  ("Revision",    UINT64),
  ("Open",        EFI_FILE_OPEN),
  ("Close",       EFI_FILE_CLOSE),
  ("Delete",      EFI_FILE_DELETE),
  ("Read",        EFI_FILE_READ),
  ("Write",       EFI_FILE_WRITE),
  ("GetPosition", EFI_FILE_GET_POSITION),
  ("SetPosition", EFI_FILE_SET_POSITION),
  ("GetInfo",     EFI_FILE_GET_INFO),
  ("SetInfo",     EFI_FILE_SET_INFO),
  ("Flush",       EFI_FILE_FLUSH),
  ("OpenEx",      EFI_FILE_OPEN_EX),
  ("ReadEx",      EFI_FILE_READ_EX),
  ("WriteEx",     EFI_FILE_WRITE_EX),
  ("FlushEx",     EFI_FILE_FLUSH_EX),
  ]

