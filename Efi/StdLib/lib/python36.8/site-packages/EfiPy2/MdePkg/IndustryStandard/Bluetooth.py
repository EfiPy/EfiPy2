# Bluetooth.py
#
# EfiPy2.MdePkg.IndustryStandard.Bluetooth
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class BLUETOOTH_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Address", UINT8 * 6)
    ]

class BLUETOOTH_CLASS_OF_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FormatType",        UINT8,  2),
    ("MinorDeviceClass",  UINT8,  6),
    ("MajorDeviceClass",  UINT16, 5),
    ("MajorServiceClass", UINT16, 11)
    ]

class BLUETOOTH_LE_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Address", UINT8 * 6),
    ("Type",    UINT8)
    ]

BLUETOOTH_HCI_COMMAND_LOCAL_READABLE_NAME_MAX_SIZE    = 248

BLUETOOTH_HCI_LINK_KEY_SIZE                           = 16

