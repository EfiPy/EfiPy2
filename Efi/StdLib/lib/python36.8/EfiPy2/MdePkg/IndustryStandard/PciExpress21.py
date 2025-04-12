# PciExpress21.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress21
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard.Pci30 import EFI_PCI_CAPABILITY_HDR

def PCI_ECAM_ADDRESS(Bus, Device, Function, Offset):

  return (((Offset) & 0xfff) | (((Function) & 0x07) << 12) | (((Device) & 0x1f) << 15) | (((Bus) & 0xff) << 20))

class PCI_REG_PCIE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",                UINT16, 4),
    ("DevicePortType",         UINT16, 4),
    ("SlotImplemented",        UINT16, 1),
    ("InterruptMessageNumber", UINT16, 5),
    ("Undefined",              UINT16, 1),
    ("FlitModeSupported",      UINT16, 1)
  ]

class PCI_REG_PCIE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_CAPABILITY_Bits),
    ("Uint16",          UINT16)
    ]

PCIE_DEVICE_PORT_TYPE_PCIE_ENDPOINT                     = 0
PCIE_DEVICE_PORT_TYPE_LEGACY_PCIE_ENDPOINT              = 1
PCIE_DEVICE_PORT_TYPE_ROOT_PORT                         = 4
PCIE_DEVICE_PORT_TYPE_UPSTREAM_PORT                     = 5
PCIE_DEVICE_PORT_TYPE_DOWNSTREAM_PORT                   = 6
PCIE_DEVICE_PORT_TYPE_PCIE_TO_PCI_BRIDGE                = 7
PCIE_DEVICE_PORT_TYPE_PCI_TO_PCIE_BRIDGE                = 8
PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_INTEGRATED_ENDPOINT  = 9
PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_EVENT_COLLECTOR      = 10

class PCI_REG_PCIE_DEVICE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxPayloadSize",                  UINT32, 3),
    ("PhantomFunctions",                UINT32, 2),
    ("ExtendedTagField",                UINT32, 1),
    ("EndpointL0sAcceptableLatency",    UINT32, 3),
    ("EndpointL1AcceptableLatency",     UINT32, 3),
    ("Undefined",                       UINT32, 3),
    ("RoleBasedErrorReporting",         UINT32, 1),
    ("ErrCorSubclassCapable",           UINT32, 1),
    ("RxMpsFixed",                      UINT32, 1),
    ("CapturedSlotPowerLimitValue",     UINT32, 8),
    ("CapturedSlotPowerLimitScale",     UINT32, 2),
    ("FunctionLevelReset",              UINT32, 1),
    ("MixedMpsSupported",               UINT32, 1),
    ("Reserved2",                       UINT32, 2)
  ]

class PCI_REG_PCIE_DEVICE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_REG_PCIE_DEVICE_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CorrectableError",                                UINT16, 1),
    ("NonFatalError",                                   UINT16, 1),
    ("FatalError",                                      UINT16, 1),
    ("UnsupportedRequest",                              UINT16, 1),
    ("RelaxedOrdering",                                 UINT16, 1),
    ("MaxPayloadSize",                                  UINT16, 3),
    ("ExtendedTagField",                                UINT16, 1),
    ("PhantomFunctions",                                UINT16, 1),
    ("AuxPower",                                        UINT16, 1),
    ("NoSnoop",                                         UINT16, 1),
    ("MaxReadRequestSize",                              UINT16, 3),
    ("BridgeConfigurationRetryOrFunctionLevelReset",    UINT16, 1)
  ]

class PCI_REG_PCIE_DEVICE_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

PCIE_MAX_PAYLOAD_SIZE_128B   = 0
PCIE_MAX_PAYLOAD_SIZE_256B   = 1
PCIE_MAX_PAYLOAD_SIZE_512B   = 2
PCIE_MAX_PAYLOAD_SIZE_1024B  = 3
PCIE_MAX_PAYLOAD_SIZE_2048B  = 4
PCIE_MAX_PAYLOAD_SIZE_4096B  = 5
PCIE_MAX_PAYLOAD_SIZE_RVSD1  = 6
PCIE_MAX_PAYLOAD_SIZE_RVSD2  = 7

