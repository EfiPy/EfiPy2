# Nvme.py
#
# EfiPy2.MdePkg.IndustryStandard.Nvme
#   part of EfiPy2
#
# Copyright (C) 2023 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

NVME_CAP_OFFSET     = 0x0000        # Controller Capabilities
NVME_VER_OFFSET     = 0x0008        # Version
NVME_INTMS_OFFSET   = 0x000c        # Interrupt Mask Set
NVME_INTMC_OFFSET   = 0x0010        # Interrupt Mask Clear
NVME_CC_OFFSET      = 0x0014        # Controller Configuration
NVME_CSTS_OFFSET    = 0x001c        # Controller Status
NVME_NSSR_OFFSET    = 0x0020        # NVM Subsystem Reset
NVME_AQA_OFFSET     = 0x0024        # Admin Queue Attributes
NVME_ASQ_OFFSET     = 0x0028        # Admin Submission Queue Base Address
NVME_ACQ_OFFSET     = 0x0030        # Admin Completion Queue Base Address
NVME_CMBLOC_OFFSET  = 0x0038        # Control Memory Buffer Location (Optional)
NVME_CMBSZ_OFFSET   = 0x003C        # Control Memory Buffer Size (Optional)
NVME_BPINFO_OFFSET  = 0x0040        # Boot Partition Information
NVME_BPRSEL_OFFSET  = 0x0044        # Boot Partition Read Select
NVME_BPMBL_OFFSET   = 0x0048        # Boot Partition Memory Buffer Location
NVME_SQ0_OFFSET     = 0x1000        # Submission Queue 0 (admin) Tail Doorbell
NVME_CQ0_OFFSET     = 0x1004        # Completion Queue 0 (admin) Head Doorbell

def NVME_SQTDBL_OFFSET(QID, DSTRD):
  return 0x1000 + ((2 * (QID)) * (4 << (DSTRD)))         # Submission Queue y (NVM) Tail Doorbell

def NVME_CQHDBL_OFFSET(QID, DSTRD):
  return 0x1000 + (((2 * (QID)) + 1) * (4 << (DSTRD)))   # Completion Queue y (NVM) Head Doorbell

class NVME_CAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mqes",   UINT16),
    ("Cqr",    UINT8,  1),
    ("Ams",    UINT8,  2),
    ("Rsvd1",  UINT8,  5),
    ("To",     UINT8),
    ("Dstrd",  UINT16, 4),
    ("Nssrs",  UINT16, 1),
    ("Css",    UINT16, 8),
    ("Bps",    UINT16, 1),
    ("Rsvd3",  UINT16, 2),
    ("Mpsmin", UINT8,  4),
    ("Mpsmax", UINT8,  4),
    ("Pmrs",   UINT8,  1),
    ("Cmbs",   UINT8,  1),
    ("Rsvd4",  UINT8,  6)
    ]

class NVME_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mnr", UINT16),
    ("Mjr", UINT16)
    ]

class NVME_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("En",     UINT16, 1),
    ("Rsvd1",  UINT16, 3),
    ("Css",    UINT16, 3),
    ("Mps",    UINT16, 4),
    ("Ams",    UINT16, 3),
    ("Shn",    UINT16, 2),
    ("Iosqes", UINT8,  4),
    ("Iocqes", UINT8,  4),
    ("Rsvd2",  UINT8)
    ]

NVME_CC_SHN_NORMAL_SHUTDOWN  = 1
NVME_CC_SHN_ABRUPT_SHUTDOWN  = 2

class NVME_CSTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rdy",   UINT32,  1),
    ("Cfs",   UINT32,  1),
    ("Shst",  UINT32,  2),
    ("Nssro", UINT32,  1),
    ("Rsvd1", UINT32,  27)
    ]

NVME_CSTS_SHST_SHUTDOWN_OCCURRING  = 1
NVME_CSTS_SHST_SHUTDOWN_COMPLETED  = 2

class NVME_AQA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Asqs",  UINT16,  12),
    ("Rsvd1", UINT16,  4),
    ("Acqs",  UINT16,  12),
    ("Rsvd2", UINT16,  4)
    ]

NVME_ASQ  = UINT64

NVME_ACQ = UINT64

