# AcpiApicParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiApicParser (ApicRaw):

    import EfiPy2 as EfiPy
    
    from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
    from EfiPy2.Lib.AcpiLib import ScanAcpiRsdp, BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType
    
    #
    # Get APIC Type, object and Raw data
    #
    ApicType    = Acpi.EFI_ACPI_6_5_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER
    ApicObj     = ApicType.from_buffer_copy (ApicRaw)
    
    ApicField = ApicType._fields_
    
    class EFI_ACPI_6_5_APIC_UNKNOWN_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = [
        ("Type",              EfiPy.UINT8),
        ("Unknown",           EfiPy.UINT8 * ApicObj.Header.Length),
      ]
    
    ApicFieldUnknown = ("Unknown",   EFI_ACPI_6_5_APIC_UNKNOWN_STRUCTURE)
    ApicFieldDict = {
      0x00: ("ProcessorLocalApic",              Acpi.EFI_ACPI_6_5_PROCESSOR_LOCAL_APIC_STRUCTURE),
      0x01: ("IoApic",                          Acpi.EFI_ACPI_6_5_IO_APIC_STRUCTURE),
      0x02: ("InterruptSourceOverride",         Acpi.EFI_ACPI_6_5_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE),
      0x03: ("NoneMakableInterruptSource",      Acpi.EFI_ACPI_6_5_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE),
      0x04: ("LocalApicNmi",                    Acpi.EFI_ACPI_6_5_LOCAL_APIC_NMI_STRUCTURE),
      0x05: ("LocalApicAddressOverride",        Acpi.EFI_ACPI_6_5_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE),
      0x06: ("IoSapic",                         Acpi.EFI_ACPI_6_5_IO_SAPIC_STRUCTURE),
      0x07: ("LocalSapic",                      Acpi.EFI_ACPI_6_5_PROCESSOR_LOCAL_SAPIC_STRUCTURE),
      0x08: ("PlatformInterruptSourceOcerride", Acpi.EFI_ACPI_6_5_PLATFORM_INTERRUPT_SOURCES_STRUCTURE),
      0x09: ("ProcessorLocalX2Apic",            Acpi.EFI_ACPI_6_5_PROCESSOR_LOCAL_X2APIC_STRUCTURE),
      0x0A: ("LocalX2ApicNmi",                  Acpi.EFI_ACPI_6_5_LOCAL_X2APIC_NMI_STRUCTURE),
      0x0B: ("Gic",                             Acpi.EFI_ACPI_6_5_GIC_STRUCTURE),
      0x0C: ("GicDistributor",                  Acpi.EFI_ACPI_6_5_GIC_DISTRIBUTOR_STRUCTURE),
      0x0D: ("GicMsiFrame",                     Acpi.EFI_ACPI_6_5_GIC_MSI_FRAME_STRUCTURE),
      0x0E: ("Gicr",                            Acpi.EFI_ACPI_6_5_GICR_STRUCTURE),
      0x0F: ("GicIts",                          Acpi.EFI_ACPI_6_5_GIC_ITS),
      0x10: ("MultiProcessorWakeup",            Acpi.EFI_ACPI_6_5_MULTIPROCESSOR_WAKEUP_STRUCTURE),
      0x11: ("CorePic",                         Acpi.EFI_ACPI_6_5_CORE_PIC),
      0x12: ("LioPic",                          Acpi.EFI_ACPI_6_5_LIO_PIC_STRUCTURE),
      0x13: ("HtPic",                           Acpi.EFI_ACPI_6_5_HT_PIC_STRUCTURE),
      0x14: ("EioPic",                          Acpi.EFI_ACPI_6_5_EIO_PIC_STRUCTURE),
      0x15: ("MsiPic",                          Acpi.EFI_ACPI_6_5_MSI_PIC_STRUCTURE),
      0x16: ("BioPic",                          Acpi.EFI_ACPI_6_5_BIO_PIC_STRUCTURE),
      0x17: ("LpcPic",                          Acpi.EFI_ACPI_6_5_LPC_PIC_STRUCTURE),
      }
    
    ApicDupDict = {
      0x00: 0,
      0x01: 0,
      0x02: 0,
      0x03: 0,
      0x04: 0,
      0x05: 0,
      0x06: 0,
      0x07: 0,
      0x08: 0,
      0x09: 0,
      0x0A: 0,
      0x0B: 0,
      0x0C: 0,
      0x0D: 0,
      0x0E: 0,
      0x0F: 0,
      0x10: 0,
      0x11: 0,
      0x12: 0,
      0x13: 0,
      0x14: 0,
      0x15: 0,
      0x16: 0,
      0x17: 0,
    }
    
    while EfiPy.sizeof (ApicType) < ApicObj.Header.Length:
      NextType = EfiPy.UINT8 ( ApicRaw [EfiPy.sizeof (ApicType)])
      FileName, FieldType = ApicFieldDict.get (NextType.value, ApicFieldUnknown)
      FileName = f'{FileName}_{ApicDupDict.get (NextType.value, 0xFF):02X}'
      ApicDupDict [NextType.value] += 1
      ApicField.append ((FileName, FieldType))
    
      class ApicType (EFIPY_INDUSTRY_STRUCTURE):
        _fields_ = ApicField
    
    ApicObj = ApicType.from_buffer_copy (ApicRaw)

    return ApicObj, ApicType

if __name__ == '__main__':

    import sys
    
    from EfiPy2.MdePkg.IndustryStandard import Acpi
    from EfiPy2.Lib.HexDump import HexDump
    from EfiPy2.Lib.StructDump import DumpStruct

    ApicFileName   = sys.argv[4]

    ApicFileHandle = open (ApicFileName, 'rb')
    if ApicFileHandle == None:
      print (f"Open {ApicFileName} error.")
      sys.exit (-1)

    ApicRaw     = ApicFileHandle.read()

    ApicObj, ApicType = AcpiApicParser (ApicRaw)

    DumpStruct (2, ApicObj, ApicType)
    print ('\n==== ACPI APIC RAW data ======')
    HexDump (ApicRaw)