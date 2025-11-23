# BluetoothLeConfig.py
#
# EfiPy2.MdePkg.Protocol.BluetoothLeConfig
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.BluetoothConfig   import EFI_BLUETOOTH_CONFIG_DATA_TYPE,                \
                                                     EFI_BLUETOOTH_CONNECT_COMPLETE_CALLBACK_TYPE

from EfiPy2.MdePkg.IndustryStandard.Bluetooth import BLUETOOTH_LE_ADDRESS

gEfiBluetoothLeConfigProtocolGuid = \
  EFI_GUID (0x8f76da58, 0x1f99, 0x4275, ( 0xa4, 0xec, 0x47, 0x56, 0x51, 0x5b, 0x1c, 0xe8 ))

class EFI_BLUETOOTH_LE_CONFIG_PROTOCOL (Structure):
  pass

EFI_BLUETOOTH_LE_CONFIG_INIT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL) # IN     *This
  )

class EFI_BLUETOOTH_LE_CONFIG_SCAN_PARAMETER (Structure):
  _fields_ = [
    ("Version",                 UINT32),
    ("ScanType",                UINT8),
    ("ScanInterval",            UINT16),
    ("ScanWindow",              UINT16),
    ("ScanningFilterPolicy",    UINT8),
    ("AdvertisementFlagFilter", UINT8)
  ]

class EFI_BLUETOOTH_LE_SCAN_CALLBACK_INFORMATION (Structure):
  _fields_ = [
    ("BDAddr",                  BLUETOOTH_LE_ADDRESS),
    ("DirectAddress",           BLUETOOTH_LE_ADDRESS),
    ("RemoteDeviceState",       UINT8),
    ("RSSI",                    INT8),
    ("AdvertisementDataSize",   UINTN),
    ("AdvertisementData",       PVOID)
  ]

EFI_BLUETOOTH_LE_CONFIG_SCAN_CALLBACK_FUNCTION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),            # IN *This
  PVOID,                                                # IN *Context,
  POINTER(EFI_BLUETOOTH_LE_SCAN_CALLBACK_INFORMATION)   # IN *CallbackInfo
  )

EFI_BLUETOOTH_LE_CONFIG_SCAN = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),        # IN *This
  BOOLEAN,                                          # IN ReScan,
  UINT32,                                           # IN Timeout,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_SCAN_PARAMETER),  # IN *ScanParameter  OPTIONAL,
  EFI_BLUETOOTH_LE_CONFIG_SCAN_CALLBACK_FUNCTION,   # IN Callback,
  PVOID                                             # IN *Context
  )

class EFI_BLUETOOTH_LE_CONFIG_CONNECT_PARAMETER (Structure):
  _fields_ = [
    ("Version",             UINT32),
    ("ScanInterval",        UINT16),
    ("ScanWindow",          UINT16),
    ("ConnIntervalMin",     UINT16),
    ("ConnIntervalMax",     UINT16),
    ("ConnLatency",         UINT16),
    ("SupervisionTimeout",  UINT16)
  ]

EFI_BLUETOOTH_LE_CONFIG_CONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),            # IN *This
  BOOLEAN,                                              # IN AutoReconnect,
  BOOLEAN,                                              # IN DoBonding,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_CONNECT_PARAMETER),   # IN *ConnectParameter  OPTIONAL,
  POINTER(BLUETOOTH_LE_ADDRESS)                         # IN BD_ADDR
  )

EFI_BLUETOOTH_LE_CONFIG_DISCONNECT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN *This
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN BD_ADDR
  UINT8                                         # IN Reason
  )

EFI_BLUETOOTH_LE_CONFIG_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN      *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,               # IN      DataType,
  POINTER(UINTN),                               # IN OUT  *DataSize,
  PVOID                                         # IN OUT  *Data OPTIONAL
  )

EFI_BLUETOOTH_LE_CONFIG_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN      *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,               # IN      DataType,
  UINTN,                                        # IN      DataSize,
  PVOID                                         # IN OUT  *Data OPTIONAL
  )

EFI_BLUETOOTH_LE_CONFIG_GET_REMOTE_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN      *This
  EFI_BLUETOOTH_CONFIG_DATA_TYPE,               # IN      DataType,
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN      *BDAddr
  POINTER(UINTN),                               # IN OUT  *DataSize,
  PVOID                                         # IN OUT  *Data
  )

EfiBluetoothSmpAuthorizationRequestEvent    = 1
EfiBluetoothSmpPasskeyReadyEvent            = 2
EfiBluetoothSmpPasskeyRequestEvent          = 3
EfiBluetoothSmpOOBDataRequestEvent          = 4
EfiBluetoothSmpNumericComparisonEvent       = 5
EFI_BLUETOOTH_LE_SMP_EVENT_DATA_TYPE        = ENUM

EFI_BLUETOOTH_LE_SMP_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN *This
  PVOID,                                        # IN *Context,
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN *BDAddr,
  EFI_BLUETOOTH_LE_SMP_EVENT_DATA_TYPE,         # IN EventDataType,
  UINTN,                                        # IN DataSize,
  PVOID                                         # IN *Data
  )

EFI_BLUETOOTH_LE_REGISTER_SMP_AUTH_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN *This
  EFI_BLUETOOTH_LE_SMP_CALLBACK,                # IN Callback,
  PVOID,                                        # IN *Context,
  )