class NVME_BPINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bpsz",  UINT32,  15),
    ("Rsvd1", UINT32,  9),
    ("Brs",   UINT32,  2),
    ("Rsvd2", UINT32,  5),
    ("Abpid", UINT32,  1)
    ]

class NVME_BPRSEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bprsz", UINT32,  10),
    ("Bprof", UINT32,  20),
    ("Rsvd1", UINT32,  1),
    ("Bpid",  UINT32,  1)
    ]

class NVME_BPMBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1", UINT64,  12),
    ("Bmbba", UINT64,  52)
    ]

class NVME_SQTDBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Sqt",   UINT16),
    ("Rsvd1", UINT16)
    ]

class NVME_CQHDBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cqh",   UINT16),
    ("Rsvd1", UINT16)
    ]

class NVME_READ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64), 
    ("Nlb",     UINT16), 
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Af",      UINT32, 4 ),
    ("Al",      UINT32, 2 ),
    ("Sr",      UINT32, 1 ),
    ("In",      UINT32, 1 ),
    ("Rsvd2",   UINT32, 24),
    ("Eilbrt",  UINT32), 
    ("Elbat ",  UINT16), 
    ("Elbatm",  UINT16)
    ]

class NVME_WRITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Af",      UINT32, 4 ),
    ("Al",      UINT32, 2 ),
    ("Sr",      UINT32, 1 ),
    ("In",      UINT32, 1 ),
    ("Rsvd2",   UINT32, 24),
    ("Ilbrt",   UINT32),
    ("Lbat",    UINT16),
    ("Lbatm",   UINT16)
    ]

class NVME_FLUSH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Flush",   UINT32)
    ]

class NVME_WRITE_UNCORRECTABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT32, 16),
    ("Rsvd1",   UINT32, 16)
    ]

class NVME_WRITE_ZEROES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Rsvd2",   UINT32),
    ("Ilbrt",   UINT32),
    ("Lbat",    UINT16),
    ("Lbatm",   UINT16)
    ]

class NVME_COMPARE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Rsvd2",   UINT32),
    ("Eilbrt",  UINT32),
    ("Elbat",   UINT16),
    ("Elbatm",  UINT16)
    ]

class NVME_CMD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Read",                NVME_READ               ),
    ("Write",               NVME_WRITE              ),
    ("Flush",               NVME_FLUSH              ),
    ("WriteUncorrectable",  NVME_WRITE_UNCORRECTABLE),
    ("WriteZeros",          NVME_WRITE_ZEROES       ),
    ("Compare",             NVME_COMPARE            )
    ]

class NVME_PSDESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mp",      UINT16),
    ("Rsvd1",   UINT8 ),
    ("Mps",     UINT8,  1),
    ("Nops",    UINT8,  1),
    ("Rsvd2",   UINT8,  6),
    ("Enlat",   UINT32),
    ("Exlat",   UINT32),
    ("Rrt",     UINT8, 5),
    ("Rsvd3",   UINT8, 3),
    ("Rrl",     UINT8, 5),
    ("Rsvd4",   UINT8, 3),
    ("Rwt",     UINT8, 5),
    ("Rsvd5",   UINT8, 3),
    ("Rwl",     UINT8, 5),
    ("Rsvd6",   UINT8, 3),
    ("Rsvd7",   UINT8 * 16)
    ]

class NVME_SANICAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Ces",     UINT32, 1),
    ("Bes",     UINT32, 1),
    ("Ows",     UINT32, 1),
    ("Rsvd1",   UINT32, 26),
    ("Ndi",     UINT32, 1),
    ("Nodmmas", UINT32, 2)
    ]

NAMESPACE_MANAGEMENT_SUPPORTED   = BIT3
FW_DOWNLOAD_ACTIVATE_SUPPORTED   = BIT2
FORMAT_NVM_SUPPORTED             = BIT1
SECURITY_SEND_RECEIVE_SUPPORTED  = BIT0

