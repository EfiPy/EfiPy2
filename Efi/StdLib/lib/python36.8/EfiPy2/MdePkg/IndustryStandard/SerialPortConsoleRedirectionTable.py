# SerialPortConsoleRedirectionTable.py
#
# EfiPy2.MdePkg.IndustryStandard.SerialPortConsoleRedirectionTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_REVISION  = 0x02

EFI_ACPI_4_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_REVISION  = 0x04

class EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("InterfaceType",         UINT8),
    ("Reserved1",             UINT8 * 3),
    ("BaseAddress",           Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("InterruptType",         UINT8),
    ("Irq",                   UINT8),
    ("GlobalSystemInterrupt", UINT32),
    ("BaudRate",              UINT8),
    ("Parity",                UINT8),
    ("StopBits",              UINT8),
    ("FlowControl",           UINT8),
    ("TerminalType",          UINT8),
    ("Language",              UINT8),
    ("PciDeviceId",           UINT16),
    ("PciVendorId",           UINT16),
    ("PciBusNumber",          UINT8),
    ("PciDeviceNumber",       UINT8),
    ("PciFunctionNumber",     UINT8),
    ("PciFlags",              UINT32),
    ("PciSegment",            UINT8),
    ("Reserved2",             UINT32)
  ]

class EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  Acpi.EFI_ACPI_DESCRIPTION_HEADER           ),
    ("InterfaceType",           UINT8                                 ),
    ("Reserved1",               UINT8 * 3                             ),
    ("BaseAddress",             Acpi.EFI_ACPI_5_0_GENERIC_ADDRESS_STRUCTURE),
    ("InterruptType",           UINT8                                 ),
    ("Irq",                     UINT8                                 ),
    ("GlobalSystemInterrupt",   UINT32                                ),
    ("BaudRate",                UINT8                                 ),
    ("Parity",                  UINT8                                 ),
    ("StopBits",                UINT8                                 ),
    ("FlowControl",             UINT8                                 ),
    ("TerminalType",            UINT8                                 ),
    ("Reserved2",               UINT8                                 ),
    ("PciDeviceId",             UINT16                                ),
    ("PciVendorId",             UINT16                                ),
    ("PciBusNumber",            UINT8                                 ),
    ("PciDeviceNumber",         UINT8                                 ),
    ("PciFunctionNumber",       UINT8                                 ),
    ("PciFlags",                UINT32                                ),
    ("PciSegment",              UINT8                                 ),
    ("UartClockFrequency",      UINT32                                ),
    ("PreciseBaudRate",         UINT32                                ),
    ("NameSpaceStrLength",      UINT16                                ),
    ("NameSpaceStrOffset",      UINT16                                ),
    ("NameSpaceString",         CHAR8 * 0                             )
  ]

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_16550  = 0

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_16450  = 1

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_ARM_PL011_UART  = 0x03

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_NVIDIA_16550_UART  = 0x05

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_ARM_SBSA_GENERIC_UART_2X  = 0x0d

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_ARM_SBSA_GENERIC_UART  = 0x0e

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_DCC  = 0x0f

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_BCM2835_UART  = 0x10

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERFACE_TYPE_16550_WITH_GAS  = 0x12

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_8259  = 0x1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_APIC  = 0x2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_SAPIC  = 0x4
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_INTERRUPT_TYPE_GIC  = 0x8

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_9600    = 3
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_19200   = 4
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_57600   = 6
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_BAUD_RATE_115200  = 7

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_PARITY_NO_PARITY  = 0

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_STOP_BITS_1  = 1

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_DCD  = 0x1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_RTS_CTS  = 0x2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_FLOW_CONTROL_XON_XOFF  = 0x4

EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT100       = 0
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT100_PLUS  = 1
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_VT_UTF8     = 2
EFI_ACPI_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_TERMINAL_TYPE_ANSI        = 3
