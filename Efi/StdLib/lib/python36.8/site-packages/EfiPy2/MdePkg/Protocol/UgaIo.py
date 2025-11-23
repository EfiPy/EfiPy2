# UgaIo.py
#
# EfiPy2.MdePkg.Protocol.UgaIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiUgaIoProtocolGuid   = \
  EFI_GUID (0x61a4d49e, 0x6f68, 0x4f1b, ( 0xb9, 0x22, 0xa8, 0x6e, 0xed, 0xb, 0x7, 0xa2 ))

class EFI_UGA_IO_PROTOCOL (Structure):
  pass

UGA_STATUS      = UINT32

UgaDtParentBus            = 1
UgaDtGraphicsController   = 2
UgaDtOutputController     = 3
UgaDtOutputPort           = 4
UgaDtOther                = 5
UGA_DEVICE_TYPE           = ENUM

UGA_DEVICE_ID   = UINT32
PUGA_DEVICE_ID  = POINTER(UGA_DEVICE_ID)

class UGA_DEVICE_DATA (Structure):
  _fields_ = [
    ("deviceType",            UGA_DEVICE_TYPE),
    ("deviceId",              UGA_DEVICE_ID),
    ("ui32DeviceContextSize", UINT32),
    ("ui32SharedContextSize", UINT32)
  ]
PUGA_DEVICE_DATA  = POINTER(UGA_DEVICE_DATA)

class UGA_DEVICE (Structure):
  pass

PUGA_DEVICE  = POINTER(UGA_DEVICE)

UGA_DEVICE._fields_ = [
    ("pvDeviceContext",   PVOID),
    ("pvSharedContext",   PVOID),
    ("pvRunTimeContext",  PVOID),
    ("pParentDevice",     POINTER(UGA_DEVICE)),
    ("pvBusIoServices",   PVOID),
    ("pvStdIoServices",   PVOID),
    ("deviceData",        UGA_DEVICE_DATA)
  ]

UgaIoGetVersion             = 1
UgaIoGetChildDevice         = 2
UgaIoStartDevice            = 3
UgaIoStopDevice             = 4
UgaIoFlushDevice            = 5
UgaIoResetDevice            = 6
UgaIoGetDeviceState         = 7
UgaIoSetDeviceState         = 8
UgaIoSetPowerState          = 9
UgaIoGetMemoryConfiguration = 10
UgaIoSetVideoMode           = 11
UgaIoCopyRectangle          = 12
UgaIoGetEdidSegment         = 13
UgaIoDeviceChannelOpen      = 14
UgaIoDeviceChannelClose     = 15
UgaIoDeviceChannelRead      = 16
UgaIoDeviceChannelWrite     = 17
UgaIoGetPersistentDataSize  = 18
UgaIoGetPersistentData      = 19
UgaIoSetPersistentData      = 20
UgaIoGetDevicePropertySize  = 21
UgaIoGetDeviceProperty      = 22
UgaIoBtPrivateInterface     = 23
UGA_IO_REQUEST_CODE         = ENUM
PUGA_IO_REQUEST_CODE = POINTER (UGA_IO_REQUEST_CODE)

class UGA_IO_REQUEST (Structure):
  _fields_ = [
    ("ioRequestCode",     UGA_IO_REQUEST_CODE), #   IN
    ("pvInBuffer",        PVOID),               #   IN
    ("ui64InBufferSize",  UINT64),              #   IN
    ("pvOutBuffer",       PVOID),               #   OUT
    ("ui64OutBufferSize", UINT64),              #   IN
    ("ui64BytesReturned", UINT64)               #   OUT
  ]
PUGA_IO_REQUEST = POINTER (UGA_IO_REQUEST)

EFI_UGA_IO_PROTOCOL_CREATE_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_IO_PROTOCOL), # IN  *This
  POINTER(UGA_DEVICE),          # IN  *ParentDevice,
  POINTER(UGA_DEVICE_DATA),     # IN  *DeviceData,
  PVOID,                        # IN  *RunTimeContext,
  POINTER(POINTER(UGA_DEVICE))  # OUT **Device
  )
  
EFI_UGA_IO_PROTOCOL_DELETE_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_IO_PROTOCOL), # IN  *This
  POINTER(UGA_DEVICE)           # OUT *Device
  )
  
PUGA_FW_SERVICE_DISPATCH = CFUNCTYPE (
  UGA_STATUS,
  PUGA_DEVICE,          # IN      pDevice
  PUGA_IO_REQUEST       # IN  OUT pIoRequest
  )

EFI_UGA_IO_PROTOCOL._fields_ = [
    ("CreateDevice",    EFI_UGA_IO_PROTOCOL_CREATE_DEVICE),
    ("DeleteDevice",    EFI_UGA_IO_PROTOCOL_DELETE_DEVICE),
    ("DispatchService", PUGA_FW_SERVICE_DISPATCH)
  ]

class EFI_DRIVER_OS_HANDOFF_HEADER (Structure):
  _fields_ = [
    ("Version",         UINT32),
    ("HeaderSize",      UINT32),
    ("SizeOfEntries",   UINT32),
    ("NumberOfEntries", UINT32)
  ]

EfiUgaDriverFromPciRom  = 0
EfiUgaDriverFromSystem  = 1
EfiDriverHandoffMax     = 2
EFI_DRIVER_HANOFF_ENUM  = ENUM

class EFI_DRIVER_OS_HANDOFF (Structure):
  _fields_ = [
    ("Type",        EFI_DRIVER_HANOFF_ENUM),
    ("DevicePath",  POINTER(EFI_DEVICE_PATH_PROTOCOL)),
    ("PciRomImage", PVOID),
    ("PciRomSize",  UINT64)
  ]

