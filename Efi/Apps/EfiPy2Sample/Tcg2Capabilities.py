# Tcg2Capabilities.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.MdePkg.Protocol.Tcg2Protocol import gEfiTcg2ProtocolGuid, EFI_TCG2_PROTOCOL, EFI_TCG2_BOOT_SERVICE_CAPABILITY
from EfiPy2.Lib.StructDump import DumpStruct

if __name__ == '__main__':
  Interface = EfiPy.PVOID ()
  Status = EfiPy.gBS.LocateProtocol (
             EfiPy.byref (gEfiTcg2ProtocolGuid),
             None,
             EfiPy.byref (Interface)
             )

  if (EfiPy.EFI_ERROR (Status)):
    import sys
    print ("Locate protocol.(Status:0x%016X)" % Status)
    sys.exit(Status)

  Tcg2Protocol = EfiPy.cast (
                   Interface,
                   EfiPy.POINTER(EFI_TCG2_PROTOCOL)
                   )

  ProtocolCapability = EFI_TCG2_BOOT_SERVICE_CAPABILITY ()
  ProtocolCapability.Size = EfiPy.sizeof (EFI_TCG2_BOOT_SERVICE_CAPABILITY)

  Status = Tcg2Protocol[0].GetCapability (
                             Tcg2Protocol,
                             EfiPy.pointer (ProtocolCapability)
                             )
  if EfiPy.EFI_ERROR (Status):
    import sys
    print ("GetCapability.(Status:0x%016X)" % Status)
    sys.exit(Status)

  print (f'''
===============
Tcg2 Capability
===============''')
  DumpStruct (0, ProtocolCapability, EFI_TCG2_BOOT_SERVICE_CAPABILITY)
print ()

  if ProtocolCapability.ProtocolVersion.Major < 0x01 or (ProtocolCapability.ProtocolVersion.Major == 0x01 and ProtocolCapability.ProtocolVersion.Minor == 0x00):
    print (f"No CurrentActivePCRBanks")
  else:
    PCRBanks = EfiPy.UINT32 ()
    Status = Tcg2Protocol[0].GetActivePcrBanks (
                               Tcg2Protocol,
                               EfiPy.pointer (PCRBanks)
                               );
    if not EfiPy.EFI_ERROR (Status):
      print (f"CurrentActivePCRBanks - 0x{PCRBanks.value:08X}")
    else:
      print ("GetActivePcrBanks.(Status:0x%016X)" % Status)

from EfiPy2.Lib.HexDump import HexDump
print ('''
========================
Tcg2 Capability raw data
========================''')
TcgCapabilitiesRaw = (EfiPy.UINT8 * ProtocolCapability.Size).from_address (EfiPy.addressof (ProtocolCapability))
HexDump (bytes (TcgCapabilitiesRaw))
