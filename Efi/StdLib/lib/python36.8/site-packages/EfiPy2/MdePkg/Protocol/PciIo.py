# PciIo.py
#
# EfiPy2.MdePkg.Protocol.PciIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPciIoProtocolGuid = \
  EFI_GUID (0x4cf5b200, 0x68b8, 0x4ca5, (0x9e, 0xec, 0xb2, 0x3e, 0x3f, 0x50, 0x2, 0x9a ))

class EFI_PCI_IO_PROTOCOL (Structure):
  pass

EfiPciIoWidthUint8          = 0
EfiPciIoWidthUint16         = 1
EfiPciIoWidthUint32         = 2
EfiPciIoWidthUint64         = 3
EfiPciIoWidthFifoUint8      = 4
EfiPciIoWidthFifoUint16     = 5
EfiPciIoWidthFifoUint32     = 6
EfiPciIoWidthFifoUint64     = 7
EfiPciIoWidthFillUint8      = 8
EfiPciIoWidthFillUint16     = 9
EfiPciIoWidthFillUint32     = 10
EfiPciIoWidthFillUint64     = 11
EfiPciIoWidthMaximum        = 12
EFI_PCI_IO_PROTOCOL_WIDTH   = ENUM

EFI_PCI_IO_PASS_THROUGH_BAR               = 0xff
EFI_PCI_IO_ATTRIBUTE_MASK                 = 0x077f
EFI_PCI_IO_ATTRIBUTE_ISA_MOTHERBOARD_IO   = 0x0001
EFI_PCI_IO_ATTRIBUTE_ISA_IO               = 0x0002
EFI_PCI_IO_ATTRIBUTE_VGA_PALETTE_IO       = 0x0004
EFI_PCI_IO_ATTRIBUTE_VGA_MEMORY           = 0x0008
EFI_PCI_IO_ATTRIBUTE_VGA_IO               = 0x0010
EFI_PCI_IO_ATTRIBUTE_IDE_PRIMARY_IO       = 0x0020
EFI_PCI_IO_ATTRIBUTE_IDE_SECONDARY_IO     = 0x0040
EFI_PCI_IO_ATTRIBUTE_MEMORY_WRITE_COMBINE = 0x0080
EFI_PCI_IO_ATTRIBUTE_IO                   = 0x0100
EFI_PCI_IO_ATTRIBUTE_MEMORY               = 0x0200
EFI_PCI_IO_ATTRIBUTE_BUS_MASTER           = 0x0400
EFI_PCI_IO_ATTRIBUTE_MEMORY_CACHED        = 0x0800
EFI_PCI_IO_ATTRIBUTE_MEMORY_DISABLE       = 0x1000
EFI_PCI_IO_ATTRIBUTE_EMBEDDED_DEVICE      = 0x2000
EFI_PCI_IO_ATTRIBUTE_EMBEDDED_ROM         = 0x4000
EFI_PCI_IO_ATTRIBUTE_DUAL_ADDRESS_CYCLE   = 0x8000
EFI_PCI_IO_ATTRIBUTE_ISA_IO_16            = 0x10000
EFI_PCI_IO_ATTRIBUTE_VGA_PALETTE_IO_16    = 0x20000
EFI_PCI_IO_ATTRIBUTE_VGA_IO_16            = 0x40000

EFI_PCI_DEVICE_ENABLE   = (EFI_PCI_IO_ATTRIBUTE_IO | EFI_PCI_IO_ATTRIBUTE_MEMORY | EFI_PCI_IO_ATTRIBUTE_BUS_MASTER)
EFI_VGA_DEVICE_ENABLE   = (EFI_PCI_IO_ATTRIBUTE_VGA_PALETTE_IO | EFI_PCI_IO_ATTRIBUTE_VGA_MEMORY | EFI_PCI_IO_ATTRIBUTE_VGA_IO | EFI_PCI_IO_ATTRIBUTE_IO)

EfiPciIoOperationBusMasterRead          = 0
EfiPciIoOperationBusMasterWrite         = 1
EfiPciIoOperationBusMasterCommonBuffer  = 2
EfiPciIoOperationMaximum                = 3
EFI_PCI_IO_PROTOCOL_OPERATION           = ENUM

EfiPciIoAttributeOperationGet             = 0
EfiPciIoAttributeOperationSet             = 1
EfiPciIoAttributeOperationEnable          = 2
EfiPciIoAttributeOperationDisable         = 3
EfiPciIoAttributeOperationSupported       = 4
EfiPciIoAttributeOperationMaximum         = 5
EFI_PCI_IO_PROTOCOL_ATTRIBUTE_OPERATION   = ENUM

EFI_PCI_IO_PROTOCOL_POLL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_IO_PROTOCOL),         # IN  *This,
  EFI_PCI_IO_PROTOCOL_WIDTH,            # IN  Width,
  UINT8,                                # IN  BarIndex,
  UINT64,                               # IN  Offset,
  UINT64,                               # IN  Mask,
  UINT64,                               # IN  Value,
  UINT64,                               # IN  Delay,
  POINTER(UINT64)                       # OUT *Result
  )

EFI_PCI_IO_PROTOCOL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_IO_PROTOCOL),         # IN      *This,
  EFI_PCI_IO_PROTOCOL_WIDTH,            # IN      Width,
  UINT8,                                # IN      BarIndex,
  UINT64,                               # IN      Offset,
  UINTN,                                # IN      Count,
  PVOID                                 # IN OUT  *Buffer
  )

