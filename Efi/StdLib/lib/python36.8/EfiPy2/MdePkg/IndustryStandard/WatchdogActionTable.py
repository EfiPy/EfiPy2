# WatchdogActionTable.py
#
# EfiPy2.MdePkg.IndustryStandard.WatchdogActionTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

class EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                            Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("WatchdogHeaderLength",              UINT32),
    ("PCISegment",                        UINT16),
    ("PCIBusNumber",                      UINT8),
    ("PCIDeviceNumber",                   UINT8),
    ("PCIFunctionNumber",                 UINT8),
    ("Reserved_45",                       UINT8 * 3),
    ("TimerPeriod",                       UINT32),
    ("MaxCount",                          UINT32),
    ("MinCount",                          UINT32),
    ("WatchdogFlags",                     UINT8),
    ("Reserved_61",                       UINT8 * 3),
    ("NumberWatchdogInstructionEntries",  UINT32)
  ]

class EFI_ACPI_WATCHDOG_ACTION_1_0_WATCHDOG_ACTION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WatchdogAction",    UINT8),
    ("InstructionFlags",  UINT8),
    ("Reserved_2",        UINT8 * 2),
    ("RegisterRegion",    Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",             UINT32),
    ("Mask",              UINT32)
  ]

EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE_REVISION  = 0x01

EFI_ACPI_WDAT_1_0_WATCHDOG_ENABLED                 = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_STOPPED_IN_SLEEP_STATE  = 0x80

EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_RESET                           = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_CURRENT_COUNTDOWN_PERIOD  = 0x4
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_COUNTDOWN_PERIOD          = 0x5
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_COUNTDOWN_PERIOD            = 0x6
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_RUNNING_STATE             = 0x8
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_RUNNING_STATE               = 0x9
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_STOPPED_STATE             = 0xA
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_STOPPED_STATE               = 0xB
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_REBOOT                    = 0x10
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_REBOOT                      = 0x11
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_SHUTDOWN                  = 0x12
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_SHUTDOWN                    = 0x13
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_WATCHDOG_STATUS           = 0x20
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_WATCHDOG_STATUS             = 0x21

EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_VALUE         = 0x0
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_COUNTDOWN     = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_VALUE        = 0x2
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_COUNTDOWN    = 0x3
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_PRESERVE_REGISTER  = 0x80
