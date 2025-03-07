# SevSnpMsr.py
#
# EfiPy2.MdePkg.Register.Amd.SevSnpMsr
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2 import *

MSR_SEV_ES_GHCB  = 0xc0010130

class MSR_SEV_ES_GHCB_REGISTER_GhcbInfo (Structure):
  _fields_ = [
    ("Function",  UINT32, 12),
    ("Reserved1", UINT32, 20),
    ("Reserved2", UINT32, 32)
  ]

class MSR_SEV_ES_GHCB_REGISTER_GhcbProtocol (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",            UINT8 * 3),
    ("SevEncryptionBitPos", UINT8),
    ("SevEsProtocolMin",    UINT16),
    ("SevEsProtocolMax",    UINT16)
  ]

class MSR_SEV_ES_GHCB_REGISTER_GhcbTerminate (Structure):
  _pack_   = 1
  _fields_ = [
    ("Function",        UINT32, 12),
    ("ReasonCodeSet",   UINT32, 4),
    ("ReasonCode",      UINT32, 8),
    ("Reserved1",       UINT32, 8),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_SEV_ES_GHCB_REGISTER_GhcbHypervisorFeatures (Structure):
  _pack_   = 1
  _fields_ = [
    ("Function",        UINT64, 12),
    ("Features",        UINT64, 52)
  ]

class MSR_SEV_ES_GHCB_REGISTER_GhcbGpaRegister (Structure):
  _pack_   = 1
  _fields_ = [
    ("Function",            UINT64, 12),
    ("GuestFrameNumber",    UINT64, 52)
  ]

class MSR_SEV_ES_GHCB_REGISTER_SnpPageStateChangeRequest (Structure):
  _pack_   = 1
  _fields_ = [
    ("Function",            UINT64, 12),
    ("GuestFrameNumber",    UINT64, 40),
    ("Operation",           UINT64, 4),
    ("Reserved",            UINT64, 8)
  ]

class MSR_SEV_ES_GHCB_REGISTER_SnpPageStateChangeResponse (Structure):
  _pack_   = 1
  _fields_ = [
    ("Function",            UINT32, 12),
    ("Reserved",            UINT32, 20),
    ("ErrorCode",           UINT32)
  ]

class MSR_SEV_ES_GHCB_REGISTER_SnpVmplRequest (Structure):
  _pack_   = 1
  _fields_ = [
  ("Function",      UINT64, 12),
  ("Reserved1",     UINT64, 20),
  ("Vmpl",          UINT64, 8),
  ("Reserved2",     UINT64, 56)
  ]

class MSR_SEV_ES_GHCB_REGISTER_SnpVmplResponse (Structure):
  _pack_   = 1
  _fields_ = [
  ("Function",      UINT32, 12),
  ("Reserved",      UINT32, 20),
  ("ErrorCode",     UINT32)
  ]

class MSR_SEV_ES_GHCB_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("GhcbInfo",                    MSR_SEV_ES_GHCB_REGISTER_GhcbInfo),
    ("GhcbProtocol",                MSR_SEV_ES_GHCB_REGISTER_GhcbProtocol),
    ("GhcbTerminate",               MSR_SEV_ES_GHCB_REGISTER_GhcbTerminate),
    ("GhcbHypervisorFeatures",      MSR_SEV_ES_GHCB_REGISTER_GhcbHypervisorFeatures),
    ("GhcbGpaRegister",             MSR_SEV_ES_GHCB_REGISTER_GhcbGpaRegister),
    ("SnpPageStateChangeRequest",   MSR_SEV_ES_GHCB_REGISTER_SnpPageStateChangeRequest),
    ("SnpPageStateChangeResponse",  MSR_SEV_ES_GHCB_REGISTER_SnpPageStateChangeResponse),
    ("SnpVmplRequest",              MSR_SEV_ES_GHCB_REGISTER_SnpVmplRequest),
    ("SnpVmplResponse",             MSR_SEV_ES_GHCB_REGISTER_SnpVmplResponse),
    ("Ghcb",                        PVOID),
    ("GhcbPhysicalAddress",         UINT64),
    ("Uint64",                      UINT64)
  ]

GHCB_INFO_SEV_INFO                        = 1
GHCB_INFO_SEV_INFO_GET                    = 2
GHCB_INFO_CPUID_REQUEST                   = 4
GHCB_INFO_CPUID_RESPONSE                  = 5
GHCB_INFO_GHCB_GPA_REGISTER_REQUEST       = 18
GHCB_INFO_GHCB_GPA_REGISTER_RESPONSE      = 19
GHCB_INFO_SNP_PAGE_STATE_CHANGE_REQUEST   = 20
GHCB_INFO_SNP_PAGE_STATE_CHANGE_RESPONSE  = 21
GHCB_INFO_SNP_VMPL_REQUEST                = 22
GHCB_INFO_SNP_VMPL_RESPONSE               = 23
GHCB_HYPERVISOR_FEATURES_REQUEST          = 128
GHCB_HYPERVISOR_FEATURES_RESPONSE         = 129
GHCB_INFO_TERMINATE_REQUEST               = 256

GHCB_TERMINATE_GHCB           = 0
GHCB_TERMINATE_GHCB_GENERAL   = 0
GHCB_TERMINATE_GHCB_PROTOCOL  = 1

MSR_SEV_STATUS  = 0xc0010131

class MSR_SEV_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SevBit",              UINT32, 1),
    ("SevEsBit",            UINT32, 1),
    ("SevSnpBit",           UINT32, 1),
    ("vTOM",                UINT32, 1),
    ("ReflectVC",           UINT32, 1),
    ("RestrictedInjection", UINT32, 1),
    ("AlternateInjection",  UINT32, 1),
    ("DebugVirtualization", UINT32, 1),
    ("PreventHostIBS",      UINT32, 1),
    ("SNPBTBIsolation",     UINT32, 1),
    ("VmplSSS",             UINT32, 1),
    ("SecureTsc",           UINT32, 1),
    ("VmgexitParameter",    UINT32, 1),
    ("PmcVirtualization",   UINT32, 1),
    ("IbsVirtualization",   UINT32, 1),
    ("Reserved1",           UINT32, 1),
    ("VmsaRegProt",         UINT32, 1),
    ("SmtProtection",       UINT32, 1),
    ("SecureAVIC",          UINT32, 1),
    ("Reserved2",           UINT32, 4),
    ("IbpbOnEntry",         UINT32, 1),
    ("Reserved3",           UINT32, 8)
  ]

class MSR_SEV_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_SEV_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

