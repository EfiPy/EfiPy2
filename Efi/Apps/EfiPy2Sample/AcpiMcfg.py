# AcpiMcfg.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.Lib.AcpiLib import BuildAcpiHub, GetAcpiVersion, RetrieveAcpiType

DsdtAddress, SsdtAddress, AcpiEntries = BuildAcpiHub ()

McfgType, McfgAddr = RetrieveAcpiType (SignatureByte = b'MCFG', AcpiEntries = AcpiEntries)

if McfgType is None or McfgAddr is None:

  print ("Error to get MCFG information")
  import sys
  sys.exit (-1)

McfgTable = McfgType.from_address (McfgAddr)
print (f"MCFG Revision        : 0x{McfgTable.Header.Header.Revision:02X}")
print (f"BaseAddress          : 0x{McfgTable.McfgDesc.BaseAddress:016X}")
print (f"PciSegmentGroupNumber: 0x{McfgTable.McfgDesc.PciSegmentGroupNumber:04X}")
print (f"StartBusNumber       : 0x{McfgTable.McfgDesc.StartBusNumber:02X}")
print (f"EndBusNumber         : 0x{McfgTable.McfgDesc.EndBusNumber:02X}")
