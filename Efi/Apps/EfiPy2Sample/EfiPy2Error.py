import traceback

import EfiPy2 as EfiPy

from EfiPy2.MdePkg.Protocol.SimpleTextOut import     \
                    gEfiSimpleTextOutProtocolGuid,  \
                    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL

try:
  Status = EfiPy.gBS.LocateProtocol (
             EfiPy.byref (gEfiSimpleTextOutProtocolGuid),
             None,
             EfiPy.byref (Interface)
             )

except:
  print ("Exception Test")
  print (traceback.format_exc())
