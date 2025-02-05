# AcpiRetrieve.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

def RetrieveAcpiInUefi ():
    print ('we are in UEFI2 environment')
    from EfiPy2.Lib.Acpi.AcpiRetrieveUefi  import ExtractMain
    ExtractMain ()

def RetrieveAcpiInLinux ():
    print ('we are in Linux environment')
    from EfiPy2.Lib.Acpi.AcpiRetrieveLinux import ExtractMain
    ExtractMain ()

def RetrieveAcpiInWindows ():
    print ('we are in Windows environment')
    from EfiPy2.Lib.Acpi.AcpiRetrieveWin import ExtractMain
    ExtractMain ()

RetrieveFuncDict = {
    'edk2'  : RetrieveAcpiInUefi,
    'posix' : RetrieveAcpiInLinux,
    'nt'    : RetrieveAcpiInWindows,
}

if __name__ == '__main__':
    import os
    try:
        RetrieveFuncDict [os.name]()
    except Exception as e:
        print (e)
