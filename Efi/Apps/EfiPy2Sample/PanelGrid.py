#
# PanelGrid.py
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# PanelGrid.py is free software: you can redistribute it and/or modify
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

def GridTest (Gfx):

  def GridPattern (Gfx, x, y, w, h, color = None):

    Gfx.Rect (x, y, w, h, color)

  def GridPattern2 (Gfx, color = None):

    for x in range (0, Gfx.Info.HorizontalResolution, 50):
      for y in range (0, Gfx.Info.VerticalResolution, 50):
        GridPattern (Gfx, x + 4, y + 4, 50 - 8, 50 - 8, color)

  GridPattern2 (Gfx, Gfx.RGB (0xFF, 0xFF, 0xFF))  # White
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x80, 0x80, 0x80))  # Gray
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0xFF, 0x00, 0x00))  # Red
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x80, 0x00, 0x00))  # Half Red
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0xFF, 0x00))  # Blue
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x80, 0x00))  # Half Blue
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x00, 0xFF))  # Green
  HintPrompt (None, None)
  GridPattern2 (Gfx, Gfx.RGB (0x00, 0x00, 0x80))  # Half Green
  HintPrompt (None, None)

if __name__ == '__main__':

  Gfx = EfiPyGfx ()
  fnt = EfiPyFont ()

  Gfx.clear ()
  HintPrompt (fnt, "Grid Demo, Press any key to begin...")
  Gfx.clear ()
  GridTest (Gfx)
  Gfx.clear ()
