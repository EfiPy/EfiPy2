import EfiPy2 as EfiPy
from EfiPy2.Lib.EfiPyVariable import Variable

class Variables:

  def __init__ (self, Name = None, Guid = None, CaseSensitive = False):
    if CaseSensitive == False and Name != None:
      self.PattenName     = Name.upper()
    else:
      self.PattenName     = Name

    self.PattenGuid     = Guid
    self.CaseSensitive  = CaseSensitive

  def __enter__ (self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    return False

  def __iter__ (self):
    self.IterName    = EfiPy.PCHAR16 ('')
    self.IterGuid    = EfiPy.EFI_GUID ()
    self.IterVarSize = EfiPy.UINTN ((len(self.IterName.value) + 1) * 2)
    
    return self

  def __PatternFilter (self, Name, Guid):
    PatternFound = True

    if not self.PattenName is None:
      if self.CaseSensitive == False:
        TargetName = Name.upper()
      else:
        TargetName = Name
      if not self.PattenName in TargetName:
        PatternFound = False

    if not self.PattenGuid is None:
      if self.PattenGuid != Guid:
        PatternFound = False

    return PatternFound

  def __next__ (self):

    ContinueNext = True
    while ContinueNext == True:

      if self.PattenName is None and self.PattenGuid is None:
        ContinueNext = False

      Status = EfiPy.gRT.GetNextVariableName (
                           EfiPy.byref (self.IterVarSize),
                           self.IterName,
                           EfiPy.byref (self.IterGuid)
                           )

      if Status == EfiPy.EFI_BUFFER_TOO_SMALL:

        l = '\00' * (self.IterVarSize.value // 2 - len(self.IterName.value))
        s = EfiPy.create_unicode_buffer (self.IterName.value + l)
        self.IterName = EfiPy.cast (s, EfiPy.PCHAR16)

        Status = EfiPy.gRT.GetNextVariableName (
                             EfiPy.byref (self.IterVarSize),
                             self.IterName,
                             EfiPy.byref (self.IterGuid)
                             )
        if Status == EfiPy.EFI_SUCCESS:
          if not self.__PatternFilter (self.IterName.value, self.IterGuid):
            continue
          return (self.IterName.value, self.IterGuid)
        else:
          raise SystemError (f"EfiPy GetNextVariableName Error: 0x{Status:016X}")

      elif Status == EfiPy.EFI_SUCCESS:
        if not self.__PatternFilter (self.IterName.value, self.IterGuid):
          continue
        return (self.IterName.value, self.IterGuid)
      elif Status == EfiPy.EFI_NOT_FOUND:
        raise StopIteration
      else:
        raise SystemError (f"EfiPy GetNextVariableName Error: 0x{Status:016X}")

if __name__ == '__main__':

  print ("with Variables() as Vars:")
  with Variables() as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT') as Vars:")
  with Variables('BOOT') as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C))) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C))) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C), CaseSensitive = True)) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C)), CaseSensitive = True) as Vars:
    for n, g in Vars:
      print (n, g)

  print ()
  print ("with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C), CaseSensitive = False)) as Vars:")
  with Variables('BOOT', EfiPy.EFI_GUID (0x8BE4DF61, 0x93CA, 0x11D2, (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8C)), CaseSensitive = False) as Vars:
    for n, g in Vars:
      print (n, g)
