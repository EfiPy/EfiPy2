from EfiPy2.Lib.PanelLib import EfiPyGfx, EfiPyFont, HintPrompt

if __name__ == '__main__':

  Mode = 0
  print (f'Set GOP to Mode {Mode}')
  Gfx = EfiPyGfx ()
  Gfx.ModeSet(Mode)

  print (f'Current GOP mode is {Gfx.Gop.Mode[0].Mode}')