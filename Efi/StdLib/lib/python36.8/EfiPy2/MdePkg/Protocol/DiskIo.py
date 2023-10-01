# DiskIo.py
#
# EfiPy2.MdePkg.Protocol.DiskIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiDiskIoProtocolGuid      = \
  EFI_GUID (0xce345171, 0xba0b, 0x11d2, (0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

DISK_IO_PROTOCOL  = gEfiDiskIoProtocolGuid

class EFI_DISK_IO_PROTOCOL (Structure):
  pass

EFI_DISK_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # OUT *Buffer
  )

EFI_DISK_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # IN  *Buffer
  )

EFI_DISK_IO_PROTOCOL_REVISION = 0x00010000

EFI_DISK_IO_INTERFACE_REVISION  = EFI_DISK_IO_PROTOCOL_REVISION

EFI_DISK_IO_PROTOCOL._fields_ = [
    ("Revision",  UINT64),
    ("ReadDisk",  EFI_DISK_READ),
    ("WriteDisk", EFI_DISK_WRITE)
  ]

