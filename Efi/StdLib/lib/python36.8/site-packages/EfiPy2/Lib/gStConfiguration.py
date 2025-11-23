# gStConfiguration.py
#
# EfiPy2.Lib.gStConfiguration
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

def RetrieveConfiguration ():

  gStConfiguration = []
  for Index in range (EfiPy.gST.NumberOfTableEntries):
    gStConfiguration.append ((EfiPy.gST.ConfigurationTable[Index].VendorGuid, EfiPy.gST.ConfigurationTable[Index].VendorTable))

  return gStConfiguration

def FindConfiguration (Guid, CfgType = None):

  if Guid is None or type (Guid) is not EfiPy.EFI_GUID:
    raise TypeError (f'Parameter Guid ({Guid}) has to be EFI_GUID type')

  Cfgs = RetrieveConfiguration ()
  for VendorGuid, VendorTable in Cfgs:
    if VendorGuid == Guid:
      del Cfgs
      if CfgType is not None:
        return CfgType.from_address (VendorTable)
      return VendorTable

  del Cfgs
  return None
