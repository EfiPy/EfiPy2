# IpmiNetFnChassis.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnChassis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

IPMI_NETFN_CHASSIS  = 0x00

IPMI_CHASSIS_GET_CAPABILITIES  = 0x00

class IPMI_GET_CHASSIS_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",                      UINT8),
    ("CapabilitiesFlags",                   UINT8),
    ("ChassisFruInfoDeviceAddress",         UINT8),
    ("ChassisSDRDeviceAddress",             UINT8),
    ("ChassisSELDeviceAddress",             UINT8),
    ("ChassisSystemManagementDeviceAddress",UINT8),
    ("ChassisBridgeDeviceAddress",          UINT8)
    ]

IPMI_CHASSIS_GET_STATUS  = 0x01

class IPMI_GET_CHASSIS_STATUS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",                  UINT8),
    ("CurrentPowerState",               UINT8),
    ("LastPowerEvent",                  UINT8),
    ("MiscChassisState",                UINT8),
    ("FrontPanelButtonCapabilities",    UINT8)
    ]

IPMI_CHASSIS_CONTROL  = 0x02

class IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChassisControl",  UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CHASSIS_CONTROL_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChassisControl",  IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL)
    ]

IPMI_CHASSIS_RESET  = 0x03

IPMI_CHASSIS_IDENTIFY  = 0x04

IPMI_CHASSIS_SET_CAPABILITIES  = 0x05

IPMI_CHASSIS_SET_POWER_RESTORE_POLICY  = 0x06

class IPMI_POWER_RESTORE_POLICY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerRestorePolicy",  UINT8, 3),
    ("Reserved",            UINT8, 5)
    ]

class IPMI_POWER_RESTORE_POLICY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_POWER_RESTORE_POLICY_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_POWER_RESTORE_POLICY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerRestorePolicy",  IPMI_POWER_RESTORE_POLICY)
    ]

class IPMI_SET_POWER_RESTORE_POLICY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("PowerRestorePolicySupport",   UINT8)
    ]

IPMI_CHASSIS_GET_SYSTEM_RESTART_CAUSE  = 0x07

IPMI_SYSTEM_RESTART_CAUSE_UNKNOWN                    = 0x0
IPMI_SYSTEM_RESTART_CAUSE_CHASSIS_CONTROL_COMMAND    = 0x1
IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_RESET           = 0x2
IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_POWERUP         = 0x3
IPMI_SYSTEM_RESTART_CAUSE_WATCHDOG_EXPIRE            = 0x4
IPMI_SYSTEM_RESTART_CAUSE_OEM                        = 0x5
IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_ALWAYS_RESTORE  = 0x6
IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_RESTORE_PREV    = 0x7
IPMI_SYSTEM_RESTART_CAUSE_PEF_RESET                  = 0x8
IPMI_SYSTEM_RESTART_CAUSE_PEF_POWERCYCLE             = 0x9
IPMI_SYSTEM_RESTART_CAUSE_SOFT_RESET                 = 0xA
IPMI_SYSTEM_RESTART_CAUSE_RTC_POWERUP                = 0xB

class IPMI_SYSTEM_RESTART_CAUSE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cause",       UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_SYSTEM_RESTART_CAUSE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_RESTART_CAUSE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_SYSTEM_RESTART_CAUSE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("RestartCause",    IPMI_SYSTEM_RESTART_CAUSE),
    ("ChannelNumber",   UINT8)
    ]

IPMI_CHASSIS_SET_SYSTEM_BOOT_OPTIONS  = 0x08

class IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("MarkParameterInvalid",UINT8, 1),
    ]

class IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterValid",  IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID),
    ("ParameterData",   UINT8 * 0)
    ]

class IPMI_SET_BOOT_OPTIONS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8, 8)
    ]

IPMI_CHASSIS_GET_SYSTEM_BOOT_OPTIONS  = 0x09

class IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR),
    ("SetSelector",         UINT8),
    ("BlockSelector",       UINT8)
    ]

class IPMI_GET_THE_SYSTEM_BOOT_OPTIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Parameter",   UINT8),
    ("Valid",       UINT8),
    ("Data1",       UINT8),
    ("Data2",       UINT8),
    ("Data3",       UINT8),
    ("Data4",       UINT8),
    ("Data5",       UINT8)
    ]

class IPMI_BOOT_INITIATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterVersion",    UINT8 ),
    ("ParameterValid",      UINT8 ),
    ("ChannelNumber",       UINT8 ),
    ("SessionId",           UINT32),
    ("TimeStamp",           UINT32),
    ("Reserved",            UINT8 * 3)
    ]

IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SET_IN_PROGRESS             = 0x0
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SELECTOR  = 0x1
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SCAN      = 0x2
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_BMC_BOOT_FLAG               = 0x3
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INFO_ACK                        = 0x4
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_FLAGS                           = 0x5
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_INFO                  = 0x6
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_MAILBOX               = 0x7
IPMI_BOOT_OPTIONS_PARAMETER_OEM_BEGIN                            = 0x60
IPMI_BOOT_OPTIONS_PARAMETER_OEM_END                              = 0x7F

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetInProgress",   UINT8, 2),
    ("Reserved",        UINT8, 6),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionSelector",    UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionDiscovered",  UINT8, 1),
    ("ServicePartitionScanRequest", UINT8, 1),
    ("Reserved",                    UINT8, 6)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BmcBootFlagValid",    UINT8, 5),
    ("Reserved",            UINT8, 3)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WriteMask",                       UINT8),
    ("BootInitiatorAcknowledgeData",    UINT8)
    ]

IPMI_BOOT_DEVICE_SELECTOR_NO_OVERRIDE           = 0x0
IPMI_BOOT_DEVICE_SELECTOR_PXE                   = 0x1
IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE             = 0x2
IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE_SAFE_MODE   = 0x3
IPMI_BOOT_DEVICE_SELECTOR_DIAGNOSTIC_PARTITION  = 0x4
IPMI_BOOT_DEVICE_SELECTOR_CD_DVD                = 0x5
IPMI_BOOT_DEVICE_SELECTOR_BIOS_SETUP            = 0x6
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_FLOPPY         = 0x7
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_CD_DVD         = 0x8
IPMI_BOOT_DEVICE_SELECTOR_PRIMARY_REMOTE_MEDIA  = 0x9
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_HARDDRIVE      = 0xB
IPMI_BOOT_DEVICE_SELECTOR_FLOPPY                = 0xF

BOOT_OPTION_HANDLED_BY_BIOS  = 0x01

BIOS_MUX_CONTROL_OVERRIDE_RECOMMEND_SETTING  = 0x00
BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_BMC       = 0x01
BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_SYSTEM    = 0x02

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("BiosBootType",        UINT8, 1),
    ("PersistentOptions",   UINT8, 1),
    ("BootFlagValid",       UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LockReset",           UINT8, 1),
    ("ScreenBlank",         UINT8, 1),
    ("BootDeviceSelector",  UINT8, 4),
    ("LockKeyboard",        UINT8, 1),
    ("CmosClear",           UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ConsoleRedirection",      UINT8, 2),
    ("LockSleep",               UINT8, 1),
    ("UserPasswordBypass",      UINT8, 1),
    ("ForceProgressEventTrap",  UINT8, 1),
    ("BiosVerbosity",           UINT8, 2),
    ("LockPower",               UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BiosMuxControlOverride",  UINT8, 3),
    ("BiosSharedModeOverride",  UINT8, 1),
    ("Reserved",                UINT8, 4),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceInstanceSelector",  UINT8, 5),
    ("Reserved",                UINT8, 3),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data1", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1),
    ("Data2", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2),
    ("Data3", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3),
    ("Data4", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4),
    ("Data5", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5)
    ]

class IPMI_BOOT_OPTIONS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Reserved",        UINT8, 4),
    ]

class IPMI_BOOT_OPTIONS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_BOOT_OPTIONS_CHANNEL_NUMBER),
    ("SessionId",           UINT8 * 4),
    ("BootInfoTimeStamp",   UINT8 * 4)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector", UINT8),
    ("BlockData",   UINT8 * 16)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Parm0", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0),
    ("Parm1", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1),
    ("Parm2", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2),
    ("Parm3", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3),
    ("Parm4", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4),
    ("Parm5", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5),
    ("Parm6", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6),
    ("Parm7", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterVersion",    UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("ParameterValid",      UINT8, 1)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_BOOT_OPTIONS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8                                  ),
    ("ParameterVersion", IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION),
    ("ParameterValid",   IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID  ),
    ("ParameterData",    UINT8 * 0                              )
    ]

IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES  = 0x0A

class IPMI_FRONT_PANEL_BUTTON_ENABLES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DisablePoweroffButton",               UINT8, 1),
    ("DisableResetButton",                  UINT8, 1),
    ("DisableDiagnosticInterruptButton",    UINT8, 1),
    ("DisableStandbyButton",                UINT8, 1),
    ("Reserved",                            UINT8, 4)
    ]

class IPMI_FRONT_PANEL_BUTTON_ENABLES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_FRONT_PANEL_BUTTON_ENABLES_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontPanelButtonEnables", IPMI_FRONT_PANEL_BUTTON_ENABLES)
    ]

IPMI_CHASSIS_SET_POWER_CYCLE_INTERVALS  = 0x0B

IPMI_CHASSIS_GET_POH_COUNTER  = 0x0F
