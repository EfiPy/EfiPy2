# Usb.py
#
# EfiPy2.MdePkg.IndustryStandard.Usb
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

USB_MASS_STORE_CLASS    = 0x08

USB_MASS_STORE_RBC      = 0x01
USB_MASS_STORE_8020I    = 0x02
USB_MASS_STORE_QIC      = 0x03
USB_MASS_STORE_UFI      = 0x04
USB_MASS_STORE_8070I    = 0x05
USB_MASS_STORE_SCSI     = 0x06

USB_MASS_STORE_CBI0     = 0x00
USB_MASS_STORE_CBI1     = 0x01
USB_MASS_STORE_BOT      = 0x50

USB_DEV_GET_STATUS                  = 0x00
USB_DEV_GET_STATUS_REQ_TYPE_D       = 0x80
USB_DEV_GET_STATUS_REQ_TYPE_I       = 0x81
USB_DEV_GET_STATUS_REQ_TYPE_E       = 0x82

USB_DEV_CLEAR_FEATURE               = 0x01
USB_DEV_CLEAR_FEATURE_REQ_TYPE_D    = 0x00
USB_DEV_CLEAR_FEATURE_REQ_TYPE_I    = 0x01
USB_DEV_CLEAR_FEATURE_REQ_TYPE_E    = 0x02

USB_DEV_SET_FEATURE                 = 0x03
USB_DEV_SET_FEATURE_REQ_TYPE_D      = 0x00
USB_DEV_SET_FEATURE_REQ_TYPE_I      = 0x01
USB_DEV_SET_FEATURE_REQ_TYPE_E      = 0x02

USB_DEV_SET_ADDRESS                 = 0x05
USB_DEV_SET_ADDRESS_REQ_TYPE        = 0x00

USB_DEV_GET_DESCRIPTOR              = 0x06
USB_DEV_GET_DESCRIPTOR_REQ_TYPE     = 0x80

USB_DEV_SET_DESCRIPTOR              = 0x07
USB_DEV_SET_DESCRIPTOR_REQ_TYPE     = 0x00

USB_DEV_GET_CONFIGURATION           = 0x08
USB_DEV_GET_CONFIGURATION_REQ_TYPE  = 0x80

USB_DEV_SET_CONFIGURATION           = 0x09
USB_DEV_SET_CONFIGURATION_REQ_TYPE  = 0x00

USB_DEV_GET_INTERFACE               = 0x0A
USB_DEV_GET_INTERFACE_REQ_TYPE      = 0x81

USB_DEV_SET_INTERFACE               = 0x0B
USB_DEV_SET_INTERFACE_REQ_TYPE      = 0x01

USB_DEV_SYNCH_FRAME                 = 0x0C
USB_DEV_SYNCH_FRAME_REQ_TYPE        = 0x82

class USB_DEVICE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RequestType", UINT8),
    ("Request",     UINT8),
    ("Value",       UINT16),
    ("Index",       UINT16),
    ("Length",      UINT16)
  ]

class USB_DEVICE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",            UINT8),
    ("DescriptorType",    UINT8),
    ("BcdUSB",            UINT16),
    ("DeviceClass",       UINT8),
    ("DeviceSubClass",    UINT8),
    ("DeviceProtocol",    UINT8),
    ("MaxPacketSize0",    UINT8),
    ("IdVendor",          UINT16),
    ("IdProduct",         UINT16),
    ("BcdDevice",         UINT16),
    ("StrManufacturer",   UINT8),
    ("StrProduct",        UINT8),
    ("StrSerialNumber",   UINT8),
    ("NumConfigurations", UINT8)
  ]

class USB_CONFIG_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",              UINT8),
    ("DescriptorType",      UINT8),
    ("TotalLength",         UINT16),
    ("NumInterfaces",       UINT8),
    ("ConfigurationValue",  UINT8),
    ("Configuration",       UINT8),
    ("Attributes",          UINT8),
    ("MaxPower",            UINT8)
  ]

