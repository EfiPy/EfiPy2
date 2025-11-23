# AcpiTpm2Parser.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def AcpiTpm2Parser (Tpm2Raw):
  import EfiPy2 as EfiPy

  from EfiPy2.MdePkg.IndustryStandard import Acpi
  from EfiPy2.Lib.AcpiTableDb import AcpiTpm2

  #
  # Get TPM2 Type, object and Raw data
  #
  Tpm2Head    = Acpi.EFI_ACPI_DESCRIPTION_HEADER.from_buffer_copy (Tpm2Raw)
  Tpm2Type    = AcpiTpm2 [Tpm2Head.Revision]
  Tpm2Obj     = Tpm2Type.from_buffer_copy (Tpm2Raw)

  return Tpm2Obj, Tpm2Type

if __name__ == '__main__':

  import sys
  from EfiPy2.Lib.StructDump import DumpStruct
  from EfiPy2.Lib.HexDump import HexDump

  Tpm2FileName   = sys.argv[4]
  Tpm2FileHandle = open (Tpm2FileName, 'rb')

  if Tpm2FileHandle == None:
    print (f"Open {Tpm2FileName} error.")
    sys.exit (-1)

  Tpm2Raw     = Tpm2FileHandle.read()

  Tpm2Obj, Tpm2Type = AcpiTpm2Parser (Tpm2Raw)

  DumpStruct (2, Tpm2Obj, Tpm2Type)
  print ('\n==== ACPI TPM2 RAW data ======')
  HexDump (Tpm2Raw)