PCIE_MAX_READ_REQ_SIZE_128B   = 0
PCIE_MAX_READ_REQ_SIZE_256B   = 1
PCIE_MAX_READ_REQ_SIZE_512B   = 2
PCIE_MAX_READ_REQ_SIZE_1024B  = 3
PCIE_MAX_READ_REQ_SIZE_2048B  = 4
PCIE_MAX_READ_REQ_SIZE_4096B  = 5
PCIE_MAX_READ_REQ_SIZE_RVSD1  = 6
PCIE_MAX_READ_REQ_SIZE_RVSD2  = 7

class PCI_REG_PCIE_DEVICE_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CorrectableError",                    UINT16, 1),
    ("NonFatalError",                       UINT16, 1),
    ("FatalError",                          UINT16, 1),
    ("UnsupportedRequest",                  UINT16, 1),
    ("AuxPower",                            UINT16, 1),
    ("TransactionsPending",                 UINT16, 1),
    ("EmergencyPowerReductionDetected",     UINT16, 1),
    ("Reserved",                            UINT16, 9)
  ]

class PCI_REG_PCIE_DEVICE_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_LINK_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxLinkSpeed",                UINT32, 4),
    ("MaxLinkWidth",                UINT32, 6),
    ("Aspm",                        UINT32, 2),
    ("L0sExitLatency",              UINT32, 3),
    ("L1ExitLatency",               UINT32, 3),
    ("ClockPowerManagement",        UINT32, 1),
    ("SurpriseDownError",           UINT32, 1),
    ("DataLinkLayerLinkActive",     UINT32, 1),
    ("LinkBandwidthNotification",   UINT32, 1),
    ("AspmOptionalityCompliance",   UINT32, 1),
    ("Reserved",                    UINT32, 1),
    ("PortNumber",                  UINT32, 8)
  ]

class PCI_REG_PCIE_LINK_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

PCIE_LINK_ASPM_L0S  = BIT0
PCIE_LINK_ASPM_L1   = BIT1

class PCI_REG_PCIE_LINK_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AspmControl",                         UINT16, 2),
    ("PtmPropagationDelayB",                UINT16, 1),
    ("ReadCompletionBoundary",              UINT16, 1),
    ("LinkDisable",                         UINT16, 1),
    ("RetrainLink",                         UINT16, 1),
    ("CommonClockConfiguration",            UINT16, 1),
    ("ExtendedSynch",                       UINT16, 1),
    ("ClockPowerManagement",                UINT16, 1),
    ("HardwareAutonomousWidthDisable",      UINT16, 1),
    ("LinkBandwidthManagementInterrupt",    UINT16, 1),
    ("LinkAutonomousBandwidthInterrupt",    UINT16, 1),
    ("SrisClocking",                        UINT16, 1),
    ("FlitModeDisable",                     UINT16, 1),
    ("DrsSignalingControl",                 UINT16, 2)
  ]

class PCI_REG_PCIE_LINK_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_LINK_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentLinkSpeed",        UINT16, 4),
    ("NegotiatedLinkWidth",     UINT16, 6),
    ("Undefined",               UINT16, 1),
    ("LinkTraining",            UINT16, 1),
    ("SlotClockConfiguration ", UINT16, 1),
    ("DataLinkLayerLinkActive", UINT16, 1),
    ("LinkBandwidthManagement", UINT16, 1),
    ("LinkAutonomousBandwidth", UINT16, 1)
  ]

class PCI_REG_PCIE_LINK_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_SLOT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButton",             UINT32, 1),
    ("PowerController",             UINT32, 1),
    ("MrlSensor",                   UINT32, 1),
    ("AttentionIndicator",          UINT32, 1),
    ("PowerIndicator",              UINT32, 1),
    ("HotPlugSurprise",             UINT32, 1),
    ("HotPlugCapable",              UINT32, 1),
    ("SlotPowerLimitValue",         UINT32, 8),
    ("SlotPowerLimitScale",         UINT32, 2),
    ("ElectromechanicalInterlock",  UINT32, 1),
    ("NoCommandCompleted",          UINT32, 1),
    ("PhysicalSlotNumber",          UINT32, 13)
  ]

