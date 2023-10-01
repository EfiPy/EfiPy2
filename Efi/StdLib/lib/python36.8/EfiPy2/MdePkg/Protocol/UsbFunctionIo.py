# UsbFunctionIo.py
#
# EfiPy2.MdePkg.Protocol.UsbFunctionIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol.UsbIo import    EFI_USB_INTERFACE_DESCRIPTOR,   \
                                            EFI_USB_ENDPOINT_DESCRIPTOR,    \
                                            EFI_USB_CONFIG_DESCRIPTOR,      \
                                            EFI_USB_DEVICE_DESCRIPTOR,      \
                                            EFI_USB_DEVICE_REQUEST

gEfiUsbFunctionIoProtocolGuid = \
  EFI_GUID (0x32d2963a, 0xfe5d, 0x4f30, (0xb6, 0x33, 0x6e, 0x5d, 0xc5, 0x58, 0x3, 0xcc))

class EFI_USBFN_IO_PROTOCOL (Structure):
  pass

EfiUsbUnknownPort                   = 0
EfiUsbStandardDownstreamPort        = 1
EfiUsbChargingDownstreamPort        = 2
EfiUsbDedicatedChargingPort         = 3
EfiUsbInvalidDedicatedChargingPort  = 4
EFI_USBFN_PORT_TYPE                 = ENUM

class EFI_USB_INTERFACE_INFO (Structure):
  _fields_ = [
    ("InterfaceDescriptor",     POINTER(EFI_USB_INTERFACE_DESCRIPTOR)),
    ("EndpointDescriptorTable", POINTER(POINTER(EFI_USB_ENDPOINT_DESCRIPTOR)))
  ]

class EFI_USB_CONFIG_INFO (Structure):
  _fields_ = [
    ("ConfigDescriptor",    POINTER(EFI_USB_CONFIG_DESCRIPTOR)),
    ("InterfaceInfoTable",  POINTER(POINTER(EFI_USB_INTERFACE_INFO)))
  ]

class EFI_USB_DEVICE_INFO (Structure):
  _fields_ = [
    ("DeviceDescriptor",  POINTER(EFI_USB_DEVICE_DESCRIPTOR)),
    ("ConfigInfoTable",   POINTER(POINTER(EFI_USB_CONFIG_INFO)))
  ]

UsbEndpointControl      = 0x00
UsbEndpointBulk         = 0x02
EFI_USB_ENDPOINT_TYPE   = ENUM

EfiUsbDeviceInfoUnknown           = 0
EfiUsbDeviceInfoSerialNumber      = 1
EfiUsbDeviceInfoManufacturerName  = 2
EfiUsbDeviceInfoProductName       = 3
EFI_USBFN_DEVICE_INFO_ID          = ENUM

EfiUsbEndpointDirectionHostOut  = 0
EfiUsbEndpointDirectionHostIn   = 1
EfiUsbEndpointDirectionDeviceTx = EfiUsbEndpointDirectionHostIn,
EfiUsbEndpointDirectionDeviceRx = EfiUsbEndpointDirectionHostOut
EFI_USBFN_ENDPOINT_DIRECTION    = ENUM

EfiUsbMsgNone                     = 0
EfiUsbMsgSetupPacket              = 1
EfiUsbMsgEndpointStatusChangedRx  = 2
EfiUsbMsgEndpointStatusChangedTx  = 3
EfiUsbMsgBusEventDetach           = 4
EfiUsbMsgBusEventAttach           = 5
EfiUsbMsgBusEventReset            = 6
EfiUsbMsgBusEventSuspend          = 7
EfiUsbMsgBusEventResume           = 8
EfiUsbMsgBusEventSpeed            = 9
EFI_USBFN_MESSAGE                 = ENUM

UsbTransferStatusUnknown    = 0
UsbTransferStatusComplete   = 1
UsbTransferStatusAborted    = 2
UsbTransferStatusActive     = 3
UsbTransferStatusNone       = 4
EFI_USBFN_TRANSFER_STATUS   = ENUM

class EFI_USBFN_TRANSFER_RESULT (Structure):
  _fields_ = [
    ("BytesTransferred",  UINTN),
    ("TransferStatus",    EFI_USBFN_TRANSFER_STATUS),
    ("EndpointIndex",     UINT8),
    ("Direction",         EFI_USBFN_ENDPOINT_DIRECTION),
    ("Buffer",            PVOID)
  ]

UsbBusSpeedUnknown  = 0
UsbBusSpeedLow      = 1
UsbBusSpeedFull     = 2
UsbBusSpeedHigh     = 3
UsbBusSpeedSuper    = 4
UsbBusSpeedMaximum  = UsbBusSpeedSuper
EFI_USB_BUS_SPEED   = ENUM

