# SmramSaveStateMap.py
#
# EfiPy2.MdePkg.Register.Intel.SmramSaveStateMap
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

SMM_DEFAULT_SMBASE  = 0x30000

SMM_HANDLER_OFFSET  = 0x8000

class SMRAM_SAVE_STATE_MAP32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",         UINT8 * 0x200),    # 7c00h
    ("Reserved1",        UINT8 * 0x0F8),    # 7e00h
    ("SMBASE",           UINT32),           # 7ef8h
    ("SMMRevId",         UINT32),           # 7efch
    ("IORestart",        UINT16),           # 7f00h
    ("AutoHALTRestart",  UINT16),           # 7f02h
    ("Reserved2",        UINT8 * 0x09C),    # 7f08h
    ("IOMemAddr",        UINT32),           # 7fa0h
    ("IOMisc",           UINT32),           # 7fa4h
    ("_ES",              UINT32),           # 7fa8h
    ("_CS",              UINT32),           # 7fach
    ("_SS",              UINT32),           # 7fb0h
    ("_DS",              UINT32),           # 7fb4h
    ("_FS",              UINT32),           # 7fb8h
    ("_GS",              UINT32),           # 7fbch
    ("Reserved3",        UINT32),           # 7fc0h
    ("_TR",              UINT32),           # 7fc4h
    ("_DR7",             UINT32),           # 7fc8h
    ("_DR6",             UINT32),           # 7fcch
    ("_EAX",             UINT32),           # 7fd0h
    ("_ECX",             UINT32),           # 7fd4h
    ("_EDX",             UINT32),           # 7fd8h
    ("_EBX",             UINT32),           # 7fdch
    ("_ESP",             UINT32),           # 7fe0h
    ("_EBP",             UINT32),           # 7fe4h
    ("_ESI",             UINT32),           # 7fe8h
    ("_EDI",             UINT32),           # 7fech
    ("_EIP",             UINT32),           # 7ff0h
    ("_EFLAGS",          UINT32),           # 7ff4h
    ("_CR3",             UINT32),           # 7ff8h
    ("_CR0",             UINT32),           # 7ffch
  ]

class SMRAM_SAVE_STATE_MAP64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",       UINT8 * 0x1D0), # 7c00h
    ("GdtBaseHiDword",  UINT32),        # 7dd0h
    ("LdtBaseHiDword",  UINT32),        # 7dd4h
    ("IdtBaseHiDword",  UINT32),        # 7dd8h
    ("Reserved2",       UINT8 * 0x00C), # 7ddch
    ("IO_EIP",          UINT64),        # 7de8h
    ("Reserved3",       UINT8 * 0x050), # 7df0h
    ("_CR4",            UINT32),        # 7e40h
    ("Reserved4",       UINT8 * 0x048), # 7e44h
    ("GdtBaseLoDword",  UINT32),        # 7e8ch
    ("Reserved5",       UINT32),        # 7e90h
    ("IdtBaseLoDword",  UINT32),        # 7e94h
    ("Reserved6",       UINT32),        # 7e98h
    ("LdtBaseLoDword",  UINT32),        # 7e9ch
    ("Reserved7",       UINT8 * 0x038), # 7ea0h
    ("EptVmxControl",   UINT64),        # 7ed8h
    ("EnEptVmxControl", UINT32),        # 7ee0h
    ("Reserved8",       UINT8 * 0x014), # 7ee4h
    ("SMBASE",          UINT32),        # 7ef8h
    ("SMMRevId",        UINT32),        # 7efch
    ("IORestart",       UINT16),        # 7f00h
    ("AutoHALTRestart", UINT16),        # 7f02h
    ("Reserved9",       UINT8 * 0x018), # 7f04h
    ("_R15",            UINT64),        # 7f1ch
    ("_R14",            UINT64),        #
    ("_R13",            UINT64),        #
    ("_R12",            UINT64),        #
    ("_R11",            UINT64),        #
    ("_R10",            UINT64),        #
    ("_R9",             UINT64),        #
    ("_R8",             UINT64),        #
    ("_RAX",            UINT64),        # 7f5ch
    ("_RCX",            UINT64),        #
    ("_RDX",            UINT64),        #
    ("_RBX",            UINT64),        #
    ("_RSP",            UINT64),        #
    ("_RBP",            UINT64),        #
    ("_RSI",            UINT64),        #
    ("_RDI",            UINT64),        #
    ("IOMemAddr",       UINT64),        # 7f9ch
    ("IOMisc",          UINT32),        # 7fa4h
    ("_ES",             UINT32),        # 7fa8h
    ("_CS",             UINT32),        #
    ("_SS",             UINT32),        #
    ("_DS",             UINT32),        #
    ("_FS",             UINT32),        #
    ("_GS",             UINT32),        #
    ("_LDTR",           UINT32),        # 7fc0h
    ("_TR",             UINT32),        #
    ("_DR7",            UINT64),        # 7fc8h
    ("_DR6",            UINT64),        #
    ("_RIP",            UINT64),        # 7fd8h
    ("IA32_EFER",       UINT64),        # 7fe0h
    ("_RFLAGS",         UINT64),        # 7fe8h
    ("_CR3",            UINT64),        # 7ff0h
    ("_CR0",            UINT64)         # 7ff8h
  ]

class SMRAM_SAVE_STATE_MAP (Union):
  _pack_   = 1
  _fields_ = [
    ("x86", SMRAM_SAVE_STATE_MAP32),
    ("x64", SMRAM_SAVE_STATE_MAP64)
  ]

SMRAM_SAVE_STATE_MIN_REV_ID_IOMISC  = 0x30004

SMM_IO_LENGTH_BYTE   = 0x01
SMM_IO_LENGTH_WORD   = 0x02
SMM_IO_LENGTH_DWORD  = 0x04

SMM_IO_TYPE_IN_IMMEDIATE   = 0x9
SMM_IO_TYPE_IN_DX          = 0x1
SMM_IO_TYPE_OUT_IMMEDIATE  = 0x8
SMM_IO_TYPE_OUT_DX         = 0x0
SMM_IO_TYPE_INS            = 0x3
SMM_IO_TYPE_OUTS           = 0x2
SMM_IO_TYPE_REP_INS        = 0x7
SMM_IO_TYPE_REP_OUTS       = 0x6

class SMRAM_SAVE_STATE_IOMISC_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SmiFlag",     UINT32, 1),
    ("Length",      UINT32, 3),
    ("Type",        UINT32, 4),
    ("Reserved1",   UINT32, 8),
    ("Port",        UINT32, 16)
  ]

class SMRAM_SAVE_STATE_IOMISC (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    SMRAM_SAVE_STATE_IOMISC_Bits),
    ("Uint32",  UINT32)
  ]

