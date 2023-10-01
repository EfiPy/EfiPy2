# PeImage.py
#
# EfiPy2.MdePkg.IndustryStandard.PeImage
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

EFI_IMAGE_SUBSYSTEM_EFI_APPLICATION         = 10
EFI_IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 11
EFI_IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER      = 12
EFI_IMAGE_SUBSYSTEM_SAL_RUNTIME_DRIVER      = 13

IMAGE_FILE_MACHINE_I386            = 0x014c
IMAGE_FILE_MACHINE_IA64            = 0x0200
IMAGE_FILE_MACHINE_EBC             = 0x0EBC
IMAGE_FILE_MACHINE_X64             = 0x8664
IMAGE_FILE_MACHINE_ARMTHUMB_MIXED  = 0x01c2
IMAGE_FILE_MACHINE_ARM64           = 0xAA64
IMAGE_FILE_MACHINE_RISCV32         = 0x5032
IMAGE_FILE_MACHINE_RISCV64         = 0x5064
IMAGE_FILE_MACHINE_RISCV128        = 0x5128
IMAGE_FILE_MACHINE_LOONGARCH32     = 0x6232
IMAGE_FILE_MACHINE_LOONGARCH64     = 0x6264

EFI_IMAGE_DOS_SIGNATURE     = SIGNATURE_16('M', 'Z')
EFI_IMAGE_OS2_SIGNATURE     = SIGNATURE_16('N', 'E')
EFI_IMAGE_OS2_SIGNATURE_LE  = SIGNATURE_16('L', 'E')
EFI_IMAGE_NT_SIGNATURE      = SIGNATURE_32('P', 'E', '\0', '\0')

class EFI_IMAGE_DOS_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("e_magic",     UINT16),
    ("e_cblp",      UINT16),
    ("e_cp",        UINT16),
    ("e_crlc",      UINT16),
    ("e_cparhdr",   UINT16),
    ("e_minalloc",  UINT16),
    ("e_maxalloc",  UINT16),
    ("e_ss",        UINT16),
    ("e_sp",        UINT16),
    ("e_csum",      UINT16),
    ("e_ip",        UINT16),
    ("e_cs",        UINT16),
    ("e_lfarlc",    UINT16),
    ("e_ovno",      UINT16),
    ("e_res",       UINT16 * 4),
    ("e_oemid",     UINT16),
    ("e_oeminfo",   UINT16),
    ("e_res2",      UINT16 * 10),
    ("e_lfanew",    UINT32)
  ]

class EFI_IMAGE_FILE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Machine",               UINT16),
    ("NumberOfSections",      UINT16),
    ("TimeDateStamp",         UINT32),
    ("PointerToSymbolTable",  UINT32),
    ("NumberOfSymbols",       UINT32),
    ("SizeOfOptionalHeader",  UINT16),
    ("Characteristics",       UINT16)
  ]

EFI_IMAGE_SIZEOF_FILE_HEADER        = 20

EFI_IMAGE_FILE_RELOCS_STRIPPED      = BIT0
EFI_IMAGE_FILE_EXECUTABLE_IMAGE     = BIT1
EFI_IMAGE_FILE_LINE_NUMS_STRIPPED   = BIT2
EFI_IMAGE_FILE_LOCAL_SYMS_STRIPPED  = BIT3
EFI_IMAGE_FILE_BYTES_REVERSED_LO    = BIT7
EFI_IMAGE_FILE_32BIT_MACHINE        = BIT8
EFI_IMAGE_FILE_DEBUG_STRIPPED       = BIT9
EFI_IMAGE_FILE_SYSTEM               = BIT12
EFI_IMAGE_FILE_DLL                  = BIT13
EFI_IMAGE_FILE_BYTES_REVERSED_HI    = BIT15

class EFI_IMAGE_DATA_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",  UINT32),
    ("Size",            UINT32)
  ]

