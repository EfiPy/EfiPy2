#
# PciScan.py
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# PciScan.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# PaTest.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import EfiPy2 as EfiPy
import EfiPy2.MdePkg.IndustryStandard.Pci as pci

class PciScan:

  def __init__ (self):

    import corepy.lib.printer as printer
    import corepy.arch.x86_64.isa as x86
    import corepy.arch.x86_64.types.registers as reg
    import corepy.arch.x86_64.platform as env
    import corepy.arch.x86_64.lib.memory as mem

    self.code   = env.InstructionStream()
    self.proc   = env.Processor()
    self.params = env.ExecParams()

    self.code.add(x86.mov(reg.rax, mem.MemRef(reg.rbp, 16)))
    self.code.add(x86.mov(reg.dx, 0x0cf8))
    self.code.add(x86.out(reg.dx, reg.eax))

    self.code.add(x86.mov(reg.dx, 0x0cfc))
    self.code.add(x86.in_(reg.eax, reg.dx))

  def scan (self, Bus = 0, Dev = 0, Func = 0, Reg = 0):

    reg   = pci.PCI_CONFIG_ACCESS_CF8((Reg & 0xFC, Func, Dev, Bus, 0, 1))

    self.params.p1 = reg.Uint32
    ret = self.proc.execute(self.code, params = self.params, mode = 'int')

    return ret

class PciDevUnion (pci.EFIPY_INDUSTRY_UNION):

  _fields_ = [
    ('PciReg',  pci.PCI_TYPE_GENERIC),
    ('PciRaw',  EfiPy.UINT32 * (EfiPy.sizeof (pci.PCI_TYPE_GENERIC) // (EfiPy.sizeof (EfiPy.UINT32))))
  ]

if __name__ == '__main__':

  PciDev  = PciScan()
  PciData = PciDevUnion()
  _p = PciData.PciReg.Device

  for Bus in range (pci.PCI_MAX_BUS):
    for Dev in range (pci.PCI_MAX_DEVICE):
      for Func in range (pci.PCI_MAX_FUNC):

        PciData.PciRaw[0] = PciDev.scan(Bus, Dev, Func, 0)

        if _p.Hdr.VendorId == 0xFFFF and Func == 0:
          break

        if _p.Hdr.VendorId == 0xFFFF:
          continue

        for idx in range (4, EfiPy.sizeof (pci.PCI_TYPE_GENERIC), 4):
          ret = PciDev.scan(Bus, Dev, Func, idx)
          PciData.PciRaw[idx // 4] = ret

        print ("Bus: %d, Dev: %d, Func: %d" % (Bus, Dev, Func))
        print ("  VendorID: 0x%04X, DeviceID: 0x%04X" % (_p.Hdr.VendorId, _p.Hdr.DeviceId))

        if Func == 0 and not pci.IS_PCI_MULTI_FUNC (_p):
          break