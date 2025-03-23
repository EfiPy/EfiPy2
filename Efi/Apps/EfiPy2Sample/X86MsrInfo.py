# X86MsrInfo.py
#
#   part of EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#

import EfiPy2 as EfiPy
from EfiPy2.Lib import Msr
from EfiPy2.Lib.X86Processor import Me, X86Processors, X86ProcessorArray
from EfiPy2.MdePkg.Register.Intel import ArchitecturalMsr as MsrReg
from EfiPy2.Lib.StructDump import DumpStruct

from typing import List

import argparse
parser = argparse.ArgumentParser (prog = 'X86MsrInfo.py')
ArgCommand = parser.add_subparsers (help = 'X86 CPU MSR operator')

parser.add_argument ('-d', '--dump', action = 'store_true', help = 'Dump mass of MSR')
parser.add_argument ('-w', '--write', action = 'store_true', help = 'Write MSR')
parser.add_argument ('-r', '--read', action = 'store_true', help = 'Read MSR')
parser.add_argument ('-c', '--ecx', type = int, help = 'ECX by Read/Write MSR register')
parser.add_argument ('-v', '--value', type = int, help = 'input value for write MSR')
parser.add_argument ('-a', '--all', action = 'store_true', help = 'MSR operation for all processor, BSP is processed if this argument is not in command parameter.')
parser.add_argument ('-p', '--processor', type = int, help = 'MSR operation for specified processor, BSP is processed if this argument is not in command parameter.')
parser.add_argument ('--verbose', action = 'store_true', help = 'Verbose output by Read/Dump MSR')

args = parser.parse_args ()

