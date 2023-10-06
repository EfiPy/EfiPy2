# EfiPyTime.py
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com All rights reserved.
#
# EfiPyTime.py is free software: you can redistribute it and/or modify
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

import EfiPy2

# EFI_TIME TimeCur;
TimeCur = EfiPy2.EFI_TIME ()
# EFI_TIME_CAPABILITIES TimeCap;
TimeCap = EfiPy2.EFI_TIME_CAPABILITIES ()

# Status = gRT->GetTime (&TimeCur, &TimeCap);
Status  = EfiPy2.gRT.GetTime (EfiPy2.byref(TimeCur), EfiPy2.byref(TimeCap))

print (" gRT.GetTime(Status:0x%016X)" % Status)
print ()
print ("   Date: %4d/%02d/%02d"  % (TimeCur.Year, TimeCur.Month,  TimeCur.Day))
print ("   Time: %02d:%02d:%02d" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second))
print ()
print ("   TimeCap.Resolution: %08X" % TimeCap.Resolution)
print ("   TimeCap.Accuracy:   %d"   % TimeCap.Accuracy)
print ("   TimeCap.SetsToZero: %08X" % TimeCap.SetsToZero)
print ()

# TimeCur.Year = 2014;
TimeCur.Year = 2014
# TimeCur.Hour = 3;
TimeCur.Hour = 3

# Status = gRT->SetTime (&TimeCur);
Status  = EfiPy2.gRT.SetTime (EfiPy2.byref(TimeCur))
# Status = gRT->GetTime (&TimeCur, NULL);
Status  = EfiPy2.gRT.GetTime (EfiPy2.byref(TimeCur), None)

print (" gRT.GetTime(Status:0x%016X)" % Status)
print ()
print ("   Date: %4d/%02d/%02d"  % (TimeCur.Year, TimeCur.Month,  TimeCur.Day))
print ("   Time: %02d:%02d:%02d" % (TimeCur.Hour, TimeCur.Minute, TimeCur.Second))
print ()