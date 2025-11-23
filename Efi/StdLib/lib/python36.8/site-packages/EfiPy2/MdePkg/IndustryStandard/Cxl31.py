# Cxl31.py
#
# EfiPy2.MdePkg.IndustryStandard.Cxl31
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Cxl20, Acpi, EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

CXL_EARLY_DISCOVERY_TABLE_REVISION_02  = 0x2

CEDT_TYPE_CSDS  = 0x4

class CXL_DOWNSTREAM_PORT_ASSOCIATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Header",          Cxl20.CEDT_STRUCTURE),
  ("Capabilities",    UINT16),
  ("Reserved",        UINT16)
  ]

