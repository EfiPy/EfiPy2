#
# CpuId.py
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# CpuId.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# CpuId.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

#
# Instruction CPUID sample
#

#
# typedef struct {
#   UINT32 EAX;
#   UINT32 EBX;
#   UINT32 ECX;
#   UINT32 EDX;
# } CpuIdStructure
#
class CpuIdStructure (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('EAX',  EfiPy.UINT32),
    ('EBX',  EfiPy.UINT32),
    ('ECX',  EfiPy.UINT32),
    ('EDX',  EfiPy.UINT32)
  ]

#
# typedef union {
#   CpuIdStructure CpuInfo;
# } CpuIdUnion
#
class CpuIdUnion (EfiPy.Union):

  _pack_   = 1
  _fields_ = [
    ('CpuInfo',  CpuIdStructure)
  ]

#
# EAX = 0x01
#
class CpuIdEax01 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('VersionInformation',  EfiPy.UINT32),
    ('BrandIndex',          EfiPy.UINT32, 8),
    ('CLFlushLineSize',     EfiPy.UINT32, 8),
    ('MaxAddrIDs',          EfiPy.UINT32, 8),
    ('ApicId',              EfiPy.UINT32, 8),
    ('FeatureInformation1', EfiPy.UINT32),
    ('FeatureInformation2', EfiPy.UINT32),
  ]

#
# EAX = 0x02
#
class CpuIdEax02 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('CacheTlbInfo1',  EfiPy.UINT32),
    ('CacheTlbInfo2',  EfiPy.UINT32),
    ('CacheTlbInfo3',  EfiPy.UINT32),
    ('CacheTlbInfo4',  EfiPy.UINT32),
  ]

#
# EAX = 0x03
#
class CpuIdEax03 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('Reserved1',       EfiPy.UINT32),
    ('Reserved2',       EfiPy.UINT32),
    ('SerialNumberL',   EfiPy.UINT32),
    ('SerialNumberH',   EfiPy.UINT32)
  ]

#
# EAX = 0x04
#
class CpuIdEax04 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('CacheType',                     EfiPy.UINT32, 5),
    ('CacheLevel',                    EfiPy.UINT32, 3),
    ('SelfInitializingCacheLevel',    EfiPy.UINT32, 1),
    ('FullyAssociativeCache',         EfiPy.UINT32, 1),
    ('Reserved1',                     EfiPy.UINT32, 4),
    ('MaxAddrIdsLpShareCache',        EfiPy.UINT32, 12),
    ('MaxAddrIdsPp',                  EfiPy.UINT32, 6),
    ('SystemCoherencyLineSize',       EfiPy.UINT32, 12),
    ('PhysicalLinePartitions',        EfiPy.UINT32, 10),
    ('WaysOfAssociativity',           EfiPy.UINT32, 10),
    ('NumberOfSets',                  EfiPy.UINT32, 32),
    ('WBINVD',                        EfiPy.UINT32, 1),
    ('CacheInclusiveness',            EfiPy.UINT32, 1),
    ('Reserved',                      EfiPy.UINT32, 30),
  ]

#
# EAX = 0x05
#
class CpuIdEax05 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('SmallestMonitor',               EfiPy.UINT32, 16),
    ('Reserved1',                     EfiPy.UINT32, 16),
    ('LargestMonitor',                EfiPy.UINT32, 16),
    ('Reserved2',                     EfiPy.UINT32, 16),
    ('MonitorMwaitExtensions',        EfiPy.UINT32,  1),
    ('TreatingInterrupts',            EfiPy.UINT32,  1),
    ('Reserved3',                     EfiPy.UINT32, 30),
    ('NumberOfC0',                    EfiPy.UINT32,  4),
    ('NumberOfC1',                    EfiPy.UINT32,  4),
    ('NumberOfC2',                    EfiPy.UINT32,  4),
    ('NumberOfC3',                    EfiPy.UINT32,  4),
    ('NumberOfC3',                    EfiPy.UINT32,  4),
    ('Reserved3',                     EfiPy.UINT32, 12),
  ]

