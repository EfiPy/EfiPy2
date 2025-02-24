# ctypesCallback.py
#
# Copyright (C) 2024 - 2025 efipy.core@gmail.com All rights reserved.
#
# asm.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PaTest.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import ctypes

def EfiPy2cFunc1 (Val1, Val2):

  print ("   EfiPy2cFunc1 Val1:", Val1)

  return 0

def EfiPy2cFunc2 (Val1, Val2):

  print ("   EfiPy2cFunc2 Val1:", Val1)

  # if not Val2:
  #   print ("   Get NULL pointer of Val2")
  #   return -1
  # 
  # Val2[0] = 5

  return 0


EFIPY2_CFUNCTYPE1 = ctypes.CFUNCTYPE (
                             ctypes.c_uint64,
                             ctypes.c_uint64,
                             ctypes.POINTER(ctypes.c_uint32)
                             )

EFIPY2_CFUNCTYPE2 = ctypes.CFUNCTYPE (
                             ctypes.c_uint64,
                             ctypes.c_uint64,
                             ctypes.POINTER(ctypes.c_uint32)
                             )


P1 = EFIPY2_CFUNCTYPE1 (EfiPy2cFunc1)

print ("Test New...")
print ("ctypes EfiPy2cFunc1 testing", ctypes.addressof(P1))
Status = P1 (20, None)
print ("Test Next...")
P2 = EFIPY2_CFUNCTYPE2 (EfiPy2cFunc2)
print ("Test Three...")

# print ("ctypes EfiPy2cFunc2 testing", ctypes.addressof(P2))
# Status = P2 (20, None)

print ("ctypes EfiPy2cFunc1 testing", ctypes.addressof(P1))
print ("a.................................................")
Status = P1 (20, None)
print ("Test Four...")

#
# Protocol Structure
#
class EFIPY2_SAMPLEPROTOCOL_CLASS (ctypes.Structure):
  _fields_ = [("P1Func1", EFIPY2_CFUNCTYPE1),
              ("P1Val",   ctypes.c_uint32),
              # ("P1Func2", EFIPY2_CFUNCTYPE2)
             ]

print ("Test Five...")
# EfiPy2SampleProtocol = EFIPY2_SAMPLEPROTOCOL_CLASS (P1, 3, P2)
EfiPy2SampleProtocol = EFIPY2_SAMPLEPROTOCOL_CLASS (P1, 3)
# EfiPy2SampleProtocol = EFIPY2_SAMPLEPROTOCOL_CLASS (P1, 3, P1)

print ("ctypes EfiPy2cFunc1 testing", ctypes.addressof(P1))
Status = P1 (20, None)
print ("EfiPy2SampleProtocol.P1Func1 testing", ctypes.addressof(EfiPy2SampleProtocol.P1Func1))
Status = EfiPy2SampleProtocol.P1Func1 (20, None)
print ("Test End")