class USB_INTERFACE_ASSOCIATION_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",                          UINT8),
    ("DescriptorType",                  UINT8),
    ("FirstInterface",                  UINT8),
    ("InterfaceCount",                  UINT8),
    ("FunctionClass",                   UINT8),
    ("FunctionSubclass",                UINT8),
    ("FunctionProtocol",                UINT8),
    ("FunctionDescriptionStringIndex",  UINT8)
  ]

class USB_INTERFACE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",            UINT8),
    ("DescriptorType",    UINT8),
    ("InterfaceNumber",   UINT8),
    ("AlternateSetting",  UINT8),
    ("NumEndpoints",      UINT8),
    ("InterfaceClass",    UINT8),
    ("InterfaceSubClass", UINT8),
    ("InterfaceProtocol", UINT8),
    ("Interface",         UINT8)
  ]

class USB_ENDPOINT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",            UINT8),
    ("DescriptorType",    UINT8),
    ("EndpointAddress",   UINT8),
    ("Attributes",        UINT8),
    ("MaxPacketSize",     UINT16),
    ("Interval",          UINT8)
  ]

class EFI_USB_STRING_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",            UINT8),
    ("DescriptorType",    UINT8),
    ("String",            CHAR16 * 1)
  ]

USB_REQ_TYPE_STANDARD   = (0x00 << 5)
USB_REQ_TYPE_CLASS      = (0x01 << 5)
USB_REQ_TYPE_VENDOR     = (0x02 << 5)

USB_REQ_GET_STATUS      = 0x00
USB_REQ_CLEAR_FEATURE   = 0x01
USB_REQ_SET_FEATURE     = 0x03
USB_REQ_SET_ADDRESS     = 0x05
USB_REQ_GET_DESCRIPTOR  = 0x06
USB_REQ_SET_DESCRIPTOR  = 0x07
USB_REQ_GET_CONFIG      = 0x08
USB_REQ_SET_CONFIG      = 0x09
USB_REQ_GET_INTERFACE   = 0x0A
USB_REQ_SET_INTERFACE   = 0x0B
USB_REQ_SYNCH_FRAME     = 0x0C

USB_TARGET_DEVICE       = 0
USB_TARGET_INTERFACE    = 0x01
USB_TARGET_ENDPOINT     = 0x02
USB_TARGET_OTHER        = 0x03

USB_DESC_TYPE_DEVICE                = 0x01
USB_DESC_TYPE_CONFIG                = 0x02
USB_DESC_TYPE_STRING                = 0x03
USB_DESC_TYPE_INTERFACE             = 0x04
USB_DESC_TYPE_ENDPOINT              = 0x05
USB_DESC_TYPE_INTERFACE_ASSOCIATION = 0x0b
USB_DESC_TYPE_HID                   = 0x21
USB_DESC_TYPE_REPORT                = 0x22
USB_DESC_TYPE_CS_INTERFACE          = 0x24
USB_DESC_TYPE_CS_ENDPOINT           = 0x25

USB_FEATURE_ENDPOINT_HALT = 0

USB_ENDPOINT_CONTROL    = 0x00
USB_ENDPOINT_ISO        = 0x01
USB_ENDPOINT_BULK       = 0x02
USB_ENDPOINT_INTERRUPT  = 0x03

USB_ENDPOINT_TYPE_MASK  = 0x03
USB_ENDPOINT_DIR_IN     = 0x80

EFI_USB_INTERRUPT_DELAY = 2000000
USB_TYPES_DEFINITION = ENUM

USB_HID_GET_DESCRIPTOR_REQ_TYPE  = 0x81

USB_HID_CLASS_GET_REQ_TYPE       = 0xa1
USB_HID_CLASS_SET_REQ_TYPE       = 0x21

HID_ITEM_FORMAT_SHORT = 0
HID_ITEM_FORMAT_LONG  = 1

HID_ITEM_TAG_LONG = 15

HID_ITEM_TYPE_MAIN      = 0
HID_ITEM_TYPE_GLOBAL    = 1
HID_ITEM_TYPE_LOCAL     = 2
HID_ITEM_TYPE_RESERVED  = 3

