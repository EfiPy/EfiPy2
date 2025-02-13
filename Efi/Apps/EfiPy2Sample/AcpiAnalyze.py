# AcpiAnalyze.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

#
# Reference from https://uefi.org/acpi
#

from EfiPy2.Lib.Acpi.AcpiGenericParser import AcpiGenericParser

from EfiPy2.Lib.Acpi.AcpiApicParser import AcpiApicParser
from EfiPy2.Lib.Acpi.AcpiAsfParser  import AcpiAsfParser
from EfiPy2.Lib.Acpi.AcpiBgrtParser import AcpiBgrtParser
# from EfiPy2.Lib.Acpi.AcpiBootParser import AcpiBootParser #(*)
from EfiPy2.Lib.Acpi.AcpiDbg2Parser import AcpiDbg2Parser
# from EfiPy2.Lib.Acpi.AcpiDbgpParser import AcpiDbgpParser # Where is the spec?
from EfiPy2.Lib.Acpi.AcpiDmarParser import AcpiDmarParser
from EfiPy2.Lib.Acpi.AcpiFacpParser import AcpiFacpParser
from EfiPy2.Lib.Acpi.AcpiFacsParser import AcpiFacsParser
from EfiPy2.Lib.Acpi.AcpiFpdtParser import AcpiFpdtParser
from EfiPy2.Lib.Acpi.AcpiHpetParser import AcpiHpetParser
from EfiPy2.Lib.Acpi.AcpiLpitParser import AcpiLpitParser
from EfiPy2.Lib.Acpi.AcpiMcfgParser import AcpiMcfgParser
# from EfiPy2.Lib.Acpi.AcpiMsdmParser import AcpiMsdmParser # Standard ACPI description # (*)
# from EfiPy2.Lib.Acpi.AcpiNhltParser import AcpiNhltParser # Where is the spec?  # (*)
# from EfiPy2.Lib.Acpi.AcpiPhatParser import AcpiPhatParser # Where is the spec?  # (*)
# from EfiPy2.Lib.Acpi.AcpiPtdtParser import AcpiPtdtParser # Where is the spec?
# from EfiPy2.Lib.Acpi.AcpiSlicParser import AcpiSlicParser # Standard ACPI description
from EfiPy2.Lib.Acpi.AcpiTpm2Parser import AcpiTpm2Parser
from EfiPy2.Lib.Acpi.AcpiUefiParser import AcpiUefiParser
from EfiPy2.Lib.Acpi.AcpiWsmtParser import AcpiWsmtParser
from EfiPy2.Lib.Acpi.AcpiXsdtParser import AcpiXsdtParser

#
# DSDT and SSDT are ignored
#

