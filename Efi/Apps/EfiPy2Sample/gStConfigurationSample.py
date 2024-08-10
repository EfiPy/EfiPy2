# gStConfigurationSample.py
#
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Guid.Acpi                import gEfiAcpiTableGuid
from EfiPy2.MdePkg.IndustryStandard.Acpi20  import EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER
from EfiPy2.Lib.gStConfiguration            import RetrieveConfiguration, FindConfiguration

Table = FindConfiguration (gEfiAcpiTableGuid)
print (f'''
Looking Configuration table from gEfiAcpiTableGuid
  Guid, {gEfiAcpiTableGuid}, Table.... 0x{Table:08X}''')

Table = FindConfiguration (gEfiAcpiTableGuid, EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER)
print (f'''
Looking Configuration table from gEfiAcpiTableGuid with class parameter EFI_ACPI_2_0_ROOT_SYSTEM_DESCRIPTION_POINTER
  Guid, {gEfiAcpiTableGuid}, Table type.... {type (Table).__name__}
  Signature: {Table.Signature.to_bytes (8, 'little')}
  OemId    : {bytes (Table.OemId[:])}''')

DummyGuid = EfiPy.EFI_GUID()
Table = FindConfiguration (DummyGuid)
print (f'''
Looking dummy guid {DummyGuid}
Table shoud be None, Table: {Table}''')

print (f'\nRetrieve every Configuration')
Cfg = RetrieveConfiguration ()
for Guid, Table in Cfg:
  print (f'  Guid {Guid}, Table 0x{Table:08X}')
