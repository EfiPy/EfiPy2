# BlockIoInfo.py
#
# BlockIoInfo.py
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import sys
import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol.BlockIo  import gEfiBlockIoProtocolGuid, EFI_BLOCK_IO_PROTOCOL
from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL, gEfiDevicePathProtocolGuid
from EfiPy2.MdePkg.Uefi.UefiSpec import EFI_SYSTEM_TABLE

# This function would need to run within a UEFI application using Python bindings (conceptual)
def EnumerateBlockIo ():

    BufferSize = EfiPy.UINTN (0)
    Status = EfiPy.gBS.LocateHandle(
                         EfiPy.ByProtocol,
                         EfiPy.byref (gEfiBlockIoProtocolGuid),
                         None,
                         EfiPy.byref(BufferSize),
                         None
                         )
    if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
      sys.exit(1)

    HandleArrayType = EfiPy.EFI_HANDLE * (BufferSize.value // EfiPy.sizeof (EfiPy.EFI_HANDLE))
    HandleArray     = HandleArrayType ()

    Status = EfiPy.gBS.LocateHandle(
                         EfiPy.ByProtocol,
                         EfiPy.byref(gEfiBlockIoProtocolGuid),
                         None,
                         EfiPy.byref(BufferSize),
                         HandleArray
                         )
    
    if Status != EfiPy.EFI_SUCCESS:
      sys.exit (1)

    for Handle in HandleArray:

        TmpDevPath = EfiPy.PVOID ()
        Status = EfiPy.gBS.HandleProtocol (
                             Handle,
                             EfiPy.byref (gEfiDevicePathProtocolGuid),
                             EfiPy.byref (TmpDevPath)
                             )
        if Status == EfiPy.EFI_SUCCESS:
          DevicePath = (EfiPy.cast (TmpDevPath, EfiPy.POINTER(EFI_DEVICE_PATH_PROTOCOL)))[0]

          print (f'Found BlockIo device: {DevicePath}')

        VoidBlockIo = EfiPy.PVOID ()
        Status = EfiPy.gBS.HandleProtocol(
                             Handle,
                             EfiPy.byref (gEfiBlockIoProtocolGuid),
                             EfiPy.byref (VoidBlockIo)
                             )
        if Status == EfiPy.EFI_SUCCESS:

          BlockIoProtocol = (EfiPy.cast (VoidBlockIo, EfiPy.POINTER(EFI_BLOCK_IO_PROTOCOL))) [0]

          if BlockIoProtocol.Media[0].RemovableMedia and BlockIoProtocol.Media[0].MediaPresent:
              # Removable disk detected
              total_sectors = BlockIoProtocol.Media[0].LastBlock + 1
              print(f"  Removable Disk has {total_sectors} sectors.")
          else:
              total_sectors = BlockIoProtocol.Media[0].LastBlock + 1
              print(f"  Fixed Disk has {total_sectors} sectors.")

    print("No more disk detected.")
    return 0

if __name__ == '__main__':
  EnumerateBlockIo ()