class NVME_ADMIN_CONTROLLER_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Vid",                 UINT16           ),
    ("Ssvid",               UINT16           ),
    ("Sn",                  UINT8  * 20      ),
    ("Mn",                  UINT8  * 40      ),
    ("Fr",                  UINT8            ),
    ("Rab",                 UINT8  * 3       ),
    ("Ieee_oui",            UINT8            ),
    ("Cmic",                UINT8            ),
    ("Mdts",                UINT8            ),
    ("Cntlid",              UINT8  * 2       ),

    ("Ver",                 UINT32),
    ("Rtd3r",               UINT32),
    ("Rtd3e",               UINT32),
    ("Oaes",                UINT32),
    ("Ctratt",              UINT32),
    ("Rrls",                UINT16),
    ("Rsvd1",               UINT8 * 9),
    ("Cntrltype",           UINT8 ),
    ("Fguid",               UINT8 * 16),
    ("Crdt1",               UINT16),
    ("Crdt2",               UINT16),
    ("Crdt3",               UINT16),
    ("Rsvd2",               UINT8 *106),
    ("Rsvd3",               UINT8 *16),

    ("Oacs",                UINT16           ),
    ("Acl",                 UINT8            ),
    ("Aerl",                UINT8            ),
    ("Frmw",                UINT8            ),
    ("Lpa",                 UINT8            ),
    ("Elpe",                UINT8            ),
    ("Npss",                UINT8            ),
    ("Avscc",               UINT8            ),
    ("Apsta",               UINT8            ),
    ("Wctemp",              UINT16           ),
    ("Cctemp",              UINT16           ),
    ("Mtfa",                UINT16           ),
    ("Hmpre",               UINT32           ),
    ("Hmmin",               UINT32           ),
    ("Tnvmcap",             UINT8   * 16     ),
    ("Unvmcap",             UINT8   * 16     ),
    ("Rpmbs",               UINT32           ),
    ("Edstt",               UINT16           ),
    ("Dsto",                UINT8            ),
    ("Fwug",                UINT8            ),

    ("Kas",       UINT16      ),
    ("Hctma",     UINT16      ),
    ("Mntmt",     UINT16      ),
    ("Mxtmt",     UINT16      ),
    ("Sanicap",   NVME_SANICAP),
    ("Hmminds",   UINT32      ),
    ("Hmmaxd",    UINT16      ),
    ("Nsetidmax", UINT16      ),
    ("Endgidmax", UINT16      ),
    ("Anatt",     UINT8       ),
    ("Anacap",    UINT8       ),
    ("Anagrpmax", UINT32      ),
    ("Nanagrpid", UINT32      ),
    ("Pels",      UINT32      ),
    ("Rsvd4",     UINT8 *156),

    ("Sqes",                UINT8            ),
    ("Cqes",                UINT8            ),
    ("Maxcmd",              UINT16           ),
    ("Nn",                  UINT32           ),
    ("Oncs ",               UINT16           ),
    ("Fuses",               UINT16           ),
    ("Fna",                 UINT8            ),
    ("Vwc",                 UINT8            ),
    ("Awun",                UINT16           ),
    ("Awupf",               UINT16           ),
    ("Nvscc",               UINT8            ),
    ("Nwpc",                UINT8            ),
    ("Acwu",                UINT16           ),
    ("Rsvd5",               UINT16           ),
    ("Sgls",                UINT32           ),

    ("Mnan",                UINT32),
    ("Rsvd6",               UINT8 * 224),
    ("Subnqn",              UINT8 * 256),
    ("Rsvd7",               UINT8 * 768),
    ("Rsvd8",               UINT8 * 256),

    ("PsDescriptor",        NVME_PSDESCRIPTOR * 32),
    ("VendorData",          UINT8   * 1024   )
  ]

LBAF_RP_BEST      = 0b00
LBAF_RP_BETTER    = 0b01
LBAF_RP_GOOD      = 0b10
LBAF_RP_DEGRADED  = 0b11

class NVME_LBAFORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Ms",      UINT16),
    ("Lbads",   UINT8 ),
    ("Rp",      UINT8,  2),
    ("Rsvd1",   UINT8,  6),
    ]

class NVME_ADMIN_NAMESPACE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Nsze",            UINT64        ),
    ("Ncap",            UINT64        ),
    ("Nuse",            UINT64        ),
    ("Nsfeat",          UINT8         ),
    ("Nlbaf",           UINT8         ),
    ("Flbas",           UINT8         ),
    ("Mc",              UINT8         ),
    ("Dpc",             UINT8         ),
    ("Dps",             UINT8         ),
    ("Nmic",            UINT8         ),
    ("Rescap",          UINT8         ),
    ("Rsvd1",           UINT8  * 88   ),
    ("Eui64",           UINT64        ),
    ("LbaFormat",       NVME_LBAFORMAT * 16),
    ("Rsvd2",           UINT8  * 192  ),
    ("VendorData",      UINT8  *3712  )
    ]

