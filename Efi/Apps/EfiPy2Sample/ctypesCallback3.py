# ctypesCallback3.py
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

import EfiPy2

def EfiPy2cFunc (lPara1, lPara2, lPara3, lPara4, lPara5, lPara6, lPara7):

  print (f"   Para1: {lPara1}, {type (lPara1)}")
  print (f"   Para2: {lPara2}, {type (lPara2)}")
  print (f"   Para3: {lPara3}, {type (lPara3)}, {bool (lPara3)}, {EfiPy2.addressof (lPara3)}")

  print (f"   Para4: {lPara4}, {type (lPara4)}, {lPara4[0]}, {lPara4.contents[0]}")
  lPara4.contents[0] = 401

  print (f"   Para5: {lPara5}, {type (lPara5)}, {lPara5[0]} ** Abnormal operaiton **")

  print (f"   Para6: {lPara6}, {type (lPara6)}, {lPara6[0]} ")
  lPara6[0] = 601

  print (f"   Para7: {lPara7}, {type (lPara7)}")
  # llPara7 = (EfiPy2.UINT64 * 3).from_address (lPara7)
  llPara7 = EfiPy2.cast ((EfiPy2.UINT64 * 1).from_address (lPara7), EfiPy2.POINTER (EfiPy2.UINT64))
  print (f"   Para7: {llPara7}, {type (llPara7)}, {llPara7[0]}")
  llPara7[0] = 701

  return 0

EFIPY2_CFUNCTYPE = EfiPy2.CFUNCTYPE (
                             EfiPy2.UINT64,                       # UINT64            // Return value
                             EfiPy2.UINT64,                       # UINT64    lPara1
                             EfiPy2.UINT64,                       # UINT64    lPara2
                             EfiPy2.POINTER(EfiPy2.UINT64),       # PVOID     lPara3
                             EfiPy2.POINTER(EfiPy2.UINT64 * 3),   # *UINT64   lPara4  //
                             EfiPy2.UINT64 * 3,                   # UINT64[3] lPara5  // Abnormal operation
                             EfiPy2.POINTER(EfiPy2.UINT64),       # *UINT64   lPara6
                             EfiPy2.PVOID,                        # PVOID     lPara7
                             )

PROC = EFIPY2_CFUNCTYPE (EfiPy2cFunc)

Para1 = 100
Para2 = EfiPy2.UINT64 (200)
Para3 = None
Para4 = (EfiPy2.UINT64 * 3)(400, 410, 420)
Para5 = (EfiPy2.UINT64 * 3)(500, 510, 520)
Para6 = (EfiPy2.UINT64 * 3)(600, 610, 620)
Para7 = (EfiPy2.UINT64 * 3)(700, 710, 720)

print (f"EfiPy2 EfiPy2cFunc testing address 0x:{EfiPy2.addressof(PROC):08X}")
Status = PROC (
           Para1,                                                               # EfiPy2.UINT64,                       # UINT64   
           Para2,                                                               # EfiPy2.UINT64,                       # UINT64   
           Para3,                                                               # EfiPy2.POINTER(EfiPy2.UINT64),       # PVOID    
           EfiPy2.byref (Para4),                                                # EfiPy2.POINTER(EfiPy2.UINT64 * 3),   # *UINT64  
           Para5,                                                               # EfiPy2.UINT64 * 3,                   # UINT64[3]
           EfiPy2.cast(EfiPy2.byref (Para6), EfiPy2.POINTER(EfiPy2.UINT64)),    # EfiPy2.POINTER(EfiPy2.UINT64),       # *UINT64  
           EfiPy2.byref (Para7)                                                 # EfiPy2.PVOID,                        # PVOID    
        )

print (f"EfiPy2 EfiPy2cFunc testing result 0x:{Status:016X}")
print (f"Para4[0]: {Para4[0]}")
print (f"Para6[0]: {Para6[0]}")
print (f"Para7[0]: {Para7[0]}")