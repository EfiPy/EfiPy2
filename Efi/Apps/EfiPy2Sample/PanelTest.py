#
# PanelTest.py
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
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

from EfiPy2.Lib.PanelLib import EfiPyGfx, EfiPyFont, HintPrompt

def FontTest ():

  Font = EfiPyFont ()

  Font.SetColor (0xFF, 0, 0)
  Font.PrintXY ("EEEEEEEEEEEEE      fffffffff                 PPPPPPPPPPP                  ", 100, 200)
  Font.NextLine ()
  Font.PrintXY ("EEEEEEEEEEEEE     fffffffffff       iii      PPPPPPPPPPPP                 ")
  Font.NextLine ()
  Font.SetColor (0xFF, 0xFF, 0)
  Font.PrintXY (" EEE      EEE     fff      fff      iii       PPP      PPP                ")
  Font.NextLine ()
  Font.PrintXY (" EEE   EEE        fff                         PPP      PPP   yyy       yyy")
  Font.NextLine ()
  Font.SetColor (0, 0xFF, 0)
  Font.PrintXY (" EEEEEEEEE     fffffffffff        iiiii       PPPPPPPPPPP    yyy       yyy")
  Font.NextLine ()
  Font.PrintXY (" EEEEEEEEE     fffffffffff        iiiii       PPPPPPPP       yyy       yyy")
  Font.NextLine ()
  Font.SetColor (0, 0xFF, 0xFF)
  Font.PrintXY (" EEE   EEE        fff               iii       PPP            yyy       yyy")
  Font.NextLine ()
  Font.PrintXY (" EEE      EEE     fff               iii       PPP            yyy       yyy")
  Font.NextLine ()
  Font.SetColor (0, 0, 0xFF)
  Font.PrintXY ("EEEEEEEEEEEEE  fffffffffff       iiiiiiiii   PPPPPPP          yyyyyyyyyyyy")
  Font.NextLine ()
  Font.PrintXY ("EEEEEEEEEEEEE  fffffffffff       iiiiiiiii   PPPPPPP          yyyyyyyyyyyy")
  Font.NextLine ()
  Font.SetColor (0xD0, 0xD0, 0xD0)
  Font.PrintXY ("                                                                      yyyy")
  Font.NextLine ()
  Font.PrintXY ("                                                             yyyyyyyyyyyy ")
  Font.SetColor (0x80, 0x80, 0x80)
  Font.NextLine ()
  Font.PrintXY ("                                                            yyyyyyyyyyy  ")

def RulerTest (Note = False):

  Gfx = EfiPyGfx ()
  fnt = EfiPyFont ()

  if Note == True:
    fnt.PrintXY ("Resolution X Axis: %d" % Gfx.Info.HorizontalResolution, 50, 50)
    fnt.PrintXY ("Resolution Y Axis: %d" % Gfx.Info.VerticalResolution, 50, 70)

  fnt.PrintXY ("0", 15, 15)

  #
  # HorizontalResolution Ruler
  #

  h = 5

  for x in range (10, Gfx.Info.HorizontalResolution, 10):

    Gfx.Rect (x, 0, 1, h)

  h = 10

  for x in range (50, Gfx.Info.HorizontalResolution, 50):

    Gfx.Rect (x, 0, 1, h)

  h = 15

  for x in range (100, Gfx.Info.HorizontalResolution, 100):

    Gfx.Rect (x, 0, 1, h)
    fnt.PrintXY ("%d" % x, x, h + 2)

  x = Gfx.Info.HorizontalResolution - 1
  Gfx.Rect (x, 0, 1, h + fnt.LineHeight * 2)
  fnt.PrintXY ("%d" % x, x - fnt.LineWidth, h + fnt.LineHeight * 2 + 2)

  #
  # Vertical Ruler
  #
  
  w = 5
  
  for y in range (10, Gfx.Info.VerticalResolution, 10):
  
    Gfx.Rect (0, y, w, 1)

  w = 10
  
  for y in range (50, Gfx.Info.VerticalResolution, 50):
  
    Gfx.Rect (0, y, w, 1)

  w = 15
  len = 0
  
  for y in range (100, Gfx.Info.VerticalResolution, 100):
  
    Gfx.Rect (0, y, w, 1)
    fnt.PrintXY ("%d" % y, w + 2, y - 19)
    len = fnt.PointerX
  
  Gfx.Rect (0, Gfx.Info.VerticalResolution - 1, w + len, 1)
  fnt.PrintXY ("%d" % (Gfx.Info.VerticalResolution - 1), w + len + 2, Gfx.Info.VerticalResolution - 20)

def TestHint (fnt = None, HintString = None):

  from EfiPy2.MdePkg.Protocol.SimpleTextIn import EFI_INPUT_KEY

  if HintString != None and fnt != None:
    fnt.PrintXY ("%s" % HintString, 200, 300)

  InKey = EFI_INPUT_KEY ()

  Status = -1

  while Status != EfiPy.EFI_SUCCESS:
    Status = EfiPy.gST.ConIn[0].ReadKeyStroke (EfiPy.gST.ConIn, EfiPy.byref (InKey))

def GridTest (Gfx):

  def GridPattern (Gfx, x, y, w, h, color = None):

    Gfx.Rect (x, y, w, h, color)

  def GridPattern2 (Gfx, color = None):

    for x in range (0, Gfx.Info.HorizontalResolution, 50):
      for y in range (0, Gfx.Info.VerticalResolution, 50):
        GridPattern (Gfx, x + 4, y + 4, 50 - 8, 50 - 8, color)

  GridPattern2 (Gfx, Gfx.RGB (0xFF, 0xFF, 0xFF))  # White
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x80, 0x80, 0x80))  # Gray
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0xFF, 0x00, 0x00))  # Red
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x80, 0x00, 0x00))  # Half Red
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0xFF, 0x00))  # Blue
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x80, 0x00))  # Half Blue
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x00, 0xFF))  # Green
  TestHint (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x00, 0x80))  # Half Green
  TestHint (None, None)

if __name__ == '__main__':

  Gfx = EfiPyGfx ()
  fnt = EfiPyFont ()

  Gfx.clear ()
  TestHint (fnt, "Font Demo, Press any key to begin...")
  Gfx.clear ()
  FontTest ()
  TestHint ()

  Gfx.clear ()
  TestHint (fnt, "Ruler Demo, Press any key to begin...")
  Gfx.clear ()
  RulerTest (True)
  TestHint ()

  Gfx.clear ()
  TestHint (fnt, "Grid Demo, Press any key to begin...")
  Gfx.clear ()
  GridTest (Gfx)

  Gfx.clear ()
  TestHint (fnt, "Demo Complete")

  Gfx.clear ()
