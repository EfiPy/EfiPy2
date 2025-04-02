# Pci22.py
#
# EfiPy2.MdePkg.IndustryStandard.Pci22
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

PCI_MAX_BUS     = 255
PCI_MAX_DEVICE  = 31
PCI_MAX_FUNC    = 7

class PCI_DEVICE_INDEPENDENT_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VendorId",      UINT16),
    ("DeviceId",      UINT16),
    ("Command",       UINT16),
    ("Status",        UINT16),
    ("RevisionID",    UINT8),
    ("ClassCode",     UINT8 * 3),
    ("CacheLineSize", UINT8),
    ("LatencyTimer",  UINT8),
    ("HeaderType",    UINT8),
    ("BIST",          UINT8)
    ]

class PCI_DEVICE_HEADER_TYPE_REGION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bar",               UINT32 * 6),
    ("CISPtr",            UINT32),
    ("SubsystemVendorID", UINT16),
    ("SubsystemID",       UINT16),
    ("ExpansionRomBar",   UINT32),
    ("CapabilityPtr",     UINT8),
    ("Reserved1",         UINT8 * 3),
    ("Reserved2",         UINT32),
    ("InterruptLine",     UINT8),
    ("InterruptPin",      UINT8),
    ("MinGnt",            UINT8),
    ("MaxLat",            UINT8)
    ]

class PCI_TYPE00 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",               PCI_DEVICE_INDEPENDENT_REGION),
    ("Device",            PCI_DEVICE_HEADER_TYPE_REGION)
    ]

class PCI_BRIDGE_CONTROL_REGISTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bar",                       UINT32 * 2),
    ("PrimaryBus",                UINT8),
    ("SecondaryBus",              UINT8),
    ("SubordinateBus",            UINT8),
    ("SecondaryLatencyTimer",     UINT8),
    ("IoBase",                    UINT8),
    ("IoLimit",                   UINT8),
    ("SecondaryStatus",           UINT16),
    ("MemoryBase",                UINT16),
    ("MemoryLimit",               UINT16),
    ("PrefetchableMemoryBase",    UINT16),
    ("PrefetchableMemoryLimit",   UINT16),
    ("PrefetchableBaseUpper32",   UINT32),
    ("PrefetchableLimitUpper32",  UINT32),
    ("IoBaseUpper16",             UINT16),
    ("IoLimitUpper16",            UINT16),
    ("CapabilityPtr",             UINT8),
    ("Reserved",                  UINT8 * 3),
    ("ExpansionRomBAR",           UINT32),
    ("InterruptLine",             UINT8),
    ("InterruptPin",              UINT8),
    ("BridgeControl",             UINT16)
    ]

class PCI_TYPE01 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",     PCI_DEVICE_INDEPENDENT_REGION),
    ("Bridge",  PCI_BRIDGE_CONTROL_REGISTER)
    ]

class PCI_TYPE_GENERIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Device",  PCI_TYPE00),
    ("Bridge",  PCI_TYPE01)
    ]

class PCI_CARDBUS_CONTROL_REGISTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CardBusSocketReg",      UINT32),
    ("Cap_Ptr",               UINT8),
    ("Reserved",              UINT8),
    ("SecondaryStatus",       UINT16),
    ("PciBusNumber",          UINT8),
    ("CardBusBusNumber",      UINT8),
    ("SubordinateBusNumber",  UINT8),
    ("CardBusLatencyTimer",   UINT8),
    ("MemoryBase0",           UINT32),
    ("MemoryLimit0",          UINT32),
    ("MemoryBase1",           UINT32),
    ("MemoryLimit1",          UINT32),
    ("IoBase0",               UINT32),
    ("IoLimit0",              UINT32),
    ("IoBase1",               UINT32),
    ("IoLimit1",              UINT32),
    ("InterruptLine",         UINT8),
    ("InterruptPin",          UINT8),
    ("BridgeControl",         UINT16)
    ]

PCI_CLASS_OLD                 = 0x00
PCI_CLASS_OLD_OTHER           = 0x00
PCI_CLASS_OLD_VGA             = 0x01

