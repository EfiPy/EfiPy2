# AcpiTableList.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
import os

if os.name == 'edk2':
    from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import AcpiTableList
elif os.name == 'posix':
    from EfiPy2.Lib.Acpi.AcpiRetrieveLinux import AcpiTableList
elif os.name == 'nt':
    from EfiPy2.Lib.Acpi.AcpiRetrieveWin import AcpiTableList

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser (prog = 'AcpiTableList.py')

    parser.add_argument ('-t', '--table', type =str, help = 'Check if specified ACPI table exist.')
    parser.add_argument ('-v', '--verbose', action = 'store_true', help = 'List table in verbose.')
    args = parser.parse_args ()

    if args.table is not None:
      AcpiTableName = bytes (args.table.encode('utf-8'))
    else:
      AcpiTableName = None

    AcpiTableList (AcpiTableName, args.verbose)