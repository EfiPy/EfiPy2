# UsbIo.py
#
# EfiPy2.MdePkg.Protocol.UsbIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.IndustryStandard import Usb

gEfiUsbIoProtocolGuid   = \
  EFI_GUID (0x2B2F68D6, 0x0CD2, 0x44cf, (0x8E, 0x8B, 0xBB, 0xA2, 0x0B, 0x1B, 0x5B, 0x75 ))

class EFI_USB_IO_PROTOCOL (Structure):
  pass

EFI_USB_DEVICE_REQUEST              = Usb.USB_DEVICE_REQUEST
EFI_USB_DEVICE_DESCRIPTOR           = Usb.USB_DEVICE_DESCRIPTOR
EFI_USB_CONFIG_DESCRIPTOR           = Usb.USB_CONFIG_DESCRIPTOR
EFI_USB_INTERFACE_DESCRIPTOR        = Usb.USB_INTERFACE_DESCRIPTOR
EFI_USB_ENDPOINT_DESCRIPTOR         = Usb.USB_ENDPOINT_DESCRIPTOR

EfiUsbDataIn            = 0
EfiUsbDataOut           = 1
EfiUsbNoData            = 2
EFI_USB_DATA_DIRECTION  = ENUM

EFI_USB_NOERROR             = 0x00
EFI_USB_ERR_NOTEXECUTE      = 0x01
EFI_USB_ERR_STALL           = 0x02
EFI_USB_ERR_BUFFER          = 0x04
EFI_USB_ERR_BABBLE          = 0x08
EFI_USB_ERR_NAK             = 0x10
EFI_USB_ERR_CRC             = 0x20
EFI_USB_ERR_TIMEOUT         = 0x40
EFI_USB_ERR_BITSTUFF        = 0x80
EFI_USB_ERR_SYSTEM          = 0x100

EFI_ASYNC_USB_TRANSFER_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  PVOID,       # IN *Data,
  UINTN,       # IN DataLength,
  PVOID,       # IN *Context,
  UINT32       # IN Status
  )

EFI_USB_IO_CONTROL_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN      *This,
  POINTER(EFI_USB_DEVICE_REQUEST),  # IN      *Request,
  EFI_USB_DATA_DIRECTION,           # IN      Direction,
  UINT32,                           # IN      Timeout,
  PVOID,                            # IN OUT  *Data OPTIONAL,
  UINTN,                            # IN      DataLength  OPTIONAL,
  POINTER(UINT32)                   # OUT     *Status
  )

EFI_USB_IO_BULK_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN      *This,
  UINT8,                            # IN      DeviceEndpoint,
  PVOID,                            # IN OUT  *Data,
  POINTER(UINTN),                   # IN OUT  *DataLength,
  UINTN,                            # IN      Timeout,
  POINTER(UINT32)                   # OUT     *Status
  )

EFI_USB_IO_ASYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN *This,
  UINT8,                            # IN DeviceEndpoint,
  BOOLEAN,                          # IN IsNewTransfer,
  UINTN,                            # IN PollingInterval    OPTIONAL,
  UINTN,                            # IN DataLength         OPTIONAL,
  EFI_ASYNC_USB_TRANSFER_CALLBACK,  # IN InterruptCallBack  OPTIONAL,
  PVOID                             # IN *Context OPTIONAL
  )

EFI_USB_IO_SYNC_INTERRUPT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL), # IN     *This,
  UINT8,                        # IN     DeviceEndpoint,
  PVOID,                        # IN OUT *Data,
  POINTER(UINTN),               # IN OUT *DataLength,
  UINTN,                        # IN     Timeout,
  POINTER(UINT32)               # OUT    *Status
  )

EFI_USB_IO_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL), # IN     *This,
  UINT8,                        # IN     DeviceEndpoint,
  PVOID,                        # IN OUT *Data,
  UINTN,                        # IN     DataLength,
  POINTER(UINT32)               # OUT    *Status
  )

EFI_USB_IO_ASYNC_ISOCHRONOUS_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN     *This,
  UINT8,                            # IN     DeviceEndpoint,
  PVOID,                            # IN OUT *Data,
  UINTN,                            # IN     DataLength,
  EFI_ASYNC_USB_TRANSFER_CALLBACK,  # IN     IsochronousCallBack,
  PVOID                             # IN     *Context OPTIONAL
  )

EFI_USB_IO_PORT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL)      # IN     *This
  )

EFI_USB_IO_GET_DEVICE_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),       # IN    *This
  POINTER(EFI_USB_DEVICE_DESCRIPTOR)  # OUT   *DeviceDescriptor
  )

EFI_USB_IO_GET_CONFIG_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),       # IN    *This
  POINTER(EFI_USB_CONFIG_DESCRIPTOR)  # OUT   *ConfigurationDescriptor
  )

EFI_USB_IO_GET_INTERFACE_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),         # IN    *This
  POINTER(EFI_USB_INTERFACE_DESCRIPTOR) # OUT   *InterfaceDescriptor
  )

EFI_USB_IO_GET_ENDPOINT_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),         # IN    *This
  UINT8,                                # IN    EndpointIndex,
  POINTER(EFI_USB_ENDPOINT_DESCRIPTOR)  # OUT   *EndpointDescriptor
  )

EFI_USB_IO_GET_STRING_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN  *This
  UINT16,                           # IN  LangID,
  UINT8,                            # IN  StringID,
  POINTER(PCHAR16)                  # OUT **String
  )

EFI_USB_IO_GET_SUPPORTED_LANGUAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USB_IO_PROTOCOL),     # IN      *This
  POINTER(POINTER(UINT16)),         #     OUT **LangIDTable,
  POINTER(UINT16)                   #     OUT *TableSize
  )

EFI_USB_IO_PROTOCOL._fields_ = [
    ("UsbControlTransfer",          EFI_USB_IO_CONTROL_TRANSFER),
    ("UsbBulkTransfer",             EFI_USB_IO_BULK_TRANSFER),
    ("UsbAsyncInterruptTransfer",   EFI_USB_IO_ASYNC_INTERRUPT_TRANSFER),
    ("UsbSyncInterruptTransfer",    EFI_USB_IO_SYNC_INTERRUPT_TRANSFER),
    ("UsbIsochronousTransfer",      EFI_USB_IO_ISOCHRONOUS_TRANSFER),
    ("UsbAsyncIsochronousTransfer", EFI_USB_IO_ASYNC_ISOCHRONOUS_TRANSFER),
    ("UsbGetDeviceDescriptor",      EFI_USB_IO_GET_DEVICE_DESCRIPTOR),
    ("UsbGetConfigDescriptor",      EFI_USB_IO_GET_CONFIG_DESCRIPTOR),
    ("UsbGetInterfaceDescriptor",   EFI_USB_IO_GET_INTERFACE_DESCRIPTOR),
    ("UsbGetEndpointDescriptor",    EFI_USB_IO_GET_ENDPOINT_DESCRIPTOR),
    ("UsbGetStringDescriptor",      EFI_USB_IO_GET_STRING_DESCRIPTOR),
    ("UsbGetSupportedLanguages",    EFI_USB_IO_GET_SUPPORTED_LANGUAGE),
    ("UsbPortReset",                EFI_USB_IO_PORT_RESET)
  ]