class PCI_REG_PCIE_SLOT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_REG_PCIE_SLOT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButtonPressed",      UINT16, 1),
    ("PowerFaultDetected",          UINT16, 1),
    ("MrlSensorChanged",            UINT16, 1),
    ("PresenceDetectChanged",       UINT16, 1),
    ("CommandCompletedInterrupt",   UINT16, 1),
    ("HotPlugInterrupt",            UINT16, 1),
    ("AttentionIndicator",          UINT16, 2),
    ("PowerIndicator",              UINT16, 2),
    ("PowerController",             UINT16, 1),
    ("ElectromechanicalInterlock",  UINT16, 1),
    ("DataLinkLayerStateChanged",   UINT16, 1),
    ("AutoSlotPowerLimitDisable",   UINT16, 1),
    ("InbandPdDisable",             UINT16, 1),
    ("Reserved",                    UINT16, 1)
  ]

class PCI_REG_PCIE_SLOT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_SLOT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButtonPressed",      UINT16, 1),
    ("PowerFaultDetected",          UINT16, 1),
    ("MrlSensorChanged",            UINT16, 1),
    ("PresenceDetectChanged",       UINT16, 1),
    ("CommandCompleted",            UINT16, 1),
    ("MrlSensor",                   UINT16, 1),
    ("PresenceDetect",              UINT16, 1),
    ("ElectromechanicalInterlock",  UINT16, 1),
    ("DataLinkLayerStateChanged",   UINT16, 1),
    ("Reserved",                    UINT16, 7)
  ]

class PCI_REG_PCIE_SLOT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_ROOT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemErrorOnCorrectableError",   UINT16, 1),
    ("SystemErrorOnNonFatalError",      UINT16, 1),
    ("SystemErrorOnFatalError",         UINT16, 1),
    ("PmeInterrupt",                    UINT16, 1),
    ("CrsSoftwareVisibility",           UINT16, 1),
    ("NoNfmSubtree",                    UINT16, 1),
    ("Reserved",                        UINT16, 10)
  ]

class PCI_REG_PCIE_ROOT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_ROOT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CrsSoftwareVisibility",           UINT16, 1),
    ("Reserved",                        UINT16, 15)
  ]

class PCI_REG_PCIE_ROOT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_CAPABILITY_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_ROOT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PmeRequesterId",  UINT32, 16),
    ("PmeStatus",       UINT32, 1),
    ("PmePending",      UINT32, 1),
    ("Reserved",        UINT32, 14)
  ]

class PCI_REG_PCIE_ROOT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_STATUS_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_REG_PCIE_DEVICE_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionTimeoutRanges",                         UINT32, 4),
    ("CompletionTimeoutDisable",                        UINT32, 1),
    ("AriForwarding",                                   UINT32, 1),
    ("AtomicOpRouting",                                 UINT32, 1),
    ("AtomicOp32Completer",                             UINT32, 1),
    ("AtomicOp64Completer",                             UINT32, 1),
    ("Cas128Completer",                                 UINT32, 1),
    ("NoRoEnabledPrPrPassing",                          UINT32, 1),
    ("LtrMechanism",                                    UINT32, 1),
    ("TphCompleter",                                    UINT32, 2),
    ("Reserved",                                        UINT32, 2),
    ("TenBitTagCompleterSupported",                     UINT32, 1),
    ("TenBitTagRequesterSupported",                     UINT32, 1),
    ("Obff",                                            UINT32, 2),
    ("ExtendedFmtField",                                UINT32, 1),
    ("EndEndTlpPrefix",                                 UINT32, 1),
    ("MaxEndEndTlpPrefixes",                            UINT32, 2),
    ("EmergencyPowerReductionSupported",                UINT32, 2),
    ("EmergencyPowerReductionInitializationRequired",   UINT32, 1),
    ("Reserved2",                                       UINT32, 1),
    ("DmwrCompleter",                                   UINT32, 1),
    ("DmwrLengths",                                     UINT32, 2),
    ("FrsSupported",                                    UINT32, 1)
  ]

class PCI_REG_PCIE_DEVICE_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CAPABILITY2_Bits),
    ("Uint32",          UINT32)
    ]

PCIE_COMPLETION_TIMEOUT_NOT_SUPPORTED            = 0
PCIE_COMPLETION_TIMEOUT_RANGE_A_SUPPORTED        = 1
PCIE_COMPLETION_TIMEOUT_RANGE_B_SUPPORTED        = 2
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_SUPPORTED      = 3
PCIE_COMPLETION_TIMEOUT_RANGE_B_C_SUPPORTED      = 6
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_SUPPORTED    = 7
PCIE_COMPLETION_TIMEOUT_RANGE_B_C_D_SUPPORTED    = 14
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_D_SUPPORTED  = 15

