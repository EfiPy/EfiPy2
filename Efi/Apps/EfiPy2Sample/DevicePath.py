#
# DevicePath.py
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# DevicePath.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol.SimpleFileSystem import gEfiSimpleFileSystemProtocolGuid
from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL, gEfiDevicePathProtocolGuid

#
# Get Simple File System Protocol numbers
#

BufferSize = EfiPy.UINTN (0)
Status = EfiPy.gBS.LocateHandle (
                     EfiPy.ByProtocol,
                     EfiPy.byref (gEfiSimpleFileSystemProtocolGuid),
                     None,
                     EfiPy.byref(BufferSize),
                     None
                     )

if Status != EfiPy.EFI_BUFFER_TOO_SMALL:
  exit(1)

#
# Get Simple File System Protocols
#

HandleArrayType = EfiPy.EFI_HANDLE * (BufferSize.value // EfiPy.sizeof (EfiPy.EFI_HANDLE))
HandleArray     = HandleArrayType ()

Status = EfiPy.gBS.LocateHandle(
                     EfiPy.ByProtocol,
                     EfiPy.byref(gEfiSimpleFileSystemProtocolGuid),
                     None,
                     EfiPy.byref(BufferSize),
                     HandleArray
                     )

if Status != EfiPy.EFI_SUCCESS:
  exit (1)

#
# Get Simple File System Device Path
#

for Handle in HandleArray:

  TmpDevPath = EfiPy.PVOID ()

  Status = EfiPy.gBS.HandleProtocol (
                       Handle,
                       EfiPy.byref (gEfiDevicePathProtocolGuid),
                       EfiPy.byref (TmpDevPath)
                       )
  if EfiPy.EFI_ERROR (Status):
    continue

  DevicePath = (EfiPy.cast (TmpDevPath, EfiPy.POINTER(EFI_DEVICE_PATH_PROTOCOL)))[0]

  print ("%s" % DevicePath)

exit (0)
