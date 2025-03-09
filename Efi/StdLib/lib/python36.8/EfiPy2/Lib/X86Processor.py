import EfiPy2 as EfiPy
import corepy.arch.x86_64.isa as x86
import corepy.arch.x86_64.types.registers as reg
import corepy.arch.x86_64.platform as env
import corepy.arch.x86_64.lib.memory as mem
from EfiPy2.MdePkg.Protocol.MpService import EFI_AP_PROCEDURE 

class X86ProcessorClass (type):

  def _GetLocalApicAddress (cls):

    ApicSignature = b'APIC'

    from EfiPy2.Lib.Acpi.AcpiApicParser import AcpiApicParser
    from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable

    ApicRaw = ExtractTable (ApicSignature, 0)
    ApicObj, ApicType = AcpiApicParser (ApicRaw)
    cls._LocalApicAddress = ApicObj.LocalApicAddress

  def _BuildMsrProcedure (cls):

    #
    # Function: RdMSR
    #
    # Input: UINT32 * 2
    #        Saved in rdx
    #           UINT32[0]:  ECX
    #           UINT32[1]:  Pointer to structure EAX, EDX
    #
    cls._RdMsrCoreCode  = env.InstructionStream()

    cls._RdMsrCoreCode.add(x86.push(reg.rdi))
    cls._RdMsrCoreCode.add(x86.push(reg.rsi))

    cls._RdMsrCoreCode.add(x86.mov(reg.edi, mem.MemRef(reg.rbp, 0x10, data_size = 32)))  # addressod((UINT32 * 2) ())

    cls._RdMsrCoreCode.add(x86.mov(reg.esi, mem.MemRef(reg.edi, 0x04, data_size = 32)))  # parameter UINT32[1]
    cls._RdMsrCoreCode.add(x86.mov(reg.ecx, mem.MemRef(reg.edi, 0x00, data_size = 32)))  # parameter UINT32[0]

    cls._RdMsrCoreCode.add(x86.rdmsr())

    cls._RdMsrCoreCode.add(x86.mov(mem.MemRef(reg.esi, 0, data_size = 32), reg.eax))
    cls._RdMsrCoreCode.add(x86.mov(mem.MemRef(reg.esi, 4, data_size = 32), reg.edx))

    cls._RdMsrCoreCode.add(x86.pop(reg.rsi))
    cls._RdMsrCoreCode.add(x86.pop(reg.rdi))

    cls._RdMsrCoreAddr, cls._RdMsrCoreBytes = cls._RdMsrCoreCode.get_code_bytes ()

    cls._RdMsrCoreFunc = EFI_AP_PROCEDURE (cls._RdMsrCoreAddr)

    #
    # Function: WrMSR
    #
    # Input: UINT32 * 2
    #        Saved in rdx
    #           UINT32[0]:  ECX
    #           UINT32[1]:  Pointer to structure EAX, EDX
    #
    cls._WrMsrCoreCode  = env.InstructionStream()

    cls._WrMsrCoreCode.add(x86.push(reg.rdi))
    cls._WrMsrCoreCode.add(x86.push(reg.rsi))

    cls._WrMsrCoreCode.add(x86.mov(reg.edi, mem.MemRef(reg.rbp, 0x10, data_size = 32)))  # addressod((UINT32 * 2) ())

    cls._WrMsrCoreCode.add(x86.mov(reg.ecx, mem.MemRef(reg.edi, 0x00, data_size = 32)))  # parameter UINT32[0]
    cls._WrMsrCoreCode.add(x86.mov(reg.esi, mem.MemRef(reg.edi, 0x04, data_size = 32)))  # parameter UINT32[1]

    cls._WrMsrCoreCode.add(x86.mov(reg.eax, mem.MemRef(reg.esi, 0, data_size = 32)))
    cls._WrMsrCoreCode.add(x86.mov(reg.edx, mem.MemRef(reg.esi, 4, data_size = 32)))

    cls._WrMsrCoreCode.add(x86.wrmsr())

    cls._WrMsrCoreCode.add(x86.pop(reg.rsi))
    cls._WrMsrCoreCode.add(x86.pop(reg.rdi))

    cls._WrMsrCoreAddr, cls._WrMsrCoreBytes = cls._WrMsrCoreCode.get_code_bytes ()

    cls._WrMsrCoreFunc = EFI_AP_PROCEDURE (cls._WrMsrCoreAddr)

  def _BuildCpuIdProcedure (cls):

    #
    # Function: CPUID
    #
    # Input: UINT32 * 3
    #        Saved in rdx
    #           UINT32[0]:  EAX
    #           UINT32[1]:  ECX
    #           UINT32[2]:  Pointer to return structure EAX, EBX, ECX, EDX
    #
    cls._CpuIdCoreCode  = env.InstructionStream()

    cls._CpuIdCoreCode.add(x86.push(reg.rdi))
    cls._CpuIdCoreCode.add(x86.push(reg.rsi))
    cls._CpuIdCoreCode.add(x86.push(reg.rbx))

    cls._CpuIdCoreCode.add(x86.mov(reg.edi, mem.MemRef(reg.rbp, 0x10, data_size = 32)))  # addressod((UINT32 * 3) ())

    cls._CpuIdCoreCode.add(x86.mov(reg.eax, mem.MemRef(reg.edi, 0x00, data_size = 32)))  # parameter UINT32[0]
    cls._CpuIdCoreCode.add(x86.mov(reg.ecx, mem.MemRef(reg.edi, 0x04, data_size = 32)))  # parameter UINT32[1]
    cls._CpuIdCoreCode.add(x86.mov(reg.esi, mem.MemRef(reg.edi, 0x08, data_size = 32)))  # parameter UINT32[2]

    cls._CpuIdCoreCode.add(x86.cpuid())

    cls._CpuIdCoreCode.add(x86.mov(mem.MemRef(reg.esi, 0, data_size = 32), reg.eax))
    cls._CpuIdCoreCode.add(x86.mov(mem.MemRef(reg.esi, 4, data_size = 32), reg.ebx))
    cls._CpuIdCoreCode.add(x86.mov(mem.MemRef(reg.esi, 8, data_size = 32), reg.ecx))
    cls._CpuIdCoreCode.add(x86.mov(mem.MemRef(reg.esi,12, data_size = 32), reg.edx))

    cls._CpuIdCoreCode.add(x86.pop(reg.rbx))
    cls._CpuIdCoreCode.add(x86.pop(reg.rsi))
    cls._CpuIdCoreCode.add(x86.pop(reg.rdi))

    cls._CpuIdCoreAddr, cls._CpuIdCoreBytes = cls._CpuIdCoreCode.get_code_bytes ()

    cls._CpuIdCoreFunc = EFI_AP_PROCEDURE (cls._CpuIdCoreAddr)

  def _BuildMemProcedure (cls):

    #
    # Function: MemGet32
    #
    # Input: UINT32 * 2
    #        Saved in rdx
    #           UINT32[0]:  Address
    #           UINT32[1]:  Value
    #
    cls._MemGet32CoreCode   = env.InstructionStream()

    cls._MemGet32CoreCode.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 0x10)))
    cls._MemGet32CoreCode.add(x86.mov(reg.ecx, mem.MemRef(reg.rdx, 0, data_size = 32)))     # rdx[0]: Address, rdx[4]: Return Value
    cls._MemGet32CoreCode.add(x86.mov(reg.eax, mem.MemRef(reg.ecx, 0, data_size = 32)))
    cls._MemGet32CoreCode.add(x86.mov(mem.MemRef(reg.rdx, 4, data_size = 32), reg.eax))

    cls._MemGet32CoreAddr, cls._MemGet32CoreBytes = cls._MemGet32CoreCode.get_code_bytes ()

    cls._MemGet32CoreFunc = EFI_AP_PROCEDURE (cls._MemGet32CoreAddr)

    #
    # Function: MemSet32
    #
    # Input: UINT32 * 2
    #        Saved in rdx
    #           UINT32[0]:  Address
    #           UINT32[1]:  Value
    #
    cls._MemSet32CoreCode   = env.InstructionStream()

    cls._MemSet32CoreCode.add(x86.mov(reg.rdx, mem.MemRef(reg.rbp, 0x10)))
    cls._MemSet32CoreCode.add(x86.mov(reg.ecx, mem.MemRef(reg.rdx, 0, data_size = 32)))     # rdx[0]: Address, rdx[4]: Return Value
    cls._MemSet32CoreCode.add(x86.mov(reg.eax, mem.MemRef(reg.rdx, 4, data_size = 32)))
    cls._MemSet32CoreCode.add(x86.mov(mem.MemRef(reg.ecx, 0, data_size = 32), reg.eax))

    cls._MemSet32CoreAddr, cls._MemSet32CoreBytes = cls._MemSet32CoreCode.get_code_bytes ()

    cls._MemSet32CoreFunc = EFI_AP_PROCEDURE (cls._MemSet32CoreAddr)

  def _BuildMpProtocol (cls):
    import EfiPy2.MdePkg.Protocol.MpService as MpService

    Interface = EfiPy.PVOID ()
    Status = EfiPy.gBS.LocateProtocol (
               EfiPy.byref (MpService.gEfiMpServiceProtocolGuid),
               None,
               EfiPy.byref (Interface)
               )

    if Status != EfiPy.EFI_SUCCESS:
      raise OSError (f"Local MpService fail!!! (0x{Status:016X})")

    cls._pMpServiceProtocol = EfiPy.cast (
                           Interface,
                           EfiPy.POINTER(MpService.EFI_MP_SERVICES_PROTOCOL)
                           )
    
    cls._MpServiceProtocol = cls._pMpServiceProtocol[0]

  def _BuildProcessorIds (cls):
    cls._ProcessirIds = []

    import EfiPy2.MdePkg.Protocol.MpService as MpService

    NumberOfProcessors          = EfiPy.UINTN ()
    NumberOfEnabledProcessors   = EfiPy.UINTN ()
    
    Status = cls._MpServiceProtocol.GetNumberOfProcessors (
               cls._pMpServiceProtocol,
               EfiPy.byref (NumberOfProcessors),
               EfiPy.byref (NumberOfEnabledProcessors)
               )
    
    if Status != EfiPy.EFI_SUCCESS:
      raise OSError (f"Get processor number fail!!! (0x{Status:016X})")
    
    ProcessorInfo = MpService.EFI_PROCESSOR_INFORMATION()
    
    for Index in range (NumberOfProcessors.value):
      Status = cls._MpServiceProtocol.GetProcessorInfo (
                 cls._pMpServiceProtocol,
                 Index,
                 EfiPy.byref (ProcessorInfo)
                 )
    
      if Status != EfiPy.EFI_SUCCESS:
        continue

      cls._ProcessirIds.append (ProcessorInfo.ProcessorId)

  def __init__ (cls, *args, **kwargs):
    cls._GetLocalApicAddress ()
    cls._BuildMpProtocol ()
    cls._BuildProcessorIds ()
    cls._BuildMemProcedure ()
    cls._BuildCpuIdProcedure ()
    cls._BuildMsrProcedure ()

  @property
  def LocalApicAddress (cls):
    return cls._LocalApicAddress

  @LocalApicAddress.setter
  def LocalApicAddress (cls, value):
    raise MemoryError ("Local Apic Address cannot be modified!!!")

  @property
  def ProcessorIds (cls):
    return cls._ProcessirIds
  
  @ProcessorIds.setter
  def ProcessorIds (cls):
    raise OSError ("Processor IDs is fiexd in current stage!!!")

  @property
  def Me (cls):
    ProcessorNumber = EfiPy.UINTN ()
    Status = cls._MpServiceProtocol.WhoAmI (
            cls._pMpServiceProtocol,
            EfiPy.byref (ProcessorNumber)
            )

    if Status != EfiPy.EFI_SUCCESS:
      raise OSError (f"Get current processor number idx!!! (0x{Status:016X})")
    
    return ProcessorNumber.value

  def __len__ (cls):
    return len (cls._ProcessirIds)

