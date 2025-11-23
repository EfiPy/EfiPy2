# Usb2HostController.py
#
# EfiPy2.MdePkg.Protocol.Usb2HostController
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.UsbIo   import EFI_USB_DEVICE_REQUEST, EFI_USB_DATA_DIRECTION, EFI_ASYNC_USB_TRANSFER_CALLBACK

gEfiUsb2HcProtocolGuid  = \
  EFI_GUID (0x3e745226, 0x9818, 0x45b6, (0xa2, 0xac, 0xd7, 0xcd, 0xe, 0x8b, 0xa2, 0xbc ))

class EFI_USB2_HC_PROTOCOL (Structure):
  pass

class EFI_USB_PORT_STATUS (Structure):
  _fields_ = [
    ("PortStatus",        UINT16),
    ("PortChangeStatus",  UINT16)
  ]

USB_PORT_STAT_CONNECTION    = 0x0001
USB_PORT_STAT_ENABLE        = 0x0002
USB_PORT_STAT_SUSPEND       = 0x0004
USB_PORT_STAT_OVERCURRENT   = 0x0008
USB_PORT_STAT_RESET         = 0x0010
USB_PORT_STAT_POWER         = 0x0100
USB_PORT_STAT_LOW_SPEED     = 0x0200
USB_PORT_STAT_HIGH_SPEED    = 0x0400
USB_PORT_STAT_SUPER_SPEED   = 0x0800
USB_PORT_STAT_OWNER         = 0x2000

USB_PORT_STAT_C_CONNECTION  = 0x0001
USB_PORT_STAT_C_ENABLE      = 0x0002
USB_PORT_STAT_C_SUSPEND     = 0x0004
USB_PORT_STAT_C_OVERCURRENT = 0x0008
USB_PORT_STAT_C_RESET       = 0x0010

EfiUsbPortEnable            = 1
EfiUsbPortSuspend           = 2
EfiUsbPortReset             = 4
EfiUsbPortPower             = 8
EfiUsbPortOwner             = 13
EfiUsbPortConnectChange     = 16
EfiUsbPortEnableChange      = 17
EfiUsbPortSuspendChange     = 18
EfiUsbPortOverCurrentChange = 19
EfiUsbPortResetChange       = 20
EFI_USB_PORT_FEATURE        = ENUM

EFI_USB_SPEED_FULL      = 0x0000
EFI_USB_SPEED_LOW       = 0x0001
EFI_USB_SPEED_HIGH      = 0x0002
EFI_USB_SPEED_SUPER     = 0x0003

class EFI_USB2_HC_TRANSACTION_TRANSLATOR (Structure):
  _fields_ = [
    ("TranslatorHubAddress",  UINT8),
    ("TranslatorPortNumber",  UINT8)
  ]

EFI_USB2_HC_PROTOCOL_GET_CAPABILITY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),    # IN  *This
  POINTER(UINT8),                   # OUT *MaxSpeed,
  POINTER(UINT8),                   # OUT *PortNumber,
  POINTER(UINT8)                    # OUT *Is64BitCapable
  )

EFI_USB_HC_RESET_GLOBAL             = 0x0001
EFI_USB_HC_RESET_HOST_CONTROLLER    = 0x0002
EFI_USB_HC_RESET_GLOBAL_WITH_DEBUG  = 0x0004
EFI_USB_HC_RESET_HOST_WITH_DEBUG    = 0x0008

EFI_USB2_HC_PROTOCOL_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),    # IN  *This
  UINT16                            # IN  Attributes
  )

EfiUsbHcStateHalt         = 0
EfiUsbHcStateOperational  = 1
EfiUsbHcStateSuspend      = 2
EfiUsbHcStateMaximum      = 3
EFI_USB_HC_STATE          = ENUM

EFI_USB2_HC_PROTOCOL_GET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),    # IN  *This
  POINTER(EFI_USB_HC_STATE)         # OUT *State
  )

EFI_USB2_HC_PROTOCOL_SET_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),    # IN  *This
  EFI_USB_HC_STATE                  # IN   State
  )

EFI_USB2_HC_PROTOCOL_CONTROL_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  POINTER(EFI_USB_DEVICE_REQUEST),              # IN     *Request,
  EFI_USB_DATA_DIRECTION,                       # IN     TransferDirection,
  PVOID,                                        # IN OUT *Data       OPTIONAL,
  POINTER(UINTN),                               # IN OUT *DataLength OPTIONAL,
  UINTN,                                        # IN     TimeOut,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator,
  POINTER(UINT32)                               # OUT    *TransferResult
  )

EFI_USB_MAX_BULK_BUFFER_NUM = 10

EFI_USB2_HC_PROTOCOL_BULK_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     EndPointAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  UINT8,                                        # IN     DataBuffersNumber,
  PVOID * EFI_USB_MAX_BULK_BUFFER_NUM,          # IN OUT *Data[EFI_USB_MAX_BULK_BUFFER_NUM],
  POINTER(UINTN),                               # IN OUT *DataLength,
  POINTER(UINT8),                               # IN OUT *DataToggle,
  UINTN,                                        # IN     TimeOut,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator,
  POINTER(UINT32)                               # OUT    *TransferResult
  )