PCIE_DEVICE_CAPABILITY_OBFF_MESSAGE  = BIT0
PCIE_DEVICE_CAPABILITY_OBFF_WAKE     = BIT1

class PCI_REG_PCIE_DEVICE_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionTimeoutValue",          UINT16, 4),
    ("CompletionTimeoutDisable",        UINT16, 1),
    ("AriForwarding",                   UINT16, 1),
    ("AtomicOpRequester",               UINT16, 1),
    ("AtomicOpEgressBlocking",          UINT16, 1),
    ("IdoRequest",                      UINT16, 1),
    ("IdoCompletion",                   UINT16, 1),
    ("LtrMechanism",                    UINT16, 1),
    ("EmergencyPowerReductionRequest",  UINT16, 1),
    ("TenBitTagRequesterEnable",        UINT16, 1),
    ("Obff",                            UINT16, 2),
    ("EndEndTlpPrefixBlocking",         UINT16, 1)
  ]

class PCI_REG_PCIE_DEVICE_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CONTROL2_Bits),
    ("Uint16",          UINT16)
    ]

PCIE_COMPLETION_TIMEOUT_50US_50MS    = 0
PCIE_COMPLETION_TIMEOUT_50US_100US   = 1
PCIE_COMPLETION_TIMEOUT_1MS_10MS     = 2
PCIE_COMPLETION_TIMEOUT_16MS_55MS    = 5
PCIE_COMPLETION_TIMEOUT_65MS_210MS   = 6
PCIE_COMPLETION_TIMEOUT_260MS_900MS  = 9
PCIE_COMPLETION_TIMEOUT_1S_3_5S      = 10
PCIE_COMPLETION_TIMEOUT_4S_13S       = 13
PCIE_COMPLETION_TIMEOUT_17S_64S      = 14

PCIE_DEVICE_CONTROL_OBFF_DISABLED   = 0
PCIE_DEVICE_CONTROL_OBFF_MESSAGE_A  = 1
PCIE_DEVICE_CONTROL_OBFF_MESSAGE_B  = 2
PCIE_DEVICE_CONTROL_OBFF_WAKE       = 3

class PCI_REG_PCIE_LINK_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                  UINT32, 1),
    ("LinkSpeedsVector",          UINT32, 7),
    ("Crosslink",                 UINT32, 1),
    ("LowerSkpOsGeneration",      UINT32, 7),
    ("LowerSkpOsReception",       UINT32, 7),
    ("RetimerPresenceDetect",     UINT32, 1),
    ("TwoRetimersPresenceDetect", UINT32, 1),
    ("Reserved2",                 UINT32, 6),
    ("DrsSupported",              UINT32, 1),
  ]

class PCI_REG_PCIE_LINK_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CAPABILITY2_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_REG_PCIE_LINK_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TargetLinkSpeed",                 UINT16, 4),
    ("EnterCompliance",                 UINT16, 1),
    ("HardwareAutonomousSpeedDisable",  UINT16, 1),
    ("SelectableDeemphasis",            UINT16, 1),
    ("TransmitMargin",                  UINT16, 3),
    ("EnterModifiedCompliance",         UINT16, 1),
    ("ComplianceSos",                   UINT16, 1),
    ("CompliancePresetDeemphasis",      UINT16, 4)
  ]

class PCI_REG_PCIE_LINK_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CONTROL2_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_LINK_STATUS2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentDeemphasisLevel",          UINT16, 1),
    ("EqualizationComplete",            UINT16, 1),
    ("EqualizationPhase1Successful",    UINT16, 1),
    ("EqualizationPhase2Successful",    UINT16, 1),
    ("EqualizationPhase3Successful",    UINT16, 1),
    ("LinkEqualizationRequest",         UINT16, 1),
    ("RetimerPresence",                 UINT16, 1),
    ("TwoRetimersPresence",             UINT16, 1),
    ("CrosslinkResolution",             UINT16, 2),
    ("FlitModeStatus",                  UINT16, 1),
    ("Reserved",                        UINT16, 1),
    ("DownstreamComponentPresence",     UINT16, 3),
    ("DRSMessageReceived",              UINT16, 1)
  ]

class PCI_REG_PCIE_LINK_STATUS2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_STATUS2_Bits),
    ("Uint16",          UINT16)
    ]

class PCI_REG_PCIE_SLOT_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InbandPdDisable",   UINT32, 1),
    ("Reserved",          UINT32, 30)
  ]

