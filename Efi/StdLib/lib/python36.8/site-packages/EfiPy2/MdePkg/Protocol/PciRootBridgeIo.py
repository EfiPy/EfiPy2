# PciRootBridgeIo.py
#
# EfiPy2.MdePkg.Protocol.PciRootBridgeIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiPciRootBridgeIoProtocolGuid = EFI_GUID( 0x2f707ebb, 0x4a1a, 0x11d4, (0x9a, 0x38, 0x00, 0x90, 0x27, 0x3f, 0xc1, 0x4d))

class EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL (Structure):
  pass

EfiPciWidthUint8                      =  0
EfiPciWidthUint16                     =  1
EfiPciWidthUint32                     =  2
EfiPciWidthUint64                     =  3
EfiPciWidthFifoUint8                  =  4
EfiPciWidthFifoUint16                 =  5
EfiPciWidthFifoUint32                 =  6
EfiPciWidthFifoUint64                 =  7
EfiPciWidthFillUint8                  =  8
EfiPciWidthFillUint16                 =  9
EfiPciWidthFillUint32                 = 10
EfiPciWidthFillUint64                 = 11
EfiPciWidthMaximum                    = 12
EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_WIDTH = ENUM

EfiPciOperationBusMasterRead              = 0
EfiPciOperationBusMasterWrite             = 1
EfiPciOperationBusMasterCommonBuffer      = 2
EfiPciOperationBusMasterRead64            = 3
EfiPciOperationBusMasterWrite64           = 4
EfiPciOperationBusMasterCommonBuffer64    = 5
EfiPciOperationMaximum                    = 6
EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_OPERATION = ENUM

EFI_PCI_ATTRIBUTE_ISA_MOTHERBOARD_IO          = 0x0001
EFI_PCI_ATTRIBUTE_ISA_IO                      = 0x0002
EFI_PCI_ATTRIBUTE_VGA_PALETTE_IO              = 0x0004
EFI_PCI_ATTRIBUTE_VGA_MEMORY                  = 0x0008
EFI_PCI_ATTRIBUTE_VGA_IO                      = 0x0010
EFI_PCI_ATTRIBUTE_IDE_PRIMARY_IO              = 0x0020
EFI_PCI_ATTRIBUTE_IDE_SECONDARY_IO            = 0x0040
EFI_PCI_ATTRIBUTE_MEMORY_WRITE_COMBINE        = 0x0080
EFI_PCI_ATTRIBUTE_MEMORY_CACHED               = 0x0800
EFI_PCI_ATTRIBUTE_MEMORY_DISABLE              = 0x1000
EFI_PCI_ATTRIBUTE_DUAL_ADDRESS_CYCLE          = 0x8000
EFI_PCI_ATTRIBUTE_ISA_IO_16                   = 0x10000
EFI_PCI_ATTRIBUTE_VGA_PALETTE_IO_16           = 0x20000
EFI_PCI_ATTRIBUTE_VGA_IO_16                   = 0x40000

EFI_PCI_ATTRIBUTE_VALID_FOR_ALLOCATE_BUFFER   = (
  EFI_PCI_ATTRIBUTE_MEMORY_WRITE_COMBINE  |
  EFI_PCI_ATTRIBUTE_MEMORY_CACHED         |
  EFI_PCI_ATTRIBUTE_DUAL_ADDRESS_CYCLE
  )

EFI_PCI_ATTRIBUTE_INVALID_FOR_ALLOCATE_BUFFER = (~EFI_PCI_ATTRIBUTE_VALID_FOR_ALLOCATE_BUFFER)

def EFI_PCI_ADDRESS(bus, dev, func, reg):

  BDF = (bus << 24) | (dev << 16) | (func << 8)

  if reg < 256:
    reg = reg
  else:
    reg = reg << 64

  return BDF | reg

class EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_PCI_ADDRESS (Structure):
  _fields_ = [
    ("Register",          UINT8),
    ("Function",          UINT8),
    ("Device",            UINT8),
    ("Bus",               UINT8),
    ("ExtendedRegister",  UINT32)
    ]

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_POLL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN  *This
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_WIDTH,      # IN  Width
  UINT64,                                     # IN  Address
  UINT64,                                     # IN  Mask
  UINT64,                                     # IN  Value
  UINT64,                                     # IN  Delay
  POINTER(UINT64)                             # OUT *Result
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_IO_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN     *This
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_WIDTH,      # IN     Width
  UINT64,                                     # IN     Address
  UINTN,                                      # IN     Count
  PVOID                                       # IN OUT *Buffer
  )

class EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ACCESS (Structure):
  _fields_ = [
    ("Read",  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_IO_MEM),
    ("Write", EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_IO_MEM)
    ]

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_COPY_MEM = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN *This
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_WIDTH,      # IN Width
  UINT64,                                     # IN DestAddress
  UINT64,                                     # IN SrcAddress
  UINTN                                       # IN Count
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_MAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN     *This
  EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_OPERATION,  # IN     Operation
  PVOID,                                      # IN     *HostAddress
  POINTER (UINTN),                            # IN OUT *NumberOfBytes
  POINTER (EFI_PHYSICAL_ADDRESS),             # OUT    *DeviceAddress
  POINTER (PVOID)                             # OUT    **Mapping
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_UNMAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN *This
  PVOID                                       # IN *Mapping
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ALLOCATE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  #   IN     *This
  EFI_ALLOCATE_TYPE,                          #   IN     Type
  EFI_MEMORY_TYPE,                            #   IN     MemoryType
  UINTN,                                      #   IN     Pages
  POINTER (PVOID),                            #   IN OUT **HostAddress
  UINT64                                      #   IN     Attributes
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_FREE_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN *This
  UINTN,                                      # IN Pages
  PVOID                                       # IN *HostAddress
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL)   # IN *This
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_GET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),  # IN  *This
  POINTER (UINT64),                           # OUT *Supports
  POINTER (UINT64)                            # OUT *Attributes
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_SET_ATTRIBUTES = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),      # IN     *This
  UINT64,                                         # IN     Attributes
  POINTER (UINT64),                               # IN OUT *ResourceBase
  POINTER (UINT64)                                # IN OUT *ResourceLength
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL),    # IN  *This
  POINTER (PVOID)                               # OUT **Resources
  )

EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL._fields_ = [
  ("ParentHandle"  , EFI_HANDLE                                     ),
  ("PollMem"       , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_POLL_IO_MEM    ),
  ("PollIo"        , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_POLL_IO_MEM    ),
  ("Mem"           , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ACCESS         ),
  ("Io"            , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ACCESS         ),
  ("Pci"           , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ACCESS         ),
  ("CopyMem"       , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_COPY_MEM       ),
  ("Map"           , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_MAP            ),
  ("Unmap"         , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_UNMAP          ),
  ("AllocateBuffer", EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_ALLOCATE_BUFFER),
  ("FreeBuffer"    , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_FREE_BUFFER    ),
  ("Flush"         , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_FLUSH          ),
  ("GetAttributes" , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_GET_ATTRIBUTES ),
  ("SetAttributes" , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_SET_ATTRIBUTES ),
  ("Configuration" , EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL_CONFIGURATION  ),
  ("SegmentNumber" , UINT32                                         )
  ]