PCI_CLASS_MASS_STORAGE        = 0x01
PCI_CLASS_MASS_STORAGE_SCSI   = 0x00
PCI_CLASS_MASS_STORAGE_IDE    = 0x01
PCI_CLASS_MASS_STORAGE_FLOPPY = 0x02
PCI_CLASS_MASS_STORAGE_IPI    = 0x03
PCI_CLASS_MASS_STORAGE_RAID   = 0x04
PCI_CLASS_MASS_STORAGE_OTHER  = 0x80
PCI_CLASS_NETWORK             = 0x02
PCI_CLASS_NETWORK_ETHERNET    = 0x00
PCI_CLASS_NETWORK_TOKENRING   = 0x01
PCI_CLASS_NETWORK_FDDI        = 0x02
PCI_CLASS_NETWORK_ATM         = 0x03
PCI_CLASS_NETWORK_ISDN        = 0x04
PCI_CLASS_NETWORK_OTHER       = 0x80

PCI_CLASS_DISPLAY             = 0x03
PCI_CLASS_DISPLAY_VGA         = 0x00
PCI_IF_VGA_VGA                = 0x00
PCI_IF_VGA_8514               = 0x01
PCI_CLASS_DISPLAY_XGA         = 0x01
PCI_CLASS_DISPLAY_3D          = 0x02
PCI_CLASS_DISPLAY_OTHER       = 0x80

PCI_CLASS_MEDIA               = 0x04
PCI_CLASS_MEDIA_VIDEO         = 0x00
PCI_CLASS_MEDIA_AUDIO         = 0x01
PCI_CLASS_MEDIA_TELEPHONE     = 0x02
PCI_CLASS_MEDIA_OTHER         = 0x80

PCI_CLASS_MEMORY_CONTROLLER   = 0x05
PCI_CLASS_MEMORY_RAM          = 0x00
PCI_CLASS_MEMORY_FLASH        = 0x01
PCI_CLASS_MEMORY_OTHER        = 0x80

PCI_CLASS_BRIDGE              = 0x06
PCI_CLASS_BRIDGE_HOST         = 0x00
PCI_CLASS_BRIDGE_ISA          = 0x01
PCI_CLASS_BRIDGE_EISA         = 0x02
PCI_CLASS_BRIDGE_MCA          = 0x03
PCI_CLASS_BRIDGE_P2P          = 0x04
PCI_IF_BRIDGE_P2P             = 0x00
PCI_IF_BRIDGE_P2P_SUBTRACTIVE = 0x01
PCI_CLASS_BRIDGE_PCMCIA       = 0x05
PCI_CLASS_BRIDGE_NUBUS        = 0x06
PCI_CLASS_BRIDGE_CARDBUS      = 0x07
PCI_CLASS_BRIDGE_RACEWAY      = 0x08
PCI_CLASS_BRIDGE_OTHER        = 0x80
PCI_CLASS_BRIDGE_ISA_PDECODE  = 0x80

PCI_CLASS_SCC                 = 0x07
PCI_SUBCLASS_SERIAL           = 0x00
PCI_IF_GENERIC_XT             = 0x00
PCI_IF_16450                  = 0x01
PCI_IF_16550                  = 0x02
PCI_IF_16650                  = 0x03
PCI_IF_16750                  = 0x04
PCI_IF_16850                  = 0x05
PCI_IF_16950                  = 0x06
PCI_SUBCLASS_PARALLEL         = 0x01
PCI_IF_PARALLEL_PORT          = 0x00
PCI_IF_BI_DIR_PARALLEL_PORT   = 0x01
PCI_IF_ECP_PARALLEL_PORT      = 0x02
PCI_IF_1284_CONTROLLER        = 0x03
PCI_IF_1284_DEVICE            = 0xFE
PCI_SUBCLASS_MULTIPORT_SERIAL = 0x02
PCI_SUBCLASS_MODEM            = 0x03
PCI_IF_GENERIC_MODEM          = 0x00
PCI_IF_16450_MODEM            = 0x01
PCI_IF_16550_MODEM            = 0x02
PCI_IF_16650_MODEM            = 0x03
PCI_IF_16750_MODEM            = 0x04
PCI_SUBCLASS_SCC_OTHER        = 0x80