class NVME_RPMB_CONFIGURATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bppe",    UINT8),
    ("Bpl",     UINT8),
    ("Nwpac",   UINT8),
    ("Rsvd1",   UINT8  * 509)
    ]

class NVME_RPMB_DATA_FRAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rpmbt",       UINT8 ),
    ("Nonce",       UINT64 * 2),
    ("Wcounter",    UINT32),
    ("Address",     UINT32),
    ("Scount",      UINT32),
    ("Result",      UINT16),
    ("Rpmessage",   UINT16)
    # ("Data",      UINT8 * N)
    ]

class NVME_RPMB_DCB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BPPEnable",    UINT8),
    ("BPLock",       UINT8),
    ("NameSpaceWrP", UINT8),
    ("Rsvd1",        UINT8 * 509)
    ]

NVME_RPMB_AUTHKEY_PROGRAM           = 0x0001
NVME_RPMB_COUNTER_READ              = 0x0002
NVME_RPMB_AUTHDATA_WRITE            = 0x0003
NVME_RPMB_AUTHDATA_READ             = 0x0004
NVME_RPMB_RESULT_READ               = 0x0005
NVME_RPMB_DCB_WRITE                 = 0x0006
NVME_RPMB_DCB_READ                  = 0x0007
NVME_RPMB_AUTHKEY_PROGRAM_RESPONSE  = 0x0100
NVME_RPMB_COUNTER_READ_RESPONSE     = 0x0200
NVME_RPMB_AUTHDATA_WRITE_RESPONSE   = 0x0300
NVME_RPMB_AUTHDATA_READ_RESPONSE    = 0x0400
NVME_RPMB_DCB_WRITE_RESPONSE        = 0x0600
NVME_RPMB_DCB_READ_RESPONSE         = 0x0700

NVME_RPMB_RESULT_SUCCESS                 = 0x00
NVME_RPMB_RESULT_GENERAL_FAILURE         = 0x01
NVME_RPMB_RESULT_AHTHENTICATION_FAILURE  = 0x02
NVME_RPMB_RESULT_COUNTER_FAILURE         = 0x03
NVME_RPMB_RESULT_ADDRESS_FAILURE         = 0x04
NVME_RPMB_RESULT_WRITE_FAILURE           = 0x05
NVME_RPMB_RESULT_READ_FAILURE            = 0x06
NVME_RPMB_RESULT_AUTHKEY_NOT_PROGRAMMED  = 0x07
NVME_RPMB_RESULT_INVALID_DCB             = 0x08

class NVME_BOOT_PARTITION_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogIdentifier",   UINT8),
    ("Rsvd1",           UINT8 * 3),
    ("Bpsz",            UINT32, 15),
    ("Rsvd2",           UINT32, 16),
    ("Abpid",           UINT32, 1),
    ("Rsvd3",           UINT8 * 8)
    ]

class NVME_ADMIN_IDENTIFY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cns",     UINT32, 2),
    ("Rsvd1",   UINT32, 30),
    ]

class NVME_ADMIN_CRIOCQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT32, 16),
    ("Qsize", UINT32, 16),
    ("Pc",    UINT32, 1 ),
    ("Ien",   UINT32, 1 ),
    ("Rsvd1", UINT32, 14),
    ("Iv",    UINT32, 16)
    ]

class NVME_ADMIN_CRIOSQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT32, 16),
    ("Qsize", UINT32, 16),
    ("Pc",    UINT32, 1 ),
    ("Qprio", UINT32, 2),
    ("Rsvd1", UINT32, 13),
    ("Cqid",  UINT32, 16),
    ]

class NVME_ADMIN_DEIOCQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT16),
    ("Rsvd1", UINT16)
    ]

class NVME_ADMIN_DEIOSQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT16),
    ("Rsvd1", UINT16)
    ]

class NVME_ADMIN_ABORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Sqid",    UINT32, 16),
    ("Cid",     UINT32, 16)
    ]

