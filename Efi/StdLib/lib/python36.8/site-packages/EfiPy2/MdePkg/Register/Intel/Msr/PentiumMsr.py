# PentiumMsr.py
#
# EfiPy2.MdePkg.Register.Intel.Msr.PentiumMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

def IS_PENTIUM_PROCESSOR(DisplayFamily, DisplayModel):
   return DisplayFamily == 0x05 and (
           DisplayModel == 0x01 or
           DisplayModel == 0x02 or
           DisplayModel == 0x04
           )

MSR_PENTIUM_P5_MC_ADDR  = 0x00000000
MSR_PENTIUM_P5_MC_TYPE  = 0x00000001

MSR_PENTIUM_TSC  = 0x00000010
MSR_PENTIUM_CESR  = 0x00000011
MSR_PENTIUM_CTR0  = 0x00000012
MSR_PENTIUM_CTR1  = 0x00000013