#
# EAX = 0x06
#
class CpuIdEax06 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('DigitalTemperatureSensor',                          EfiPy.UINT32, 1),
    ('IntelTurboBoostTechnologyAvailable',                EfiPy.UINT32, 1),
    ('ARAT',                                              EfiPy.UINT32, 1),
    ('Reserved1',                                         EfiPy.UINT32, 29),
    ('NumberOfInterruptThresholdsInDigitalThermalSensor', EfiPy.UINT32, 4),
    ('Reserved2',                                         EfiPy.UINT32, 28),
    ('HardwareCoordinationFeedbackCapability',            EfiPy.UINT32, 1),
    ('Reserved3',                                         EfiPy.UINT32, 31),
    ('Reserved4',                                         EfiPy.UINT32)
  ]

#
# EAX = 0x09
#
class CpuIdEax09 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('ValueOfIA32_PLATFORM_DCA_CAP_MSR',                  EfiPy.UINT32),
    ('Reserved1',                                         EfiPy.UINT32),
    ('Reserved2',                                         EfiPy.UINT32),
    ('Reserved3',                                         EfiPy.UINT32),
  ]

#
# EAX = 0x0A
#
class CpuIdEax0A (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('VersionIdOfarchiPm',                      EfiPy.UINT32, 8),
    ('NofGpPerformanceMonitoringCounterPerLp',  EfiPy.UINT32, 8),
    ('BitWidthMonitorCounter',                  EfiPy.UINT32, 8),
    ('LengthOfEbxBitVector',                    EfiPy.UINT32, 8),
    ('CoreCycleEvent',                          EfiPy.UINT32, 1),
    ('InstructionRetiredEvent',                 EfiPy.UINT32, 1),
    ('ReferenceCyclesEvent',                    EfiPy.UINT32, 1),
    ('LastLevelCacheReferenceEvent',            EfiPy.UINT32, 1),
    ('LastLevelCacheMissesEvent',               EfiPy.UINT32, 1),
    ('BranchInstructionRetiredEvent',           EfiPy.UINT32, 1),
    ('BranchMispredictRetiredEvent',            EfiPy.UINT32, 1),
    ('Reserved1',                               EfiPy.UINT32, 25),
    ('Reserved2',                               EfiPy.UINT32),
    ('NumberOfFixedFunctionPerformanceCounters',    EfiPy.UINT32, 5),
    ('BitWidthOfFixedFunctionPerformanceCounters',  EfiPy.UINT32, 8),
    ('Reserved3',                                   EfiPy.UINT32, 19),
  ]

#
# EAX = 0x0B
#
class CpuIdEax0B (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('NumberOfBitsToShiftRightOnx2APIC',  EfiPy.UINT32, 5),
    ('Reserved1',                         EfiPy.UINT32, 27),
    ('NumberOfLogicalProcessors',         EfiPy.UINT32, 16),
    ('Reserved2',                         EfiPy.UINT32, 16),
    ('LevelNumber',                       EfiPy.UINT32, 8),
    ('LevelType',                         EfiPy.UINT32, 8),
    ('Reserved3',                         EfiPy.UINT32, 16),
    ('x2ApicId',                          EfiPy.UINT32),
  ]

#
# EAX = 0x80000000
#
class CpuIdEax8x00 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('MaximumInputExtendedFunctionCPUIDInformation',  EfiPy.UINT32),
    ('Reserved1',                         EfiPy.UINT32),
    ('Reserved2',                         EfiPy.UINT32),
    ('Reserved3',                         EfiPy.UINT32),
  ]

