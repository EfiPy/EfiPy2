# StructDumpSample.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib.StructDump import DumpStruct

class MSR_IA32_APIC_BASE_REGISTER_Bits (EfiPy.Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   EfiPy.UINT32, 8),
    ("BSP",         EfiPy.UINT32, 1),
    ("Reserved2",   EfiPy.UINT32, 1),
    ("EXTD",        EfiPy.UINT32, 1),
    ("EN",          EfiPy.UINT32, 1),
    ("ApicBase",    EfiPy.UINT32, 20),
    ("ApicBaseHi",  EfiPy.UINT32, 32)
  ]

class MSR_IA32_APIC_BASE_REGISTER (EfiPy.Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_APIC_BASE_REGISTER_Bits),
    ("Uint64",  EfiPy.UINT64)
  ]

class InnerStructure (EfiPy.Structure):
    _fields_ = [
        ("Inner0",      EfiPy.UINT32),
        ("Inner1",      EfiPy.UINT8 * 0x16),
    ]

class InnerArray (EfiPy.Structure):
    _fields_ = [
        ("Array0",      EfiPy.UINT32),
        ("Array1",      EfiPy.UINT8 * 0x16),
    ]

class SampleStructure (EfiPy.Structure):
    _fields_ = [
        ("Revision",    EfiPy.UINT64),
        ("Media",       EfiPy.POINTER(EfiPy.UINT32)),
        ("Reset",       EfiPy.UINT32),
        ("FieldStruct", InnerStructure),
        ("FieldArray",  InnerArray * 3),
        ("ReadBlocks",  EfiPy.UINT32),
        ("MsrReg",      MSR_IA32_APIC_BASE_REGISTER),
        ("WriteBlocks", EfiPy.UINT32),
        ("RawData0",    EfiPy.UINT8 * 0x24),
        ("RawData1",    EfiPy.UINT16 * 3),
        ("FlushBlocks", EfiPy.UINT32),
    ]

SampleObject = SampleStructure ()

DumpStruct (2, SampleObject, SampleStructure)