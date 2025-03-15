# CpuIdBasic.py
#
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.Register.Intel.Cpuid as CpuidRegs
from EfiPy2.Lib import CpuIdIntel as CpuId
from EfiPy2.Lib.X86Processor import Me

CpuIdReg  = CpuId.CPUID_GENERIC_REGISTERs()

Me.CpuId (0x00, 0x00, CpuIdReg)

print (f'''
CPU signature From cpuid instruction
============================================
  EAX = 0x{CpuIdReg.EAX:08X}
  EBX = 0x{CpuIdReg.EBX:08X}
  ECX = 0x{CpuIdReg.ECX:08X}
  EDX = 0x{CpuIdReg.EDX:08X}
''')

print (f'''
CPU signature from pre-defined constant
============================================
  EBX = 0x{CpuidRegs.CPUID_SIGNATURE_GENUINE_INTEL_EBX:08X}
  ECX = 0x{CpuidRegs.CPUID_SIGNATURE_GENUINE_INTEL_ECX:08X}
  EDX = 0x{CpuidRegs.CPUID_SIGNATURE_GENUINE_INTEL_EDX:08X}
''')

CpuIdReg  = CpuId.CPUID_VERSION_INFO_REGISTERs()

Me.CpuId (CpuidRegs.CPUID_VERSION_INFO, 0x00, CpuIdReg)

print (f'''
CPU version information in UINT32 format
============================================
  EAX = 0x{CpuIdReg.EAX.Uint32:08X}
  EBX = 0x{CpuIdReg.EBX.Uint32:08X}
  ECX = 0x{CpuIdReg.ECX.Uint32:08X}
  EDX = 0x{CpuIdReg.EDX.Uint32:08X}
''')

