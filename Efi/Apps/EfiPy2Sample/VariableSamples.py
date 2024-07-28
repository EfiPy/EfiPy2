import EfiPy2 as EfiPy
from EfiPy2.MdePkg.Guid.GlobalVariable import gEfiGlobalVariableGuid
from EfiPy2.Lib.EfiPyVariable import Variable, EfiPyVarGuid, EfiPyVarAttr

EfiPyVarAttr =  EfiPy.EFI_VARIABLE_NON_VOLATILE | EfiPy.EFI_VARIABLE_BOOTSERVICE_ACCESS | EfiPy.EFI_VARIABLE_RUNTIME_ACCESS

if __name__ == '__main__':

  print (f'Variable default GUID: {EfiPyVarGuid}')
  print (f'Variable default attribute: 0x{EfiPyVarAttr:016x}')

  print (f'==============================================================')
  var = Variable ('Boot0001')
  var.GetVariable ()
  print (f'{var.Value}\n  size: {len(var)}, Attribute: {var.Attribute}')
  print (f'{var}')
  print (f'')

  print (f'==============================================================')
  VariableGuid  = EfiPy.EFI_GUID (
                          0x8BE4DF61,
                          0x93CA,
                          0x11d2,
                          (0xAA, 0x0D, 0x00, 0xE0, 0x98, 0x03, 0x2B, 0x8D)
                          )

  var = Variable ('EfiPy2VariableTest', VariableGuid)
  var.Value = bytearray (b'\x01abcde\x001234')
  var.SetVariable ()
  var.GetVariable ()
  print (f'Attribute: {var.Attribute}')
  print (f'{var.Value}, size: {len(var)}')
