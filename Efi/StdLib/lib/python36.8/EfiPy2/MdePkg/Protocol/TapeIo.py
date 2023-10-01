# TapeIo.py
#
# EfiPy2.MdePkg.Protocol.TapeIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiTapeIoProtocolGuid    = \
  EFI_GUID (0x1e93e633, 0xd65a, 0x459e, (0xab, 0x84, 0x93, 0xd9, 0xec, 0x26, 0x6d, 0x18 ))

class EFI_TAPE_IO_PROTOCOL (Structure):
  pass

class EFI_TAPE_HEADER (Structure):
  _fields_ = [
    ("Signature",     UINT64),
    ("Revision",      UINT32),
    ("BootDescSize",  UINT32),
    ("BootDescCRC",   UINT32),
    ("TapeGUID",      EFI_GUID),
    ("TapeType",      EFI_GUID),
    ("TapeUnique",    EFI_GUID),
    ("BLLocation",    UINT32),
    ("BLBlocksize",   UINT32),
    ("BLFilesize",    UINT32),
    ("OSVersion",     CHAR8 * 40),
    ("AppVersion",    CHAR8 * 40),
    ("CreationDate",  CHAR8 * 10),
    ("CreationTime",  CHAR8 * 10),
    ("SystemName",    CHAR8 * 256),
    ("TapeTitle",     CHAR8 * 120),
    ("pad",           CHAR8 * 468)
  ]

EFI_TAPE_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL),  # IN      *This
  POINTER(UINTN),                 # IN OUT  *BufferSize,
  PVOID                           #    OUT  *Buffer
  )

EFI_TAPE_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL),  # IN  *This
  POINTER(UINTN),                 # IN  *BufferSize,
  PVOID                           # IN  *Buffer
  )

EFI_TAPE_REWIND = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL)   # IN  *This
  )

EFI_TAPE_SPACE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL),  # IN *This
  INTN,                           # IN Direction,
  UINTN                           # IN Type
  )

EFI_TAPE_WRITEFM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL),  # IN *This
  UINTN                           # IN Count
  )

EFI_TAPE_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_TAPE_IO_PROTOCOL),  # IN *This
  BOOLEAN                         # IN ExtendedVerification
  )

EFI_TAPE_IO_PROTOCOL._fields_ = [
    ("TapeRead",    EFI_TAPE_READ),
    ("TapeWrite",   EFI_TAPE_WRITE),
    ("TapeRewind",  EFI_TAPE_REWIND),
    ("TapeSpace",   EFI_TAPE_SPACE),
    ("TapeWriteFM", EFI_TAPE_WRITEFM),
    ("TapeReset",   EFI_TAPE_RESET)
  ]

