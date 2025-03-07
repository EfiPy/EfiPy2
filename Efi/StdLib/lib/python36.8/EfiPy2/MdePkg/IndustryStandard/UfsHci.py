# UfsHci.py
#
# EfiPy2.MdePkg.IndustryStandard.UfsHci
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import Ufs, EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION

UFS_HC_CAP_OFFSET   = 0x0000
UFS_HC_VER_OFFSET   = 0x0008
UFS_HC_DDID_OFFSET  = 0x0010
UFS_HC_PMID_OFFSET  = 0x0014
UFS_HC_AHIT_OFFSET  = 0x0018

UFS_HC_IS_OFFSET       = 0x0020
UFS_HC_IE_OFFSET       = 0x0024
UFS_HC_STATUS_OFFSET   = 0x0030
UFS_HC_ENABLE_OFFSET   = 0x0034
UFS_HC_UECPA_OFFSET    = 0x0038
UFS_HC_UECDL_OFFSET    = 0x003c
UFS_HC_UECN_OFFSET     = 0x0040
UFS_HC_UECT_OFFSET     = 0x0044
UFS_HC_UECDME_OFFSET   = 0x0048
UFS_HC_UTRIACR_OFFSET  = 0x004c

UFS_HC_UTRLBA_OFFSET   = 0x0050
UFS_HC_UTRLBAU_OFFSET  = 0x0054
UFS_HC_UTRLDBR_OFFSET  = 0x0058
UFS_HC_UTRLCLR_OFFSET  = 0x005c
UFS_HC_UTRLRSR_OFFSET  = 0x0060

UFS_HC_UTMRLBA_OFFSET   = 0x0070
UFS_HC_UTMRLBAU_OFFSET  = 0x0074
UFS_HC_UTMRLDBR_OFFSET  = 0x0078
UFS_HC_UTMRLCLR_OFFSET  = 0x007c
UFS_HC_UTMRLRSR_OFFSET  = 0x0080

UFS_HC_UIC_CMD_OFFSET    = 0x0090
UFS_HC_UCMD_ARG1_OFFSET  = 0x0094
UFS_HC_UCMD_ARG2_OFFSET  = 0x0098
UFS_HC_UCMD_ARG3_OFFSET  = 0x009c

UFS_HC_UMA_OFFSET  = 0x00b0

UFS_HC_HCE_EN      = BIT0
UFS_HC_HCS_DP      = BIT0
UFS_HC_HCS_UCRDY   = BIT3
UFS_HC_IS_ULSS     = BIT8
UFS_HC_IS_UCCS     = BIT10
UFS_HC_CAP_64ADDR  = BIT24
UFS_HC_CAP_NUTMRS  = (BIT16 | BIT17 | BIT18)
UFS_HC_CAP_NUTRS   = (BIT0 | BIT1 | BIT2 | BIT3 | BIT4)
UFS_HC_UTMRLRSR    = BIT0
UFS_HC_UTRLRSR     = BIT0

UFS_HC_TRD_OCS_INIT_VALUE  = 0x0F

UFS_MAX_DATA_LEN_PER_PRD  = 0x40000

UFS_STORAGE_COMMAND_TYPE  = 0x01

UFS_REGULAR_COMMAND    = 0x00
UFS_INTERRUPT_COMMAND  = 0x01

class UFS_HC_CAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Nutrs",     UINT8, 4),
  ("Rsvd1",     UINT8, 4),
  ("NoRtt",     UINT8),
  ("Nutmrs",    UINT8, 3),
  ("Rsvd2",     UINT8, 4),
  ("AutoHs",    UINT8, 1),
  ("As64",      UINT8, 1),
  ("Oodds",     UINT8, 1),
  ("UicDmetms", UINT8, 1),
  ("Ume",       UINT8, 1),
  ("Rsvd4",     UINT8, 4)
  ]

