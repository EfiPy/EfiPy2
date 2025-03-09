from EfiPy2.Lib.X86Processor import X86Processors, X86ProcessorArray
from EfiPy2.Lib.CpuId import CPUID_GENERIC_REGISTERs
from EfiPy2.Lib.Msr import MSR_GENERIC_REGISTER
from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_APIC_BASE_REGISTER

print (f'APIC base address: 0x{X86Processors .LocalApicAddress:08X}')
print (f'Processor IDs from EFI_MP_SERVICES_PROTOCOL: {X86Processors .ProcessorIds}')
print (f'Me (WhAmI): {X86Processors .Me}, Processor numbers: {len (X86Processors )}, {len (X86ProcessorArray)}')

# X86ProcessorArray = []
# for Index in range (len (X86Processors )):
for Index, Processor in enumerate (X86ProcessorArray):

  print (f'\nCPU {Index} infromation....')

  # Processor = X86Processors  (Index)
  # X86ProcessorArray.append (Processor)
  MmioAddress = 0xFEE00020
  print (f'  From MMIO 0x{MmioAddress:08X}: 0x{Processor.MemGet32(MmioAddress):08X}')

  CpuIndex = 0x0B

  CpuIdReg = CPUID_GENERIC_REGISTERs()
  Processor.CpuId (CpuIndex, 0x00, CpuIdReg)
  print (f'  From CPUID 0x{CpuIndex:02X}: 0x{CpuIdReg.EDX:08X}')

  MsrIndex = 0x1B
  MsrReg = MSR_IA32_APIC_BASE_REGISTER ()
  Processor.RdMsr (MsrIndex, MsrReg)

  if MsrReg.Bits.EXTD != 0x01:
    MsrReg.Bits.EXTD = 1
    Processor.WrMsr (MsrIndex, MsrReg)

    MsrReg = MSR_IA32_APIC_BASE_REGISTER ()
    Processor.RdMsr (MsrIndex, MsrReg)

  MsrIndex = 0x802
  MsrReg = MSR_GENERIC_REGISTER ()
  Processor.RdMsr (MsrIndex, MsrReg)
  print (f'  From MSR 0x{MsrIndex:X}: 0x{MsrReg.Uint64:016X}')