class EFI_USBFN_MESSAGE_PAYLOAD (Union):
  _fields_ = [
    ("udr", EFI_USB_DEVICE_REQUEST),
    ("utr", EFI_USBFN_TRANSFER_RESULT),
    ("ubs", EFI_USB_BUS_SPEED)
  ]

EfiUsbPolicyUndefined                     = 0
EfiUsbPolicyMaxTransactionSize            = 1
EfiUsbPolicyZeroLengthTerminationSupport  = 2
EfiUsbPolicyZeroLengthTermination         = 3
EFI_USBFN_POLICY_TYPE                     = ENUM

EFI_USBFN_IO_DETECT_PORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  POINTER(EFI_USBFN_PORT_TYPE)    # OUT *PortType
  )

EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  POINTER(EFI_USB_DEVICE_INFO)    # OUT *DeviceInfo
  )

EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  EFI_USB_ENDPOINT_TYPE,          # IN  EndpointType
  EFI_USB_BUS_SPEED,              # IN  BusSpeed
  POINTER(UINT16)                 # OUT *MaxPacketSize
  )

EFI_USBFN_IO_GET_DEVICE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  EFI_USBFN_DEVICE_INFO_ID,       # IN      Id
  POINTER(UINTN),                 # IN OUT  *BufferSize,
  PVOID                           # OUT     *Buffer OPTIONAL
  )

EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  POINTER(UINT16),                #    OUT  *Vid,
  POINTER(UINT16)                 #    OUT  *Pid
  )

EFI_USBFN_IO_ABORT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  UINT8,                          # IN  EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION    # IN  Direction
  )

EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction
  POINTER(BOOLEAN)                # IN OUT  *State
  )

EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  POINTER(BOOLEAN)                # IN OUT  *State
  )

EFI_USBFN_IO_EVENTHANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL),     # IN      *This
  POINTER(EFI_USBFN_MESSAGE),         #    OUT *Message,
  POINTER(UINTN),                     # IN OUT *PayloadSize,
  POINTER(EFI_USBFN_MESSAGE_PAYLOAD)  #    OUT *Payload
  )

EFI_USBFN_IO_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  POINTER(UINTN),                 # IN OUT *BufferSize,
  PVOID                           # IN OUT *Buffer
  )

EFI_USBFN_IO_GET_MAXTRANSFER_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  POINTER(UINTN)                  #    OUT  *MaxTransferSize
  )

EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINTN,                          # IN      Size,
  POINTER(PVOID)                  #    OUT  **Buffer
  )

EFI_USBFN_IO_FREE_TRANSFER_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  PVOID                           # IN      *Buffer
  )

EFI_USBFN_IO_START_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL)  # IN      *This
  )

EFI_USBFN_IO_STOP_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL)  # IN      *This
  )

EFI_USBFN_IO_SET_ENDPOINT_POLICY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN *This
  UINT8,                          # IN EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN Direction,
  EFI_USBFN_POLICY_TYPE,          # IN PolicyType,
  UINTN,                          # IN BufferSize,
  PVOID                           # IN Buffer
  )

EFI_USBFN_IO_GET_ENDPOINT_POLICY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  EFI_USBFN_POLICY_TYPE,          # IN      PolicyType,
  POINTER(UINTN),                 # IN OUT  *BufferSize,
  PVOID                           # IN OUT  *Buffer
  )

EFI_USBFN_IO_PROTOCOL._fields_ = [
    ("Revision",                  UINT32),
    ("DetectPort",                EFI_USBFN_IO_DETECT_PORT),
    ("ConfigureEnableEndpoints",  EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS),
    ("GetEndpointMaxPacketSize",  EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE),
    ("GetDeviceInfo",             EFI_USBFN_IO_GET_DEVICE_INFO),
    ("GetVendorIdProductId",      EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID),
    ("AbortTransfer",             EFI_USBFN_IO_ABORT_TRANSFER),
    ("GetEndpointStallState",     EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE),
    ("SetEndpointStallState",     EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE),
    ("EventHandler",              EFI_USBFN_IO_EVENTHANDLER),
    ("Transfer",                  EFI_USBFN_IO_TRANSFER),
    ("GetMaxTransferSize",        EFI_USBFN_IO_GET_MAXTRANSFER_SIZE),
    ("AllocateTransferBuffer",    EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER),
    ("FreeTransferBuffer",        EFI_USBFN_IO_FREE_TRANSFER_BUFFER),
    ("StartController",           EFI_USBFN_IO_START_CONTROLLER),
    ("StopController",            EFI_USBFN_IO_STOP_CONTROLLER),
    ("SetEndpointPolicy",         EFI_USBFN_IO_SET_ENDPOINT_POLICY),
    ("GetEndpointPolicy",         EFI_USBFN_IO_GET_ENDPOINT_POLICY)
  ]