EFI_IMAGE_DIRECTORY_ENTRY_EXPORT      = 0
EFI_IMAGE_DIRECTORY_ENTRY_IMPORT      = 1
EFI_IMAGE_DIRECTORY_ENTRY_RESOURCE    = 2
EFI_IMAGE_DIRECTORY_ENTRY_EXCEPTION   = 3
EFI_IMAGE_DIRECTORY_ENTRY_SECURITY    = 4
EFI_IMAGE_DIRECTORY_ENTRY_BASERELOC   = 5
EFI_IMAGE_DIRECTORY_ENTRY_DEBUG       = 6
EFI_IMAGE_DIRECTORY_ENTRY_COPYRIGHT   = 7
EFI_IMAGE_DIRECTORY_ENTRY_GLOBALPTR   = 8
EFI_IMAGE_DIRECTORY_ENTRY_TLS         = 9
EFI_IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG = 10

EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES = 16

EFI_IMAGE_NT_OPTIONAL_HDR32_MAGIC = 0x10b

class EFI_IMAGE_OPTIONAL_HEADER32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Magic",                         UINT16),
    ("MajorLinkerVersion",            UINT8),
    ("MinorLinkerVersion",            UINT8),
    ("SizeOfCode",                    UINT32),
    ("SizeOfInitializedData",         UINT32),
    ("SizeOfUninitializedData",       UINT32),
    ("AddressOfEntryPoint",           UINT32),
    ("BaseOfCode",                    UINT32),
    ("BaseOfData",                    UINT32),
    ("ImageBase",                     UINT32),
    ("SectionAlignment",              UINT32),
    ("FileAlignment",                 UINT32),
    ("MajorOperatingSystemVersion",   UINT16),
    ("MinorOperatingSystemVersion",   UINT16),
    ("MajorImageVersion",             UINT16),
    ("MinorImageVersion",             UINT16),
    ("MajorSubsystemVersion",         UINT16),
    ("MinorSubsystemVersion",         UINT16),
    ("Win32VersionValue",             UINT32),
    ("SizeOfImage",                   UINT32),
    ("SizeOfHeaders",                 UINT32),
    ("CheckSum",                      UINT32),
    ("Subsystem",                     UINT16),
    ("DllCharacteristics",            UINT16),
    ("SizeOfStackReserve",            UINT32),
    ("SizeOfStackCommit",             UINT32),
    ("SizeOfHeapReserve",             UINT32),
    ("SizeOfHeapCommit",              UINT32),
    ("LoaderFlags",                   UINT32),
    ("NumberOfRvaAndSizes",           UINT32),
    ("DataDirectory",                 EFI_IMAGE_DATA_DIRECTORY * EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES)
  ]

EFI_IMAGE_NT_OPTIONAL_HDR64_MAGIC = 0x20b

class EFI_IMAGE_OPTIONAL_HEADER64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Magic",                       UINT16),
    ("MajorLinkerVersion",          UINT8),
    ("MinorLinkerVersion",          UINT8),
    ("SizeOfCode",                  UINT32),
    ("SizeOfInitializedData",       UINT32),
    ("SizeOfUninitializedData",     UINT32),
    ("AddressOfEntryPoint",         UINT32),
    ("BaseOfCode",                  UINT32),
    ("ImageBase",                   UINT64),
    ("SectionAlignment",            UINT32),
    ("FileAlignment",               UINT32),
    ("MajorOperatingSystemVersion", UINT16),
    ("MinorOperatingSystemVersion", UINT16),
    ("MajorImageVersion",           UINT16),
    ("MinorImageVersion",           UINT16),
    ("MajorSubsystemVersion",       UINT16),
    ("MinorSubsystemVersion",       UINT16),
    ("Win32VersionValue",           UINT32),
    ("SizeOfImage",                 UINT32),
    ("SizeOfHeaders",               UINT32),
    ("CheckSum",                    UINT32),
    ("Subsystem",                   UINT16),
    ("DllCharacteristics",          UINT16),
    ("SizeOfStackReserve",          UINT64),
    ("SizeOfStackCommit",           UINT64),
    ("SizeOfHeapReserve",           UINT64),
    ("SizeOfHeapCommit",            UINT64),
    ("LoaderFlags",                 UINT32),
    ("NumberOfRvaAndSizes",         UINT32),
    ("DataDirectory",               EFI_IMAGE_DATA_DIRECTORY * EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES)
  ]

