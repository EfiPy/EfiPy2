# SmramSaveStateMap.py
#
# EfiPy2.MdePkg.Register.Amd.SmramSaveStateMap
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
# 
from EfiPy2  import *

SMM_DEFAULT_SMBASE  = 0x30000

SMM_HANDLER_OFFSET  = 0x8000

AMD_SMM_MIN_REV_ID_X64  = 0x30064

class AMD_SMRAM_SAVE_STATE_MAP32 (Structure):
  _pack_   = 1
  _fields_ = [
  ("Reserved",            UINT8 * 0x200),
  ("Reserved1",           UINT8 * 0xf8),
  ("SMBASE",              UINT32),
  ("SMMRevId",            UINT32),
  ("IORestart",           UINT16),
  ("AutoHALTRestart",     UINT16),
  ("Reserved2",           UINT8 * 0x84),
  ("GDTBase",             UINT32),
  ("Reserved3",           UINT64),
  ("IDTBase",             UINT32),
  ("Reserved4",           UINT8 * 0x10),
  ("_ES",                 UINT32),
  ("_CS",                 UINT32),
  ("_SS",                 UINT32),
  ("_DS",                 UINT32),
  ("_FS",                 UINT32),
  ("_GS",                 UINT32),
  ("LDTBase",             UINT32),
  ("_TR",                 UINT32),
  ("_DR7",                UINT32),
  ("_DR6",                UINT32),
  ("_EAX",                UINT32),
  ("_ECX",                UINT32),
  ("_EDX",                UINT32),
  ("_EBX",                UINT32),
  ("_ESP",                UINT32),
  ("_EBP",                UINT32),
  ("_ESI",                UINT32),
  ("_EDI",                UINT32),
  ("_EIP",                UINT32),
  ("_EFLAGS",             UINT32),
  ("_CR3",                UINT32),
  ("_CR0",                UINT32)
  ]

class AMD_SMRAM_SAVE_STATE_MAP64 (Structure):
  _pack_   = 1
  _fields_ = [
  ("Reserved",                  UINT8 * 0x200),
  ("_ES",                       UINT16),
  ("_ESAttributes",             UINT16),
  ("_ESLimit",                  UINT32),
  ("_ESBase",                   UINT64),
  ("_CS",                       UINT16),
  ("_CSAttributes",             UINT16),
  ("_CSLimit",                  UINT32),
  ("_CSBase",                   UINT64),
  ("_SS",                       UINT16),
  ("_SSAttributes",             UINT16),
  ("_SSLimit",                  UINT32),
  ("_SSBase",                   UINT64),
  ("_DS",                       UINT16),
  ("_DSAttributes",             UINT16),
  ("_DSLimit",                  UINT32),
  ("_DSBase",                   UINT64),
  ("_FS",                       UINT16),
  ("_FSAttributes",             UINT16),
  ("_FSLimit",                  UINT32),
  ("_FSBase",                   UINT64),
  ("_GS",                       UINT16),
  ("_GSAttributes",             UINT16),
  ("_GSLimit",                  UINT32),
  ("_GSBase",                   UINT64),
  ("_GDTRReserved1",            UINT32),
  ("_GDTRLimit",                UINT16),
  ("_GDTRReserved2",            UINT16),
  ("_GDTRBaseLoDword",          UINT32),
  ("_GDTRBaseHiDword",          UINT32),
  ("_LDTR",                     UINT16),
  ("_LDTRAttributes",           UINT16),
  ("_LDTRLimit",                UINT32),
  ("_LDTRBaseLoDword",          UINT32),
  ("_LDTRBaseHiDword",          UINT32),
  ("_IDTRReserved1",            UINT32),
  ("_IDTRLimit",                UINT16),
  ("_IDTRReserved2",            UINT16),
  ("_IDTRBaseLoDword",          UINT32),
  ("_IDTRBaseHiDword",          UINT32),
  ("_TR",                       UINT16),
  ("_TRAttributes",             UINT16),
  ("_TRLimit",                  UINT32),
  ("_TRBase",                   UINT64),
  ("IO_RIP",                    UINT64),
  ("IO_RCX",                    UINT64),
  ("IO_RSI",                    UINT64),
  ("IO_RDI",                    UINT64),
  ("IO_DWord",                  UINT32),
  ("Reserved1",                 UINT8 * 0x04),
  ("IORestart",                 UINT8),
  ("AutoHALTRestart",           UINT8),
  ("Reserved2",                 UINT8 * 0x06),
  ("EFER",                      UINT64),
  ("SVM_Guest",                 UINT64),
  ("SVM_GuestVMCB",             UINT64),
  ("SVM_GuestVIntr",            UINT64),
  ("Reserved3",                 UINT8 * 0x0C),
  ("SMMRevId",                  UINT32),
  ("SMBASE",                    UINT32),
  ("Reserved4",                 UINT8 * 0x14),
  ("SSP",                       UINT64),
  ("SVM_GuestPAT",              UINT64),
  ("SVM_HostEFER",              UINT64),
  ("SVM_HostCR4",               UINT64),
  ("SVM_HostCR3",               UINT64),
  ("SVM_HostCR0",               UINT64),
  ("_CR4",                      UINT64),
  ("_CR3",                      UINT64),
  ("_CR0",                      UINT64),
  ("_DR7",                      UINT64),
  ("_DR6",                      UINT64),
  ("_RFLAGS",                   UINT64),
  ("_RIP",                      UINT64),
  ("_R15",                      UINT64),
  ("_R14",                      UINT64),
  ("_R13",                      UINT64),
  ("_R12",                      UINT64),
  ("_R11",                      UINT64),
  ("_R10",                      UINT64),
  ("_R9",                       UINT64),
  ("_R8",                       UINT64),
  ("_RDI",                      UINT64),
  ("_RSI",                      UINT64),
  ("_RBP",                      UINT64),
  ("_RSP",                      UINT64),
  ("_RBX",                      UINT64),
  ("_RDX",                      UINT64),
  ("_RCX",                      UINT64),
  ("_RAX",                      UINT64)
  ]

class AMD_SMRAM_SAVE_STATE_MAP (Union):
  _pack_   = 1
  _fields_ = [
  ("x86",   AMD_SMRAM_SAVE_STATE_MAP32),
  ("x64",   AMD_SMRAM_SAVE_STATE_MAP64)
  ]