def MsrDump (processor: List[X86Processors], verbose: bool = False) -> None:
    MsrRegDict = {
        MsrReg.MSR_IA32_P5_MC_ADDR:                 Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_P5_MC_TYPE:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_MONITOR_FILTER_SIZE:        Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_TIME_STAMP_COUNTER:         Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PLATFORM_ID:                MsrReg.MSR_IA32_PLATFORM_ID_REGISTER,
        MsrReg.MSR_IA32_APIC_BASE:                  MsrReg.MSR_IA32_APIC_BASE_REGISTER,
        MsrReg.MSR_IA32_FEATURE_CONTROL:            MsrReg.MSR_IA32_FEATURE_CONTROL_REGISTER,
        MsrReg.MSR_IA32_TSC_ADJUST:                 Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_BIOS_UPDT_TRIG:             Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_BIOS_SIGN_ID:               MsrReg.MSR_IA32_BIOS_SIGN_ID_REGISTER,
        # MsrReg.MSR_IA32_SGXLEPUBKEYHASH0:           Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_SGXLEPUBKEYHASH1:           Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_SGXLEPUBKEYHASH2:           Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_SGXLEPUBKEYHASH3:           Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_SMM_MONITOR_CTL:            MsrReg.MSR_IA32_SMM_MONITOR_CTL_REGISTER,
        # MsrReg.MSR_IA32_SMBASE:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC0:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC1:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC2:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC3:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC4:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC5:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC6:                       Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PMC7:                       Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_MPERF:                      Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_APERF:                      Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRRCAP:                    MsrReg.MSR_IA32_MTRRCAP_REGISTER,
        MsrReg.MSR_IA32_SYSENTER_CS:                MsrReg.MSR_IA32_SYSENTER_CS_REGISTER,
        MsrReg.MSR_IA32_SYSENTER_ESP:               Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_SYSENTER_EIP:               Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MCG_CAP:                    MsrReg.MSR_IA32_MCG_CAP_REGISTER,

        MsrReg.MSR_IA32_MCG_STATUS:                 MsrReg.MSR_IA32_MCG_STATUS_REGISTER,
        # MsrReg.MSR_IA32_MCG_CTL:                    Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PERFEVTSEL0:                MsrReg.MSR_IA32_PERFEVTSEL_REGISTER,
        MsrReg.MSR_IA32_PERFEVTSEL1:                MsrReg.MSR_IA32_PERFEVTSEL_REGISTER,
        MsrReg.MSR_IA32_PERFEVTSEL2:                MsrReg.MSR_IA32_PERFEVTSEL_REGISTER,
        MsrReg.MSR_IA32_PERFEVTSEL3:                MsrReg.MSR_IA32_PERFEVTSEL_REGISTER,
        MsrReg.MSR_IA32_PERF_CTL:                   MsrReg.MSR_IA32_PERF_CTL_REGISTER,
        ## MsrReg.MSR_IA32_CLOCK_MODULATION:           MsrReg.MSR_IA32_CLOCK_MODULATION_REGISTER,
        ## MsrReg.MSR_IA32_THERM_INTERRUPT:            MsrReg.MSR_IA32_THERM_INTERRUPT_REGISTER,
        ## MsrReg.MSR_IA32_THERM_STATUS:               MsrReg.MSR_IA32_THERM_STATUS_REGISTER,
        MsrReg.MSR_IA32_MISC_ENABLE:                MsrReg.MSR_IA32_MISC_ENABLE_REGISTER,
        ## MsrReg.MSR_IA32_ENERGY_PERF_BIAS:           MsrReg.MSR_IA32_ENERGY_PERF_BIAS_REGISTER,
        ## MsrReg.MSR_IA32_PACKAGE_THERM_STATUS:       MsrReg.MSR_IA32_PACKAGE_THERM_STATUS_REGISTER,
        ## MsrReg.MSR_IA32_PACKAGE_THERM_INTERRUPT:    MsrReg.MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER,
        MsrReg.MSR_IA32_DEBUGCTL:                   MsrReg.MSR_IA32_DEBUGCTL_REGISTER,
        ## MsrReg.MSR_IA32_SMRR_PHYSBASE:              MsrReg.MSR_IA32_SMRR_PHYSBASE_REGISTER,
        ## MsrReg.MSR_IA32_SMRR_PHYSMASK:              MsrReg.MSR_IA32_SMRR_PHYSMASK_REGISTER,
        # MsrReg.MSR_IA32_PLATFORM_DCA_CAP:           Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_CPU_DCA_CAP:                Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_DCA_0_CAP:                  MsrReg.MSR_IA32_DCA_0_CAP_REGISTER,

        MsrReg.MSR_IA32_MTRR_PHYSBASE0:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE1:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE2:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE3:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE4:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE5:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE6:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSBASE7:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        ## MsrReg.MSR_IA32_MTRR_PHYSBASE8:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,
        ## MsrReg.MSR_IA32_MTRR_PHYSBASE9:             MsrReg.MSR_IA32_MTRR_PHYSBASE_REGISTER,

        MsrReg.MSR_IA32_MTRR_PHYSMASK0:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK1:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK2:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK3:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK4:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK5:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK6:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        MsrReg.MSR_IA32_MTRR_PHYSMASK7:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        ## MsrReg.MSR_IA32_MTRR_PHYSMASK8:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,
        ## MsrReg.MSR_IA32_MTRR_PHYSMASK9:             MsrReg.MSR_IA32_MTRR_PHYSMASK_REGISTER,

        MsrReg.MSR_IA32_MTRR_FIX64K_00000:          Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX16K_80000:          Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX16K_A0000:          Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_C0000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_C8000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_D0000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_D8000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_E0000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_E8000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_F0000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_MTRR_FIX4K_F8000:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PAT:                        MsrReg.MSR_IA32_PAT_REGISTER,

        ## MsrReg.MSR_IA32_MC0_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC1_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC2_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC3_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC4_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC5_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC6_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC7_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC8_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC9_CTL2:                   MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC10_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC11_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC12_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC13_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC14_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC15_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC16_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC17_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC18_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC19_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC20_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC21_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC22_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC23_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC24_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC25_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC26_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC27_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC28_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC29_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC30_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MC31_CTL2:                  MsrReg.MSR_IA32_MC_CTL2_REGISTER,
        ## MsrReg.MSR_IA32_MTRR_DEF_TYPE:              MsrReg.MSR_IA32_MTRR_DEF_TYPE_REGISTER,

        MsrReg.MSR_IA32_FIXED_CTR0:                 Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_FIXED_CTR1:                 Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_FIXED_CTR2:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_FIXED_CTR3:                 Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_FIXED_CTR4:                 Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_FIXED_CTR5:                 Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_FIXED_CTR6:                 Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_PERF_CAPABILITIES:          MsrReg.MSR_IA32_PERF_CAPABILITIES_REGISTER,
        MsrReg.MSR_IA32_FIXED_CTR_CTRL:             MsrReg.MSR_IA32_FIXED_CTR_CTRL_REGISTER,
        MsrReg.MSR_IA32_PERF_GLOBAL_STATUS:         MsrReg.MSR_IA32_PERF_GLOBAL_STATUS_REGISTER,
        MsrReg.MSR_IA32_PERF_GLOBAL_CTRL:           MsrReg.MSR_IA32_PERF_GLOBAL_CTRL_REGISTER,
        ## MsrReg.MSR_IA32_PERF_GLOBAL_OVF_CTRL:       MsrReg.MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER,
        ## MsrReg.MSR_IA32_PERF_GLOBAL_STATUS_RESET:   MsrReg.MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER,
        ## MsrReg.MSR_IA32_PERF_GLOBAL_STATUS_SET:     MsrReg.MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER,
        ## MsrReg.MSR_IA32_PERF_GLOBAL_INUSE:          MsrReg.MSR_IA32_PERF_GLOBAL_INUSE_REGISTER,
        ## MsrReg.MSR_IA32_PEBS_ENABLE:                MsrReg.MSR_IA32_PEBS_ENABLE_REGISTER,

        MsrReg.MSR_IA32_MC0_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC1_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC2_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC3_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC4_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC5_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC6_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC7_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC8_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC9_CTL:                    Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC10_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC11_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC12_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC13_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC14_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC15_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC16_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC17_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC18_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC19_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC20_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC21_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC22_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC23_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC24_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC25_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC26_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC27_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC28_CTL:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC0_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC1_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC2_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC3_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC4_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC5_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC6_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC7_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC8_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC9_STATUS:                 Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC10_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC11_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC12_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC13_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC14_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC15_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC16_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC17_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC18_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC19_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC20_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC21_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC22_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC23_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC24_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC25_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC26_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC27_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC28_STATUS:                Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC0_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC1_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC2_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC3_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC4_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC5_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC6_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC7_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC8_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC9_ADDR:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC10_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC11_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC12_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC13_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC14_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC15_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC16_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC17_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC18_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC19_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC20_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC21_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC22_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC23_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC24_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC25_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC26_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC27_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC28_ADDR:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC0_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC1_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC2_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC3_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC4_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC5_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC6_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC7_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC8_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        MsrReg.MSR_IA32_MC9_MISC:                   Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC10_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC11_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC12_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC13_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC14_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC15_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC16_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC17_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC18_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC19_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC20_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC21_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC22_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC23_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC24_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC25_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC26_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC27_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3
        ## MsrReg.MSR_IA32_MC28_MISC:                  Msr.MSR_GENERIC_REGISTER,    # SDM Vol 3

        MsrReg.MSR_IA32_VMX_BASIC:                  MsrReg.MSR_IA32_VMX_BASIC_REGISTER,

        MsrReg.MSR_IA32_VMX_PINBASED_CTLS:          Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_PROCBASED_CTLS:         Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_EXIT_CTLS:              Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_ENTRY_CTLS:             Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_MISC:                   MsrReg.IA32_VMX_MISC_REGISTER,

        MsrReg.MSR_IA32_VMX_CR0_FIXED0:             Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_CR4_FIXED0:             Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_CR4_FIXED1:             Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_VMCS_ENUM:              Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_PROCBASED_CTLS2:        Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_EPT_VPID_CAP:           Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_TRUE_PINBASED_CTLS:     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_TRUE_PROCBASED_CTLS:    Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_TRUE_EXIT_CTLS:         Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_TRUE_ENTRY_CTLS:        Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_VMX_VMFUNC:                 Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC0:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC1:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC2:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC3:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC4:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC5:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC6:                     Msr.MSR_GENERIC_REGISTER,
        MsrReg.MSR_IA32_A_PMC7:                     Msr.MSR_GENERIC_REGISTER,

        # MsrReg.MSR_IA32_MCG_EXT_CTL:                MsrReg.MSR_IA32_MCG_EXT_CTL_REGISTER,
        # MsrReg.MSR_IA32_SGX_SVN_STATUS:             MsrReg.MSR_IA32_SGX_SVN_STATUS_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_OUTPUT_BASE:           MsrReg.MSR_IA32_RTIT_OUTPUT_BASE_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_OUTPUT_MASK_PTRS:      MsrReg.MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_CTL:                   MsrReg.MSR_IA32_RTIT_CTL_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_STATUS:                MsrReg.MSR_IA32_RTIT_STATUS_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_CR3_MATCH:             MsrReg.MSR_IA32_RTIT_CR3_MATCH_REGISTER,

        ## MsrReg.MSR_IA32_RTIT_ADDR0_A:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_ADDR1_A:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        # MsrReg.MSR_IA32_RTIT_ADDR2_A:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        # MsrReg.MSR_IA32_RTIT_ADDR3_A:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_ADDR0_B:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        ## MsrReg.MSR_IA32_RTIT_ADDR1_B:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        # MsrReg.MSR_IA32_RTIT_ADDR2_B:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,
        # MsrReg.MSR_IA32_RTIT_ADDR3_B:               MsrReg.MSR_IA32_RTIT_ADDR_REGISTER,

        ## MsrReg.MSR_IA32_DS_AREA:                    Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_TSC_DEADLINE:               Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_PM_ENABLE:                  MsrReg.MSR_IA32_PM_ENABLE_REGISTER,
        # MsrReg.MSR_IA32_HWP_CAPABILITIES:           MsrReg.MSR_IA32_HWP_CAPABILITIES_REGISTER,
        # MsrReg.MSR_IA32_HWP_REQUEST_PKG:            MsrReg.MSR_IA32_HWP_REQUEST_PKG_REGISTER,
        ## MsrReg.MSR_IA32_HWP_INTERRUPT:              MsrReg.MSR_IA32_HWP_INTERRUPT_REGISTER,
        # MsrReg.MSR_IA32_HWP_REQUEST:                MsrReg.MSR_IA32_HWP_REQUEST_REGISTER,
        # MsrReg.MSR_IA32_HWP_STATUS:                 MsrReg.MSR_IA32_HWP_STATUS_REGISTER,

        ## MsrReg.MSR_IA32_X2APIC_APICID:              Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_VERSION:             Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TPR:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_PPR:                 Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_X2APIC_EOI:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LDR:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_SIVR:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR0:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR1:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR2:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR3:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR4:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR5:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR6:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ISR7:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR0:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR1:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR2:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR3:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR4:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR5:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR6:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_TMR7:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR0:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR1:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR2:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR3:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR4:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR5:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR6:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_IRR7:                Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ESR:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_CMCI:            Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_ICR:                 Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_TIMER:           Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_THERMAL:         Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_PMI:             Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_LINT0:           Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_LINT1:           Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_LVT_ERROR:           Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_INIT_COUNT:          Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_X2APIC_CUR_COUNT:           Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_X2APIC_DIV_CONF:            Msr.MSR_GENERIC_REGISTER,
        # MsrReg.MSR_IA32_X2APIC_SELF_IPI:            Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_TME_ACTIVATE:               MsrReg.MSR_IA32_TME_ACTIVATE_REGISTER,

        ## MsrReg.MSR_IA32_DEBUG_INTERFACE:            MsrReg.MSR_IA32_DEBUG_INTERFACE_REGISTER,
        # MsrReg.MSR_IA32_L3_QOS_CFG:                 MsrReg.MSR_IA32_L3_QOS_CFG_REGISTER,
        ## MsrReg.MSR_IA32_L2_QOS_CFG:                 MsrReg.MSR_IA32_L2_QOS_CFG_REGISTER,
        # MsrReg.MSR_IA32_QM_EVTSEL:                  MsrReg.MSR_IA32_QM_EVTSEL_REGISTER,
        # MsrReg.MSR_IA32_QM_CTR:                     MsrReg.MSR_IA32_QM_CTR_REGISTER,
        ## MsrReg.MSR_IA32_PQR_ASSOC:                  MsrReg.MSR_IA32_PQR_ASSOC_REGISTER,
        # MsrReg.MSR_IA32_BNDCFGS:                    MsrReg.MSR_IA32_BNDCFGS_REGISTER,
        ## MsrReg.MSR_IA32_XSS:                        MsrReg.MSR_IA32_XSS_REGISTER,
        # MsrReg.MSR_IA32_PKG_HDC_CTL:                MsrReg.MSR_IA32_PKG_HDC_CTL_REGISTER,
        # MsrReg.MSR_IA32_PM_CTL1:                    MsrReg.MSR_IA32_PM_CTL1_REGISTER,
        # MsrReg.MSR_IA32_THREAD_STALL:               Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_EFER:                       MsrReg.MSR_IA32_EFER_REGISTER,
        ## MsrReg.MSR_IA32_STAR:                       Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_LSTAR:                      Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_CSTAR:                      Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_FMASK:                      Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_FS_BASE:                    Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_GS_BASE:                    Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_KERNEL_GS_BASE:             Msr.MSR_GENERIC_REGISTER,
        ## MsrReg.MSR_IA32_TSC_AUX:                    MsrReg.MSR_IA32_TSC_AUX_REGISTER,
    }

    for r, s in MsrRegDict.items():
      v = s ()
      print (f'0x{r:08X}...')
      for p in Processors:
        p.RdMsr (r, v)
        if verbose == False:
          print (f'    processor: {p.Index:2d}: 0x{v.Uint64:016X}')
        else:
          print (f'    processor: {p.Index:2d}:')
          DumpStruct (6, v, s)

def MsrWrite(processor: List[X86Processors], ecx: int, value: int) -> None:
    print (f'MsrWrite, processor: {processor.Index}, ecx: 0x{ecx:08X}, value: 0x{value:016X}')
    for p in Processors:
      v = EfiPy.UINT64 (value)
      p.WrMsr (ecx, v)

def MsrRead (processor: List[X86Processors], ecx: int, verbose: bool = False) -> int:
    print (f'MsrRead , processor: {processor.Index}, ecx: 0x{ecx:08X}, verbose: {verbose}')
    for p in Processors:
      v = Msr.MSR_GENERIC_REGISTER (0)
      p.RdMsr (ecx, v)
      print (f'    processor: {p.Index:2d}: 0x{v.Uint64:016X}')

if args.all:
    Processors = X86ProcessorArray
elif args.processor in tuple (range(len(X86ProcessorArray))):
    Processors = [X86ProcessorArray[args.processor]]
else:
    Processors = [Me]

if args.dump:
    MsrDump (Processors, args.verbose)
elif args.write:
    MsrWrite (Processors)
elif args.read:
    MsrRead (Processors, args.verbose)
else:
    print (f'Read, Write or dump is one of required parameter in X86MsrInfo')
    exit(-1)