class UFS_HC_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Vs",    UINT8, 4),
  ("Mnr",   UINT8, 4),
  ("Mjr",   UINT8),
  ("Rsvd1", UINT16)
  ]

UFS_HC_PID  = UINT32

UFS_HC_MID  = UINT32

class UFS_HC_AHIT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ahitv",     UINT32, 10),
  ("Ts",        UINT32, 3),
  ("Rsvd1",     UINT32, 19)
  ]

class UFS_HC_IS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Utrcs",         UINT16, 1),
  ("Udepri",        UINT16, 1),
  ("Ue",            UINT16, 1),
  ("Utms",          UINT16, 1),
  ("Upms",          UINT16, 1),
  ("Uhxs",          UINT16, 1),
  ("Uhes",          UINT16, 1),
  ("Ulls",          UINT16, 1),
  ("Ulss",          UINT16, 1),
  ("Utmrcs",        UINT16, 1),
  ("Uccs",          UINT16, 1),
  ("Dfes",          UINT16, 1),
  ("Utpes",         UINT16, 1),
  ("Rsvd1",         UINT16, 3),
  ("Hcfes",         UINT16, 1),
  ("Sbfes",         UINT16, 1),
  ("Rsvd2",         UINT16, 14)
  ]

class UFS_HC_IE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Utrce",     UINT16, 1),
  ("Udeprie",   UINT16, 1),
  ("Uee",       UINT16, 1),
  ("Utmse",     UINT16, 1),
  ("Upmse",     UINT16, 1),
  ("Uhxse",     UINT16, 1),
  ("Uhese",     UINT16, 1),
  ("Ullse",     UINT16, 1),
  ("Ulsse",     UINT16, 1),
  ("Utmrce",    UINT16, 1),
  ("Ucce",      UINT16, 1),
  ("Dfee",      UINT16, 1),
  ("Utpee",     UINT16, 1),
  ("Rsvd1",     UINT16, 3),
  ("Hcfee",     UINT16, 1),
  ("Sbfee",     UINT16, 1),
  ("Rsvd2",     UINT16, 14)
  ]

class UFS_HC_STATUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Dp",        UINT8, 1),
  ("UtrlRdy",   UINT8, 1),
  ("UtmrlRdy",  UINT8, 1),
  ("UcRdy",     UINT8, 1),
  ("Rsvd1",     UINT8, 4),
  ("Upmcrs",    UINT8, 3),
  ("Rsvd2",     UINT8, 1),
  ("Utpec",     UINT8, 4),
  ("TtagUtpE",  UINT8),
  ("TlunUtpE",  UINT8)
  ]

class UFS_HC_ENABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Hce",       UINT32, 1),
  ("Rsvd1",     UINT32, 31)
  ]

class UFS_HC_UECPA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ec",        UINT32, 5),
  ("Rsvd1",     UINT32, 26),
  ("Err",       UINT32, 1)
  ]

class UFS_HC_UECDL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ec",        UINT32, 15),
  ("Rsvd1",     UINT32, 16),
  ("Err",       UINT32, 1)
  ]

class UFS_HC_UECN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ec",        UINT32, 3),
  ("Rsvd1",     UINT32, 28),
  ("Err",       UINT32, 1)
  ]

class UFS_HC_UECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ec",        UINT32, 7),
  ("Rsvd1",     UINT32, 24),
  ("Err",       UINT32, 1)
  ]

class UFS_HC_UECDME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Ec",        UINT32, 1),
  ("Rsvd1",     UINT32, 30),
  ("Err",       UINT32, 1)
  ]

class UFS_HC_UTRIACR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("IaToVal",       UINT8),
  ("IacTh",         UINT8, 5),
  ("Rsvd1",         UINT8, 3),
  ("Ctr",           UINT8, 1),
  ("Rsvd2",         UINT8, 3),
  ("Iasb",          UINT8, 1),
  ("Rsvd3",         UINT8, 3),
  ("IapwEn",        UINT8, 1),
  ("Rsvd4",         UINT8, 6),
  ("IaEn",          UINT8, 1)
  ]