class EFI_IMAGE_NT_HEADERS32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("FileHeader",      EFI_IMAGE_FILE_HEADER),
    ("OptionalHeader",  EFI_IMAGE_OPTIONAL_HEADER32)
  ]

EFI_IMAGE_SIZEOF_NT_OPTIONAL32_HEADER = sizeof (EFI_IMAGE_NT_HEADERS32)

class EFI_IMAGE_NT_HEADERS64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("FileHeader",      EFI_IMAGE_FILE_HEADER),
    ("OptionalHeader",  EFI_IMAGE_OPTIONAL_HEADER64)
  ]

EFI_IMAGE_SIZEOF_NT_OPTIONAL64_HEADER = sizeof (EFI_IMAGE_NT_HEADERS64)

EFI_IMAGE_SUBSYSTEM_UNKNOWN     = 0
EFI_IMAGE_SUBSYSTEM_NATIVE      = 1
EFI_IMAGE_SUBSYSTEM_WINDOWS_GUI = 2
EFI_IMAGE_SUBSYSTEM_WINDOWS_CUI = 3
EFI_IMAGE_SUBSYSTEM_OS2_CUI     = 5
EFI_IMAGE_SUBSYSTEM_POSIX_CUI   = 7

EFI_IMAGE_SIZEOF_SHORT_NAME = 8

class EFI_IMAGE_SECTION_HEADER_Misc (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("PhysicalAddress", UINT32),
    ("VirtualSize",     UINT32)
  ]

class EFI_IMAGE_NT_HEADERS64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Name",                  UINT8 * EFI_IMAGE_SIZEOF_SHORT_NAME),
    ("Misc",                  EFI_IMAGE_SECTION_HEADER_Misc),
    ("VirtualAddress",        UINT32),
    ("SizeOfRawData",         UINT32),
    ("PointerToRawData",      UINT32),
    ("PointerToRelocations",  UINT32),
    ("PointerToLinenumbers",  UINT32),
    ("NumberOfRelocations",   UINT16),
    ("NumberOfLinenumbers",   UINT16),
    ("Characteristics",       UINT32)
  ]

EFI_IMAGE_SIZEOF_SECTION_HEADER       = 40

EFI_IMAGE_SCN_TYPE_NO_PAD                  = BIT3
EFI_IMAGE_SCN_CNT_CODE                     = BIT5
EFI_IMAGE_SCN_CNT_INITIALIZED_DATA         = BIT6
EFI_IMAGE_SCN_CNT_UNINITIALIZED_DATA       = BIT7

EFI_IMAGE_SCN_LNK_OTHER                    = BIT8
EFI_IMAGE_SCN_LNK_INFO                     = BIT9
EFI_IMAGE_SCN_LNK_REMOVE                   = BIT11
EFI_IMAGE_SCN_LNK_COMDAT                   = BIT12

EFI_IMAGE_SCN_ALIGN_1BYTES    =              BIT20 
EFI_IMAGE_SCN_ALIGN_2BYTES    =              BIT21 
EFI_IMAGE_SCN_ALIGN_4BYTES    =       (BIT20|BIT21)
EFI_IMAGE_SCN_ALIGN_8BYTES    =              BIT22 
EFI_IMAGE_SCN_ALIGN_16BYTES   =       (BIT20|BIT22)
EFI_IMAGE_SCN_ALIGN_32BYTES   =       (BIT21|BIT22)
EFI_IMAGE_SCN_ALIGN_64BYTES   = (BIT20|BIT21|BIT22)

