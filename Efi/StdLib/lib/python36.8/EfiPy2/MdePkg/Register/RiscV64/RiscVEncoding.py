# RiscVEncoding.py
#
# EfiPy2.MdePkg.Register.RiscV64.RiscVEncoding
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
MSTATUS_SIE         = 0x00000002
MSTATUS_MIE         = 0x00000008
MSTATUS_SPIE_SHIFT  = 5
MSTATUS_SPIE        = (1 << MSTATUS_SPIE_SHIFT)
MSTATUS_UBE         = 0x00000040
MSTATUS_MPIE        = 0x00000080
MSTATUS_SPP_SHIFT   = 8
MSTATUS_SPP         = (1 << MSTATUS_SPP_SHIFT)
MSTATUS_MPP_SHIFT   = 11
MSTATUS_MPP         = (3 << MSTATUS_MPP_SHIFT)
MSTATUS_FS          = 0x00006000

SSTATUS_SIE         = MSTATUS_SIE
SSTATUS_SPIE_SHIFT  = MSTATUS_SPIE_SHIFT
SSTATUS_SPIE        = MSTATUS_SPIE
SSTATUS_SPP_SHIFT   = MSTATUS_SPP_SHIFT
SSTATUS_SPP         = MSTATUS_SPP

IRQ_S_SOFT    = 1
IRQ_VS_SOFT   = 2
IRQ_M_SOFT    = 3
IRQ_S_TIMER   = 5
IRQ_VS_TIMER  = 6
IRQ_M_TIMER   = 7
IRQ_S_EXT     = 9
IRQ_VS_EXT    = 10
IRQ_M_EXT     = 11
IRQ_S_GEXT    = 12
IRQ_PMU_OVF   = 13

MIP_SSIP    = 1 << IRQ_S_SOFT
MIP_VSSIP   = 1 << IRQ_VS_SOFT
MIP_MSIP    = 1 << IRQ_M_SOFT
MIP_STIP    = 1 << IRQ_S_TIMER
MIP_VSTIP   = 1 << IRQ_VS_TIMER
MIP_MTIP    = 1 << IRQ_M_TIMER
MIP_SEIP    = 1 << IRQ_S_EXT
MIP_VSEIP   = 1 << IRQ_VS_EXT
MIP_MEIP    = 1 << IRQ_M_EXT
MIP_SGEIP   = 1 << IRQ_S_GEXT
MIP_LCOFIP  = 1 << IRQ_PMU_OVF

SIP_SSIP  = MIP_SSIP
SIP_STIP  = MIP_STIP

PRV_U  = 0
PRV_S  = 1
PRV_M  = 3

SATP64_MODE        = 0xF000000000000000
SATP64_MODE_SHIFT  = 60
SATP64_ASID        = 0x0FFFF00000000000
SATP64_PPN         = 0x00000FFFFFFFFFFF

SATP_MODE_OFF   = 0
SATP_MODE_SV32  = 1
SATP_MODE_SV39  = 8
SATP_MODE_SV48  = 9
SATP_MODE_SV57  = 10
SATP_MODE_SV64  = 11

SATP_MODE  = SATP64_MODE

CSR_CYCLE  = 0xc00
CSR_TIME   = 0xc01

CSR_FCSR  = 0x003

CSR_SSTATUS  = 0x100
CSR_SEDELEG  = 0x102
CSR_SIDELEG  = 0x103
CSR_SIE      = 0x104
CSR_STVEC    = 0x105

CSR_SENVCFG  = 0x10a

CSR_SSCRATCH  = 0x140
CSR_SEPC      = 0x141
CSR_SCAUSE    = 0x142
CSR_STVAL     = 0x143
CSR_SIP       = 0x144

CSR_SATP  = 0x180

CSR_STIMECMP  = 0x14D

CAUSE_MISALIGNED_FETCH          = 0x0
CAUSE_FETCH_ACCESS              = 0x1
CAUSE_ILLEGAL_INSTRUCTION       = 0x2
CAUSE_BREAKPOINT                = 0x3
CAUSE_MISALIGNED_LOAD           = 0x4
CAUSE_LOAD_ACCESS               = 0x5
CAUSE_MISALIGNED_STORE          = 0x6
CAUSE_STORE_ACCESS              = 0x7
CAUSE_USER_ECALL                = 0x8
CAUSE_SUPERVISOR_ECALL          = 0x9
CAUSE_VIRTUAL_SUPERVISOR_ECALL  = 0xa
CAUSE_MACHINE_ECALL             = 0xb
CAUSE_FETCH_PAGE_FAULT          = 0xc
CAUSE_LOAD_PAGE_FAULT           = 0xd
CAUSE_STORE_PAGE_FAULT          = 0xf
CAUSE_FETCH_GUEST_PAGE_FAULT    = 0x14
CAUSE_LOAD_GUEST_PAGE_FAULT     = 0x15
CAUSE_VIRTUAL_INST_FAULT        = 0x16
CAUSE_STORE_GUEST_PAGE_FAULT    = 0x17

CSR_SEED  = 0x15

SEED_OPST_MASK     = 0xc0000000
SEED_OPST_BIST     = 0x00000000
SEED_OPST_WAIT     = 0x40000000
SEED_OPST_ES16     = 0x80000000
SEED_OPST_DEAD     = 0xc0000000
SEED_ENTROPY_MASK  = 0xffff

