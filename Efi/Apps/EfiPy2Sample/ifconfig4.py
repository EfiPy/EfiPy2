#!/usr/bin/python

#
# ifconfig4.py
#
# Copyright (C) 2018 - 2024 MaxWu efipy.core@gmail.com All rights reserved.
#
# ifconfig4.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy2.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import EfiPy2 as e
from EfiPy2.MdePkg.Protocol.Ip4          import gEfiIp4ServiceBindingProtocolGuid
import EfiPy2.MdePkg.Protocol.Ip4Config2 as Ip4Cfg2

def GetIfConfig4Info (IfName = None):

  HandleArrayCount = e.UINTN()
  HandleArray      = e.POINTER (e.EFI_HANDLE)()
  Status = e.gBS.LocateHandleBuffer (
                   e.ByProtocol,
                   e.byref (gEfiIp4ServiceBindingProtocolGuid),
                   None,
                   e.byref (HandleArrayCount),
                   e.byref (HandleArray)
                   )
  if e.EFI_ERROR (Status):
    print (f"Locate gEfiIp4ServiceBindingProtocolGuid Protocol Error (Status:0x{Status:08X})")
    return
  print (f"Locate gEfiIp4ServiceBindingProtocolGuid Protocol Success ({HandleArrayCount.value})")

  for Index in range (HandleArrayCount.value):

    print ("===========================================================")

    TempV = e.PVOID ()
    Status = e.gBS.HandleProtocol (
              HandleArray[Index],
              e.byref (Ip4Cfg2.gEfiIp4Config2ProtocolGuid),
              e.byref (TempV)
              )
    if e.EFI_ERROR (Status):
      print (f"HandleProtocol gEfiIp4Config2ProtocolGuid fail: 0x{Status:08X}")
      continue
    print (f"HandleProtocol gEfiIp4Config2ProtocolGuid ({Index}):")

    #
    # Get the interface information size.
    #
    DataSize = e.UINTN()
    Ip4Cfg2P = e.cast (TempV, e.POINTER (Ip4Cfg2.EFI_IP4_CONFIG2_PROTOCOL))
    Status = Ip4Cfg2P[0].GetData (
                         Ip4Cfg2P,
                         Ip4Cfg2.Ip4Config2DataTypeInterfaceInfo,
                         e.byref (DataSize),
                         None
                         )

    if Status != e.EFI_BUFFER_TOO_SMALL and Status != e.EFI_NOT_FOUND:
      print (f"Ip4Cfg2P GetData Ip4Config2DataTypeInterfaceInfo (1) fail: 0x{Status:08}")
      continue
    print (f"   Ip4Cfg2P GetData Ip4Config2DataTypeInterfaceInfo (1) size: 0x{DataSize.value:08X}")

    #
    # Get the interface info.
    #
    IfInfo = Ip4Cfg2.EFI_IP4_CONFIG2_INTERFACE_INFO ()
    Status = Ip4Cfg2P[0].GetData (
                       Ip4Cfg2P,
                       Ip4Cfg2.Ip4Config2DataTypeInterfaceInfo,
                       e.byref (DataSize),
                       e.cast (e.byref (IfInfo), e.PVOID)
                       )
    if e.EFI_ERROR (Status):
      print (f"Ip4Cfg2P GetData Ip4Config2DataTypeInterfaceInfo (2) fail: 0x{Status:08X}")
      continue
    print ("   Ip4Cfg2P GetData Ip4Config2DataTypeInterfaceInfo (2) Done", end = '')

    #
    # Check the interface name if required.
    #
    # BUGBUG: String compare
    #
    if IfName != None and IfName != IfInfo.Name:
      continue;

    print (f"""
    IfInfo.Name:           {IfInfo.Name}
    IfInfo.IfType:         {IfInfo.IfType}
    IfInfo.HwAddressSize:  {IfInfo.HwAddressSize}""")

    print ("   IfInfo.HwAddress:      ", end = '')
    for hwA in IfInfo.HwAddress.Addr[:IfInfo.HwAddressSize]:
      print (f"{hwA:02X} ", end = '')
    print ("")

    print ("   IfInfo.StationAddress: ", end = '')
    for Addr in IfInfo.StationAddress.Addr:
      print (f"{Addr:02X} ", end = '')
    print ("")

    print ("   IfInfo.SubnetMask:     ", end = '')
    for Addr in IfInfo.SubnetMask.Addr:
      print (f"{Addr:02X} ", end = '')

    print (f"""
   IfInfo.RouteTableSize: {IfInfo.RouteTableSize}""")

    #
    # Get the size of dns server list.
    #
    DataSize.value = 0
    Status = Ip4Cfg2P[0].GetData (
                           Ip4Cfg2P,
                           Ip4Cfg2.Ip4Config2DataTypeDnsServer,
                           e.byref (DataSize),
                           None
                           )

    if Status != e.EFI_BUFFER_TOO_SMALL and Status != e.EFI_NOT_FOUND:
      print (f"Ip4Cfg2P Ip4Config2DataTypeDnsServer (1) fail: 0x{Status:08X}")
      continue
    print (f"   Ip4Cfg2P GetData Ip4Config2DataTypeDnsServer (1) size: 0x{DataSize.value:08X}")

    if DataSize.value != 0:

      DnsAddr = (e.EFI_IPv4_ADDRESS * (DataSize.value // e.sizeof (e.EFI_IPv4_ADDRESS))) ()

      #
      # Get the dns server list if has.
      #
      Status = Ip4Cfg2P[0].GetData (
                            Ip4Cfg2P,
                            Ip4Cfg2.Ip4Config2DataTypeDnsServer,
                            e.byref (DataSize),
                            e.cast (e.byref (DnsAddr), e.PVOID)
                            )

      if e.EFI_ERROR (Status):
        print (f"Ip4Cfg2P Ip4Config2DataTypeDnsServer (2) fail: 0x{Status:08X}")
        continue
      print (f"   Ip4Cfg2P GetData Ip4Config2DataTypeDnsServer (2) Done")

      for Dns in DnsAddr:
        print ("   DnsAddr:")
        for Addr in Dns.Addr:
          print (f"{Addr:02X} ", end = '')
        print

    #
    # Get the config policy.
    #
    DataSize.value = e.sizeof (Ip4Cfg2.EFI_IP4_CONFIG2_POLICY)
    Policy = e.ENUM ()
    Status = Ip4Cfg2P[0].GetData (
                           Ip4Cfg2P,
                           Ip4Cfg2.Ip4Config2DataTypePolicy,
                           e.byref (DataSize),
                           e.cast (e.byref (Policy), e.PVOID)
                           )

    if e.EFI_ERROR (Status):
      print (f"Ip4Cfg2P Ip4Config2DataTypePolicy (1) fail: 0x{Status:08X}")
      continue
    print (f"   Ip4Cfg2P GetData Ip4Config2DataTypePolicy (1) Done, value: {Policy.value}")

  print ("===========================================================")

if __name__ == '__main__':

  GetIfConfig4Info ()