PCI_CLASS_SYSTEM_PERIPHERAL   = 0x08
PCI_SUBCLASS_PIC              = 0x00
PCI_IF_8259_PIC               = 0x00
PCI_IF_ISA_PIC                = 0x01
PCI_IF_EISA_PIC               = 0x02
PCI_IF_APIC_CONTROLLER        = 0x10
PCI_IF_APIC_CONTROLLER2       = 0x20
PCI_SUBCLASS_DMA              = 0x01
PCI_IF_8237_DMA               = 0x00
PCI_IF_ISA_DMA                = 0x01
PCI_IF_EISA_DMA               = 0x02
PCI_SUBCLASS_TIMER            = 0x02
PCI_IF_8254_TIMER             = 0x00
PCI_IF_ISA_TIMER              = 0x01
PCI_IF_EISA_TIMER             = 0x02
PCI_SUBCLASS_RTC              = 0x03
PCI_IF_GENERIC_RTC            = 0x00
PCI_IF_ISA_RTC                = 0x01
PCI_SUBCLASS_PNP_CONTROLLER   = 0x04
PCI_SUBCLASS_PERIPHERAL_OTHER = 0x80

PCI_CLASS_INPUT_DEVICE        = 0x09
PCI_SUBCLASS_KEYBOARD         = 0x00
PCI_SUBCLASS_PEN              = 0x01
PCI_SUBCLASS_MOUSE_CONTROLLER = 0x02
PCI_SUBCLASS_SCAN_CONTROLLER  = 0x03
PCI_SUBCLASS_GAMEPORT         = 0x04
PCI_IF_GAMEPORT               = 0x00
PCI_IF_GAMEPORT1              = 0x10
PCI_SUBCLASS_INPUT_OTHER      = 0x80

PCI_CLASS_DOCKING_STATION     = 0x0A
PCI_SUBCLASS_DOCKING_GENERIC  = 0x00
PCI_SUBCLASS_DOCKING_OTHER    = 0x80

PCI_CLASS_PROCESSOR           = 0x0B
PCI_SUBCLASS_PROC_386         = 0x00
PCI_SUBCLASS_PROC_486         = 0x01
PCI_SUBCLASS_PROC_PENTIUM     = 0x02
PCI_SUBCLASS_PROC_ALPHA       = 0x10
PCI_SUBCLASS_PROC_POWERPC     = 0x20
PCI_SUBCLASS_PROC_MIPS        = 0x30
PCI_SUBCLASS_PROC_CO_PORC     = 0x40

PCI_CLASS_SERIAL              = 0x0C
PCI_CLASS_SERIAL_FIREWIRE     = 0x00
PCI_IF_1394                   = 0x00
PCI_IF_1394_OPEN_HCI          = 0x10
PCI_CLASS_SERIAL_ACCESS_BUS   = 0x01
PCI_CLASS_SERIAL_SSA          = 0x02
PCI_CLASS_SERIAL_USB          = 0x03
PCI_IF_UHCI                   = 0x00
PCI_IF_OHCI                   = 0x10
PCI_IF_USB_OTHER              = 0x80
PCI_IF_USB_DEVICE             = 0xFE
PCI_CLASS_SERIAL_FIBRECHANNEL = 0x04
PCI_CLASS_SERIAL_SMB          = 0x05

PCI_CLASS_WIRELESS            = 0x0D
PCI_SUBCLASS_IRDA             = 0x00
PCI_SUBCLASS_IR               = 0x01
PCI_SUBCLASS_RF               = 0x10
PCI_SUBCLASS_WIRELESS_OTHER   = 0x80

PCI_CLASS_INTELLIGENT_IO      = 0x0E