class EFI_PCI_IO_PROTOCOL_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_PCI_IO_PROTOCOL_IO_MEM),
    ("Write", EFI_PCI_IO_PROTOCOL_IO_MEM),
  ]

EFI_PCI_IO_PROTOCOL_CONFIG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN     *This
  EFI_PCI_IO_PROTOCOL_WIDTH,      # IN     Width,
  UINT32,                         # IN     Offset,
  UINTN,                          # IN     Count,
  PVOID                           # IN OUT *Buffer
  )

class EFI_PCI_IO_PROTOCOL_CONFIG_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_PCI_IO_PROTOCOL_CONFIG),
    ("Write", EFI_PCI_IO_PROTOCOL_CONFIG),
  ]

EFI_PCI_IO_PROTOCOL_COPY_MEM = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN     *This
  EFI_PCI_IO_PROTOCOL_WIDTH,      # IN     Width,
  UINT8,                          # IN     DestBarIndex,
  UINT64,                         # IN     DestOffset,
  UINT8,                          # IN     SrcBarIndex,
  UINT64,                         # IN     SrcOffset,
  UINTN                           # IN     Count
  )

EFI_PCI_IO_PROTOCOL_MAP = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN     *This
  EFI_PCI_IO_PROTOCOL_OPERATION,  # IN     Operation,
  PVOID,                          # IN     *HostAddress,
  POINTER(UINTN),                 # IN OUT *NumberOfBytes,
  POINTER(EFI_PHYSICAL_ADDRESS),  # OUT    *DeviceAddress,
  POINTER(PVOID)                  # OUT    **Mapping
  )

EFI_PCI_IO_PROTOCOL_UNMAP = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN     *This
  PVOID                           # IN     *Mapping
  )

EFI_PCI_IO_PROTOCOL_ALLOCATE_BUFFER = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN  *This
  EFI_ALLOCATE_TYPE,              # IN  Type,
  EFI_MEMORY_TYPE,                # IN  MemoryType,
  UINTN,                          # IN  Pages,
  POINTER(PVOID),                 # OUT **HostAddress,
  UINT64                          # IN  Attributes
  )

EFI_PCI_IO_PROTOCOL_FREE_BUFFER = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),   # IN  *This
  UINTN,                          # IN  Pages,
  PVOID                           # IN  *HostAddress
  )

EFI_PCI_IO_PROTOCOL_FLUSH = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL)    # IN  *This
  )

EFI_PCI_IO_PROTOCOL_GET_LOCATION = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),         # IN  *This
  POINTER(UINTN),                       # OUT *SegmentNumber,
  POINTER(UINTN),                       # OUT *BusNumber,
  POINTER(UINTN),                       # OUT *DeviceNumber,
  POINTER(UINTN)                        # OUT *FunctionNumber
  )

EFI_PCI_IO_PROTOCOL_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),             # IN  *This
  EFI_PCI_IO_PROTOCOL_ATTRIBUTE_OPERATION,  # OUT *SegmentNumber,
  UINT64,                                   # IN  Attributes,
  POINTER(UINT64)                           # OUT *Result OPTIONAL
  )

EFI_PCI_IO_PROTOCOL_GET_BAR_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),         # IN  *This
  UINT8,                                # IN  BarIndex,
  UINT64,                               # OUT *Supports, OPTIONAL
  POINTER(PVOID)                        # OUT **Resources OPTIONAL
  )

EFI_PCI_IO_PROTOCOL_SET_BAR_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,                     
  POINTER(EFI_PCI_IO_PROTOCOL),         # IN     *This
  UINT64,                               # IN     Attributes,
  UINT8,                                # IN     BarIndex,
  POINTER(UINT64),                      # IN OUT *Offset,
  POINTER(UINT64)                       # IN OUT *Length
  )

EFI_PCI_IO_PROTOCOL._fields_ = [
    ("PollMem",           EFI_PCI_IO_PROTOCOL_POLL_IO_MEM),
    ("PollIo",            EFI_PCI_IO_PROTOCOL_POLL_IO_MEM),
    ("Mem",               EFI_PCI_IO_PROTOCOL_ACCESS),
    ("Io",                EFI_PCI_IO_PROTOCOL_ACCESS),
    ("Pci",               EFI_PCI_IO_PROTOCOL_CONFIG_ACCESS),
    ("CopyMem",           EFI_PCI_IO_PROTOCOL_COPY_MEM),
    ("Map",               EFI_PCI_IO_PROTOCOL_MAP),
    ("Unmap",             EFI_PCI_IO_PROTOCOL_UNMAP),
    ("AllocateBuffer",    EFI_PCI_IO_PROTOCOL_ALLOCATE_BUFFER),
    ("FreeBuffer",        EFI_PCI_IO_PROTOCOL_FREE_BUFFER),
    ("Flush",             EFI_PCI_IO_PROTOCOL_FLUSH),
    ("GetLocation",       EFI_PCI_IO_PROTOCOL_GET_LOCATION),
    ("Attributes",        EFI_PCI_IO_PROTOCOL_ATTRIBUTES),
    ("GetBarAttributes",  EFI_PCI_IO_PROTOCOL_GET_BAR_ATTRIBUTES),
    ("SetBarAttributes",  EFI_PCI_IO_PROTOCOL_SET_BAR_ATTRIBUTES),
    ("RomSize",           UINT64),
    ("RomImage",          PVOID)
  ]

