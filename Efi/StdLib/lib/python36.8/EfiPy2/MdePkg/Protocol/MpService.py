# MpService.py
#
# EfiPy2.MdePkg.Protocol.MpService
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMultiPhase  import EFI_AP_PROCEDURE

gEfiMpServiceProtocolGuid = \
  EFI_GUID (0x3fdda605, 0xa76e, 0x4f46, (0xad, 0x29, 0x12, 0xf4, 0x53, 0x1b, 0x3d, 0x08))

CPU_V2_EXTENDED_TOPOLOGY  = BIT24

class EFI_MP_SERVICES_PROTOCOL (Structure):
  pass

END_OF_CPU_LIST    = 0xffffffff

PROCESSOR_AS_BSP_BIT         = 0x00000001
PROCESSOR_ENABLED_BIT        = 0x00000002
PROCESSOR_HEALTH_STATUS_BIT  = 0x00000004

class EFI_CPU_PHYSICAL_LOCATION (Structure):
  _fields_ = [
    ("Package", UINT32),
    ("Core",    UINT32),
    ("Thread",  UINT32)
  ]

class EFI_CPU_PHYSICAL_LOCATION2 (Structure):
  _fields_ = [
    ("Package", UINT32),
    ("Module",  UINT32),
    ("Tile",    UINT32),
    ("Die",     UINT32),
    ("Core",    UINT32),
    ("Thread",  UINT32)
  ]

class EXTENDED_PROCESSOR_INFORMATION (Union):
  _fields_ = [
    ("Location2",   EFI_CPU_PHYSICAL_LOCATION2)
  ]

class EFI_PROCESSOR_INFORMATION (Structure):
  _fields_ = [
    ("ProcessorId",         UINT64),
    ("StatusFlag",          UINT32),
    ("Location",            EFI_CPU_PHYSICAL_LOCATION),
    ("ExtendedInformation", EXTENDED_PROCESSOR_INFORMATION)
  ]

EFI_MP_SERVICES_GET_NUMBER_OF_PROCESSORS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  POINTER(UINTN),                     # OUT *NumberOfProcessors,
  POINTER(UINTN)                      # OUT *NumberOfEnabledProcessors
  )

EFI_MP_SERVICES_GET_PROCESSOR_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  POINTER(EFI_PROCESSOR_INFORMATION)  # OUT *ProcessorInfoBuffer
  )

EFI_MP_SERVICES_STARTUP_ALL_APS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  EFI_AP_PROCEDURE,                   # IN  Procedure,
  BOOLEAN,                            # IN  SingleThread,
  EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
  UINTN,                              # IN  TimeoutInMicroSeconds,
  PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
  POINTER(POINTER(UINTN))             # OUT **FailedCpuList         OPTIONAL
  )

EFI_MP_SERVICES_STARTUP_THIS_AP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  EFI_AP_PROCEDURE,                   # IN  Procedure,
  UINTN,                              # IN  ProcessorNumber,
  EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
  UINTN,                              # IN  TimeoutInMicroseconds,
  PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
  POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
  )

EFI_MP_SERVICES_SWITCH_BSP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  BOOLEAN                             # IN  EnableOldBSP
  )

EFI_MP_SERVICES_ENABLEDISABLEAP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  UINTN,                              # IN  ProcessorNumber,
  BOOLEAN,                            # IN  EnableAP
  POINTER(UINT32)                     # IN  *HealthFlag OPTIONAL
  )

EFI_MP_SERVICES_WHOAMI = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
  POINTER(UINTN)                      # OUT *ProcessorNumber
  )

EFI_MP_SERVICES_PROTOCOL._fields_ = [
    ("GetNumberOfProcessors", EFI_MP_SERVICES_GET_NUMBER_OF_PROCESSORS),
    ("GetProcessorInfo",      EFI_MP_SERVICES_GET_PROCESSOR_INFO),
    ("StartupAllAPs",         EFI_MP_SERVICES_STARTUP_ALL_APS),
    ("StartupThisAP",         EFI_MP_SERVICES_STARTUP_THIS_AP),
    ("SwitchBSP",             EFI_MP_SERVICES_SWITCH_BSP),
    ("EnableDisableAP",       EFI_MP_SERVICES_ENABLEDISABLEAP),
    ("WhoAmI",                EFI_MP_SERVICES_WHOAMI)
  ]

