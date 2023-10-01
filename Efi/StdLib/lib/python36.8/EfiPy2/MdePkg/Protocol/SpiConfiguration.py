# SpiConfiguration.py
#
# EfiPy2.MdePkg.Protocol.SpiConfiguration
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiSpiConfigurationProtocolGuid = \
  EFI_GUID (0x85a6d3e6, 0xb65b, 0x4afc, (0xb3, 0x8f, 0xc6, 0xd5, 0x4a, 0xf6, 0xdd, 0xc8 ))

class EFI_SPI_PERIPHERAL (Structure):
  pass

EFI_SPI_CHIP_SELECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_PERIPHERAL),      # IN *SpiPeripheral
  BOOLEAN                           # IN PinValue
  )

EFI_SPI_CLOCK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SPI_PERIPHERAL),      # IN *SpiPeripheral
  POINTER(UINT32)                   # IN *ClockHz
  )

class EFI_SPI_PART (Structure):
  _fields_ = [
    ("Vendor",              POINTER(CHAR16)),
    ("PartNumber",          POINTER(CHAR16)),
    ("MinClockHz",          UINT32),
    ("MaxClockHz",          UINT32),
    ("ChipSelectPolarity",  BOOLEAN)
  ]

class EFI_SPI_BUS (Structure):
  _fields_ = [
    ("FriendlyName",    POINTER(CHAR16)),
    ("Peripherallist",  POINTER(EFI_SPI_PERIPHERAL)),
    ("ControllerPath",  POINTER(EFI_DEVICE_PATH_PROTOCOL)),
    ("Clock",           EFI_SPI_CLOCK),
    ("ClockParameter",  PVOID)
  ]

EFI_SPI_PERIPHERAL._fields_ = [
    ("NextSpiPeripheral",       POINTER(EFI_SPI_PERIPHERAL)),
    ("FriendlyName",            POINTER(CHAR16)),
    ("SpiPeripheralDriverGuid", POINTER(GUID)),
    ("SpiPart",                 POINTER(EFI_SPI_PART)),
    ("MaxClockHz",              UINT32),
    ("ClockPolarity",           BOOLEAN),
    ("ClockPhase",              BOOLEAN),
    ("Attributes",              UINT32),
    ("ConfigurationData",       PVOID),
    ("SpiBus",                  POINTER(EFI_SPI_BUS)),
    ("ChipSelect",              EFI_SPI_CHIP_SELECT),
    ("ChipSelectParameter",     PVOID)
  ]

class EFI_SPI_CONFIGURATION_PROTOCOL (Structure):
  _fields_ = [
    ("BusCount", UINT32),
    ("Buslist",  POINTER(POINTER(EFI_SPI_BUS)))
  ]

