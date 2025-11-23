# BluetoothAttribute.py
#
# EfiPy2.MdePkg.Protocol.BluetoothAttribute
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard.Bluetooth import BLUETOOTH_LE_ADDRESS

gEfiBluetoothAttributeServiceBindingProtocolGuid    = \
  EFI_GUID (0x5639867a, 0x8c8e, 0x408d, ( 0xac, 0x2f, 0x4b, 0x61, 0xbd, 0xc0, 0xbb, 0xbb))

gEfiBluetoothAttributeProtocolGuid                  = \
  EFI_GUID (0x898890e9, 0x84b2, 0x4f3a, ( 0x8c, 0x58, 0xd8, 0x57, 0x78, 0x13, 0xe0, 0xac))

class EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL (Structure):
  pass

class EFI_BLUETOOTH_UUID_Data (Union):
  _pack_   = 1
  _fields_ = [
    ("Uuid16",              UINT16),
    ("Uuid32",              UINT32),
    ("Uuid128",             UINT8 * 16),
  ]

class EFI_BLUETOOTH_UUID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Length",  UINT8),
    ("Data",    EFI_BLUETOOTH_UUID_Data)
  ]

UUID_16BIT_TYPE_LEN   = 2
UUID_32BIT_TYPE_LEN   = 4
UUID_128BIT_TYPE_LEN  = 16

def BLUETOOTH_IS_ATTRIBUTE_OF_TYPE(a, t):
    return a.Type[0].Length == UUID_16BIT_TYPE_LEN and a.Type[0].Data.Uuid16 == t

class EFI_BLUETOOTH_ATTRIBUTE_PERMISSION_Permission (Structure):
  _pack_   = 1
  _fields_ = [
    ("Readable",            UINT16, 1),
    ("ReadEncryption",      UINT16, 1),
    ("ReadAuthentication",  UINT16, 1),
    ("ReadAuthorization",   UINT16, 1),
    ("ReadKeySize",         UINT16, 5),
    ("Reserved1",           UINT16, 7),
    ("Writeable",           UINT16, 1),
    ("WriteEncryption",     UINT16, 1),
    ("WriteAuthentication", UINT16, 1),
    ("WriteAuthorization",  UINT16, 1),
    ("WriteKeySize",        UINT16, 5),
    ("Reserved2",           UINT16, 7)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_PERMISSION (Union):
  _pack_   = 1
  _fields_ = [
    ("Permission",  EFI_BLUETOOTH_ATTRIBUTE_PERMISSION_Permission),
    ("Data32",      UINT32)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",                EFI_BLUETOOTH_UUID),
    ("Length",              UINT16),
    ("AttributeHandle",     UINT16),
    ("AttributePermission", EFI_BLUETOOTH_ATTRIBUTE_PERMISSION)
  ]

class EFI_BLUETOOTH_GATT_PRIMARY_SERVICE_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_BLUETOOTH_ATTRIBUTE_HEADER),
    ("EndGroupHandle",  UINT16),
    ("ServiceUuid",     EFI_BLUETOOTH_UUID)
  ]

class EFI_BLUETOOTH_GATT_INCLUDE_SERVICE_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_BLUETOOTH_ATTRIBUTE_HEADER),
    ("StartGroupHandle",    UINT16),
    ("EndGroupHandle",      UINT16),
    ("ServiceUuid",         EFI_BLUETOOTH_UUID)
  ]

class EFI_BLUETOOTH_GATT_CHARACTERISTIC_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                      EFI_BLUETOOTH_ATTRIBUTE_HEADER),
    ("CharacteristicProperties",    UINT8),
    ("CharacteristicValueHandle",   UINT16),
    ("CharacteristicUuid",          EFI_BLUETOOTH_UUID)
  ]

class EFI_BLUETOOTH_GATT_CHARACTERISTIC_DESCRIPTOR_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                          EFI_BLUETOOTH_ATTRIBUTE_HEADER),
    ("CharacteristicDescriptorUuid",    EFI_BLUETOOTH_UUID)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_NOTIFICATION (Structure):
  _fields_ = [
    ("AttributeHandle", UINT16)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_INDICATION (Structure):
  _fields_ = [
    ("AttributeHandle", UINT16)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_Parameter (Union):
  _fields_ = [
    ("Notification",    EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_NOTIFICATION),
    ("Indication",      EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_INDICATION)
  ]

class EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER (Structure):
  _fields_ = [
    ("Version",         UINT32),
    ("AttributeOpCode", UINT8),
    ("Parameter",       EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER_Parameter)
  ]

class EFI_BLUETOOTH_LE_DEVICE_INFO (Structure):
  _fields_ = [
    ("Version",                 UINT32),
    ("BD_ADDR",                 BLUETOOTH_LE_ADDRESS),
    ("DirectAddress",           BLUETOOTH_LE_ADDRESS),
    ("RSSI",                    UINT8),
    ("AdvertisementDataSize",   UINTN),
    ("AdvertisementData",       PVOID)
  ]

EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL), # IN *This,
  PVOID,                                     # IN *Data,
  UINTN,                                     # IN DataLength,
  PVOID                                      # IN *Context
  )

EFI_BLUETOOTH_ATTRIBUTE_SEND_REQUEST = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL),    # IN *This,
  PVOID,                                        # IN *Data,
  UINTN,                                        # IN DataLength,
  EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_FUNCTION,    # IN Callback,
  PVOID                                         # IN *Context
  )

EFI_BLUETOOTH_ATTRIBUTE_REGISTER_FOR_SERVER_NOTIFICATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL),            # IN *This,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_PARAMETER),  # IN *CallbackParameter,
  EFI_BLUETOOTH_ATTRIBUTE_CALLBACK_FUNCTION,            # IN Callback,
  PVOID                                                 # IN *Context
  )

EFI_BLUETOOTH_ATTRIBUTE_GET_SERVICE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL), # IN  *This,
  POINTER(UINTN),                            # OUT *ServiceInfoSize,
  POINTER(PVOID)                             # OUT **ServiceInfo
  )

EFI_BLUETOOTH_ATTRIBUTE_GET_DEVICE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL), # IN  *This,
  POINTER(UINTN),                            # OUT *DeviceInfoSize,
  POINTER(PVOID)                             # OUT **DeviceInfo
  )

EFI_BLUETOOTH_ATTRIBUTE_PROTOCOL._fields_ = [
    ("SendRequest",                     EFI_BLUETOOTH_ATTRIBUTE_SEND_REQUEST),
    ("RegisterForServerNotification",   EFI_BLUETOOTH_ATTRIBUTE_REGISTER_FOR_SERVER_NOTIFICATION),
    ("GetServiceInfo",                  EFI_BLUETOOTH_ATTRIBUTE_GET_SERVICE_INFO),
    ("GetDeviceInfo",                   EFI_BLUETOOTH_ATTRIBUTE_GET_DEVICE_INFO)
  ]