class NVME_ADMIN_FIRMWARE_ACTIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fs",      UINT32, 3),
    ("Aa",      UINT32, 2),
    ("Rsvd1",   UINT32, 27)
    ]

class NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Numd",    UINT32),
    ("Ofst",    UINT32)
    ]

class NVME_ADMIN_GET_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fid",     UINT32, 8),
    ("Sel",     UINT32, 3),
    ("Rsvd1",   UINT32, 21),
    ]

LID_ERROR_INFO            = 0x1
LID_SMART_INFO            = 0x2
LID_FW_SLOT_INFO          = 0x3
LID_BP_INFO               = 0x15
LID_SANITIZE_STATUS_INFO  = 0x81

class NVME_ADMIN_GET_LOG_PAGE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Lid",     UINT32, 8),
    ("Rsvd1",   UINT32, 8),
    ("Numd",    UINT32, 12),
    ("Rsvd2",   UINT32, 4),
    ]

class NVME_ADMIN_SET_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fid",     UINT32, 8),
    ("Rsvd1",   UINT32, 23),
    ("Sv",      UINT32, 1),
    ]

class NVME_ADMIN_SANITIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [

    ("Sanact",  UINT32,  3),
    ("Ause",    UINT32,  1),
    ("Owpass",  UINT32,  4),
    ("Oipbp",   UINT32,  1),
    ("Nodas",   UINT32,  1),
    ("Rsvd1",   UINT32,  22),
    ("Ovrpat",  UINT32)
    ]

SANITIZE_ACTION_NO_ACTION          = 0x0
SANITIZE_ACTION_EXIT_FAILURE_MODE  = 0x1
SANITIZE_ACTION_BLOCK_ERASE        = 0x2
SANITIZE_ACTION_OVERWRITE          = 0x3
SANITIZE_ACTION_CRYPTO_ERASE       = 0x4

class NVME_ADMIN_FORMAT_NVM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Lbaf",    UINT32, 4),
    ("Ms",      UINT32, 1),
    ("Pi",      UINT32, 3),
    ("Pil",     UINT32, 1),
    ("Ses",     UINT32, 3),
    ("Rsvd1",   UINT32, 20)
    ]

SES_NO_SECURE_ERASE  = 0x0
SES_USER_DATA_ERASE  = 0x1
SES_CRYPTO_ERASE     = 0x2

class NVME_ADMIN_SECURITY_RECEIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1",   UINT32, 8),
    ("Spsp",    UINT32, 16),
    ("Secp",    UINT32, 8)
    ]

class NVME_ADMIN_SECURITY_SEND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1",   UINT32, 8),
    ("Spsp",    UINT32, 16),
    ("Secp",    UINT32, 8),
    ("Tl",      UINT32)
    ]

class NVME_ADMIN_CMD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Identify",              NVME_ADMIN_IDENTIFY               ),
    ("CrIoCq",                NVME_ADMIN_CRIOCQ                 ),
    ("CrIoSq",                NVME_ADMIN_CRIOSQ                 ),
    ("DeIoCq",                NVME_ADMIN_DEIOCQ                 ),
    ("DeIoSq",                NVME_ADMIN_DEIOSQ                 ),
    ("Abort",                 NVME_ADMIN_ABORT                  ),
    ("Activate",              NVME_ADMIN_FIRMWARE_ACTIVATE      ),
    ("FirmwareImageDownload", NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD),
    ("GetFeatures",           NVME_ADMIN_GET_FEATURES           ),
    ("GetLogPage",            NVME_ADMIN_GET_LOG_PAGE           ),
    ("SetFeatures",           NVME_ADMIN_SET_FEATURES           ),
    ("FormatNvm",             NVME_ADMIN_FORMAT_NVM             ),
    ("SecurityReceive",       NVME_ADMIN_SECURITY_RECEIVE       ),
    ("SecuritySend",          NVME_ADMIN_SECURITY_SEND          ),
    ("Sanitize",              NVME_ADMIN_SANITIZE               )
    ]

class NVME_RAW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cdw10",   UINT32),
    ("Cdw11",   UINT32),
    ("Cdw12",   UINT32),
    ("Cdw13",   UINT32),
    ("Cdw14",   UINT32),
    ("Cdw15",   UINT32),
    ]