EFI_IMAGE_SCN_MEM_DISCARDABLE              = BIT25
EFI_IMAGE_SCN_MEM_NOT_CACHED               = BIT26
EFI_IMAGE_SCN_MEM_NOT_PAGED                = BIT27
EFI_IMAGE_SCN_MEM_SHARED                   = BIT28
EFI_IMAGE_SCN_MEM_EXECUTE                  = BIT29
EFI_IMAGE_SCN_MEM_READ                     = BIT30
EFI_IMAGE_SCN_MEM_WRITE                    = BIT31

EFI_IMAGE_SIZEOF_SYMBOL = 18

EFI_IMAGE_SYM_UNDEFINED  =  0
EFI_IMAGE_SYM_ABSOLUTE   = -1
EFI_IMAGE_SYM_DEBUG      = -2

EFI_IMAGE_SYM_TYPE_NULL   = 0
EFI_IMAGE_SYM_TYPE_VOID   = 1
EFI_IMAGE_SYM_TYPE_CHAR   = 2
EFI_IMAGE_SYM_TYPE_SHORT  = 3
EFI_IMAGE_SYM_TYPE_INT    = 4
EFI_IMAGE_SYM_TYPE_LONG   = 5
EFI_IMAGE_SYM_TYPE_FLOAT  = 6
EFI_IMAGE_SYM_TYPE_DOUBLE = 7
EFI_IMAGE_SYM_TYPE_STRUCT = 8
EFI_IMAGE_SYM_TYPE_UNION  = 9
EFI_IMAGE_SYM_TYPE_ENUM   = 10
EFI_IMAGE_SYM_TYPE_MOE    = 11
EFI_IMAGE_SYM_TYPE_BYTE   = 12
EFI_IMAGE_SYM_TYPE_WORD   = 13
EFI_IMAGE_SYM_TYPE_UINT   = 14
EFI_IMAGE_SYM_TYPE_DWORD  = 15

EFI_IMAGE_SYM_DTYPE_NULL      = 0
EFI_IMAGE_SYM_DTYPE_POINTER   = 1
EFI_IMAGE_SYM_DTYPE_FUNCTION  = 2
EFI_IMAGE_SYM_DTYPE_ARRAY     = 3

EFI_IMAGE_SYM_CLASS_END_OF_FUNCTION   = -1
EFI_IMAGE_SYM_CLASS_NULL              = 0
EFI_IMAGE_SYM_CLASS_AUTOMATIC         = 1
EFI_IMAGE_SYM_CLASS_EXTERNAL          = 2
EFI_IMAGE_SYM_CLASS_STATIC            = 3
EFI_IMAGE_SYM_CLASS_REGISTER          = 4
EFI_IMAGE_SYM_CLASS_EXTERNAL_DEF      = 5
EFI_IMAGE_SYM_CLASS_LABEL             = 6
EFI_IMAGE_SYM_CLASS_UNDEFINED_LABEL   = 7
EFI_IMAGE_SYM_CLASS_MEMBER_OF_STRUCT  = 8
EFI_IMAGE_SYM_CLASS_ARGUMENT          = 9
EFI_IMAGE_SYM_CLASS_STRUCT_TAG        = 10
EFI_IMAGE_SYM_CLASS_MEMBER_OF_UNION   = 11
EFI_IMAGE_SYM_CLASS_UNION_TAG         = 12
EFI_IMAGE_SYM_CLASS_TYPE_DEFINITION   = 13
EFI_IMAGE_SYM_CLASS_UNDEFINED_STATIC  = 14
EFI_IMAGE_SYM_CLASS_ENUM_TAG          = 15
EFI_IMAGE_SYM_CLASS_MEMBER_OF_ENUM    = 16
EFI_IMAGE_SYM_CLASS_REGISTER_PARAM    = 17
EFI_IMAGE_SYM_CLASS_BIT_FIELD         = 18
EFI_IMAGE_SYM_CLASS_BLOCK             = 100
EFI_IMAGE_SYM_CLASS_FUNCTION          = 101
EFI_IMAGE_SYM_CLASS_END_OF_STRUCT     = 102
EFI_IMAGE_SYM_CLASS_FILE              = 103
EFI_IMAGE_SYM_CLASS_SECTION           = 104
EFI_IMAGE_SYM_CLASS_WEAK_EXTERNAL     = 105