EFI_BLUETOOTH_LE_SEND_SMP_AUTH_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN *This
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN *BDAddr,
  EFI_BLUETOOTH_LE_SMP_EVENT_DATA_TYPE,         # IN EventDataType,
  UINTN,                                        # IN DataSize,
  PVOID                                         # IN *Data
  )

EfiBluetoothSmpLocalIR         = 0
EfiBluetoothSmpLocalER         = 1
EfiBluetoothSmpLocalDHK        = 2

EfiBluetoothSmpKeysDistributed = 0x1000
EfiBluetoothSmpKeySize         = 0x1001 
EfiBluetoothSmpKeyType         = 0x1002 
EfiBluetoothSmpPeerLTK         = 0x1003 
EfiBluetoothSmpPeerIRK         = 0x1004 
EfiBluetoothSmpPeerCSRK        = 0x1005 
EfiBluetoothSmpPeerRand        = 0x1006 
EfiBluetoothSmpPeerEDIV        = 0x1007 
EfiBluetoothSmpPeerSignCounter = 0x1008 
EfiBluetoothSmpLocalLTK        = 0x1009 
EfiBluetoothSmpLocalIRK        = 0x100A
EfiBluetoothSmpLocalCSRK       = 0x100B
EfiBluetoothSmpLocalSignCounter= 0x100C
EfiBluetoothSmpLocalDIV        = 0x100D
EfiBluetoothSmpPeerAddressList = 0x100E
EfiBluetoothSmpMax             = 0x100F
EFI_BLUETOOTH_LE_SMP_DATA_TYPE = ENUM

EFI_BLUETOOTH_LE_CONFIG_SMP_GET_DATA_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN     *This
  PVOID,                                        # IN     *Context
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN     *BDAddr,
  EFI_BLUETOOTH_LE_SMP_DATA_TYPE,               # IN     DataType,
  POINTER(UINTN),                               # IN OUT *DataSize,
  PVOID                                         # IN OUT *Data
  )

EFI_BLUETOOTH_LE_CONFIG_REGISTER_SMP_GET_DATA_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),        # IN     *This
  EFI_BLUETOOTH_LE_CONFIG_SMP_GET_DATA_CALLBACK,    # IN     Callback,
  PVOID                                             # IN     *Context
  )

EFI_BLUETOOTH_LE_CONFIG_SMP_SET_DATA_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),    # IN *This
  PVOID,                                        # IN *Context
  POINTER(BLUETOOTH_LE_ADDRESS),                # IN *BDAddr,
  EFI_BLUETOOTH_LE_SMP_DATA_TYPE,               # IN Type,
  UINTN,                                        # IN DataSize,
  PVOID                                         # IN *Data
)

EFI_BLUETOOTH_LE_CONFIG_REGISTER_SMP_SET_DATA_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),        # IN *This
  EFI_BLUETOOTH_LE_CONFIG_SMP_SET_DATA_CALLBACK,    # IN Callback,
  PVOID                                             # IN *Context
)

EFI_BLUETOOTH_LE_CONFIG_CONNECT_COMPLETE_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),       # IN *This
  PVOID,                                           # IN *Context,
  EFI_BLUETOOTH_CONNECT_COMPLETE_CALLBACK_TYPE,    # IN CallbackType,
  POINTER(BLUETOOTH_LE_ADDRESS),                   # IN *BDAddr,
  PVOID,                                           # IN *InputBuffer,
  UINTN                                            # IN InputBufferSize
)

EFI_BLUETOOTH_LE_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_BLUETOOTH_LE_CONFIG_PROTOCOL),            # IN *This
  EFI_BLUETOOTH_LE_CONFIG_CONNECT_COMPLETE_CALLBACK,    # IN Callback,
  PVOID                                                 # IN *Context
)

EFI_BLUETOOTH_LE_CONFIG_PROTOCOL._fields_ = [
    ("Init",                                EFI_BLUETOOTH_LE_CONFIG_INIT),
    ("Scan",                                EFI_BLUETOOTH_LE_CONFIG_SCAN),
    ("Connect",                             EFI_BLUETOOTH_LE_CONFIG_CONNECT),
    ("Disconnect",                          EFI_BLUETOOTH_LE_CONFIG_DISCONNECT),
    ("GetData",                             EFI_BLUETOOTH_LE_CONFIG_GET_DATA),
    ("SetData",                             EFI_BLUETOOTH_LE_CONFIG_SET_DATA),
    ("GetRemoteData",                       EFI_BLUETOOTH_LE_CONFIG_GET_REMOTE_DATA),
    ("RegisterSmpAuthCallback",             EFI_BLUETOOTH_LE_REGISTER_SMP_AUTH_CALLBACK),
    ("SendSmpAuthData",                     EFI_BLUETOOTH_LE_SEND_SMP_AUTH_DATA),
    ("RegisterSmpGetDataCallback",          EFI_BLUETOOTH_LE_CONFIG_REGISTER_SMP_GET_DATA_CALLBACK),
    ("RegisterSmpSetDataCallback",          EFI_BLUETOOTH_LE_CONFIG_REGISTER_SMP_SET_DATA_CALLBACK),
    ("RegisterLinkConnectCompleteCallback", EFI_BLUETOOTH_LE_CONFIG_REGISTER_CONNECT_COMPLETE_CALLBACK)
  ]