class UFS_HC_UTRLBA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Rsvd1",     UINT32, 10),
  ("UtrlBa",    UINT32, 22)
  ]

UFS_HC_UTRLBAU  = UINT32

UFS_HC_UTRLDBR  = UINT32

UFS_HC_UTRLCLR  = UINT32

if False:
  class UFS_HC_UTRLRSR (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
    ("UtrlRsr",   UINT32, 1),
    ("Rsvd1",     UINT32, 31)
    ]

class UFS_HC_UTMRLBA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Rsvd1",     UINT32, 10),
  ("UtmrlBa",   UINT32, 22)
  ]

UFS_HC_UTMRLBAU  = UINT32

class UFS_HC_UTMRLDBR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("UtmrlDbr",      UINT32, 8),
  ("Rsvd1",         UINT32, 24)
  ]

class UFS_HC_UTMRLCLR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("UtmrlClr",      UINT32, 8),
  ("Rsvd1",         UINT32, 24)
  ]

if False:
    class UFS_HC_UTMRLRSR (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = [
      ("UtmrlRsr",      UINT32, 1),
      ("Rsvd1",         UINT32, 31)
      ]

class UFS_HC_UICCMD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("CmdOp",         UINT32, 8),
  ("Rsvd1",         UINT32, 24)
  ]

UFS_HC_UICCMD_ARG1  = UINT32

UFS_HC_UICCMD_ARG2  = UINT32

UFS_HC_UICCMD_ARG3  = UINT32

UfsUicDmeGet            = 0x01
UfsUicDmeSet            = 0x02
UfsUicDmePeerGet        = 0x03
UfsUicDmePeerSet        = 0x04
UfsUicDmePwrOn          = 0x10
UfsUicDmePwrOff         = 0x11
UfsUicDmeEnable         = 0x12
UfsUicDmeReset          = 0x14
UfsUicDmeEndpointReset  = 0x15
UfsUicDmeLinkStartup    = 0x16
UfsUicDmeHibernateEnter = 0x17
UfsUicDmeHibernateExit  = 0x18
UfsUicDmeTestMode       = 0x1A
UFS_UIC_OPCODE          = ENUM

class UTP_TRD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Rsvd1",     UINT32, 24),
  ("Int",       UINT32, 1),
  ("Dd",        UINT32, 2),
  ("Rsvd2",     UINT32, 1),
  ("Ct",        UINT32, 4),
  ("Rsvd3",     UINT32),
  ("Ocs",       UINT32, 8),
  ("Rsvd4",     UINT32, 24),
  ("Rsvd5",     UINT32),
  ("Rsvd6",     UINT32, 7),
  ("UcdBa",     UINT32, 25),
  ("UcdBaU",    UINT32),
  ("RuL",       UINT16),
  ("RuO",       UINT16),
  ("PrdtL",     UINT16),
  ("PrdtO",     UINT16)
  ]

UfsNoData           = 0
UfsDataOut          = 1
UfsDataIn           = 2
UfsDdReserved       = 3
UFS_DATA_DIRECTION  = ENUM

class UTP_TR_PRD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Rsvd1",         UINT32, 2),
  ("DbAddr",        UINT32, 30),
  ("DbAddrU",       UINT32),
  ("Rsvd2",         UINT32),
  ("DbCount",       UINT32, 18),
  ("Rsvd3",         UINT32, 14)
  ]

class UTP_TMRD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
  ("Rsvd1",         UINT32, 24),
  ("Int",           UINT32, 1),
  ("Rsvd2",         UINT32, 7),
  ("Rsvd3",         UINT32),
  ("Ocs",           UINT32, 8),
  ("Rsvd4",         UINT32, 24),
  ("Rsvd5",         UINT32),
  ("TmReq",         Ufs.UTP_TM_REQ_UPIU),
  ("TmResp",        Ufs.UTP_TM_RESP_UPIU)
  ]

