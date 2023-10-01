# ServiceBinding.py
#
# EfiPy2.MdePkg.Protocol.ServiceBinding
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

class EFI_SERVICE_BINDING_PROTOCOL (Structure):
  pass

EFI_SERVICE_BINDING_CREATE_CHILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERVICE_BINDING_PROTOCOL),  # IN      *This
  POINTER(EFI_HANDLE)                     # IN  OUT *ChildHandle
  )

EFI_SERVICE_BINDING_DESTROY_CHILD = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SERVICE_BINDING_PROTOCOL),  # IN  *This
  EFI_HANDLE                              # IN  ChildHandle
  )

EFI_SERVICE_BINDING_PROTOCOL._fields_ = [
    ("CreateChild",   EFI_SERVICE_BINDING_CREATE_CHILD),
    ("DestroyChild",  EFI_SERVICE_BINDING_DESTROY_CHILD)
  ]