class PCI_REG_PCIE_SLOT_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_CAPABILITY2_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_CAPABILITY_PCIEXP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 EFI_PCI_CAPABILITY_HDR             ),
    ("Capability",          PCI_REG_PCIE_CAPABILITY            ),
    ("DeviceCapability",    PCI_REG_PCIE_DEVICE_CAPABILITY     ),
    ("DeviceControl",       PCI_REG_PCIE_DEVICE_CONTROL        ),
    ("DeviceStatus",        PCI_REG_PCIE_DEVICE_STATUS         ),
    ("LinkCapability",      PCI_REG_PCIE_LINK_CAPABILITY       ),
    ("LinkControl",         PCI_REG_PCIE_LINK_CONTROL          ),
    ("LinkStatus",          PCI_REG_PCIE_LINK_STATUS           ),
    ("SlotCapability",      PCI_REG_PCIE_SLOT_CAPABILITY       ),
    ("SlotControl",         PCI_REG_PCIE_SLOT_CONTROL          ),
    ("SlotStatus",          PCI_REG_PCIE_SLOT_STATUS           ),
    ("RootControl",         PCI_REG_PCIE_ROOT_CONTROL          ),
    ("RootCapability",      PCI_REG_PCIE_ROOT_CAPABILITY       ),
    ("RootStatus",          PCI_REG_PCIE_ROOT_STATUS           ),
    ("DeviceCapability2",   PCI_REG_PCIE_DEVICE_CAPABILITY2    ),
    ("DeviceControl2",      PCI_REG_PCIE_DEVICE_CONTROL2       ),
    ("DeviceStatus2",       UINT16                             ),
    ("LinkCapability2",     PCI_REG_PCIE_LINK_CAPABILITY2      ),
    ("LinkControl2",        PCI_REG_PCIE_LINK_CONTROL2         ),
    ("LinkStatus2",         PCI_REG_PCIE_LINK_STATUS2          ),
    ("SlotCapability2",     PCI_REG_PCIE_SLOT_CAPABILITY2      ),
    ("SlotControl2",        UINT16                             ),
    ("SlotStatus2",         UINT16                             )
  ]

EFI_PCIE_CAPABILITY_BASE_OFFSET                             = 0x100
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL_ARI_HIERARCHY          = 0x10 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_OFFSET            = 0x24 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_ARI_FORWARDING    = 0x20 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_OFFSET                 = 0x28 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_ARI_FORWARDING         = 0x20 

EFI_PCIE_CAPABILITY_ID_ARI        = 0x0E
EFI_PCIE_CAPABILITY_ID_ATS        = 0x0F
EFI_PCIE_CAPABILITY_ID_SRIOV      = 0x10
EFI_PCIE_CAPABILITY_ID_MRIOV      = 0x11

class SR_IOV_CAPABILITY_REGISTER (Structure):
  _fields_ = [
    ("CapabilityHeader",            UINT32),
    ("Capability",                  UINT32),
    ("Control",                     UINT16),
    ("Status",                      UINT16),
    ("InitialVFs",                  UINT16),
    ("TotalVFs",                    UINT16),
    ("NumVFs",                      UINT16),
    ("FunctionDependencyLink",      UINT8),
    ("Reserved0",                   UINT8),
    ("FirstVFOffset",               UINT16),
    ("VFStride",                    UINT16),
    ("Reserved1",                   UINT16),
    ("VFDeviceID",                  UINT16),
    ("SupportedPageSize",           UINT32),
    ("SystemPageSize",              UINT32),
    ("VFBar",                       UINT32 * 6),
    ("VFMigrationStateArrayOffset", UINT32)
    ]

EFI_PCIE_CAPABILITY_ID_SRIOV_CAPABILITIES               = 0x04
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL                    = 0x08
EFI_PCIE_CAPABILITY_ID_SRIOV_STATUS                     = 0x0A
EFI_PCIE_CAPABILITY_ID_SRIOV_INITIALVFS                 = 0x0C
EFI_PCIE_CAPABILITY_ID_SRIOV_TOTALVFS                   = 0x0E
EFI_PCIE_CAPABILITY_ID_SRIOV_NUMVFS                     = 0x10
EFI_PCIE_CAPABILITY_ID_SRIOV_FUNCTION_DEPENDENCY_LINK   = 0x12
EFI_PCIE_CAPABILITY_ID_SRIOV_FIRSTVF                    = 0x14
EFI_PCIE_CAPABILITY_ID_SRIOV_VFSTRIDE                   = 0x16
EFI_PCIE_CAPABILITY_ID_SRIOV_VFDEVICEID                 = 0x1A
EFI_PCIE_CAPABILITY_ID_SRIOV_SUPPORTED_PAGE_SIZE        = 0x1C
EFI_PCIE_CAPABILITY_ID_SRIOV_SYSTEM_PAGE_SIZE           = 0x20
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR0                       = 0x24
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR1                       = 0x28
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR2                       = 0x2C
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR3                       = 0x30
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR4                       = 0x34
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR5                       = 0x38
EFI_PCIE_CAPABILITY_ID_SRIOV_VF_MIGRATION_STATE         = 0x3C

class PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER (Structure):
  _fields_ = [
    ("CapabilityId",            UINT32, 16),
    ("CapabilityVersion",       UINT32,  4),
    ("NextCapabilityOffset",    UINT32, 12)
    ]

PCI_EXP_EXT_HDR = PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER

PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_ID   = 0x0001
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER1 = 0x1   
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER2 = 0x2   

class PCI_EXPRESS_REG_UNCORRECTABLE_ERROR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Undefined",                   UINT32, 1),
    ("Reserved",                    UINT32, 3),
    ("DataLinkProtocolError",       UINT32, 1),
    ("SurpriseDownError",           UINT32, 1),
    ("Reserved2",                   UINT32, 6),
    ("PoisonedTlp",                 UINT32, 1),
    ("FlowControlProtocolError",    UINT32, 1),
    ("CompletionTimeout",           UINT32, 1),
    ("CompleterAbort",              UINT32, 1),
    ("UnexpectedCompletion",        UINT32, 1),
    ("ReceiverOverflow",            UINT32, 1),
    ("MalformedTlp",                UINT32, 1),
    ("EcrcError",                   UINT32, 1),
    ("UnsupportedRequestError",     UINT32, 1),
    ("AcsVoilation",                UINT32, 1),
    ("UncorrectableInternalError",  UINT32, 1),
    ("McBlockedTlp",                UINT32, 1),
    ("AtomicOpEgressBlocked",       UINT32, 1),
    ("TlpPrefixBlockedError",       UINT32, 1),
    ("Reserved3",                   UINT32, 6)
  ]