class NVME_PAYLOAD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Admin",   NVME_ADMIN_CMD),
    ("Nvm",     NVME_CMD      ),
    ("Raw",     NVME_RAW      )
    ]

class NVME_SQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Opc",     UINT8),
    ("Fuse",    UINT8, 2),
    ("Rsvd1",   UINT8, 5),
    ("Psdt",    UINT8, 1),
    ("Cid",     UINT16),
    ("Nsid",    UINT32),
    ("Rsvd2",   UINT64),
    ("Mptr",    UINT64),
    ("Prp",     UINT64 * 2),
    ("Payload", NVME_PAYLOAD)
    ]

class NVME_CQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Dword0",  UINT32),
    ("Rsvd1",   UINT32),
    ("Sqhd",    UINT16),
    ("Sqid",    UINT16),
    ("Cid",     UINT16),
    ("Pt",      UINT16, 1),
    ("Sc",      UINT16, 8),
    ("Sct",     UINT16, 3),
    ("Rsvd2",   UINT16, 2),
    ("Mo",      UINT16, 1),
    ("Dnr",     UINT16, 1)
    ]

NVME_ADMIN_DEIOSQ_CMD               = 0x00
NVME_ADMIN_CRIOSQ_CMD               = 0x01
NVME_ADMIN_GET_LOG_PAGE_CMD         = 0x02
NVME_ADMIN_DEIOCQ_CMD               = 0x04
NVME_ADMIN_CRIOCQ_CMD               = 0x05
NVME_ADMIN_IDENTIFY_CMD             = 0x06
NVME_ADMIN_ABORT_CMD                = 0x08
NVME_ADMIN_SET_FEATURES_CMD         = 0x09
NVME_ADMIN_GET_FEATURES_CMD         = 0x0A
NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD  = 0x0C
NVME_ADMIN_NAMESACE_MANAGEMENT_CMD  = 0x0D
NVME_ADMIN_FW_COMMIT_CMD            = 0x10
NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD    = 0x11
NVME_ADMIN_NAMESACE_ATTACHMENT_CMD  = 0x15
NVME_ADMIN_FORMAT_NVM_CMD           = 0x80
NVME_ADMIN_SECURITY_SEND_CMD        = 0x81
NVME_ADMIN_SECURITY_RECEIVE_CMD     = 0x82
NVME_ADMIN_SANITIZE_CMD             = 0x84

NVME_IO_FLUSH_OPC  = 0
NVME_IO_WRITE_OPC  = 1
NVME_IO_READ_OPC   = 2

DeleteIOSubmissionQueueOpcode = NVME_ADMIN_DEIOSQ_CMD,
CreateIOSubmissionQueueOpcode = NVME_ADMIN_CRIOSQ_CMD,
GetLogPageOpcode              = NVME_ADMIN_GET_LOG_PAGE_CMD,
DeleteIOCompletionQueueOpcode = NVME_ADMIN_DEIOCQ_CMD,
CreateIOCompletionQueueOpcode = NVME_ADMIN_CRIOCQ_CMD,
IdentifyOpcode                = NVME_ADMIN_IDENTIFY_CMD,
AbortOpcode                   = NVME_ADMIN_ABORT_CMD,
SetFeaturesOpcode             = NVME_ADMIN_SET_FEATURES_CMD,
GetFeaturesOpcode             = NVME_ADMIN_GET_FEATURES_CMD,
AsyncEventRequestOpcode       = NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD,
NamespaceManagementOpcode     = NVME_ADMIN_NAMESACE_MANAGEMENT_CMD,
FirmwareCommitOpcode          = NVME_ADMIN_FW_COMMIT_CMD,
FirmwareImageDownloadOpcode   = NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD,
NamespaceAttachmentOpcode     = NVME_ADMIN_NAMESACE_ATTACHMENT_CMD,
FormatNvmOpcode               = NVME_ADMIN_FORMAT_NVM_CMD,
SecuritySendOpcode            = NVME_ADMIN_SECURITY_SEND_CMD,
SecurityReceiveOpcode         = NVME_ADMIN_SECURITY_RECEIVE_CMD
SanitizeOpcode                = NVME_ADMIN_SANITIZE_CMD
NVME_ADMIN_COMMAND_OPCODE     = ENUM

