#
# PanelFont.py
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

from EfiPy2.Lib.PanelLib import EfiPyGfx, EfiPyFont, HintPrompt

def FontTest (Font = None):

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

if __name__ == '__main__':

  Gfx = EfiPyGfx ()
  fnt = EfiPyFont ()

  Gfx.clear ()
  HintPrompt (fnt, "Font Demo, Press any key to begin...")
  Gfx.clear ()
  FontTest (fnt)
  HintPrompt ()
