# ResetNotification.py
#
# EfiPy2.MdePkg.Protocol.ResetNotification
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiResetNotificationProtocolGuid           = \
  EFI_GUID (0x9da34ae0, 0xeaf9, 0x4bbf, ( 0x8e, 0xc3, 0xfd, 0x60, 0x22, 0x6c, 0x44, 0xbe ))

class EFI_RESET_NOTIFICATION_PROTOCOL (Structure):
  pass

EFI_REGISTER_RESET_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_RESET_NOTIFICATION_PROTOCOL), # IN *This
  EFI_RESET_SYSTEM                          # IN ResetFunction
  )

EFI_UNREGISTER_RESET_NOTIFY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_RESET_NOTIFICATION_PROTOCOL), # IN *This
  EFI_RESET_SYSTEM                          # IN ResetFunction
  )

EFI_RESET_NOTIFICATION_PROTOCOL._fields_ = [
    ("RegisterResetNotify",     EFI_REGISTER_RESET_NOTIFY),
    ("UnregisterResetNotify",   EFI_UNREGISTER_RESET_NOTIFY)
  ]