EFI_IMAGE_N_BTMASK  = 0o17
EFI_IMAGE_N_TMASK   = 0o60
EFI_IMAGE_N_TMASK1  = 0o300
EFI_IMAGE_N_TMASK2  = 0o360
EFI_IMAGE_N_BTSHFT  = 4
EFI_IMAGE_N_TSHIFT  = 2

EFI_IMAGE_COMDAT_SELECT_NODUPLICATES    = 1
EFI_IMAGE_COMDAT_SELECT_ANY             = 2
EFI_IMAGE_COMDAT_SELECT_SAME_SIZE       = 3
EFI_IMAGE_COMDAT_SELECT_EXACT_MATCH     = 4
EFI_IMAGE_COMDAT_SELECT_ASSOCIATIVE     = 5

EFI_IMAGE_WEAK_EXTERN_SEARCH_NOLIBRARY  = 1
EFI_IMAGE_WEAK_EXTERN_SEARCH_LIBRARY    = 2
EFI_IMAGE_WEAK_EXTERN_SEARCH_ALIAS      = 3

class EFI_IMAGE_RELOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",    UINT32),
    ("SymbolTableIndex",  UINT32),
    ("Type",              UINT16)
  ]

EFI_IMAGE_SIZEOF_RELOCATION = 10

EFI_IMAGE_REL_I386_ABSOLUTE = 0x0000
EFI_IMAGE_REL_I386_DIR16    = 0x0001
EFI_IMAGE_REL_I386_REL16    = 0x0002
EFI_IMAGE_REL_I386_DIR32    = 0x0006
EFI_IMAGE_REL_I386_DIR32NB  = 0x0007
EFI_IMAGE_REL_I386_SEG12    = 0x0009
EFI_IMAGE_REL_I386_SECTION  = 0x000A
EFI_IMAGE_REL_I386_SECREL   = 0x000B
EFI_IMAGE_REL_I386_REL32    = 0x0014

IMAGE_REL_AMD64_ABSOLUTE  = 0x0000
IMAGE_REL_AMD64_ADDR64    = 0x0001
IMAGE_REL_AMD64_ADDR32    = 0x0002
IMAGE_REL_AMD64_ADDR32NB  = 0x0003
IMAGE_REL_AMD64_REL32     = 0x0004
IMAGE_REL_AMD64_REL32_1   = 0x0005
IMAGE_REL_AMD64_REL32_2   = 0x0006
IMAGE_REL_AMD64_REL32_3   = 0x0007
IMAGE_REL_AMD64_REL32_4   = 0x0008
IMAGE_REL_AMD64_REL32_5   = 0x0009
IMAGE_REL_AMD64_SECTION   = 0x000A
IMAGE_REL_AMD64_SECREL    = 0x000B
IMAGE_REL_AMD64_SECREL7   = 0x000C
IMAGE_REL_AMD64_TOKEN     = 0x000D
IMAGE_REL_AMD64_SREL32    = 0x000E
IMAGE_REL_AMD64_PAIR      = 0x000F
IMAGE_REL_AMD64_SSPAN32   = 0x0010

class EFI_IMAGE_BASE_RELOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",  UINT32),
    ("SizeOfBlock",     UINT32)
  ]

EFI_IMAGE_SIZEOF_BASE_RELOCATION  = 8

EFI_IMAGE_REL_BASED_ABSOLUTE        = 0
EFI_IMAGE_REL_BASED_HIGH            = 1
EFI_IMAGE_REL_BASED_LOW             = 2
EFI_IMAGE_REL_BASED_HIGHLOW         = 3
EFI_IMAGE_REL_BASED_HIGHADJ         = 4
EFI_IMAGE_REL_BASED_MIPS_JMPADDR    = 5
EFI_IMAGE_REL_BASED_ARM_MOV32A      = 5
EFI_IMAGE_REL_BASED_ARM_MOV32T      = 7
EFI_IMAGE_REL_BASED_IA64_IMM64      = 9
EFI_IMAGE_REL_BASED_MIPS_JMPADDR16  = 9
EFI_IMAGE_REL_BASED_DIR64           = 10