PCI_CLASS_SATELLITE           = 0x0F
PCI_SUBCLASS_TV               = 0x01
PCI_SUBCLASS_AUDIO            = 0x02
PCI_SUBCLASS_VOICE            = 0x03
PCI_SUBCLASS_DATA             = 0x04

PCI_SECURITY_CONTROLLER       = 0x10
PCI_SUBCLASS_NET_COMPUT       = 0x00
PCI_SUBCLASS_ENTERTAINMENT    = 0x10
PCI_SUBCLASS_SECURITY_OTHER   = 0x80

PCI_CLASS_DPIO                = 0x11
PCI_SUBCLASS_DPIO             = 0x00
PCI_SUBCLASS_DPIO_OTHER       = 0x80

def IS_CLASS1(_p, c):
  return _p.Hdr.ClassCode[2] == (c)

def IS_CLASS2(_p, c, s):
  return IS_CLASS1 (_p, c) and _p.Hdr.ClassCode[1] == s

def IS_CLASS3(_p, c, s, p):
  return IS_CLASS2 (_p, c, s) and _p.Hdr.ClassCode[0] == p

def IS_PCI_DISPLAY(_p):
  return IS_CLASS1 (_p, PCI_CLASS_DISPLAY)

def IS_PCI_VGA(_p):
  return IS_CLASS3 (_p, PCI_CLASS_DISPLAY, PCI_CLASS_DISPLAY_VGA, PCI_IF_VGA_VGA)

def IS_PCI_8514(_p):
  return IS_CLASS3 (_p, PCI_CLASS_DISPLAY, PCI_CLASS_DISPLAY_VGA, PCI_IF_VGA_8514)

def IS_PCI_OLD(_p):
  return IS_CLASS1 (_p, PCI_CLASS_OLD)

def IS_PCI_OLD_VGA(_p):
  return IS_CLASS2 (_p, PCI_CLASS_OLD, PCI_CLASS_OLD_VGA)

def IS_PCI_IDE(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_IDE)

def IS_PCI_SCSI(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_SCSI)

def IS_PCI_RAID(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_RAID)

def IS_PCI_LPC(_p):
  return IS_CLASS2 (_p, PCI_CLASS_BRIDGE, PCI_CLASS_BRIDGE_ISA)

def IS_PCI_P2P(_p):

  return IS_CLASS3 (_p, PCI_CLASS_BRIDGE, PCI_CLASS_BRIDGE_P2P, PCI_IF_BRIDGE_P2P)

def IS_PCI_P2P_SUB(_p):
  return IS_CLASS3 (_p, PCI_CLASS_BRIDGE, PCI_CLASS_BRIDGE_P2P, PCI_IF_BRIDGE_P2P_SUBTRACTIVE)

def IS_PCI_16550_SERIAL(_p):
  return IS_CLASS3 (_p, PCI_CLASS_SCC, PCI_SUBCLASS_SERIAL, PCI_IF_16550)

def IS_PCI_USB(_p):
  return IS_CLASS2 (_p, PCI_CLASS_SERIAL, PCI_CLASS_SERIAL_USB)

HEADER_TYPE_DEVICE            = 0x00
HEADER_TYPE_PCI_TO_PCI_BRIDGE = 0x01
HEADER_TYPE_CARDBUS_BRIDGE    = 0x02
HEADER_TYPE_MULTI_FUNCTION    = 0x80

HEADER_LAYOUT_CODE            = 0x7f

def IS_PCI_BRIDGE(_p):
  return (_p.Hdr.HeaderType & HEADER_LAYOUT_CODE) == HEADER_TYPE_PCI_TO_PCI_BRIDGE

def IS_CARDBUS_BRIDGE(_p):
  return (_p.Hdr.HeaderType & HEADER_LAYOUT_CODE) == HEADER_TYPE_CARDBUS_BRIDGE

def IS_PCI_MULTI_FUNC(_p):
  return (_p.Hdr.HeaderType & HEADER_TYPE_MULTI_FUNCTION) == HEADER_TYPE_MULTI_FUNCTION

PCI_BRIDGE_ROMBAR             = 0x38

