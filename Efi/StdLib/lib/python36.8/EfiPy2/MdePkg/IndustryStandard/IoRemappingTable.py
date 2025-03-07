# IoRemappingTable.py
#
# EfiPy2.MdePkg.IndustryStandard.IoRemappingTable
#   part of EfiPy2
#
# Copyright (C) 2023 - 20025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

EFI_ACPI_IO_REMAPPING_TABLE_REVISION_00  = 0x0
EFI_ACPI_IO_REMAPPING_TABLE_REVISION_04  = 0x4
EFI_ACPI_IO_REMAPPING_TABLE_REVISION_05  = 0x5
EFI_ACPI_IO_REMAPPING_TABLE_REVISION_06  = 0x6

EFI_ACPI_IORT_TYPE_ITS_GROUP     = 0x0
EFI_ACPI_IORT_TYPE_NAMED_COMP    = 0x1
EFI_ACPI_IORT_TYPE_ROOT_COMPLEX  = 0x2
EFI_ACPI_IORT_TYPE_SMMUv1v2      = 0x3
EFI_ACPI_IORT_TYPE_SMMUv3        = 0x4
EFI_ACPI_IORT_TYPE_PMCG          = 0x5
EFI_ACPI_IORT_TYPE_RMR           = 0x6

EFI_ACPI_IORT_MEM_ACCESS_PROP_CCA  = BIT0

EFI_ACPI_IORT_MEM_ACCESS_PROP_AH_TR   = BIT0
EFI_ACPI_IORT_MEM_ACCESS_PROP_AH_WA   = BIT1
EFI_ACPI_IORT_MEM_ACCESS_PROP_AH_RA   = BIT2
EFI_ACPI_IORT_MEM_ACCESS_PROP_AH_AHO  = BIT3

EFI_ACPI_IORT_MEM_ACCESS_FLAGS_CPM     = BIT0
EFI_ACPI_IORT_MEM_ACCESS_FLAGS_DACS    = BIT1
EFI_ACPI_IORT_MEM_ACCESS_FLAGS_CANWBS  = BIT2

EFI_ACPI_IORT_SMMUv1v2_MODEL_v1             = 0x0
EFI_ACPI_IORT_SMMUv1v2_MODEL_v2             = 0x1
EFI_ACPI_IORT_SMMUv1v2_MODEL_MMU400         = 0x2
EFI_ACPI_IORT_SMMUv1v2_MODEL_MMU500         = 0x3
EFI_ACPI_IORT_SMMUv1v2_MODEL_MMU401         = 0x4
EFI_ACPI_IORT_SMMUv1v2_MODEL_CAVIUM_THX_v2  = 0x5

EFI_ACPI_IORT_SMMUv1v2_FLAG_DVM       = BIT0
EFI_ACPI_IORT_SMMUv1v2_FLAG_COH_WALK  = BIT1

EFI_ACPI_IORT_SMMUv1v2_INT_FLAG_LEVEL  = 0x0
EFI_ACPI_IORT_SMMUv1v2_INT_FLAG_EDGE   = 0x1

EFI_ACPI_IORT_SMMUv3_FLAG_COHAC_OVERRIDE    = BIT0
EFI_ACPI_IORT_SMMUv3_FLAG_HTTU_OVERRIDE     = BIT1
EFI_ACPI_IORT_SMMUv3_FLAG_HTTU_OVERRIDE_DS  = BIT2
EFI_ACPI_IORT_SMMUv3_FLAG_PROXIMITY_DOMAIN  = BIT3
EFI_ACPI_IORT_SMMUv3_FLAG_DEVICEID_VALID    = BIT4

EFI_ACPI_IORT_SMMUv3_MODEL_GENERIC           = 0x0
EFI_ACPI_IORT_SMMUv3_MODEL_HISILICON_HI161X  = 0x1
EFI_ACPI_IORT_SMMUv3_MODEL_CAVIUM_CN99XX     = 0x2

EFI_ACPI_IORT_ROOT_COMPLEX_ATS_UNSUPPORTED  = 0x0
EFI_ACPI_IORT_ROOT_COMPLEX_ATS_SUPPORTED    = BIT0

EFI_ACPI_IORT_ROOT_COMPLEX_PRI_UNSUPPORTED  = 0x0
EFI_ACPI_IORT_ROOT_COMPLEX_PRI_SUPPORTED    = BIT1

EFI_ACPI_IORT_ROOT_COMPLEX_PASID_FWD_UNSUPPORTED  = 0x0
EFI_ACPI_IORT_ROOT_COMPLEX_PASID_FWD_SUPPORTED    = BIT2

EFI_ACPI_IORT_ROOT_COMPLEX_PASID_UNSUPPORTED  = 0x0
EFI_ACPI_IORT_ROOT_COMPLEX_PASID_SUPPORTED    = BIT1

EFI_ACPI_IORT_RMR_REMAP_NOT_PERMITTED  = 0x0
EFI_ACPI_IORT_RMR_REMAP_PERMITTED      = BIT0