IdentifyNamespaceCns    = 0x0,
IdentifyControllerCns   = 0x1,
IdentifyActiveNsListCns = 0x2
NVME_ADMIN_IDENTIFY_CNS = ENUM

ActivateActionReplace         = 0x0,
ActivateActionReplaceActivate = 0x1,
ActivateActionActivate        = 0x2
NVME_FW_ACTIVATE_ACTION       = ENUM

FirmwareSlotCtrlChooses = 0x0
FirmwareSlot1           = 0x1
FirmwareSlot2           = 0x2
FirmwareSlot3           = 0x3
FirmwareSlot4           = 0x4
FirmwareSlot5           = 0x5
FirmwareSlot6           = 0x6
FirmwareSlot7           = 0x7
NVME_FW_ACTIVATE_SLOT   = ENUM

ErrorInfoLogID          = LID_ERROR_INFO
SmartHealthInfoLogID    = LID_SMART_INFO
FirmwareSlotInfoLogID   = LID_FW_SLOT_INFO
BootPartitionInfoLogID  = LID_BP_INFO,
SanitizeStatusInfoLogID = LID_SANITIZE_STATUS_INFO
NVME_LOG_ID             = ENUM

class NVME_ACTIVE_FW_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActivelyRunningFwSlot",   UINT8, 3),
    ("Empty1",                  UINT8, 1),
    ("NextActiveFwSlot",        UINT8, 3),
    ("Empty2",                  UINT8, 1)
    ]

class NVME_FW_SLOT_INFO_LOG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActiveFwInfo",    NVME_ACTIVE_FW_INFO),
    ("Reserved1",       UINT8 * 7),
    ("FwRevisionSlot", (UINT8 * 8) * 7),
    ("Reserved2",       UINT8 * 448),
    ]

class NVME_SMART_HEALTH_INFO_LOG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CriticalWarningAvailableSpare",    UINT8, 1),
    ("CriticalWarningTemperature",       UINT8, 1),
    ("CriticalWarningReliability",       UINT8, 1),
    ("CriticalWarningMediaReadOnly",     UINT8, 1),
    ("CriticalWarningVolatileBackup",    UINT8, 1),
    ("CriticalWarningReserved",          UINT8, 3),
    ("CompositeTemp",                    UINT16),
    ("AvailableSpare",                   UINT8),
    ("AvailableSpareThreshold",          UINT8),
    ("PercentageUsed",                   UINT8),
    ("Reserved1",                        UINT8 * 26),
    ("DataUnitsRead",                    UINT8 * 16),
    ("DataUnitsWritten",                 UINT8 * 16),
    ("HostReadCommands",                 UINT8 * 16),
    ("HostWriteCommands",                UINT8 * 16),
    ("ControllerBusyTime",               UINT8 * 16),
    ("PowerCycles",                      UINT8 * 16),
    ("PowerOnHours",                     UINT8 * 16),
    ("UnsafeShutdowns",                  UINT8 * 16),
    ("MediaAndDataIntegrityErrors",      UINT8 * 16),
    ("NumberErrorInformationLogEntries", UINT8 * 16),
    ("WarningCompositeTemperatureTime",  UINT32),
    ("CriticalCompositeTemperatureTime", UINT32),
    ("TemperatureSensor",                UINT16 * 8),
    ("Reserved2",                        UINT8 * 296)
    ]

class NVME_SMART_HEALTH_INFO_LOG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SanitizeProgress",                  UINT16),
    ("SanitizeStatus",                    UINT16, 3),
    ("OverwriteSanitizeCompletedNumber",  UINT16, 5),
    ("GlobalDataErased",                  UINT16, 1),
    ("SanitizeStatusRsvd",                UINT16, 7),
    ("SanitizeCmdDw10Info",               UINT32),
    ("OverwriteEstimatedTime",            UINT32),
    ("BlockEraseEstimatedTime",           UINT32),
    ("CryptoEraseEstimatedTime",          UINT32),
    ("OverwriteEstimatedTimeWithNodmm",   UINT32),
    ("BlockEraseEstimatedTimeWithNodmm",  UINT32),
    ("CryptoEraseEstimatedTimeWithNodmm", UINT32),
    ("Reserved",                          UINT8 * 480)
    ]