EFI_USB2_HC_PROTOCOL_ASYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     EndPointAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  BOOLEAN,                                      # IN     IsNewTransfer,
  POINTER(UINT8),                               # IN OUT *DataToggle,
  UINTN,                                        # IN     PollingInterval  OPTIONAL,
  UINTN,                                        # IN     DataLength       OPTIONAL,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator      OPTIONAL,
  EFI_ASYNC_USB_TRANSFER_CALLBACK,              # IN     CallBackFunction OPTIONAL,
  PVOID                                         # IN     *Context         OPTIONAL
  )

EFI_USB2_HC_PROTOCOL_SYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     EndPointAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  PVOID,                                        # IN OUT *Data,
  POINTER(UINTN),                               # IN OUT *DataLength,
  POINTER(UINT8),                               # IN OUT *DataToggle,
  UINTN,                                        # IN     TimeOut,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator,
  POINTER(UINT32)                               # OUT    *TransferResult
  )

EFI_USB_MAX_ISO_BUFFER_NUM  = 7
EFI_USB_MAX_ISO_BUFFER_NUM1 = 2

EFI_USB2_HC_PROTOCOL_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     EndPointAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  UINT8,                                        # IN     DataBuffersNumber,
  PVOID,                                        # IN OUT *Data[EFI_USB_MAX_ISO_BUFFER_NUM],
  UINTN,                                        # IN     DataLength,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator,
  POINTER(UINT32)                               # OUT    *TransferResult
  )

EFI_USB2_HC_PROTOCOL_ASYNC_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),                # IN     *This
  UINT8,                                        # IN     DeviceAddress,
  UINT8,                                        # IN     EndPointAddress,
  UINT8,                                        # IN     DeviceSpeed,
  UINTN,                                        # IN     MaximumPacketLength,
  UINT8,                                        # IN     DataBuffersNumber,
  PVOID,                                        # IN OUT *Data[EFI_USB_MAX_ISO_BUFFER_NUM],
  UINTN,                                        # IN     DataLength,
  POINTER(EFI_USB2_HC_TRANSACTION_TRANSLATOR),  # IN     *Translator,
  EFI_ASYNC_USB_TRANSFER_CALLBACK,              # IN     IsochronousCallBack,
  PVOID                                         # IN     *Context OPTIONAL
  )

EFI_USB2_HC_PROTOCOL_GET_ROOTHUB_PORT_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),  # IN     *This
  UINT8,                          # IN     PortNumber,
  POINTER(EFI_USB_PORT_STATUS)    # OUT    *PortStatus
  )

EFI_USB2_HC_PROTOCOL_SET_ROOTHUB_PORT_FEATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),  # IN     *This
  UINT8,                          # IN     PortNumber,
  EFI_USB_PORT_FEATURE            # IN     PortFeature
  )

EFI_USB2_HC_PROTOCOL_CLEAR_ROOTHUB_PORT_FEATURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB2_HC_PROTOCOL),  # IN     *This
  UINT8,                          # IN     PortNumber,
  EFI_USB_PORT_FEATURE            # IN     PortFeature
  )

EFI_USB2_HC_PROTOCOL._fields_ = [
    ("GetCapability",             EFI_USB2_HC_PROTOCOL_GET_CAPABILITY),
    ("Reset",                     EFI_USB2_HC_PROTOCOL_RESET),
    ("GetState",                  EFI_USB2_HC_PROTOCOL_GET_STATE),
    ("SetState",                  EFI_USB2_HC_PROTOCOL_SET_STATE),
    ("ControlTransfer",           EFI_USB2_HC_PROTOCOL_CONTROL_TRANSFER),
    ("BulkTransfer",              EFI_USB2_HC_PROTOCOL_BULK_TRANSFER),
    ("AsyncInterruptTransfer",    EFI_USB2_HC_PROTOCOL_ASYNC_INTERRUPT_TRANSFER),
    ("SyncInterruptTransfer",     EFI_USB2_HC_PROTOCOL_SYNC_INTERRUPT_TRANSFER),
    ("IsochronousTransfer",       EFI_USB2_HC_PROTOCOL_ISOCHRONOUS_TRANSFER),
    ("AsyncIsochronousTransfer",  EFI_USB2_HC_PROTOCOL_ASYNC_ISOCHRONOUS_TRANSFER),
    ("GetRootHubPortStatus",      EFI_USB2_HC_PROTOCOL_GET_ROOTHUB_PORT_STATUS),
    ("SetRootHubPortFeature",     EFI_USB2_HC_PROTOCOL_SET_ROOTHUB_PORT_FEATURE),
    ("ClearRootHubPortFeature",   EFI_USB2_HC_PROTOCOL_CLEAR_ROOTHUB_PORT_FEATURE),
    ("MajorRevision",             UINT16), 
    ("MinorRevision",             UINT16) 
  ]

