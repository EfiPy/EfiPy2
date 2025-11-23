# StmResourceDescriptor.py
#
# EfiPy2.MdePkg.Register.Intel.StmResourceDescriptor
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class STM_RSC_DESC_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("RscType",         UINT32),
    ("Length",          UINT16),
    ("ReturnStatus",    UINT16, 1),
    ("Reserved",        UINT16, 14),
    ("IgnoreResource",  UINT16, 1)
  ]

END_OF_RESOURCES      = 0
MEM_RANGE             = 1
IO_RANGE              = 2
MMIO_RANGE            = 3
MACHINE_SPECIFIC_REG  = 4
PCI_CFG_RANGE         = 5
TRAPPED_IO_RANGE      = 6
ALL_RESOURCES         = 7
REGISTER_VIOLATION    = 8
MAX_DESC_TYPE         = 8

class STM_RSC_END (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                         STM_RSC_DESC_HEADER),
    ("ResourceListContinuation",    UINT64)
  ]

class STM_RSC_MEM_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("Base",            UINT64),
    ("Length",          UINT64),
    ("RWXAttributes",   UINT32, 3),
    ("Reserved",        UINT32, 29),
    ("Reserved_2",      UINT32)
  ]

STM_RSC_MEM_R  = 0x1
STM_RSC_MEM_W  = 0x2
STM_RSC_MEM_X  = 0x4

class STM_RSC_IO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER),
    ("Base",        UINT16),
    ("Length",      UINT16),
    ("Reserved",    UINT32)
  ]

class STM_RSC_MMIO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("Base",            UINT64),
    ("Length",          UINT64),
    ("RWXAttributes",   UINT32, 3),
    ("Reserved",        UINT32, 29),
    ("Reserved_2",      UINT32)
  ]

STM_RSC_MMIO_R  = 0x1
STM_RSC_MMIO_W  = 0x2
STM_RSC_MMIO_X  = 0x4

class STM_RSC_MSR_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                     STM_RSC_DESC_HEADER),
    ("MsrIndex",                UINT32),
    ("KernelModeProcessing",    UINT32, 1),
    ("Reserved",                UINT32, 31),
    ("ReadMask",                UINT64),
    ("WriteMask",               UINT64)
  ]

class STM_PCI_DEVICE_PATH_NODE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT8),
    ("Subtype",     UINT8),
    ("Length",      UINT16),
    ("PciFunction", UINT8),
    ("PciDevice",   UINT8)
  ]

class STM_RSC_PCI_CFG_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                     STM_RSC_DESC_HEADER),
    ("RWAttributes",            UINT16, 2),
    ("Reserved",                UINT16, 14),
    ("Base",                    UINT16),
    ("Length",                  UINT16),
    ("OriginatingBusNumber",    UINT8),
    ("LastNodeIndex",           UINT8),
    ("PciDevicePath",           STM_PCI_DEVICE_PATH_NODE * 1)
    # ("PciDevicePath",           STM_PCI_DEVICE_PATH_NODE * (LastNodeIndex + 1))
  ]

STM_RSC_PCI_CFG_R  = 0x1
STM_RSC_PCI_CFG_W  = 0x2

class STM_RSC_TRAPPED_IO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER),
    ("Base",        UINT16),
    ("Length",      UINT16),
    ("In",          UINT16, 1),
    ("Out",         UINT16, 1),
    ("Api",         UINT16, 1),
    ("Reserved1",   UINT16, 13),
    ("Reserved2",   UINT16)
  ]

class STM_RSC_ALL_RESOURCES_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER)
  ]

class STM_REGISTER_VIOLATION_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("RegisterType",    UINT32),
    ("Reserved",        UINT32),
    ("ReadMask",        UINT64),
    ("WriteMask",       UINT64)
  ]

StmRegisterCr0 = 0
StmRegisterCr2 = 1
StmRegisterCr3 = 2
StmRegisterCr4 = 3
StmRegisterCr8 = 4
StmRegisterMax = 5
STM_REGISTER_VIOLATION_TYPE = ENUM

class STM_RSC (Union):
  _pack_   = 1
  _fields_ = [
    ("Header",              STM_RSC_DESC_HEADER),
    ("End",                 STM_RSC_END),
    ("Mem",                 STM_RSC_MEM_DESC),
    ("Io",                  STM_RSC_IO_DESC),
    ("Mmio",                STM_RSC_MMIO_DESC),
    ("Msr",                 STM_RSC_MSR_DESC),
    ("PciCfg",              STM_RSC_PCI_CFG_DESC),
    ("TrappedIo",           STM_RSC_TRAPPED_IO_DESC),
    ("All",                 STM_RSC_ALL_RESOURCES_DESC),
    ("RegisterViolation",   STM_REGISTER_VIOLATION_DESC)
  ]