EFI_IMAGE_REL_BASED_RISCV_HI20    = 5
EFI_IMAGE_REL_BASED_RISCV_LOW12I  = 7
EFI_IMAGE_REL_BASED_RISCV_LOW12S  = 8

EFI_IMAGE_REL_BASED_LOONGARCH32_MARK_LA  = 8
EFI_IMAGE_REL_BASED_LOONGARCH64_MARK_LA  = 8

class EFI_IMAGE_LINENUMBER_Type (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("SymbolTableIndex",  UINT32),
    ("VirtualAddress",    UINT32)
  ]

class EFI_IMAGE_LINENUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        EFI_IMAGE_LINENUMBER_Type),
    ("Linenumber",  UINT16)
  ]

EFI_IMAGE_SIZEOF_LINENUMBER = 6

EFI_IMAGE_ARCHIVE_START_SIZE        = 8
EFI_IMAGE_ARCHIVE_START             = b"!<arch>\n"
EFI_IMAGE_ARCHIVE_END               = b"`\n"
EFI_IMAGE_ARCHIVE_PAD               = b"\n"
EFI_IMAGE_ARCHIVE_LINKER_MEMBER     = b"/               " 
EFI_IMAGE_ARCHIVE_LONGNAMES_MEMBER  = b"//              " 

class EFI_IMAGE_ARCHIVE_MEMBER_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Name",      UINT8 * 16),
    ("Date",      UINT8 * 12),
    ("UserID",    UINT8 * 6),
    ("GroupID",   UINT8 * 6),
    ("Mode",      UINT8 * 8),
    ("Size",      UINT8 * 10),
    ("EndHeader", UINT8 * 2)
  ]

EFI_IMAGE_SIZEOF_ARCHIVE_MEMBER_HDR = 60

class EFI_IMAGE_EXPORT_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics",       UINT32),
    ("TimeDateStamp",         UINT32),
    ("MajorVersion",          UINT16),
    ("MinorVersion",          UINT16),
    ("Name",                  UINT32),
    ("Base",                  UINT32),
    ("NumberOfFunctions",     UINT32),
    ("NumberOfNames",         UINT32),
    ("AddressOfFunctions",    UINT32),
    ("AddressOfNames",        UINT32),
    ("AddressOfNameOrdinals", UINT32)
  ]

class EFI_IMAGE_IMPORT_BY_NAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hint",  UINT16),
    ("Name",  UINT8 * 1)
  ]

class EFI_IMAGE_THUNK_DATA_u1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Function",      UINT32),
    ("Ordinal",       UINT32),
    ("AddressOfData", POINTER (EFI_IMAGE_IMPORT_BY_NAME))
  ]

class EFI_IMAGE_THUNK_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("u1",  EFI_IMAGE_THUNK_DATA_u1)
  ]

EFI_IMAGE_ORDINAL_FLAG              = BIT31

def EFI_IMAGE_SNAP_BY_ORDINAL (Ordinal):

  if (Ordinal & EFI_IMAGE_ORDINAL_FLAG) != 0:
    return True
  else:
    return False

def EFI_IMAGE_ORDINAL(Ordinal):
  return Ordinal & 0xffff

class EFI_IMAGE_IMPORT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics", UINT32),
    ("TimeDateStamp",   UINT32),
    ("ForwarderChain",  UINT32),
    ("Name",            UINT32),
    ("FirstThunk",      POINTER (EFI_IMAGE_THUNK_DATA))
  ]

class EFI_IMAGE_DEBUG_DIRECTORY_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics", UINT32),
    ("TimeDateStamp",   UINT32),
    ("MajorVersion",    UINT16),
    ("MinorVersion",    UINT16),
    ("Type",            UINT32),
    ("SizeOfData",      UINT32),
    ("RVA",             UINT32),
    ("FileOffset",      UINT32)
  ]