class X86Processors (metaclass = X86ProcessorClass):

  def __init__ (self, Index: int):

    self.Index = Index

  def MemGet32 (self, Address: int) -> int:

    me = type(self).Me
    Parameter = (EfiPy.UINT32 * 2)(Address, - 1)

    if self.Index == me:
      self._MemGet32CoreFunc  (EfiPy.byref (Parameter))
    else:
      Status = self._MpServiceProtocol.StartupThisAP (
               self._pMpServiceProtocol,    # POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
               self._MemGet32CoreFunc ,     # EFI_AP_PROCEDURE,                   # IN  Procedure,
               self.Index,                  # UINTN,                              # IN  ProcessorNumber,
               None,                        # EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
               1000* 1000,                  # UINTN,                              # IN  TimeoutInMicroseconds,
               EfiPy.byref (Parameter),     # PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
               None,                        # POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
               )

    return Parameter[1]

  def CpuId (self, Eax: int, Ecx: int, CpuIdReg):

    me = type(self).Me
    CpuIdRegAddr    = EfiPy.addressof (CpuIdReg)
    Parameter = (EfiPy.UINT32 * 3)(Eax, Ecx, CpuIdRegAddr)

    if self.Index == me:
      self._CpuIdCoreFunc  (EfiPy.byref (Parameter))
    else:
      Status = self._MpServiceProtocol.StartupThisAP (
                      self._pMpServiceProtocol,    # POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
                      self._CpuIdCoreFunc,         # EFI_AP_PROCEDURE,                   # IN  Procedure,
                      self.Index,                  # UINTN,                              # IN  ProcessorNumber,
                      None,                        # EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
                      1000* 1000,                  # UINTN,                              # IN  TimeoutInMicroseconds,
                      EfiPy.byref (Parameter),     # PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
                      None,                        # POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
                      )

  def WrMsr (self, Ecx: int, MsrReg):

    me          = type(self).Me
    MsrRegAddr  = EfiPy.addressof (MsrReg)
    Parameter   = (EfiPy.UINT32 * 2)(Ecx, MsrRegAddr)

    if self.Index == me:
      self._WrMsrCoreFunc (EfiPy.byref (Parameter))
    else:
      Status = self._MpServiceProtocol.StartupThisAP (
                      self._pMpServiceProtocol,    # POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
                      self._WrMsrCoreFunc,         # EFI_AP_PROCEDURE,                   # IN  Procedure,
                      self.Index,                  # UINTN,                              # IN  ProcessorNumber,
                      None,                        # EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
                      1000* 1000,                  # UINTN,                              # IN  TimeoutInMicroseconds,
                      EfiPy.byref (Parameter),     # PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
                      None,                        # POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
                      )
      pass

  def RdMsr (self, Ecx: int, MsrReg):

    me          = type(self).Me
    MsrRegAddr  = EfiPy.addressof (MsrReg)
    Parameter   = (EfiPy.UINT32 * 2)(Ecx, MsrRegAddr)

    if self.Index == me:
      self._RdMsrCoreFunc (EfiPy.byref (Parameter))
    else:
      Status = self._MpServiceProtocol.StartupThisAP (
                      self._pMpServiceProtocol,    # POINTER(EFI_MP_SERVICES_PROTOCOL),  # IN  *This
                      self._RdMsrCoreFunc,         # EFI_AP_PROCEDURE,                   # IN  Procedure,
                      self.Index,                  # UINTN,                              # IN  ProcessorNumber,
                      None,                        # EFI_EVENT,                          # IN  WaitEvent               OPTIONAL,
                      1000* 1000,                  # UINTN,                              # IN  TimeoutInMicroseconds,
                      EfiPy.byref (Parameter),     # PVOID,                              # IN  *ProcedureArgument      OPTIONAL,
                      None,                        # POINTER(BOOLEAN)                    # OUT *Finished               OPTIONAL
                      )

X86ProcessorArray = []
for Index in range (len (X86Processors)):
  X86ProcessorArray.append (X86Processors (Index))

if __name__ == '__main__':

  from EfiPy2.Lib.CpuId import CPUID_GENERIC_REGISTERs
  from EfiPy2.Lib.Msr import MSR_GENERIC_REGISTER
  from EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr import MSR_IA32_APIC_BASE_REGISTER

  print (f'APIC base address: 0x{X86Processors.LocalApicAddress:08X}')
  print (f'Processor IDs from EFI_MP_SERVICES_PROTOCOL: {X86Processors.ProcessorIds}')
  print (f'Me: {X86Processors.Me}, Processor numbers: {len (X86Processors)}')

  X86ProcessorArray = []
  for Index in range (len (X86Processors)):

    print (f'\nCPU {Index} infromation....')

    MmioAddress = 0xFEE00020
    Processor = X86Processors (Index)
    X86ProcessorArray.append (Processor)
    print (f'  From MMIO 0x{MmioAddress:08X}: 0x{Processor.MemGet32(MmioAddress):08X}')

    CpuIdReg = CPUID_GENERIC_REGISTERs()

    CpuIndex = 0x0B
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