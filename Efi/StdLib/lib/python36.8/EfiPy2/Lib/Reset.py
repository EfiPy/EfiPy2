# Reset.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference from https://github.com/torvalds/linux/blob/master/arch/x86/kernel/reboot.c
#

class Reset:

    @staticmethod
    def Cf9Reset (Value: int):
        print (f'Process CF9 reset with value 0x{Value:02X}')

        from EfiPy2.Lib.X86Processor import Me
        Me.Iow32 (0xCF9, Value)

    @staticmethod
    def AcpiReset ():

        from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable
        from EfiPy2.Lib.Acpi.AcpiFacpParser import AcpiFacpParser

        FacpRaw = ExtractTable (b'FACP', 0)
        FacpObj, FacpType = AcpiFacpParser (FacpRaw)

        print (f'Process ACPI reset, ID: 0x{FacpObj.ResetReg.AddressSpaceId:X}, Address: 0x{FacpObj.ResetReg.Address:X}, Value: 0x{FacpObj.ResetValue:X}')

        from EfiPy2.Lib.X86Processor import Me
        from EfiPy2.MdePkg.IndustryStandard import Acpi
        if FacpObj.ResetReg.AddressSpaceId == Acpi.EFI_ACPI_2_0_SYSTEM_MEMORY:
            Me.MemSet32 (FacpObj.ResetReg.Address, FacpObj.ResetValue)
        elif FacpObj.ResetReg.AddressSpaceId == Acpi.EFI_ACPI_2_0_SYSTEM_IO:
            Me.Iow32 (FacpObj.ResetReg.Address, FacpObj.ResetValue)
        elif FacpObj.ResetReg.AddressSpaceId == Acpi.EFI_ACPI_2_0_PCI_CONFIGURATION_SPACE:
            import EfiPy2.MdePkg.IndustryStandard.Pci as pci
            Bus = 0
            Dev, Func = (FacpObj.ResetReg.Address >> 32) & 0xFFFF, (FacpObj.ResetReg.Address >> 16) & 0xFFFF
            PciCfgOffset  = pci.PCI_ECAM_ADDRESS (Bus, Dev, Func, FacpObj.ResetReg.Address & 0xFFFF)

            from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable
            from EfiPy2.Lib.Acpi.AcpiMcfgParser import AcpiMcfgParser
            from EfiPy2 import UINT32
            AcpiRaw = ExtractTable (b'MCFG', 0)
            AcpiObj, AcpiType = AcpiMcfgParser (AcpiRaw)
            PciResetAddress = AcpiObj.McfgDesc.BaseAddress + PciCfgOffset
            PciResetPointer = UINT32.from_address (PciResetAddress)
            PciResetPointer[0] = FacpObj.ResetValue

    @staticmethod
    def KeyboardReset ():
        print (f'Process keyboard reset')

        from EfiPy2.Lib.X86Processor import Me
        Me.Iow32 (0x64, 0xFE)

    @staticmethod
    def PortReset (offset, value):
        print (f'Process Port reset')

        from EfiPy2.Lib.X86Processor import Me
        Me.Iow32 (offset, value)

    @staticmethod
    def CmosReset ():
        print (f'Process CMOS reset, This needs to be confirm.')

        from EfiPy2.Lib.X86Processor import Me
        Me.IndexDataw32 (0x70, 0x71, 0x0F, 0x00)

    @staticmethod
    def UefiOp (ResetType):
        print (f'Process UEFI Runtime Service SystemReset({ResetType}).')

        from EfiPy2 import gRT, EFI_SUCCESS
        gRT.ResetSystem (ResetType, EFI_SUCCESS, 0, None)
        