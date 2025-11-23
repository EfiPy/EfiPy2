# AcpiDmarParser.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference from
#
#   https://www.kernel.org/doc/Documentation/Intel-IOMMU.txt
#   http://www.intel.com/content/dam/www/public/us/en/documents/product-specifications/vt-directed-io-spec.pdf
#
import EfiPy2 as EfiPy

import copy
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE
from EfiPy2.MdePkg.IndustryStandard import DmaRemappingReportingTable
   
def AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField):

   #
   # Device Scope []
   #
   DeviceScopeIdx = 0
   while True:
      DeviceScopeName = f"DeviceScope_{DeviceScopeIdx}"
      RemapField.append ((DeviceScopeName, DmaRemappingReportingTable.EFI_ACPI_DMAR_DEVICE_SCOPE_STRUCTURE_HEADER))

      class RemapType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = RemapField

      DmarField [-1] = (RemapName, RemapType)

      class DmarType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = DmarField

      #
      # Device Scope add Path
      #
      DmarObj = DmarType.from_buffer (DmarRaw)
      RemapObj = getattr (DmarObj, RemapName)
      DeviceScopeObj = getattr (RemapObj, DeviceScopeName)

      #
      # Calculate Path Number
      #
      PciPathNum = (DeviceScopeObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_DEVICE_SCOPE_STRUCTURE_HEADER)) // 2
      DeviceScopeField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_DEVICE_SCOPE_STRUCTURE_HEADER._fields_)
      DeviceScopeField.append (("Path", DmaRemappingReportingTable.EFI_ACPI_DMAR_PCI_PATH * PciPathNum))
      class DeviceScopeType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = DeviceScopeField

      RemapField[-1] = ((DeviceScopeName, DeviceScopeType))

      class RemapType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = RemapField

      if EfiPy.sizeof (RemapType) < RemapObj.Header.Length:
         DeviceScopeIdx += 1
         continue
      break

   pass
   return RemapField

def AcpiDmarParser (DmarRaw):

    #
    # Get MAR Type, object and Raw data
    #
    DmarType    = DmaRemappingReportingTable.EFI_ACPI_DMAR_HEADER
    DmarObj     = DmarType.from_buffer (DmarRaw)

    idx = 1
  
    #
    # Analyze Remapping Structure
    #
    while EfiPy.sizeof (DmarType) < DmarObj.Header.Length:
      RemapName = f"Dmar{idx}"

      #
      # Common remap structure header
      #
      DmarField   = copy.copy (DmarType._fields_)
      DmarField.append ((RemapName, DmaRemappingReportingTable.EFI_ACPI_DMAR_STRUCTURE_HEADER))

      class DmarType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = DmarField

      DmarObj = DmarType.from_buffer (DmarRaw)
      RemapObj = getattr (DmarObj, RemapName)
      
      RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_STRUCTURE_HEADER._fields_)
      RemapField.append (("Todo_0", EfiPy.UINT8 * (RemapObj.Length - 4)))

      #
      # Individual Remap structure.
      #
      if RemapObj.Type == 0:
         RemapName = f"DRHD_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_DRHD_HEADER._fields_)

         RemapField = AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField)

      elif RemapObj.Type == 1:
         RemapName = f"RMRR_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_RMRR_HEADER._fields_)
         # RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_RMRR_HEADER);
         # RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

         RemapField = AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField)

      elif RemapObj.Type == 2:
         RemapName = f"ATSR_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_ATSR_HEADER._fields_)
         # RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_ATSR_HEADER);
         # RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

         RemapField = AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField)

      elif RemapObj.Type == 3:
         RemapName = f"RHSA_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_RHSA_HEADER._fields_)
         RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_RHSA_HEADER);
         RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

      elif RemapObj.Type == 4:
         RemapName = f"ANDD_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_ANDD_HEADER._fields_)
         RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_ANDD_HEADER);
         RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

      elif RemapObj.Type == 5:
         RemapName = f"SATC_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_SATC_HEADER._fields_)
         # RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_SATC_HEADER);
         # RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

         RemapField = AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField)

      elif RemapObj.Type == 6:
         RemapName = f"SIDP_{idx}"
         RemapField = copy.copy (DmaRemappingReportingTable.EFI_ACPI_DMAR_SIDP_HEADER._fields_)
         # RemainLength = RemapObj.Length - EfiPy.sizeof (DmaRemappingReportingTable.EFI_ACPI_DMAR_SIDP_HEADER);
         # RemapField.append ((f"Todo_{idx}", EfiPy.UINT8 * RemainLength))

         RemapField = AcpiDmarBuildScope (DmarRaw, RemapName, RemapField, DmarField)

      class RemapType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = RemapField

      DmarField [-1] = (RemapName, RemapType)

      class DmarType (EFIPY_INDUSTRY_STRUCTURE):
         _fields_ = DmarField

      DmarObj = DmarType.from_buffer (DmarRaw)
      idx += 1

    return DmarObj, DmarType

if __name__ == '__main__':

    import sys
    from EfiPy2.Lib.StructDump import DumpStruct
    from EfiPy2.Lib.HexDump import HexDump
    
    DmarFileName   = sys.argv[4]
    DmarFileHandle = open (DmarFileName, 'rb')
    if DmarFileHandle == None:
      print (f"Open {DmarFileName} error.")
      sys.exit (-1)
    DmarRaw     = bytearray (DmarFileHandle.read())
    
    DmarObj, DmarType = AcpiDmarParser (DmarRaw)

    DumpStruct (2, DmarObj, DmarType)
    print ('\n==== ACPI DMAR RAW data ======')
    HexDump (DmarRaw)