print (f'''
CPU version information in bit field format
============================================
  CpuIdReg.EAX.Bits.SteppingId:           {CpuIdReg.EAX.Bits.SteppingId}
  CpuIdReg.EAX.Bits.Model:                {CpuIdReg.EAX.Bits.Model}
  CpuIdReg.EAX.Bits.FamilyId:             {CpuIdReg.EAX.Bits.FamilyId}
  CpuIdReg.EAX.Bits.ProcessorType:        {CpuIdReg.EAX.Bits.ProcessorType}
  CpuIdReg.EAX.Bits.Reserved1:            {CpuIdReg.EAX.Bits.Reserved1}
  CpuIdReg.EAX.Bits.ExtendedModelId:      {CpuIdReg.EAX.Bits.ExtendedModelId}
  CpuIdReg.EAX.Bits.ExtendedFamilyId:     {CpuIdReg.EAX.Bits.ExtendedFamilyId}
  CpuIdReg.EAX.Bits.Reserved2:            {CpuIdReg.EAX.Bits.Reserved2}

  CpuIdReg.EBX.Bits.BrandIndex:           {CpuIdReg.EBX.Bits.BrandIndex}
  CpuIdReg.EBX.Bits.CacheLineSize:        {CpuIdReg.EBX.Bits.CacheLineSize}
  CpuIdReg.EBX.Bits.MaximumAddressableIdsForLogicalProcessors: {CpuIdReg.EBX.Bits.MaximumAddressableIdsForLogicalProcessors}
  CpuIdReg.EBX.Bits.InitialLocalApicId:   {CpuIdReg.EBX.Bits.InitialLocalApicId}

  CpuIdReg.ECX.Bits.SSE3:                 {CpuIdReg.ECX.Bits.SSE3}
  CpuIdReg.ECX.Bits.PCLMULQDQ:            {CpuIdReg.ECX.Bits.PCLMULQDQ}
  CpuIdReg.ECX.Bits.DTES64:               {CpuIdReg.ECX.Bits.DTES64}
  CpuIdReg.ECX.Bits.MONITOR:              {CpuIdReg.ECX.Bits.MONITOR}
  CpuIdReg.ECX.Bits.DS_CPL:               {CpuIdReg.ECX.Bits.DS_CPL}
  CpuIdReg.ECX.Bits.VMX:                  {CpuIdReg.ECX.Bits.VMX}
  CpuIdReg.ECX.Bits.SMX:                  {CpuIdReg.ECX.Bits.SMX}
  CpuIdReg.ECX.Bits.EIST:                 {CpuIdReg.ECX.Bits.EIST}
  CpuIdReg.ECX.Bits.TM2:                  {CpuIdReg.ECX.Bits.TM2}
  CpuIdReg.ECX.Bits.SSSE3:                {CpuIdReg.ECX.Bits.SSSE3}
  CpuIdReg.ECX.Bits.CNXT_ID:              {CpuIdReg.ECX.Bits.CNXT_ID}
  CpuIdReg.ECX.Bits.FMA:                  {CpuIdReg.ECX.Bits.FMA}
  CpuIdReg.ECX.Bits.CMPXCHG16B:           {CpuIdReg.ECX.Bits.CMPXCHG16B}
  CpuIdReg.ECX.Bits.xTPR_Update_Control:  {CpuIdReg.ECX.Bits.xTPR_Update_Control}
  CpuIdReg.ECX.Bits.PDCM:                 {CpuIdReg.ECX.Bits.PDCM}
  CpuIdReg.ECX.Bits.Reserved:             {CpuIdReg.ECX.Bits.Reserved}
  CpuIdReg.ECX.Bits.PCID:                 {CpuIdReg.ECX.Bits.PCID}
  CpuIdReg.ECX.Bits.DCA:                  {CpuIdReg.ECX.Bits.DCA}
  CpuIdReg.ECX.Bits.SSE4_1:               {CpuIdReg.ECX.Bits.SSE4_1}
  CpuIdReg.ECX.Bits.SSE4_2:               {CpuIdReg.ECX.Bits.SSE4_2}
  CpuIdReg.ECX.Bits.x2APIC:               {CpuIdReg.ECX.Bits.x2APIC}
  CpuIdReg.ECX.Bits.MOVBE:                {CpuIdReg.ECX.Bits.MOVBE}
  CpuIdReg.ECX.Bits.POPCNT:               {CpuIdReg.ECX.Bits.POPCNT}
  CpuIdReg.ECX.Bits.TSC_Deadline:         {CpuIdReg.ECX.Bits.TSC_Deadline}
  CpuIdReg.ECX.Bits.AESNI:                {CpuIdReg.ECX.Bits.AESNI}
  CpuIdReg.ECX.Bits.XSAVE:                {CpuIdReg.ECX.Bits.XSAVE}
  CpuIdReg.ECX.Bits.OSXSAVE:              {CpuIdReg.ECX.Bits.OSXSAVE}
  CpuIdReg.ECX.Bits.AVX:                  {CpuIdReg.ECX.Bits.AVX}
  CpuIdReg.ECX.Bits.F16C:                 {CpuIdReg.ECX.Bits.F16C}
  CpuIdReg.ECX.Bits.RDRAND:               {CpuIdReg.ECX.Bits.RDRAND}
  CpuIdReg.ECX.Bits.ParaVirtualized:      {CpuIdReg.ECX.Bits.ParaVirtualized}

  CpuIdReg.EDX.Bits.FPU:                  {CpuIdReg.EDX.Bits.FPU}
  CpuIdReg.EDX.Bits.VME:                  {CpuIdReg.EDX.Bits.VME}
  CpuIdReg.EDX.Bits.DE:                   {CpuIdReg.EDX.Bits.DE}
  CpuIdReg.EDX.Bits.PSE:                  {CpuIdReg.EDX.Bits.PSE}
  CpuIdReg.EDX.Bits.TSC:                  {CpuIdReg.EDX.Bits.TSC}
  CpuIdReg.EDX.Bits.MSR:                  {CpuIdReg.EDX.Bits.MSR}
  CpuIdReg.EDX.Bits.PAE:                  {CpuIdReg.EDX.Bits.PAE}
  CpuIdReg.EDX.Bits.MCE:                  {CpuIdReg.EDX.Bits.MCE}
  CpuIdReg.EDX.Bits.CX8:                  {CpuIdReg.EDX.Bits.CX8}
  CpuIdReg.EDX.Bits.APIC:                 {CpuIdReg.EDX.Bits.APIC}
  CpuIdReg.EDX.Bits.Reserved1:            {CpuIdReg.EDX.Bits.Reserved1}
  CpuIdReg.EDX.Bits.SEP:                  {CpuIdReg.EDX.Bits.SEP}
  CpuIdReg.EDX.Bits.MTRR:                 {CpuIdReg.EDX.Bits.MTRR}
  CpuIdReg.EDX.Bits.PGE:                  {CpuIdReg.EDX.Bits.PGE}
  CpuIdReg.EDX.Bits.MCA:                  {CpuIdReg.EDX.Bits.MCA}
  CpuIdReg.EDX.Bits.CMOV:                 {CpuIdReg.EDX.Bits.CMOV}
  CpuIdReg.EDX.Bits.PAT:                  {CpuIdReg.EDX.Bits.PAT}
  CpuIdReg.EDX.Bits.PSE_36:               {CpuIdReg.EDX.Bits.PSE_36}
  CpuIdReg.EDX.Bits.PSN:                  {CpuIdReg.EDX.Bits.PSN}
  CpuIdReg.EDX.Bits.CLFSH:                {CpuIdReg.EDX.Bits.CLFSH}
  CpuIdReg.EDX.Bits.Reserved2:            {CpuIdReg.EDX.Bits.Reserved2}
  CpuIdReg.EDX.Bits.DS:                   {CpuIdReg.EDX.Bits.DS}
  CpuIdReg.EDX.Bits.ACPI:                 {CpuIdReg.EDX.Bits.ACPI}
  CpuIdReg.EDX.Bits.MMX:                  {CpuIdReg.EDX.Bits.MMX}
  CpuIdReg.EDX.Bits.FXSR:                 {CpuIdReg.EDX.Bits.FXSR}
  CpuIdReg.EDX.Bits.SSE:                  {CpuIdReg.EDX.Bits.SSE}
  CpuIdReg.EDX.Bits.SSE2:                 {CpuIdReg.EDX.Bits.SSE2}
  CpuIdReg.EDX.Bits.SS:                   {CpuIdReg.EDX.Bits.SS}
  CpuIdReg.EDX.Bits.HTT:                  {CpuIdReg.EDX.Bits.HTT}
  CpuIdReg.EDX.Bits.TM:                   {CpuIdReg.EDX.Bits.TM}
  CpuIdReg.EDX.Bits.Reserved3:            {CpuIdReg.EDX.Bits.Reserved3}
  CpuIdReg.EDX.Bits.PBE:                  {CpuIdReg.EDX.Bits.PBE}
''')
