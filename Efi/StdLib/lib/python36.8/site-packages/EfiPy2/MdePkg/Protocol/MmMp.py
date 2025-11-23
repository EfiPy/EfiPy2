# MmMp.py
#
# EfiPy2.MdePkg.Protocol.MmMp
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.Pi.PiMultiPhase  import EFI_AP_PROCEDURE, EFI_AP_PROCEDURE2

gEfiMmMpProtocolGuid = \
  EFI_GUID (0x5d5450d7, 0x990c, 0x4180, (0xa8, 0x3, 0x8e, 0x63, 0xf0, 0x60, 0x83, 0x7 ))

EFI_MM_MP_PROTOCOL_REVISION  = 0x00

EFI_MM_MP_TIMEOUT_SUPPORTED  = 0x01

MM_COMPLETION = PVOID

class MM_DISPATCH_COMPLETION_TOKEN (Structure):
  _fields_ = [
    ("Completion",  MM_COMPLETION),
    ("Status",      EFI_STATUS)
  ]

class EFI_MM_MP_PROTOCOL (Structure):
  pass

EFI_MM_GET_NUMBER_OF_PROCESSORS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  POINTER(UINTN)                #   OUT      *NumberOfProcessors
  )

EFI_MM_DISPATCH_PROCEDURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  EFI_AP_PROCEDURE2,            #   IN       Procedure,
  UINTN,                        #   IN       CpuNumber,
  UINTN,                        #   IN       TimeoutInMicroseconds,
  PVOID,                        #   IN OUT   *ProcedureArguments OPTIONAL,
  POINTER(MM_COMPLETION),       #   IN OUT   *Token,
  POINTER(EFI_STATUS)           #   IN OUT   *CPUStatus
  )

EFI_MM_BROADCAST_PROCEDURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  EFI_AP_PROCEDURE2,            #   IN       Procedure,
  UINTN,                        #   IN       TimeoutInMicroseconds,
  PVOID,                        #   IN OUT   *ProcedureArguments OPTIONAL,
  POINTER(MM_COMPLETION),       #   IN OUT   *Token,
  POINTER(EFI_STATUS)           #   IN OUT   *CPUStatus
  )

EFI_MM_SET_STARTUP_PROCEDURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  EFI_AP_PROCEDURE,             #   IN       Procedure,
  PVOID                         #   IN OUT   *ProcedureArguments OPTIONAL,
  )

EFI_CHECK_FOR_PROCEDURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  MM_COMPLETION                 #   IN       Token
  )

EFI_WAIT_FOR_PROCEDURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_MP_PROTOCOL),  #   IN CONST *This
  MM_COMPLETION                 #   IN       Token
  )

EFI_MM_MP_PROTOCOL._fields_ = [
    ("Revision",                UINT32),
    ("Attributes",              UINT32),
    ("GetNumberOfProcessors",   EFI_MM_GET_NUMBER_OF_PROCESSORS),
    ("DispatchProcedure",       EFI_MM_DISPATCH_PROCEDURE),
    ("BroadcastProcedure",      EFI_MM_BROADCAST_PROCEDURE),
    ("SetStartupProcedure",     EFI_MM_SET_STARTUP_PROCEDURE),
    ("CheckForProcedure",       EFI_CHECK_FOR_PROCEDURE),
    ("WaitForProcedure",        EFI_WAIT_FOR_PROCEDURE)
  ]