PCI_MAX_BAR                   = 0x0006
PCI_MAX_CONFIG_OFFSET         = 0x0100

PCI_VENDOR_ID_OFFSET                        = 0x00
PCI_DEVICE_ID_OFFSET                        = 0x02
PCI_COMMAND_OFFSET                          = 0x04
PCI_PRIMARY_STATUS_OFFSET                   = 0x06
PCI_REVISION_ID_OFFSET                      = 0x08
PCI_CLASSCODE_OFFSET                        = 0x09
PCI_CACHELINE_SIZE_OFFSET                   = 0x0C
PCI_LATENCY_TIMER_OFFSET                    = 0x0D
PCI_HEADER_TYPE_OFFSET                      = 0x0E
PCI_BIST_OFFSET                             = 0x0F
PCI_BASE_ADDRESSREG_OFFSET                  = 0x10
PCI_CARDBUS_CIS_OFFSET                      = 0x28
PCI_SVID_OFFSET                             = 0x2C
PCI_SUBSYSTEM_VENDOR_ID_OFFSET              = 0x2C
PCI_SID_OFFSET                              = 0x2E
PCI_SUBSYSTEM_ID_OFFSET                     = 0x2E
PCI_EXPANSION_ROM_BASE                      = 0x30
PCI_CAPBILITY_POINTER_OFFSET                = 0x34
PCI_INT_LINE_OFFSET                         = 0x3C
PCI_INT_PIN_OFFSET                          = 0x3D
PCI_MAXGNT_OFFSET                           = 0x3E
PCI_MAXLAT_OFFSET                           = 0x3F

PCI_BRIDGE_PRIMARY_BUS_REGISTER_OFFSET      = 0x18
PCI_BRIDGE_SECONDARY_BUS_REGISTER_OFFSET    = 0x19
PCI_BRIDGE_SUBORDINATE_BUS_REGISTER_OFFSET  = 0x1a
PCI_BRIDGE_STATUS_REGISTER_OFFSET           = 0x1E
PCI_BRIDGE_CONTROL_REGISTER_OFFSET          = 0x3E

PCI_INT_LINE_UNKNOWN                        = 0xFF

class PCI_CONFIG_ACCESS_CF8_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reg",     UINT32, 8),
    ("Func",    UINT32, 3),
    ("Dev",     UINT32, 5),
    ("Bus",     UINT32, 8),
    ("Reserved",UINT32, 7),
    ("Enable",  UINT32, 1)
    ]

class PCI_CONFIG_ACCESS_CF8 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    PCI_CONFIG_ACCESS_CF8_Bits),
    ("Uint32",  UINT32)
    ]

EFI_PCI_COMMAND_IO_SPACE                        = BIT0
EFI_PCI_COMMAND_MEMORY_SPACE                    = BIT1
EFI_PCI_COMMAND_BUS_MASTER                      = BIT2
EFI_PCI_COMMAND_SPECIAL_CYCLE                   = BIT3
EFI_PCI_COMMAND_MEMORY_WRITE_AND_INVALIDATE     = BIT4
EFI_PCI_COMMAND_VGA_PALETTE_SNOOP               = BIT5
EFI_PCI_COMMAND_PARITY_ERROR_RESPOND            = BIT6
EFI_PCI_COMMAND_STEPPING_CONTROL                = BIT7
EFI_PCI_COMMAND_SERR                            = BIT8
EFI_PCI_COMMAND_FAST_BACK_TO_BACK               = BIT9

EFI_PCI_BRIDGE_CONTROL_PARITY_ERROR_RESPONSE    = BIT0 
EFI_PCI_BRIDGE_CONTROL_SERR                     = BIT1 
EFI_PCI_BRIDGE_CONTROL_ISA                      = BIT2 
EFI_PCI_BRIDGE_CONTROL_VGA                      = BIT3 
EFI_PCI_BRIDGE_CONTROL_VGA_16                   = BIT4 
EFI_PCI_BRIDGE_CONTROL_MASTER_ABORT             = BIT5 
EFI_PCI_BRIDGE_CONTROL_RESET_SECONDARY_BUS      = BIT6 
EFI_PCI_BRIDGE_CONTROL_FAST_BACK_TO_BACK        = BIT7 
EFI_PCI_BRIDGE_CONTROL_PRIMARY_DISCARD_TIMER    = BIT8 
EFI_PCI_BRIDGE_CONTROL_SECONDARY_DISCARD_TIMER  = BIT9 
EFI_PCI_BRIDGE_CONTROL_TIMER_STATUS             = BIT10
EFI_PCI_BRIDGE_CONTROL_DISCARD_TIMER_SERR       = BIT11