EFI_ACPI_IORT_RMR_ACCESS_REQ_NOT_PRIVILEGED  = 0x0
EFI_ACPI_IORT_RMR_ACCESS_REQ_PRIVILEGED      = BIT1

EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_DEV_NGNRNE             = 0x0
EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_DEV_NGNRE              = 0x1
EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_DEV_NGRE               = 0x2
EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_DEV_GRE                = 0x3
EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_NORM_IN_NC_OUT_NC      = 0x4
EFI_ACPI_IORT_RMR_ACCESS_ATTRIB_NORM_IN_WB_OUT_WB_ISH  = 0x5

EFI_ACPI_IORT_ID_MAPPING_FLAGS_SINGLE  = BIT0

EFI_ACPI_IORT_RMR_NODE_REVISION_02  = 0x2    # Deprecated

class EFI_ACPI_6_0_IO_REMAPPING_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("NumNodes",    UINT32                     ),
    ("NodeOffset",  UINT32                     ),
    ("Reserved",    UINT32                     )
  ]

class EFI_ACPI_6_0_IO_REMAPPING_ID_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InputBase",       UINT32),
    ("NumIds",          UINT32),
    ("OutputBase",      UINT32),
    ("OutputReference", UINT32),
    ("Flags",           UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8 ),
    ("Length",          UINT16),
    ("Revision",        UINT8 ),
    ("Identifier",      UINT32),
    ("NumIdMappings",   UINT32),
    ("IdReference",     UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_ITS_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("NumItsIdentifiers",   UINT32)
    # ("ItsIdentifiers",      UINT32 * NumItsIdentifiers)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_RC_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("CacheCoherent",       UINT32),
    ("AllocationHints",     UINT8 ),
    ("Reserved",            UINT16),
    ("MemoryAccessFlags",   UINT8 ),
    ("AtsAttribute",        UINT32),
    ("PciSegmentNumber",    UINT32),
    ("MemoryAddressSize",   UINT8 ),
    ("PasidCapabilities",   UINT16),
    ("Reserved1",           UINT8 * 1),
    ("Flags",               UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_NAMED_COMP_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("Flags",               UINT32),
    ("CacheCoherent",       UINT32),
    ("AllocationHints",     UINT8 ),
    ("Reserved",            UINT16),
    ("MemoryAccessFlags",   UINT8 ),
    ("AddressSizeLimit",    UINT8 )
    # ("ObjectName",          UINT8 * N),
  ]

class EFI_ACPI_6_0_IO_REMAPPING_SMMU_INT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Interrupt",       UINT32),
    ("InterruptFlags",  UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_SMMU_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                        EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("Base",                        UINT64),
    ("Span",                        UINT64),
    ("Model",                       UINT32),
    ("Flags",                       UINT32),
    ("GlobalInterruptArrayRef",     UINT32),
    ("NumContextInterrupts",        UINT32),
    ("ContextInterruptArrayRef",    UINT32),
    ("NumPmuInterrupts",            UINT32),
    ("PmuInterruptArrayRef",        UINT32),
    ("SMMU_NSgIrpt",                UINT32),
    ("SMMU_NSgIrptFlags",           UINT32),
    ("SMMU_NSgCfgIrpt",             UINT32),
    ("SMMU_NSgCfgIrptFlags",        UINT32)
    # ("ContextInterrupt",            EFI_ACPI_6_0_IO_REMAPPING_SMMU_CTX_INT * NumContextInterrupts),
    # ("PmuInterrupt",                EFI_ACPI_6_0_IO_REMAPPING_SMMU_CTX_INT * NumPmuInterrupts),
  ]

class EFI_ACPI_6_0_IO_REMAPPING_SMMU3_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                        EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("Base",                        UINT64),
    ("Flags",                       UINT32),
    ("Reserved",                    UINT32),
    ("VatosAddress",                UINT64),
    ("Model",                       UINT32),
    ("Event",                       UINT32),
    ("Pri",                         UINT32),
    ("Gerr",                        UINT32),
    ("Sync",                        UINT32),
    ("ProximityDomain",             UINT32),
    ("DeviceIdMappingIndex",        UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_PMCG_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",                        EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("Base",                        UINT64),
    ("OverflowInterruptGsiv",       UINT32),
    ("NodeReference",               UINT32),
    ("Page1Base",                   UINT64)
    # ("OverflowInterruptMsiMapping", EFI_ACPI_6_0_IO_REMAPPING_ID_TABLE * 1)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_MEM_RANGE_DESC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Base",        UINT64),
    ("Length",      UINT64),
    ("Reserved",    UINT32)
  ]

class EFI_ACPI_6_0_IO_REMAPPING_RMR_NODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Node",            EFI_ACPI_6_0_IO_REMAPPING_NODE),
    ("Flags",           UINT32),
    ("NumMemRangeDesc", UINT32),
    ("MemRangeDescRef", UINT32)
    # ("IdMapping",       EFI_ACPI_6_0_IO_REMAPPING_ID_TABLE * 1),
    # ("MemRangeDesc",    EFI_ACPI_6_0_IO_REMAPPING_MEM_RANGE_DESC * 1),
  ]

