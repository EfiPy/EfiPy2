# PciExpress60.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress60
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard.PciExpress50 import *

PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_64_0_ID    = 0x0031
PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_64_0_VER1  = 0x1

PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CAPABILITIES_OFFSET               = 0x04
PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CONTROL_OFFSET                    = 0x08
PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_STATUS_OFFSET                     = 0x0C
PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_LANE_EQUALIZATION_CONTROL_OFFSET  = 0x10

PCI_EXPRESS_EXTENDED_CAPABILITY_DEVICE3_ID    = 0x002F
PCI_EXPRESS_EXTENDED_CAPABILITY_DEVICE3_VER1  = 0x1

EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_3_OFFSET  = 0x04
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_3_OFFSET       = 0x08
EFI_PCIE_CAPABILITY_DEVICE_STATUS_3_OFFSET        = 0x0C

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CAPABILITIES_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CONTROL_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationComplete",      UINT32, 1),
    ("EqualizationPhase1Success", UINT32, 1),
    ("EqualizationPhase2Success", UINT32, 1),
    ("EqualizationPhase3Success", UINT32, 1),
    ("LinkEqualizationRequest",   UINT32, 1),
    ("TransmitterPrecodingOn",    UINT32, 1),
    ("TransmitterPrecodeRequest", UINT32, 1),
    ("NoEqualizationNeededRcvd",  UINT32, 1),
    ("Reserved",                  UINT32, 24)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_STATUS_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset", UINT8, 4),
    ("UpstreamPortTransmitterPreset",   UINT8, 4)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint8",   UINT8)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_PHYSICAL_LAYER_64_0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                     ),
    ("Capablities",             PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CAPABILITIES             ),
    ("Control",                 PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_CONTROL                  ),
    ("Status",                  PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_STATUS                   ),
    ("LaneEqualizationControl", PCI_EXPRESS_REG_PHYSICAL_LAYER_64_0_LANE_EQUALIZATION_CONTROL * 1)
    ]

class PCI_REG_PCIE_DEVICE_CAPABILITY3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DmwrRequestRouting",        UINT32, 1),
    ("FourteenBitTagCompleter",   UINT32, 1),
    ("FourteenBitTagRequester",   UINT32, 1),
    ("ReceiverL0p",               UINT32, 1),
    ("PortL0pExitLatencyLatency", UINT32, 3),
    ("RetimerL0pExit",            UINT32, 3),
    ("Reserved",                  UINT32, 22)
  ]

class PCI_REG_PCIE_DEVICE_CAPABILITY3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PCI_REG_PCIE_DEVICE_CAPABILITY3_Bits),
    ("Uint32",  UINT32)
    ]

class PCI_REG_PCIE_DEVICE_CONTROL3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DmwrRequesterEnable",           UINT32, 1),
    ("DmwrEgressBlocking",            UINT32, 1),
    ("FourteenBitTagRequesterEnable", UINT32, 1),
    ("L0pEnable",                     UINT32, 1),
    ("TargetLinkWidth",               UINT32, 3),
    ("Reserved",                      UINT32, 25)
  ]

class PCI_REG_PCIE_DEVICE_CONTROL3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PCI_REG_PCIE_DEVICE_CONTROL3_Bits),
    ("Uint32",  UINT32)
    ]

class PCI_REG_PCIE_DEVICE_STATUS3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InitialLinkWidth   ", UINT32, 3),
    ("SegmentCaptured    ", UINT32, 1),
    ("RemoteL0pSupported ", UINT32, 1),
    ("Reserved           ", UINT32, 27)
  ]

class PCI_REG_PCIE_DEVICE_STATUS3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PCI_REG_PCIE_DEVICE_STATUS3_Bits),
    ("Uint32",  UINT32)
    ]

