# DevicePathEfiPy.py
#
# EfiPy2.MdePkg.Protocol.DevicePathEfiPy
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2                                     import *
from EfiPy2.MdePkg.Protocol.DevicePath          import *
from EfiPy2.MdePkg.Protocol.DevicePathToText    import *

DevToTextProtocol = None

if DevToTextProtocol == None:
  Interface = PVOID ()
  Status = gBS.LocateProtocol (byref (gEfiDevicePathToTextProtocolGuid), None, byref (Interface))
  if not EFI_ERROR (Status):
    DevToTextProtocol = cast (Interface, POINTER(EFI_DEVICE_PATH_TO_TEXT_PROTOCOL))[0]

def EfiPyDevToText (self):

  if DevToTextProtocol == None:
    return None

  return DevToTextProtocol.ConvertDevicePathToText (self, self.DisplayOnly, self.AllowShortcuts)

  return u"TestBook"

EFIPY_DEVICE_PATH_STRUCTURE.__str__ = EfiPyDevToText
EFI_DEVICE_PATH_PROTOCOL.__str__    = EfiPyDevToText
