# Microcode.py
#
# EfiPy2.MdePkg.Register.Intel.Microcode
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class CPU_MICROCODE_DATE_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Year",    UINT32, 16),
    ("Day",     UINT32, 8),
    ("Month",   UINT32, 8)
  ]

class CPU_MICROCODE_DATE (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPU_MICROCODE_DATE_Bits),
    ("Uint32",  UINT32)
  ]

class CPU_MICROCODE_PROCESSOR_SIGNATURE_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Stepping",        UINT32, 4),
    ("Model",           UINT32, 4),
    ("Family",          UINT32, 4),
    ("Type",            UINT32, 2),
    ("Reserved1",       UINT32, 2),
    ("ExtendedModel",   UINT32, 4),
    ("ExtendedFamily",  UINT32, 8),
    ("Reserved2",       UINT32, 4)
  ]

class CPU_MICROCODE_PROCESSOR_SIGNATURE (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    CPU_MICROCODE_PROCESSOR_SIGNATURE_Bits),
    ("Uint32",  UINT32)
  ]

class CPU_MICROCODE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("HeaderVersion",       UINT32),
    ("UpdateRevision",      UINT32),
    ("Date",                CPU_MICROCODE_DATE),
    ("ProcessorSignature",  CPU_MICROCODE_PROCESSOR_SIGNATURE),
    ("Checksum",            UINT32),
    ("LoaderRevision",      UINT32),
    ("ProcessorFlags",      UINT32),
    ("DataSize",            UINT32),
    ("TotalSize",           UINT32),
    ("Reserved",            UINT8 * 12)
  ]

class CPU_MICROCODE_EXTENDED_TABLE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtendedSignatureCount",  UINT32),
    ("ExtendedChecksum",        UINT32),
    ("Reserved",                UINT8 * 12)
  ]

class CPU_MICROCODE_EXTENDED_TABLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("ProcessorSignature",  CPU_MICROCODE_PROCESSOR_SIGNATURE),
    ("ProcessorFlag",       UINT32),
    ("Checksum",            UINT32)
  ]