HID_MAIN_ITEM_TAG_INPUT             = 8
HID_MAIN_ITEM_TAG_OUTPUT            = 9
HID_MAIN_ITEM_TAG_FEATURE           = 11
HID_MAIN_ITEM_TAG_BEGIN_COLLECTION  = 10
HID_MAIN_ITEM_TAG_END_COLLECTION    = 12

HID_MAIN_ITEM_CONSTANT      = 0x001
HID_MAIN_ITEM_VARIABLE      = 0x002
HID_MAIN_ITEM_RELATIVE      = 0x004
HID_MAIN_ITEM_WRAP          = 0x008
HID_MAIN_ITEM_NONLINEAR     = 0x010
HID_MAIN_ITEM_NO_PREFERRED  = 0x020
HID_MAIN_ITEM_NULL_STATE    = 0x040
HID_MAIN_ITEM_VOLATILE      = 0x080
HID_MAIN_ITEM_BUFFERED_BYTE = 0x100

HID_COLLECTION_PHYSICAL     = 0
HID_COLLECTION_APPLICATION  = 1
HID_COLLECTION_LOGICAL      = 2

HID_GLOBAL_ITEM_TAG_USAGE_PAGE        = 0
HID_GLOBAL_ITEM_TAG_LOGICAL_MINIMUM   = 1
HID_GLOBAL_ITEM_TAG_LOGICAL_MAXIMUM   = 2
HID_GLOBAL_ITEM_TAG_PHYSICAL_MINIMUM  = 3
HID_GLOBAL_ITEM_TAG_PHYSICAL_MAXIMUM  = 4
HID_GLOBAL_ITEM_TAG_UNIT_EXPONENT     = 5
HID_GLOBAL_ITEM_TAG_UNIT              = 6
HID_GLOBAL_ITEM_TAG_REPORT_SIZE       = 7
HID_GLOBAL_ITEM_TAG_REPORT_ID         = 8
HID_GLOBAL_ITEM_TAG_REPORT_COUNT      = 9
HID_GLOBAL_ITEM_TAG_PUSH              = 10
HID_GLOBAL_ITEM_TAG_POP               = 11

HID_LOCAL_ITEM_TAG_USAGE              = 0
HID_LOCAL_ITEM_TAG_USAGE_MINIMUM      = 1
HID_LOCAL_ITEM_TAG_USAGE_MAXIMUM      = 2
HID_LOCAL_ITEM_TAG_DESIGNATOR_INDEX   = 3
HID_LOCAL_ITEM_TAG_DESIGNATOR_MINIMUM = 4
HID_LOCAL_ITEM_TAG_DESIGNATOR_MAXIMUM = 5
HID_LOCAL_ITEM_TAG_STRING_INDEX       = 7
HID_LOCAL_ITEM_TAG_STRING_MINIMUM     = 8
HID_LOCAL_ITEM_TAG_STRING_MAXIMUM     = 9
HID_LOCAL_ITEM_TAG_DELIMITER          = 10

HID_INPUT_REPORT    = 1
HID_OUTPUT_REPORT   = 2
HID_FEATURE_REPORT  = 3

EFI_USB_GET_REPORT_REQUEST    = 0x01
EFI_USB_GET_IDLE_REQUEST      = 0x02
EFI_USB_GET_PROTOCOL_REQUEST  = 0x03
EFI_USB_SET_REPORT_REQUEST    = 0x09
EFI_USB_SET_IDLE_REQUEST      = 0x0a
EFI_USB_SET_PROTOCOL_REQUEST  = 0x0b

class EFI_USB_HID_CLASS_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorType",    UINT8),
    ("DescriptorLength",  CHAR16)
  ]

class EFI_USB_HID_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",          UINT8),
    ("DescriptorType",  UINT8),
    ("BcdHID",          UINT16),
    ("CountryCode",     UINT8),
    ("NumDescriptors",  UINT8),
    ("HidClassDesc",    EFI_USB_HID_CLASS_DESCRIPTOR * 1)
  ]

