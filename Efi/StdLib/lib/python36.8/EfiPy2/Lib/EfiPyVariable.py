# EfiPyVariable.py
#
# EfiPy2.Lib.EfiPyVariable
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid

EfiPyVarGuid =  gEfiGlobalVariableGuid
EfiPyVarAttr =  EfiPy.EFI_VARIABLE_NON_VOLATILE | EfiPy.EFI_VARIABLE_BOOTSERVICE_ACCESS | EfiPy.EFI_VARIABLE_RUNTIME_ACCESS

class Variable:

  def __init__ (self, Name, Guid = EfiPyVarGuid, Attribute = EfiPyVarAttr):
    self.VarName    = Name
    self.VarGuid    = Guid
    self.VarAttr    = EfiPy.UINT32 (Attribute)
    self.VarSize    = EfiPy.UINTN (0)
    self.VarValue   = EfiPy.create_string_buffer (0)

  def __len__ (self):
    return len (self.VarValue)

  def GetVariable (self):
    Status = EfiPy.gRT.GetVariable (
                         self.VarName,
                         EfiPy.byref (self.VarGuid),
                         EfiPy.byref (self.VarAttr),
                         EfiPy.byref (self.VarSize),
                         EfiPy.byref (self.VarValue)
                         )
    if Status == EfiPy.EFI_BUFFER_TOO_SMALL:
      self.VarValue = EfiPy.create_string_buffer (self.VarSize.value)
      Status = EfiPy.gRT.GetVariable (
                           self.VarName,
                           EfiPy.byref (self.VarGuid),
                           EfiPy.byref (self.VarAttr),
                           EfiPy.byref (self.VarSize),
                           EfiPy.byref (self.VarValue)
                           )
      if Status != EfiPy.EFI_SUCCESS:
        raise SystemError (f"EfiPy GetVariable Error: 0x{Status:016X}")
    elif Status == EfiPy.EFI_SUCCESS:
      return
    else:
      raise SystemError (f"EfiPy GetVariable Error: 0x{Status:016X}")

  def SetVariable (self):
    Status = EfiPy.gRT.SetVariable (
                         self.VarName,
                         EfiPy.byref (self.VarGuid),
                         self.VarAttr,
                         self.VarSize,
                         EfiPy.byref (self.VarValue)
                         )
    if Status != EfiPy.EFI_SUCCESS:
      raise SystemError (f"EfiPy SetVariable Error: 0x{Status:016X}")


  @property
  def Name (self):
    return self.Name

  @property
  def Guid (self):
    return self.Guid

  @property
  def Attribute (self):
    return self.VarAttr.value

  @Attribute.setter
  def Attribute (self, Attr):
    self.VarAttr.value = Attr

  @property
  def Value (self):
    return self.VarValue.raw

  @Value.setter
  def Value (self, Value):
    if not type(Value) in (bytearray, bytes):
      raise TypeError (f'Value has to be ether bytearray or bytes, it got the type {type(Value)}')
    if type(Value) is bytearray:
      Value = bytes (Value)
    self.VarValue = EfiPy.create_string_buffer (Value)
    self.VarSize.value = len (Value)

  def __repr__ (self):
    return f"{self.VarName}:{self.VarGuid} 0x{self.VarAttr.value:X}"

if __name__ == '__main__':

  # print (f'Variable default GUID: {EfiPyVarGuid}')
  # print (f'Variable default attribute: 0x{EfiPyVarAttr:016x}')

  VariableGuid  = EfiPy.EFI_GUID (
                          0x8BE4DF61,
                          0x93CA,
                          0x11d2,
                          (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8D)
                          )

  # var = Variable ('DefaultTest', VariableGuid)
  # var.Value = bytearray (b'\x01abcde\x001234')
  # var.SetVariable ()
  # var.GetVariable ()
  # print (f'Attribute: {var.Attribute}')
  # print (f'{var.Value}, size: {len(var)}')

  var = Variable ('Boot0001')
  var.GetVariable ()
  print (f'{var.Value}, size: {len(var)}')
  print (f'{var}')