#
# EAX = 0x80000001
#
class CpuIdEax8x01 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('ExtendedProcessorSignatureAndFeatureBits',  EfiPy.UINT32),
    ('Reserved1',                                 EfiPy.UINT32),
    ('LahfSahfAvailableIn64bitMode',              EfiPy.UINT32, 1),
    ('Reserved2',                                 EfiPy.UINT32, 31),
    ('Reserved3',                                 EfiPy.UINT32, 11),
    ('SyscallSysretAvailable',                    EfiPy.UINT32, 1),
    ('Reserved4',                                 EfiPy.UINT32, 8),
    ('ExecuteDisableBitAvailable',                EfiPy.UINT32, 1),
    ('Reserved5',                                 EfiPy.UINT32, 6),
    ('RdtscpAndIA32_TSC_AUX',                     EfiPy.UINT32, 1),
    ('Reserved6',                                 EfiPy.UINT32, 1),
    ('Ia64Available',                             EfiPy.UINT32, 1),
    ('Reserved7',                                 EfiPy.UINT32, 2),
  ]

#
# EAX = 0x80000002
#
class CpuIdEax8x02 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('ProcessorBrandString0',  EfiPy.UINT32),
    ('ProcessorBrandString1',  EfiPy.UINT32),
    ('ProcessorBrandString2',  EfiPy.UINT32),
    ('ProcessorBrandString3',  EfiPy.UINT32),
  ]

#
# EAX = 0x80000003
#
class CpuIdEax8x03 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('ProcessorBrandString4',  EfiPy.UINT32),
    ('ProcessorBrandString5',  EfiPy.UINT32),
    ('ProcessorBrandString6',  EfiPy.UINT32),
    ('ProcessorBrandString7',  EfiPy.UINT32),
  ]

#
# EAX = 0x80000004
#
class CpuIdEax8x04 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('ProcessorBrandString8',   EfiPy.UINT32),
    ('ProcessorBrandString9',   EfiPy.UINT32),
    ('ProcessorBrandString10',  EfiPy.UINT32),
    ('ProcessorBrandString11',  EfiPy.UINT32),
  ]

#
# EAX = 0x80000005
#
class CpuIdEax8x05 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('Reserved0',   EfiPy.UINT32),
    ('Reserved1',   EfiPy.UINT32),
    ('Reserved2',   EfiPy.UINT32),
    ('Reserved3',   EfiPy.UINT32),
  ]

#
# EAX = 0x80000006
#
class CpuIdEax8x06 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('Reserved0',             EfiPy.UINT32),
    ('Reserved1',             EfiPy.UINT32),
    ('CacheLineSize',         EfiPy.UINT32, 8),
    ('Reserved2',             EfiPy.UINT32, 4),
    ('L2AssociativityField',  EfiPy.UINT32, 4),
    ('CacheSizeIn1KUnits',    EfiPy.UINT32, 16),
    ('Reserved3',             EfiPy.UINT32),
  ]

#
# EAX = 0x80000007
#
class CpuIdEax8x07 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('Reserved0',             EfiPy.UINT32),
    ('Reserved1',             EfiPy.UINT32),
    ('Reserved2',             EfiPy.UINT32),
    ('Reserved3',             EfiPy.UINT32, 8),
    ('InvariantTscAvailable', EfiPy.UINT32, 1),
    ('Reserved4',             EfiPy.UINT32, 23),
  ]

#
# EAX = 0x80000008
#
class CpuIdEax8x08 (EfiPy.Structure):

  _pack_   = 1
  _fields_ = [
    ('PhysicalAddressBits',   EfiPy.UINT32, 8),
    ('VirtualAddressBits',    EfiPy.UINT32, 8),
    ('Reserved0',             EfiPy.UINT32, 16),
    ('Reserved1',             EfiPy.UINT32),
    ('Reserved2',             EfiPy.UINT32),
    ('Reserved3',             EfiPy.UINT32),
  ]