class PCI_EXPRESS_REG_UNCORRECTABLE_ERROR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_UNCORRECTABLE_ERROR_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ADVANCED_ERROR_REPORTING (Structure):
  _fields_ = [
    ("Header",                                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("UncorrectableErrorStatus",              PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("UncorrectableErrorMask",                PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("UncorrectableErrorSeverity",            PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("CorrectableErrorStatus",                UINT32),
    ("CorrectableErrorMask",                  UINT32),
    ("AdvancedErrorCapabilitiesAndControl",   UINT32),
    ("HeaderLog",                             UINT32 * 4),
    ("RootErrorCommand",                      UINT32),
    ("RootErrorStatus",                       UINT32),
    ("ErrorSourceIdentification",             UINT16),
    ("CorrectableErrorSourceIdentification",  UINT16),
    ("TlpPrefixLog",                          UINT32 * 4)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_ID    = 0x0002
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_MFVC  = 0x0009
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC (Structure):
  _fields_ = [
    ("VcResourceCapability",  UINT32, 24),
    ("PortArbTableOffset",    UINT32,  8),
    ("VcResourceControl",     UINT32),
    ("Reserved1",             UINT16),
    ("VcResourceStatus",      UINT16)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ExtendedVcCount",   UINT32,  3),
    ("PortVcCapability1", UINT32, 29),
    ("PortVcCapability2", UINT32, 24),
    ("VcArbTableOffset",  UINT32,  8),
    ("PortVcControl",     UINT16),
    ("PortVcStatus",      UINT16),
    ("Capability",        PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC * 1)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_ID    = 0x0003
PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_SERIAL_NUMBER (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("SerialNumber",  UINT64)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_ID   = 0x0005
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_LINK_DECLARATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ElementSelfDescription",  UINT32),
    ("Reserved",                UINT32),
    ("LinkEntry",               UINT32 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_GET_LINK_COUNT (LINK_DECLARATION):

  return ((LINK_DECLARATION.ElementSelfDescription) & 0x0000ff00)>>8

PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_ID   = 0x0006
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_INTERNAL_LINK_CONTROL (Structure):
  _fields_ = [
    ("Header",                      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("RootComplexLinkCapabilities", UINT32),
    ("RootComplexLinkControl",      UINT16),
    ("RootComplexLinkStatus",       UINT16)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_ID   = 0x0004
PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_POWER_BUDGETING (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DataSelect",            UINT32,  8),
    ("Reserved",              UINT32, 24),
    ("Data",                  UINT32),
    ("PowerBudgetCapability", UINT32,  1),
    ("Reserved2",             UINT32,  7),
    ("Reserved3",             UINT32, 24)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_ID   = 0x000D
PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ACS_EXTENDED (Structure):
  _fields_ = [
    ("Header",                    PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AcsCapability",             UINT16),
    ("AcsControl",                UINT16),
    ("EgressControlVectorArray",  UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_CONTROL (ACS_EXTENDED):

  return ((ACS_EXTENDED.AcsCapability)&0x00000020)

def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_VECTOR_SIZE(ACS_EXTENDED):

  return ((ACS_EXTENDED.AcsCapability)&0x0000FF00)

PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_ID   = 0x0007
PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AssociationBitmap", UINT32)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_ID    = 0x0008
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_VER1  = 0x1   

PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTI_FUNCTION_VIRTUAL_CHANNEL_CAPABILITY = PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY

PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_ID   = 0x000B
PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_VENDOR_SPECIFIC (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorSpecificHeader",  UINT32),
    ("VendorSpecific",        UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_GET_SIZE(VENDOR):

  return ((VENDOR.VendorSpecificHeader)&0xFFF00000)>>20

PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_ID   = 0x000A
PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RCRB_HEADER (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorId",          UINT16),
    ("DeviceId",          UINT16),
    ("RcrbCapabilities",  UINT32),
    ("RcrbControl",       UINT32),
    ("Reserved",          UINT32)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_ID   = 0x0012
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_VER1 = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTICAST (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("MultiCastCapability", UINT16),
    ("MulticastControl",    UINT16),
    ("McBaseAddress",       UINT64),
    ("McReceiveAddress",    UINT64),
    ("McBlockAll",          UINT64),
    ("McBlockUntranslated", UINT64),
    ("McOverlayBar",        UINT64)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_ID    = 0x0015
PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT32, 4),
    ("BarSizeCapability",   UINT32, 28)
  ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BarIndex",            UINT32, 3),
    ("Reserved",            UINT32, 2),
    ("ResizableBarNumber",  UINT32, 3),
    ("BarSize",             UINT32, 6),
    ("Reserved2",           UINT32, 2),
    ("BarSizeCapability",   UINT32, 16)
  ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL_Bits),
    ("Uint32",          UINT32)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY (Structure):
  _fields_ = [
    ("ResizableBarCapability",  PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY),
    ("ResizableBarControl",     PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL)
    ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR (Structure):
  _fields_ = [
    ("Header",      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("Capability",  PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY * 1)
    ]

def GET_NUMBER_RESIZABLE_BARS(x):

  return x.Capability[0].ResizableBarControl.Bits.ResizableBarNumber

PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_ID    = 0x000E
PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_ARI_CAPABILITY (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AriCapability", UINT16),
    ("AriControl",    UINT16)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_ID    = 0x0016
PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_DYNAMIC_POWER_ALLOCATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DpaCapability",           UINT32),
    ("DpaLatencyIndicator",     UINT32),
    ("DpaStatus",               UINT16),
    ("DpaControl",              UINT16),
    ("DpaPowerAllocationArray", UINT8 * 1)
    ]

def PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_GET_SUBSTATE_MAX(POWER):

  return ((POWER.DpaCapability)&0x0000000F)

PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_ID    = 0x0018
PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_LATENCE_TOLERANCE_REPORTING (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("MaxSnoopLatency",         UINT16),
    ("MaxNoSnoopLatency",       UINT16)
    ]

PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_ID    = 0x0017
PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_VER1  = 0x1   

class PCI_EXPRESS_EXTENDED_CAPABILITIES_TPH (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("TphRequesterCapability",  UINT32),
    ("TphRequesterControl",     UINT32),
    ("TphStTable",              UINT16 * 1)
    ]

def GET_TPH_TABLE_SIZE(x):

  return ((x.TphRequesterCapability & 0x7FF0000)>>16) * sizeof(UINT16)
