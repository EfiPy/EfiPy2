#!/usr/bin/python

#
# x86_64_exec.py
#
# Copyright (C) 2016 efipy.core@gmail.com All rights reserved.
#
# x86_64_exec.py is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy

class ExecParams (EfiPy.Structure):
  _pack_ = 1
  _fields_ = [
    ("p1", EfiPy.UINT64),
    ("p2", EfiPy.UINT64),
    ("p3", EfiPy.UINT64),
    ("p4", EfiPy.UINT64),
    ("p5", EfiPy.UINT64),
    ("p6", EfiPy.UINT64),
    ("p7", EfiPy.UINT64),
    ("p8", EfiPy.UINT64)
  ]

Stream_func_int = EfiPy.CFUNCTYPE (
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64
  )

Stream_func_fp = EfiPy.CFUNCTYPE (
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64,
  EfiPy.UINT64
  )


def make_executable (addr, size):
  return 0

def execute_int (addr, params):

  func = Stream_func_int(addr)
  
  # return func (params)
  return func (params.p1, params.p2, params.p3, params.p4, params.p5, params.p6, params.p7, params.p8)

def execute_fp (addr, params):

  func = Stream_func_fp(addr)

  return func (params.p1, params.p2, params.p3, params.p4, params.p5, params.p6, params.p7, params.p8)