EFI_IMAGE_DEBUG_TYPE_CODEVIEW               = 2
EFI_IMAGE_DEBUG_TYPE_EX_DLLCHARACTERISTICS  = 20

CODEVIEW_SIGNATURE_NB10  = SIGNATURE_32('N', 'B', '1', '0')

class EFI_IMAGE_DEBUG_CODEVIEW_NB10_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Unknown",   UINT32),
    ("Unknown2",  UINT32),
    ("Unknown3",  UINT32)
  ]

CODEVIEW_SIGNATURE_RSDS  = SIGNATURE_32('R', 'S', 'D', 'S')

class EFI_IMAGE_DEBUG_CODEVIEW_RSDS_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Unknown",   UINT32),
    ("Unknown2",  UINT32),
    ("Unknown3",  UINT32),
    ("Unknown4",  UINT32),
    ("Unknown5",  UINT32)
  ]

CODEVIEW_SIGNATURE_MTOC  = SIGNATURE_32('M', 'T', 'O', 'C')

class EFI_IMAGE_DEBUG_CODEVIEW_MTOC_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("MachOUuid", GUID)
  ]

EFI_IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT          = 0x0001
EFI_IMAGE_DLLCHARACTERISTICS_EX_FORWARD_CFI_COMPAT  = 0x0040

class EFI_IMAGE_DEBUG_EX_DLLCHARACTERISTICS_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DllCharacteristicsEx", UINT32)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics",       UINT32),
    ("TimeDateStamp",         UINT32),
    ("MajorVersion",          UINT16),
    ("MinorVersion",          UINT16),
    ("NumberOfNamedEntries",  UINT16),
    ("NumberOfIdEntries",     UINT16)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1_s (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NameOffset",    UINT32, 31),
    ("NameIsString",  UINT32, 1),
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("s",   EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1_s),
    ("Id",  UINT32)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2_s (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OffsetToDirectory", UINT32, 31),
    ("DataIsDirectory",   UINT32, 1)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("OffsetToData",  UINT32),
    ("s",             EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2_s)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("u1",  EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1),
    ("u2",  EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",  UINT16),
    ("String",  CHAR16 * 1)
  ]

class EFI_IMAGE_RESOURCE_DATA_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OffsetToData",  UINT32),
    ("Size",          UINT32),
    ("CodePage",      UINT32),
    ("Reserved",      UINT32)
  ]

class EFI_TE_IMAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT16),
    ("Machine",             UINT16),
    ("NumberOfSections",    UINT8),
    ("Subsystem",           UINT8),
    ("StrippedSize",        UINT16),
    ("AddressOfEntryPoint", UINT32),
    ("BaseOfCode",          UINT32),
    ("ImageBase",           UINT64),
    ("DataDirectory",       EFI_IMAGE_DATA_DIRECTORY * 2)
  ]

EFI_TE_IMAGE_HEADER_SIGNATURE  = SIGNATURE_16('V', 'Z')

EFI_TE_IMAGE_DIRECTORY_ENTRY_BASERELOC  = 0
EFI_TE_IMAGE_DIRECTORY_ENTRY_DEBUG      = 1

class EFI_IMAGE_OPTIONAL_HEADER_UNION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Pe32",      EFI_IMAGE_NT_HEADERS32),
    ("Pe32Plus",  EFI_IMAGE_NT_HEADERS64),
    ("Te",        EFI_TE_IMAGE_HEADER)
  ]

class EFI_IMAGE_OPTIONAL_HEADER_PTR_UNION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Pe32",      POINTER (EFI_IMAGE_NT_HEADERS32)),
    ("Pe32Plus",  POINTER (EFI_IMAGE_NT_HEADERS64)),
    ("Te",        POINTER (EFI_TE_IMAGE_HEADER)),
    ("Union",     POINTER (EFI_IMAGE_OPTIONAL_HEADER_UNION))
  ]