AcpiTableDict = {
    b'AEST': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'AGDI': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'APIC': lambda AcpiRaw: AcpiApicParser (AcpiRaw), 
    b'APMT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'ASF!': lambda AcpiRaw: AcpiAsfParser (AcpiRaw), 
    b'BDAT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'BERT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'BGRT': lambda AcpiRaw: AcpiBgrtParser (AcpiRaw), 
    b'BOOT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'CCEL': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'CEDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'CSRT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'CPEP': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'DBG2': lambda AcpiRaw: AcpiDbg2Parser (AcpiRaw), 
    b'DBGP': lambda AcpiRaw: AcpiGenericParser (AcpiRaw),  # Where is the spec?
    b'DMAR': lambda AcpiRaw: AcpiDmarParser (AcpiRaw), 
    b'DSDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'DRTM': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'DTPR': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'ECDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'EINJ': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'ERST': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'ETDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'FACP': lambda AcpiRaw: AcpiFacpParser (AcpiRaw), 
    b'FACS': lambda AcpiRaw: AcpiFacsParser (AcpiRaw), 
    b'FPDT': lambda AcpiRaw: AcpiFpdtParser (AcpiRaw),
    b'GTDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'HEST': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'HPET': lambda AcpiRaw: AcpiHpetParser (AcpiRaw), 
    b'IBFT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'IERS': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'IORT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'IVRS': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'KEYP': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'LPIT': lambda AcpiRaw: AcpiLpitParser (AcpiRaw), 
    b'MCFG': lambda AcpiRaw: AcpiMcfgParser (AcpiRaw), 
    b'MCHI': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'MHSP': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'MISC': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'MPAM': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'MSCT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'MSDM': lambda AcpiRaw: AcpiGenericParser (AcpiRaw),  # Standard ACPI description
    b'MPST': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'NBFT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'NFIT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'NHLT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw),  # Where is the spec?
    b'PCCT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PHAT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PMTT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PPTT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PRMT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PSDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'PTDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw),  # Where is the spec?
    b'RASF': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'RAS2': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'RGRT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'RSDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SBST': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SDEI': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SDEV': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SLIC': lambda AcpiRaw: AcpiGenericParser (AcpiRaw),  # Standard ACPI description
    b'SLIT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SPCR': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SPMI': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SRAT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'STAO': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SSDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SVKL': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'SWFT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'TCPA': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'TPM2': lambda AcpiRaw: AcpiTpm2Parser (AcpiRaw), 
    b'UEFI': lambda AcpiRaw: AcpiUefiParser (AcpiRaw), 
    b'WAET': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'WDAT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'WDDT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'WPBT': lambda AcpiRaw: AcpiGenericParser (AcpiRaw), # ACPI spec
    b'WSMT': lambda AcpiRaw: AcpiWsmtParser (AcpiRaw), 
    b'XSDT': lambda AcpiRaw: AcpiXsdtParser (AcpiRaw), 
    b'XENV': lambda AcpiRaw: AcpiWsmtParser (AcpiRaw), 
}

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser (prog = 'AcpiAnalyze.py')

    ArgCommand = parser.add_subparsers (help = 'Analyze ACPI command')

    ArgCommandFile = ArgCommand.add_parser ('file', help = 'parse ACPI file (Windows, Linux, UEFI Shell)')
    ArgCommandFile.add_argument ('-f', '--file', help = 'ACPI file name.')

    ArgCommandMem  = ArgCommand.add_parser ('table', help = 'parse ACPI in host (Windows, Linux, UEFI Shell)')
    ArgCommandMem.add_argument ('-t', '--table', help = 'ACPI table name.')
    ArgCommandMem.add_argument ('-i', '--index', type = int, help = 'ACPI nth table by name name.')

    parser.add_argument ('-r', '--raw', action = 'store_true', help = 'Dump ACPI raw data.')
    parser.add_argument ('-d', '--dummy', action = 'store_true', help = 'Analyze ACPI table dummy.')
    args = parser.parse_args ()

    if hasattr (args, "file"):
      try:
          from EfiPy2 import sizeof
          from EfiPy2.MdePkg.IndustryStandard import Acpi

          from EfiPy2.Lib.StructDump import DumpStruct
          from EfiPy2.Lib.HexDump import HexDump

          AcpiFileHandle = open (args.file, 'rb')
          AcpiRaw = bytearray (AcpiFileHandle.read ())

          AcpiHeader = Acpi.EFI_ACPI_COMMON_HEADER.from_buffer (AcpiRaw)
          AcpiSignature = AcpiHeader.Signature.to_bytes (4, 'little')

          # try:
          #   AcpiObj, AcpiType = AcpiTableDict [AcpiSignature] (AcpiRaw)
          # except KeyError as e:
          #   AcpiObj, AcpiType = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer (AcpiRaw), Acpi.EFI_ACPI_DESCRIPTION_HEADER

          if AcpiRaw[:8] == b'RSD PTR ':
            from EfiPy2.Lib.Acpi.AcpiRsdpParser import AcpiRsdpParser
            AcpiObj, AcpiType = AcpiRsdpParser (AcpiRaw)
          else:
            AcpiObj, AcpiType = AcpiTableDict [AcpiSignature] (AcpiRaw)

          if args.dummy == False:
            print (f'==== ACPI {AcpiSignature} ======')
            DumpStruct (2, AcpiObj, AcpiType)
          if args.raw == True:
            print (f'\n==== ACPI RAW data ======')
            HexDump (AcpiRaw)

      except Exception as e:
          print (e)
          sys.exit (-1)

    elif hasattr (args, "table"):
      if args.index != None:
         AcpiIndex = args.index
      else:
         AcpiIndex = 0

      AcpiSignature = bytes (args.table.encode('utf-8'))
      print (f'Analyze signature {AcpiSignature}')

      import os
      if os.name == 'nt':
        from EfiPy2.Lib.Acpi.AcpiRetrieveWin  import ExtractTable
      elif os.name == 'posix':
        from EfiPy2.Lib.Acpi.AcpiRetrieveLinux  import ExtractTable
      elif os.name == 'edk2':
        from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractTable

      AcpiRaw = ExtractTable (AcpiSignature, AcpiIndex)

      if AcpiSignature == b'RSDP':
        from EfiPy2.Lib.Acpi.AcpiRsdpParser import AcpiRsdpParser
        AcpiObj, AcpiType = AcpiRsdpParser (AcpiRaw)
      else:
        AcpiObj, AcpiType = AcpiTableDict [AcpiSignature] (AcpiRaw)

      from EfiPy2.Lib.StructDump import DumpStruct
      from EfiPy2.Lib.HexDump import HexDump
      if args.dummy == False:
        print (f'==== ACPI {AcpiSignature} ======')
        DumpStruct (2, AcpiObj, AcpiType)
      if args.raw == True:
        print (f'\n==== ACPI RAW data ======')
        HexDump (AcpiRaw)