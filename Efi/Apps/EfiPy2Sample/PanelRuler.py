#
# PanelRuler.py
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# PanelRuler.py is free software: you can redistribute it and/or modify
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

from PanelLib import EfiPyGfx, EfiPyFont, HintPrompt

def RulerTest (fnt = None, Gfx = False, Note= False):

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
    fnt.PrintXY ("%d" % x, x - fnt.LineWidth, h + 2)

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

if __name__ == '__main__':

  Gfx = EfiPyGfx ()
  fnt = EfiPyFont ()

  Gfx.clear ()
  HintPrompt (fnt, "Ruler Demo, Press any key to begin...")
  Gfx.clear ()
  RulerTest (fnt, Gfx, True)
  HintPrompt ()
