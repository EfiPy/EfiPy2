#
# GopFb.py
#
# Copyright (C) 2016 - 2025 MaxWu efipy.core@gmail.com All rights reserved.
#
# GopFb.py is free software: you can redistribute it and/or modify
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

from EfiPy2.MdePkg.Protocol.GraphicsOutput import gEfiGraphicsOutputProtocolGuid, EFI_GRAPHICS_OUTPUT_PROTOCOL, EFI_GRAPHICS_OUTPUT_MODE_INFORMATION

def GetGop ():

  HandleCount  = EfiPy.UINTN ()
  HandleBuffer = EfiPy.POINTER (EfiPy.EFI_HANDLE) ()

  Status = EfiPy.gBS.LocateHandleBuffer (
                       EfiPy.ByProtocol,
                       EfiPy.byref (gEfiGraphicsOutputProtocolGuid),
                       None,
                       EfiPy.byref (HandleCount),
                       EfiPy.byref (HandleBuffer))

  if EfiPy.EFI_ERROR (Status):
    return None

  Gop = None

  for idx in range(HandleCount.value):

    TmpProtocol = EfiPy.PVOID ()

    Status = EfiPy.gBS.HandleProtocol (
	                     HandleBuffer[idx],
                         EfiPy.byref (gEfiGraphicsOutputProtocolGuid),
	                     EfiPy.byref (TmpProtocol))

    if EfiPy.EFI_ERROR (Status):
      continue

    Gop = EfiPy.cast (TmpProtocol, EfiPy.POINTER(EFI_GRAPHICS_OUTPUT_PROTOCOL)) [0]
    break

  return Gop

#
# Return Frame, length
#

def GetFrameBuffer (Gop):

  if Gop == None:
    return None, None

  PixelBytes = Gop.Mode[0].FrameBufferSize // EfiPy.sizeof (EfiPy.UINT32)
  Frame      = (EfiPy.UINT32 * (PixelBytes)).from_address (Gop.Mode[0].FrameBufferBase)

  return Frame, PixelBytes

if __name__ == '__main__':

  Gop = GetGop()

  Frame, Length = GetFrameBuffer (Gop)

  for idx in range (Length // 2):
    Frame[idx] = (~Frame[idx]) & 0xFFFFFF | 0xFF00
