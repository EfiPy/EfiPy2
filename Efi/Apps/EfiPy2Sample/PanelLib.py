#
# PanelLib.py
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# PanelTest.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#
import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol.GraphicsOutput import gEfiGraphicsOutputProtocolGuid, EFI_GRAPHICS_OUTPUT_PROTOCOL, EFI_GRAPHICS_OUTPUT_MODE_INFORMATION, EFI_GRAPHICS_OUTPUT_BLT_PIXEL
from EfiPy2.MdePkg.Protocol.GraphicsOutput import PixelRedGreenBlueReserved8BitPerColor, PixelBlueGreenRedReserved8BitPerColor, PixelBitMask, PixelBltOnly, EfiBltVideoFill

class EfiPyGfx:

  Gop  = None
  Info = None

  def _GetGop (self):

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

  def _GetInfo (self, Gop):

    SizeOfInfo = EfiPy.UINTN ()
    Info       = EfiPy.POINTER (EFI_GRAPHICS_OUTPUT_MODE_INFORMATION) ()

    Status = Gop.QueryMode (
                   EfiPy.byref (Gop),
                   Gop.Mode[0].Mode,
                   EfiPy.byref (SizeOfInfo),
                   EfiPy.byref (Info)
                   )

    return Info[0]

  def __init__ (self):

    self.Gop  = self._GetGop()
    self.Info = self._GetInfo(self.Gop)

    self.PixelBytes = self.Gop.Mode[0].FrameBufferSize // 4
    self.Frame      = (EfiPy.UINT32 * (self.PixelBytes)).from_address (self.Gop.Mode[0].FrameBufferBase)

  def RGB (self, R, G, B):
  
    return EFI_GRAPHICS_OUTPUT_BLT_PIXEL (B, G, R, 0xFF)

  def Rect (self, x, y, w, h, color = None):

    if color == None:
      color = self.RGB (0xFF, 0xFF, 0xFF)

    self.Gop.Blt (
          EfiPy.byref (self.Gop),
          EfiPy.byref (color),
          EfiBltVideoFill,
          0, 0, # SourceX, SourceY
          x, y, # DestinationX, DestinationY
          w, h, # Width, Height
          0
          )

  def clear (self, color = None):

    if color == None:
      color = self.RGB (0, 0, 0)

    self.Rect (0, 0, self.Info.HorizontalResolution - 1, self.Info.VerticalResolution - 1, color)

  def Dump (self):

    print ("Current Mode: %d" %    self.Gop.Mode[0].Mode)
    print ("Max Mode: %X" %        self.Gop.Mode[0].MaxMode)
    print ("FrameBufferBase: %X" % self.Gop.Mode[0].FrameBufferBase)
    print ("FrameBufferSize: %X" % self.Gop.Mode[0].FrameBufferSize)

    SizeOfInfo = EfiPy.UINTN ()
    Info       = EfiPy.POINTER (EFI_GRAPHICS_OUTPUT_MODE_INFORMATION) ()

    for idx in range (self.Gop.Mode[0].MaxMode):

      Status = self.Gop.QueryMode (
                          EfiPy.byref (self.Gop),
                          idx,
                          EfiPy.byref (SizeOfInfo),
                          EfiPy.byref (Info)
                          )

      if EfiPy.EFI_ERROR (Status):
        print ("Get Mode %d error (Status: %X" % (idx, Status))
        continue

      print ("\nMode %d Information" % idx)
      print ("===================================================================================")
      print ("Version: %X"              %       Info[0].Version)
      print ("HorizontalResolution: %d" %       Info[0].HorizontalResolution)
      print ("VerticalResolution: %d"   %       Info[0].VerticalResolution)
      print ("PixelFormat: %d"          %       Info[0].PixelFormat)
      print ("PixelInformation (R:0x%08X, G:0x%08X, B:0x%08X)" % (Info[0].PixelInformation.RedMask, Info[0].PixelInformation.GreenMask, Info[0].PixelInformation.BlueMask))
      print ("PixelsPerScanLine %d"     %       Info[0].PixelsPerScanLine)