class CpuId:

  def __init__ (self):

    import corepy.lib.printer as printer
    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.platform as env
    import corepy.arch.x86_64.lib.memory as mem

    self.code   = env.InstructionStream()
    self.proc   = env.Processor()
    self.params = env.ExecParams()

    self.code.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 16)))  # parameter 1
    self.code.add(x86.mov(reg.rcx, mem.MemRef(reg.rbp, 24)))  # parameter 2
    self.code.add(x86.mov(reg.rdi, mem.MemRef(reg.rbp, 32)))  # parameter 3

    self.code.add(x86.push(reg.rax))                          # save input parameter

    self.code.add(x86.cpuid())

    self.code.add(x86.mov(mem.MemRef(reg.edi,  0, data_size = 32), reg.eax))
    self.code.add(x86.mov(mem.MemRef(reg.edi,  4, data_size = 32), reg.ebx))
    self.code.add(x86.mov(mem.MemRef(reg.edi,  8, data_size = 32), reg.ecx))
    self.code.add(x86.mov(mem.MemRef(reg.edi, 12, data_size = 32), reg.edx))

    self.code.add(x86.pop(reg.rax))                           # restore input parameter as return value

  #
  # UINT32 GetId (UINT32 eax, UINT32 ecx, CpuIdUnion *CpuInfoAddr);
  #
  def GetId (self, eax, ecx, CpuInfoAddr):

    self.params.p1 = eax
    self.params.p2 = ecx
    self.params.p3 = CpuInfoAddr
    return self.proc.execute(self.code, params = self.params, mode = 'int')

if __name__ == '__main__':

  cpu  = CpuId()
  CpuInfo = CpuIdUnion()

  Ieax = {0x00000000: (0x00, None),
          0x00000001: (0x00, CpuIdEax01),
          0x00000002: (0x00, CpuIdEax02),
          0x00000003: (0x00, CpuIdEax03),
          0x00000004: (0x00, CpuIdEax04),
          0x00000005: (0x00, CpuIdEax05),
          0x00000006: (0x00, CpuIdEax06),
          0x00000009: (0x00, CpuIdEax09),
          0x0000000A: (0x00, CpuIdEax0A),
          0x0000000B: (0x00, CpuIdEax0B),
          0x0000000D: (0x00, None),
          0x80000000: (0x00, CpuIdEax8x00),
          0x80000001: (0x00, CpuIdEax8x01),
          0x80000002: (0x00, CpuIdEax8x02),
          0x80000003: (0x00, CpuIdEax8x03),
          0x80000004: (0x00, CpuIdEax8x04),
          0x80000005: (0x00, CpuIdEax8x05),
          0x80000006: (0x00, CpuIdEax8x06),
          0x80000007: (0x00, CpuIdEax8x07),
          0x80000008: (0x00, CpuIdEax8x08)
         }


  for eax in sorted(Ieax):

    if Ieax[eax][1] == None:
      CpuInfoAddr = EfiPy.addressof (CpuInfo)
      cpuI = CpuInfo
    else:
      class CpuIdEaxU (EfiPy.Union):
        _pack_   = 1
        _fields_ = [
          ('CpuInfo',  CpuIdStructure),
          ('CpuField', Ieax[eax][1])
        ]

      # cpuI = Ieax[eax][1]()
      cpuI = CpuIdEaxU()
      CpuInfoAddr = EfiPy.addressof (cpuI)

    rax = cpu.GetId(eax, Ieax[eax][0], CpuInfoAddr)

    print ("============================================")
    print ("   Input      EAX      EBX      ECX      EDX")
    print ("%08X %08X %08X %08X %08X" % (rax,
                                         cpuI.CpuInfo.EAX,
                                         cpuI.CpuInfo.EBX,
                                         cpuI.CpuInfo.ECX,
                                         cpuI.CpuInfo.EDX))

    print ()

    if Ieax[eax][1] != None:
      for field in cpuI._fields_[1][1]._fields_:
        print (" %30s" % field[0], ": 0x%08X" % getattr(cpuI.CpuField, field[0]))

    print ()