EFI_PCI_BRIDGE_CONTROL_IREQINT_ENABLE           = BIT7 
EFI_PCI_BRIDGE_CONTROL_RANGE0_MEMORY_TYPE       = BIT8 
EFI_PCI_BRIDGE_CONTROL_RANGE1_MEMORY_TYPE       = BIT9 
EFI_PCI_BRIDGE_CONTROL_WRITE_POSTING_ENABLE     = BIT10

EFI_PCI_STATUS_CAPABILITY                       = BIT4
EFI_PCI_STATUS_66MZ_CAPABLE                     = BIT5
EFI_PCI_FAST_BACK_TO_BACK_CAPABLE               = BIT7
EFI_PCI_MASTER_DATA_PARITY_ERROR                = BIT8

EFI_PCI_CARDBUS_BRIDGE_CAPABILITY_PTR = 0x14

EFI_PCI_CAPABILITY_ID_PMI     = 0x01
EFI_PCI_CAPABILITY_ID_AGP     = 0x02
EFI_PCI_CAPABILITY_ID_VPD     = 0x03
EFI_PCI_CAPABILITY_ID_SLOTID  = 0x04
EFI_PCI_CAPABILITY_ID_MSI     = 0x05
EFI_PCI_CAPABILITY_ID_HOTPLUG = 0x06
EFI_PCI_CAPABILITY_ID_SHPC    = 0x0C

class EFI_PCI_CAPABILITY_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CapabilityID",  UINT8),
    ("NextItemPtr",   UINT8)
    ]

class EFI_PCI_PMC_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",                       UINT16, 3),
    ("PmeClock",                      UINT16, 1),
    ("None",                          UINT16, 1),
    ("DeviceSpecificInitialization",  UINT16, 1),
    ("AuxCurrent",                    UINT16, 3),
    ("D1Support",                     UINT16, 1),
    ("D2Support",                     UINT16, 1),
    ("PmeSupport",                    UINT16, 5)
    ]

class EFI_PCI_PMC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    EFI_PCI_PMC_Bits),
    ("Uint32",  UINT16)
    ]

EFI_PCI_PMC_D3_COLD_MASK    = BIT15

class EFI_PCI_PMCSR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerState",  UINT16, 2),
    ("None",        UINT16, 6),
    ("PmeEnable",   UINT16, 1),
    ("DataSelect",  UINT16, 4),
    ("DataScale",   UINT16, 2),
    ("PmeStatus",   UINT16, 1)
    ]

class EFI_PCI_PMCSR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    EFI_PCI_PMCSR_Bits),
    ("Uint32",  UINT16)
    ]

PCI_POWER_STATE_D0      = 0
PCI_POWER_STATE_D1      = 1
PCI_POWER_STATE_D2      = 2
PCI_POWER_STATE_D3_HOT  = 3

class EFI_PCI_PMCSR_BSE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 6),
    ("B2B3",                    UINT8, 1),
    ("BusPowerClockControl",    UINT8, 1)
    ]

class EFI_PCI_PMCSR_BSE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    EFI_PCI_PMCSR_BSE_Bits),
    ("Uint8",   UINT8)
    ]

class EFI_PCI_CAPABILITY_PMI (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",             EFI_PCI_CAPABILITY_HDR),
    ("PMC",             EFI_PCI_PMC),
    ("PMCSR",           EFI_PCI_PMCSR),
    ("BridgeExtention", EFI_PCI_PMCSR_BSE),
    ("Data",            UINT8)
    ]