from EfiPy2.MdePkg.Protocol.HiiFont  import gEfiHiiFontProtocolGuid, EFI_HII_FONT_PROTOCOL, EFI_FONT_DISPLAY_INFO, EFI_HII_ROW_INFO
from EfiPy2.MdePkg.Protocol          import HiiFont as ft
from EfiPy2.MdePkg.Protocol.HiiImage import EFI_IMAGE_OUTPUT

class EfiPyFont:

  def __init__ (self):

    TmpProtocol = EfiPy.PVOID ()

    Status = EfiPy.gBS.LocateProtocol (
                        EfiPy.byref (gEfiHiiFontProtocolGuid),
                        None,
                        EfiPy.byref(TmpProtocol))

    if EfiPy.EFI_ERROR (Status):
      return

    self.Gfx = EfiPyGfx ()

    self.HiiFont = EfiPy.cast (TmpProtocol, EfiPy.POINTER (EFI_HII_FONT_PROTOCOL))[0]

    self.Blt   = EFI_IMAGE_OUTPUT ()
    self.pBlt  = EfiPy.pointer (self.Blt)
    self.Blt.Width   = self.Gfx.Info.HorizontalResolution
    self.Blt.Height  = self.Gfx.Info.VerticalResolution
    self.Blt.Image.Screen = EfiPy.pointer (self.Gfx.Gop)

    self.FontInfo    = EFI_FONT_DISPLAY_INFO ()

    self.RowInfoArray      = EfiPy.POINTER (EFI_HII_ROW_INFO) ()
    self.RowInfoArraySize  = EfiPy.UINTN ()

    self.FontInfo.ForegroundColor = self.Gfx.RGB (0xFF, 0xFF, 0xFF)
    self.FontInfo.BackgroundColor = self.Gfx.RGB (0x00, 0x00, 0x00)

    self.OrigX    = 0
    self.PointerX = 0
    self.PointerY = 0
    self.LineHeight = 0
    self.LineWidth  = 0

  def GotoXY (self, uString, x = -1, y = -1):

    if x != -1:
      self.PointerX = x
    else:
      self.PointerX = 0

    if y != -1:
      self.PointerY = y
    else:
      self.PointerY = 0

  def PrintXY (self, uString, x = -1, y = -1):

    if x != -1:
      self.PointerX = x

    if y != -1:
      self.PointerY = y

    self.HiiFont.StringToImage (
                   EfiPy.byref (self.HiiFont),
                   ft.EFI_HII_IGNORE_IF_NO_GLYPH | ft.EFI_HII_OUT_FLAG_CLIP |  \
                   ft.EFI_HII_OUT_FLAG_CLIP_CLEAN_X | ft.EFI_HII_OUT_FLAG_CLIP_CLEAN_Y | \
                   ft.EFI_HII_IGNORE_LINE_BREAK | ft.EFI_HII_DIRECT_TO_SCREEN,
                   uString,
                   EfiPy.byref (self.FontInfo),
                   EfiPy.byref (self.pBlt),
                   self.PointerX,
                   self.PointerY,
                   EfiPy.byref (self.RowInfoArray),
                   EfiPy.byref (self.RowInfoArraySize),
                   None)

    for idx in range (self.RowInfoArraySize.value):

      RowInfo = self.RowInfoArray [idx]

      self.OrigX      = self.PointerX
      self.PointerX  += RowInfo.LineWidth
      self.LineHeight = RowInfo.LineHeight
      self.LineWidth  = RowInfo.LineWidth

  def NextLine (self):
    self.PointerY += self.LineHeight
    self.PointerX  = self.OrigX

  def SetColor (self, fgR, fgG, fgB, bgR = 0, bgG = 0, bgB = 0):

    self.FontInfo.ForegroundColor = self.Gfx.RGB (fgR, fgG, fgB)
    self.FontInfo.BackgroundColor = self.Gfx.RGB (bgR, bgG, bgB)

def HintPrompt (fnt = None, HintString = None):

  from EfiPy2.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY

  if HintString != None and fnt != None:
    fnt.PrintXY ("%s" % HintString, 200, 300)

  InKey = EFI_INPUT_KEY ()

  Status = -1

  while Status != EfiPy.EFI_SUCCESS:
    Status = EfiPy.gST.ConIn[0].ReadKeyStroke (EfiPy.gST.ConIn, EfiPy.byref (InKey))
