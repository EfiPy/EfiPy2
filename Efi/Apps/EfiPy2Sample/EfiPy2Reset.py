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
    parser.add_argument ('-w', '--warm', action = 'store_true', help = 'hard reset via CF9 set as 0x06.')
    parser.add_argument ('-H', '--hard', action = 'store_true', help = 'hard reset via CF9 set as 0x0E.')
    parser.add_argument ('-a', '--acpi', action = 'store_true', help = 'system reset via ACPI.')
    parser.add_argument ('-k', '--keyboard', action = 'store_true', help = 'system reset via keyboard IO port 60/64.')
    parser.add_argument ('-c', '--cmos', action = 'store_true', help = 'system reset via CMOS offset 0x0F.')
    args = parser.parse_args ()

    if sum ((args.soft, args.hard, args.acpi, args.keyboard, args.cmos)) > 1:
        print ('Only one or none argument are allowed in this program')
        return

    if args.soft:
        Reset.Cf9Reset (0x04)
    elif args.warm:
        Reset.Cf9Reset (0x06)
    elif args.hard:
        Reset.Cf9Reset (0x0E)
    elif args.acpi:
        Reset.AcpiReset ()
    elif args.keyboard:
        Reset.KeyboardReset ()
    elif args.cmos:
        Reset.CmosReset ()
    else:
        Reset.Cf9Reset (0x0E)

if __name__ == '__main__':
    main ()