class EFI_PCI_CAPABILITY_AGP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",       EFI_PCI_CAPABILITY_HDR),
    ("Rev",       UINT8),
    ("Reserved",  UINT8),
    ("Status",    UINT32),
    ("Command",   UINT32)
    ]

class EFI_PCI_CAPABILITY_VPD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",     EFI_PCI_CAPABILITY_HDR),
    ("AddrReg", UINT16),
    ("DataReg", UINT32)
    ]

class EFI_PCI_CAPABILITY_SLOTID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",           EFI_PCI_CAPABILITY_HDR),
    ("ExpnsSlotReg",  UINT8),
    ("ChassisNo",     UINT8)
    ]

class EFI_PCI_CAPABILITY_MSI32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",           EFI_PCI_CAPABILITY_HDR),
    ("MsgCtrlReg",    UINT16),
    ("MsgAddrReg",    UINT32),
    ("MsgDataReg",    UINT16)
    ]

class EFI_PCI_CAPABILITY_MSI64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",             EFI_PCI_CAPABILITY_HDR),
    ("MsgCtrlReg",      UINT16),
    ("MsgAddrRegLsdw",  UINT32),
    ("MsgAddrRegMsdw",  UINT32),
    ("MsgDataReg",      UINT16)
    ]

class EFI_PCI_CAPABILITY_HOTPLUG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr", EFI_PCI_CAPABILITY_HDR)
    ]

PCI_BAR_IDX0        = 0x00
PCI_BAR_IDX1        = 0x01
PCI_BAR_IDX2        = 0x02
PCI_BAR_IDX3        = 0x03
PCI_BAR_IDX4        = 0x04
PCI_BAR_IDX5        = 0x05

EFI_ROOT_BRIDGE_LIST                            = 'eprb'
EFI_PCI_EXPANSION_ROM_HEADER_EFISIGNATURE       = 0x0EF1

PCI_EXPANSION_ROM_HEADER_SIGNATURE              = 0xaa55
PCI_DATA_STRUCTURE_SIGNATURE                    = SIGNATURE_32 ('P', 'C', 'I', 'R')
PCI_CODE_TYPE_PCAT_IMAGE                        = 0x00  
EFI_PCI_EXPANSION_ROM_HEADER_COMPRESSED         = 0x0001

class PCI_EXPANSION_ROM_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",   UINT16),
    ("Reserved",    UINT8 * 0x16),
    ("PcirOffset",  UINT16)
    ]

class EFI_LEGACY_EXPANSION_ROM_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT16),
    ("Size512",         UINT8),
    ("InitEntryPoint",  UINT8 * 3),
    ("Reserved",        UINT8 * 0x12),
    ("PcirOffset",      UINT16)
    ]

class PCI_DATA_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",     UINT32),
    ("VendorId",      UINT16),
    ("DeviceId",      UINT16),
    ("Reserved0",     UINT16),
    ("Length",        UINT16),
    ("Revision",      UINT8),
    ("ClassCode",     UINT8 * 3),
    ("ImageLength",   UINT16),
    ("CodeRevision",  UINT16),
    ("CodeType",      UINT8),
    ("Indicator",     UINT8),
    ("Reserved1",     UINT16)
    ]

class EFI_PCI_EXPANSION_ROM_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT16),
    ("InitializationSize",  UINT16),
    ("EfiSignature",        UINT32),
    ("EfiSubsystem",        UINT16),
    ("EfiMachineType",      UINT16),
    ("CompressionType",     UINT16),
    ("Reserved",            UINT8 * 8),
    ("EfiImageHeaderOffset",UINT16),
    ("PcirOffset",          UINT16)
    ]

class EFI_PCI_ROM_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Raw",     POINTER (UINT8)),
    ("Generic", POINTER (PCI_EXPANSION_ROM_HEADER)),
    ("Efi",     POINTER (EFI_PCI_EXPANSION_ROM_HEADER)),
    ("PcAt",    POINTER (EFI_LEGACY_EXPANSION_ROM_HEADER))
    ]
