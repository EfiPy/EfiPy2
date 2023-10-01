# DebugPort2Table.py
#
# EfiPy2.MdePkg.IndustryStandard.DebugPort2Table
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_DBG2_DEBUG_DEVICE_INFORMATION_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",                        UINT8 ),
    ("Length",                          UINT16),
    ("NumberofGenericAddressRegisters", UINT8 ),
    ("NameSpaceStringLength",           UINT16),
    ("NameSpaceStringOffset",           UINT16),
    ("OemDataLength",                   UINT16),
    ("OemDataOffset",                   UINT16),
    ("PortType",                        UINT16),
    ("PortSubtype",                     UINT16),
    ("Reserved",                        UINT8 * 2),
    ("BaseAddressRegisterOffset",       UINT16),
    ("AddressSizeOffset",               UINT16)
  ]

EFI_ACPI_DBG2_DEBUG_DEVICE_INFORMATION_STRUCT_REVISION      = 0x00

EFI_ACPI_DBG2_PORT_TYPE_SERIAL                                                 = 0x8000
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_FULL_16550                                   = 0x0000
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC    = 0x0001
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_ARM_PL011_UART                               = 0x0003
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_NVIDIA_16550_UART                            = 0x0005
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_ARM_SBSA_GENERIC_UART_2X                     = 0x000d
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_ARM_SBSA_GENERIC_UART                        = 0x000e
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_DCC                                          = 0x000f
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_BCM2835_UART                                 = 0x0010
EFI_ACPI_DBG2_PORT_SUBTYPE_SERIAL_16550_WITH_GAS                               = 0x0012
EFI_ACPI_DBG2_PORT_TYPE_1394                                                   = 0x8001
EFI_ACPI_DBG2_PORT_SUBTYPE_1394_STANDARD                                       = 0x0000
EFI_ACPI_DBG2_PORT_TYPE_USB                                                    = 0x8002
EFI_ACPI_DBG2_PORT_SUBTYPE_USB_XHCI                                            = 0x0000
EFI_ACPI_DBG2_PORT_SUBTYPE_USB_EHCI                                            = 0x0001
EFI_ACPI_DBG2_PORT_TYPE_NET                                                    = 0x8003

class EFI_ACPI_DEBUG_PORT_2_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("OffsetDbgDeviceInfo",   UINT32),
    ("NumberDbgDeviceInfo",   UINT32)
  ]

EFI_ACPI_DEBUG_PORT_2_TABLE_REVISION      = 0x00
