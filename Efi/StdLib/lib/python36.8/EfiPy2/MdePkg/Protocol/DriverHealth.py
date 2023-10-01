# DriverHealth.py
#
# EfiPy2.MdePkg.Protocol.DriverHealth
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import  \
                                     EFI_HII_HANDLE,           \
                                     EFI_STRING_ID

gEfiDriverHealthProtocolGuid            = \
  EFI_GUID (0x2a534210, 0x9280, 0x41d8, ( 0xae, 0x79, 0xca, 0xda, 0x1, 0xa2, 0xb1, 0x27 ))

class EFI_DRIVER_HEALTH_PROTOCOL (Structure):
  pass

EfiDriverHealthStatusHealthy                = 0
EfiDriverHealthStatusRepairRequired         = 1
EfiDriverHealthStatusConfigurationRequired  = 2
EfiDriverHealthStatusFailed                 = 3
EfiDriverHealthStatusReconnectRequired      = 4
EfiDriverHealthStatusRebootRequired         = 5
EFI_DRIVER_HEALTH_STATUS                    = ENUM

class EFI_DRIVER_HEALTH_HII_MESSAGE (Structure):
  _fields_ = [
    ("HiiHandle",   EFI_HII_HANDLE),
    ("StringId",    EFI_STRING_ID),
    ("MessageCode", UINT64)
  ]

EFI_DRIVER_HEALTH_REPAIR_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  UINTN,      # IN Value,
  UINTN       # IN Limit
  )

EFI_DRIVER_HEALTH_GET_HEALTH_STATUS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_HEALTH_PROTOCOL),              # IN  *This,
  EFI_HANDLE,                                       # IN  ControllerHandle OPTIONAL,
  EFI_HANDLE,                                       # IN  ChildHandle      OPTIONAL,
  POINTER(EFI_DRIVER_HEALTH_STATUS),                # OUT *HealthStatus,
  POINTER(POINTER(EFI_DRIVER_HEALTH_HII_MESSAGE)),  # OUT **MessageList    OPTIONAL,
  POINTER(EFI_HII_HANDLE)                           # OUT *FormHiiHandle   OPTIONAL
  )

EFI_DRIVER_HEALTH_REPAIR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DRIVER_HEALTH_PROTOCOL),              # IN *This,
  EFI_HANDLE,                                       # IN ControllerHandle,
  EFI_HANDLE,                                       # IN ChildHandle       OPTIONAL,
  EFI_DRIVER_HEALTH_REPAIR_NOTIFY                   # IN RepairNotify      OPTIONAL
  )

EFI_DRIVER_HEALTH_PROTOCOL._fields_ = [
    ("GetHealthStatus", EFI_DRIVER_HEALTH_GET_HEALTH_STATUS),
    ("Repair",          EFI_DRIVER_HEALTH_REPAIR)
  ]

