# EfiPy2Reset.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

from EfiPy2.Lib.Reset import Reset

def main ():
    import argparse

    parser = argparse.ArgumentParser (prog = 'EfiPy2Reset.py')

    parser.add_argument ('-s', '--soft', action = 'store_true', help = 'soft reset via CF9 set as 0x04.')
    parser.add_argument ('-w', '--warm', action = 'store_true', help = 'warn reset via CF9 set as 0x06.')
    parser.add_argument ('-c', '--cold', action = 'store_true', help = 'cold reset via CF9 set as 0x0E.')
    parser.add_argument ('-a', '--acpi', action = 'store_true', help = 'system reset via ACPI.')
    parser.add_argument ('-k', '--keyboard', action = 'store_true', help = 'system reset via keyboard IO port 60/64.')
    parser.add_argument ('-p', '--port92', action = 'store_true', help = 'system reset via port 92h.')
    parser.add_argument ('-u', '--uefi', action = 'store_true', help = 'UEFI gRT.ResetSystem operation')
    parser.add_argument ('-d', '--shutdown', action = 'store_true', help = 'Shutdown via gRT.ResetSystem')
    args = parser.parse_args ()

    if sum ((args.soft, args.warm, args.cold, args.acpi, args.keyboard, args.port92)) > 1:
        print ('Only one or none argument are allowed in this program')
        return

    if args.uefi:
        import EfiPy2.MdePkg.Uefi.UefiMultiPhase as UefiMultiPhase

    if args.soft:
        Reset.Cf9Reset (0x04)
    elif args.warm:
        if args.uefi == True:
            from EfiPy2.MdePkg.Uefi.UefiMultiPhase import EfiResetWarm
            Reset.UefiOp (EfiResetWarm)
        else:
            Reset.Cf9Reset (0x06)
    elif args.cold:
        if args.uefi == True:
            from EfiPy2.MdePkg.Uefi.UefiMultiPhase import EfiResetCold
            Reset.UefiOp (EfiResetCold)
        else:
            Reset.Cf9Reset (0x0E)
    elif args.acpi:
        Reset.AcpiReset ()
    elif args.port92:
        Reset.PortReset (0x92, 0x01)
    elif args.keyboard:
        Reset.KeyboardReset ()
    elif args.shutdown:
        from EfiPy2.MdePkg.Uefi.UefiMultiPhase import EfiResetShutdown
        Reset.UefiOp (EfiResetShutdown)
    elif args.uefi:
        from EfiPy2.MdePkg.Uefi.UefiMultiPhase import EfiResetPlatformSpecific
        Reset.UefiOp (EfiResetPlatformSpecific)
    else:
        from EfiPy2.MdePkg.Uefi.UefiMultiPhase import EfiResetShutdown
        Reset.UefiOp (EfiResetShutdown)

if __name__ == '__main__':
    main ()