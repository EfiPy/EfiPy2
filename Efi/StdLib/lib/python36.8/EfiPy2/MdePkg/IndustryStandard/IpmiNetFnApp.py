# IpmiNetFnApp.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnApp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

IPMI_NETFN_APP  = 0x06

IPMI_APP_GET_DEVICE_ID = 0x1

class IPMI_GET_DEVICE_ID_DEVICE_REV_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceRevision",          UINT8, 4),
    ("Reserved",                UINT8, 3),
    ("DeviceSdr",               UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_DEVICE_REV (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_DEVICE_REV_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_DEVICE_ID_FIRMWARE_REV_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MajorFirmwareRev",    UINT8, 7),
    ("UpdateMode",          UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_FIRMWARE_REV_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_FIRMWARE_REV_1_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_DEVICE_ID_DEVICE_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SensorDeviceSupport",     UINT8, 1),
    ("SdrRepositorySupport",    UINT8, 1),
    ("SelDeviceSupport",        UINT8, 1),
    ("FruInventorySupport",     UINT8, 1),
    ("IpmbMessageReceiver",     UINT8, 1),
    ("IpmbMessageGenerator",    UINT8, 1),
    ("BridgeSupport",           UINT8, 1),
    ("ChassisSupport",          UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_DEVICE_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_DEVICE_SUPPORT_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_DEVICE_ID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8                            ),
    ("DeviceId",            UINT8                            ),
    ("DeviceRevision",      IPMI_GET_DEVICE_ID_DEVICE_REV    ),
    ("FirmwareRev1",        IPMI_GET_DEVICE_ID_FIRMWARE_REV_1),
    ("MinorFirmwareRev",    UINT8                            ),
    ("SpecificationVersion",UINT8                            ),
    ("DeviceSupport",       IPMI_GET_DEVICE_ID_DEVICE_SUPPORT),
    ("ManufacturerId",      UINT8 * 3                        ),
    ("ProductId",           UINT16                           ),
    ("AuxFirmwareRevInfo",  UINT32                           )
    ]

IPMI_APP_COLD_RESET  = 0x2

IPMI_APP_WARM_RESET  = 0x3

IPMI_APP_GET_SELFTEST_RESULTS  = 0x4

class IPMI_SELF_TEST_RESULT_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Result",          UINT8),
    ("Param",           UINT8)
  ]

IPMI_APP_SELFTEST_NO_ERROR             = 0x55
IPMI_APP_SELFTEST_NOT_IMPLEMENTED      = 0x56
IPMI_APP_SELFTEST_ERROR                = 0x57
IPMI_APP_SELFTEST_FATAL_HW_ERROR       = 0x58
IPMI_APP_SELFTEST_INACCESSIBLE_SEL     = 0x80
IPMI_APP_SELFTEST_INACCESSIBLE_SDR     = 0x40
IPMI_APP_SELFTEST_INACCESSIBLE_FRU     = 0x20
IPMI_APP_SELFTEST_IPMB_SIGNAL_FAIL     = 0x10
IPMI_APP_SELFTEST_SDR_REPOSITORY_EMPTY = 0x08
IPMI_APP_SELFTEST_FRU_CORRUPT          = 0x04
IPMI_APP_SELFTEST_FW_BOOTBLOCK_CORRUPT = 0x02
IPMI_APP_SELFTEST_FW_CORRUPT           = 0x01

IPMI_APP_MANUFACTURING_TEST_ON = 0x5

IPMI_APP_SET_ACPI_POWERSTATE = 0x6

IPMI_SYSTEM_POWER_STATE_S0_G0  = 0x0
IPMI_SYSTEM_POWER_STATE_S1     = 0x1
IPMI_SYSTEM_POWER_STATE_S2     = 0x2
IPMI_SYSTEM_POWER_STATE_S3     = 0x3
IPMI_SYSTEM_POWER_STATE_S4     = 0x4
IPMI_SYSTEM_POWER_STATE_S5_G2  = 0x5
IPMI_SYSTEM_POWER_STATE_S4_S5  = 0x6
IPMI_SYSTEM_POWER_STATE_G3  = 0x7
IPMI_SYSTEM_POWER_STATE_SLEEPING  = 0x8
IPMI_SYSTEM_POWER_STATE_G1_SLEEPING  = 0x9
IPMI_SYSTEM_POWER_STATE_OVERRIDE    = 0xA
IPMI_SYSTEM_POWER_STATE_LEGACY_ON   = 0x20
IPMI_SYSTEM_POWER_STATE_LEGACY_OFF  = 0x21
IPMI_SYSTEM_POWER_STATE_UNKNOWN     = 0x2A
IPMI_SYSTEM_POWER_STATE_NO_CHANGE   = 0x7F

IPMI_DEVICE_POWER_STATE_D0         = 0x0
IPMI_DEVICE_POWER_STATE_D1         = 0x1
IPMI_DEVICE_POWER_STATE_D2         = 0x2
IPMI_DEVICE_POWER_STATE_D3         = 0x3
IPMI_DEVICE_POWER_STATE_UNKNOWN    = 0x2A
IPMI_DEVICE_POWER_STATE_NO_CHANGE  = 0x7F

class IPMI_ACPI_POWER_STATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerState",  UINT8, 7),
    ("StateChange", UINT8, 1)
    ]

class IPMI_ACPI_POWER_STATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_ACPI_POWER_STATE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_ACPI_POWER_STATE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemPowerState",   IPMI_ACPI_POWER_STATE),
    ("DevicePowerState",   IPMI_ACPI_POWER_STATE)
    ]

IPMI_APP_GET_ACPI_POWERSTATE  = 0x7

IPMI_APP_GET_DEVICE_GUID  = 0x8

class IPMI_GET_DEVICE_GUID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Guid",            UINT8 * 16)
  ]

IPMI_APP_RESET_WATCHDOG_TIMER  = 0x22

IPMI_APP_SET_WATCHDOG_TIMER  = 0x24

IPMI_WATCHDOG_TIMER_BIOS_FRB2  = 0x1
IPMI_WATCHDOG_TIMER_BIOS_POST  = 0x2
IPMI_WATCHDOG_TIMER_OS_LOADER  = 0x3
IPMI_WATCHDOG_TIMER_SMS        = 0x4
IPMI_WATCHDOG_TIMER_OEM        = 0x5

class IPMI_WATCHDOG_TIMER_USE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                    UINT8, 3),
    ("Reserved",                    UINT8, 3),
    ("TimerRunning",                UINT8, 1),
    ("TimerUseExpirationFlagLog",   UINT8, 1)
    ]

class IPMI_WATCHDOG_TIMER_USE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_WATCHDOG_TIMER_USE_Bits),
    ("Uint8",   UINT8)
    ]

IPMI_WATCHDOG_TIMER_ACTION_NO_ACTION    = 0x0
IPMI_WATCHDOG_TIMER_ACTION_HARD_RESET   = 0x1
IPMI_WATCHDOG_TIMER_ACTION_POWER_DONW   = 0x2
IPMI_WATCHDOG_TIMER_ACTION_POWER_CYCLE  = 0x3

IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NONE       = 0x0
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_SMI        = 0x1
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NMI        = 0x2
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_MESSAGING  = 0x3

class IPMI_WATCHDOG_TIMER_ACTIONS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimeoutAction",       UINT8, 3),
    ("Reserved1",           UINT8, 1),
    ("PreTimeoutInterrupt", UINT8, 3),
    ("Reserved2",           UINT8, 1)
    ]

class IPMI_WATCHDOG_TIMER_ACTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_WATCHDOG_TIMER_ACTIONS_Bits),
    ("Uint8",   UINT8)
    ]

IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_FRB2  = BIT1
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_POST  = BIT2
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OS_LOAD    = BIT3
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_SMS_OS     = BIT4
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OEM        = BIT5

class IPMI_SET_WATCHDOG_TIMER_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                        IPMI_WATCHDOG_TIMER_USE    ),
    ("TimerActions",                    IPMI_WATCHDOG_TIMER_ACTIONS),
    ("PretimeoutInterval",              UINT8                      ),
    ("TimerUseExpirationFlagsClear",    UINT8                      ),
    ("InitialCountdownValue",           UINT16                     )
    ]

IPMI_APP_GET_WATCHDOG_TIMER  = 0x25

class IPMI_GET_WATCHDOG_TIMER_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("TimerUse",                    IPMI_WATCHDOG_TIMER_USE),
    ("TimerActions",                IPMI_WATCHDOG_TIMER_ACTIONS),
    ("PretimeoutInterval",          UINT8),
    ("TimerUseExpirationFlagsClear",UINT8),
    ("InitialCountdownValue",       UINT16),
    ("PresentCountdownValue",       UINT16)
  ]

IPMI_APP_SET_BMC_GLOBAL_ENABLES  = 0x2E

class IPMI_BMC_GLOBAL_ENABLES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReceiveMessageQueueInterrupt",    UINT8, 1),
    ("EventMessageBufferFullInterrupt", UINT8, 1),
    ("EventMessageBuffer",              UINT8, 1),
    ("SystemEventLogging",              UINT8, 1),
    ("Reserved",                        UINT8, 1),
    ("Oem0Enable",                      UINT8, 1),
    ("Oem1Enable",                      UINT8, 1),
    ("Oem2Enable",                      UINT8, 1)
    ]

class IPMI_BMC_GLOBAL_ENABLES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BMC_GLOBAL_ENABLES_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_BMC_GLOBAL_ENABLES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetEnables",  IPMI_BMC_GLOBAL_ENABLES)
    ]

IPMI_APP_GET_BMC_GLOBAL_ENABLES  = 0x2F

class IPMI_GET_BMC_GLOBAL_ENABLES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("GetEnables",      IPMI_BMC_GLOBAL_ENABLES)
    ]

IPMI_APP_CLEAR_MESSAGE_FLAGS = 0x30

class IPMI_MESSAGE_FLAGS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReceiveMessageQueue",         UINT8, 1),
    ("EventMessageBuffer",          UINT8, 1),
    ("Reserved1",                   UINT8, 1),
    ("WatchdogPerTimeoutInterrupt", UINT8, 1),
    ("Reserved2",                   UINT8, 1),
    ("Oem0",                        UINT8, 1),
    ("Oem1",                        UINT8, 1),
    ("Oem2",                        UINT8, 1),
    ]

class IPMI_MESSAGE_FLAGS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_MESSAGE_FLAGS_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CLEAR_MESSAGE_FLAGS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ClearFlags",  IPMI_MESSAGE_FLAGS)
    ]

IPMI_APP_GET_MESSAGE_FLAGS  = 0x31

class IPMI_GET_MESSAGE_FLAGS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("GetFlags",        IPMI_MESSAGE_FLAGS)
    ]

IPMI_APP_ENABLE_MESSAGE_CHANNEL_RECEIVE  = 0x32

IPMI_APP_GET_MESSAGE  = 0x33

class IPMI_GET_MESSAGE_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",           UINT8, 4),
    ("InferredPrivilegeLevel",  UINT8, 4)
    ]

class IPMI_GET_MESSAGE_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_MESSAGE_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_MESSAGE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ChannelNumber",   IPMI_GET_MESSAGE_CHANNEL_NUMBER),
    ("MessageData",     UINT8 * 0)
    ]

IPMI_APP_SEND_MESSAGE  = 0x34

class IPMI_SEND_MESSAGE_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Authentication",  UINT8, 1),
    ("Encryption",      UINT8, 1),
    ("Tracking",        UINT8, 2)
    ]

class IPMI_SEND_MESSAGE_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SEND_MESSAGE_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SEND_MESSAGE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ChannelNumber",   IPMI_SEND_MESSAGE_CHANNEL_NUMBER),
    ("MessageData",     UINT8 * 0)
    ]

class IPMI_SEND_MESSAGE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ResponseData",    UINT8 * 0)
    ]

IPMI_APP_READ_EVENT_MSG_BUFFER  = 0x35

IPMI_APP_GET_BT_INTERFACE_CAPABILITY  = 0x36

IPMI_APP_GET_SYSTEM_GUID  = 0x37

class IPMI_GET_SYSTEM_UUID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("SystemUuid",      EFI_GUID)
    ]

IPMI_APP_GET_CHANNEL_AUTHENTICATION_CAPABILITIES  = 0x38

IPMI_APP_GET_SESSION_CHALLENGE  = 0x39

IPMI_APP_ACTIVATE_SESSION  = 0x3A

IPMI_APP_SET_SESSION_PRIVELEGE_LEVEL  = 0x3B

IPMI_APP_CLOSE_SESSION  = 0x3C

IPMI_APP_GET_SESSION_INFO  = 0x3D

IPMI_APP_GET_AUTHCODE  = 0x3F

IPMI_APP_SET_CHANNEL_ACCESS  = 0x40
IPMI_APP_GET_CHANNEL_ACCESS  = 0x41

IPMI_CHANNEL_ACCESS_MEMORY_TYPE_NON_VOLATILE              = 0x1
IPMI_CHANNEL_ACCESS_MEMORY_TYPE_PRESENT_VOLATILE_SETTING  = 0x2

IPMI_CHANNEL_ACCESS_MODES_DISABLED          = 0x0
IPMI_CHANNEL_ACCESS_MODES_PRE_BOOT_ONLY     = 0x1
IPMI_CHANNEL_ACCESS_MODES_ALWAYS_AVAILABLE  = 0x2
IPMI_CHANNEL_ACCESS_MODES_SHARED            = 0x3

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_CHANNEL_ACCESS_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 6),
    ("MemoryType",  UINT8, 2)
    ]

class IPMI_GET_CHANNEL_ACCESS_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_CHANNEL_ACCESS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER),
    ("AccessType",      IPMI_GET_CHANNEL_ACCESS_TYPE)
    ]

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AccessMode",              UINT8, 3),
    ("UserLevelAuthEnabled",    UINT8, 1),
    ("MessageAuthEnable",       UINT8, 1),
    ("Alert",                   UINT8, 1),
    ("Reserved",                UINT8, 2)
    ]

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelPriviledgeLimit",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_CHANNEL_ACCESS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8),
    ("ChannelAccess",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS),
    ("PrivilegeLimit",   IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT)
    ]

IPMI_APP_GET_CHANNEL_INFO  = 0x42

IPMI_CHANNEL_MEDIA_TYPE_IPMB  = 0x1
IPMI_CHANNEL_MEDIA_TYPE_ICMB_1_0  = 0x2
IPMI_CHANNEL_MEDIA_TYPE_ICMB_0_9  = 0x3
IPMI_CHANNEL_MEDIA_TYPE_802_3_LAN  = 0x4
IPMI_CHANNEL_MEDIA_TYPE_RS_232  = 0x5
IPMI_CHANNEL_MEDIA_TYPE_OTHER_LAN  = 0x6
IPMI_CHANNEL_MEDIA_TYPE_PCI_SM_BUS  = 0x7
IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V1  = 0x8
IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V2  = 0x9
IPMI_CHANNEL_MEDIA_TYPE_USB1  = 0xA
IPMI_CHANNEL_MEDIA_TYPE_USB2  = 0xB
IPMI_CHANNEL_MEDIA_TYPE_SYSTEM_INTERFACE  = 0xC
IPMI_CHANNEL_MEDIA_TYPE_OEM_START  = 0x60
IPMI_CHANNEL_MEDIA_TYPE_OEM_END    = 0x7F

IPMI_CHANNEL_PROTOCOL_TYPE_NA  = 0x00
IPMI_CHANNEL_PROTOCOL_TYPE_IPMB_1_0  = 0x01
IPMI_CHANNEL_PROTOCOL_TYPE_ICMB_1_0  = 0x02
IPMI_CHANNEL_PROTOCOL_TYPE_RESERVED  = 0x03
IPMI_CHANNEL_PROTOCOL_TYPE_IPMI_SMBUS  = 0x04
IPMI_CHANNEL_PROTOCOL_TYPE_KCS  = 0x05
IPMI_CHANNEL_PROTOCOL_TYPE_SMIC  = 0x06
IPMI_CHANNEL_PROTOCOL_TYPE_BT_10  = 0x07
IPMI_CHANNEL_PROTOCOL_TYPE_BT_15  = 0x08
IPMI_CHANNEL_PROTOCOL_TYPE_TMODE  = 0x09

class IPMI_CHANNEL_INFO_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_CHANNEL_INFO_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CHANNEL_INFO_MEDIUM_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelMediumType",   UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class IPMI_CHANNEL_INFO_MEDIUM_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_MEDIUM_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CHANNEL_INFO_PROTOCOL_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelProtocolType", UINT8, 5),
    ("Reserved",            UINT8, 3)
    ]

class IPMI_CHANNEL_INFO_PROTOCOL_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_PROTOCOL_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_CHANNEL_INFO_SESSION_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActiveSessionCount",  UINT8, 6),
    ("SessionSupport",      UINT8, 2)
    ]

class IPMI_CHANNEL_INFO_SESSION_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_SESSION_SUPPORT_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_CHANNEL_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8                            ),
    ("ChannelNumber",   IPMI_CHANNEL_INFO_CHANNEL_NUMBER ),
    ("MediumType",      IPMI_CHANNEL_INFO_MEDIUM_TYPE    ),
    ("ProtocolType",    IPMI_CHANNEL_INFO_PROTOCOL_TYPE  ),
    ("SessionSupport",  IPMI_CHANNEL_INFO_SESSION_SUPPORT),
    ("VendorId",        UINT8 * 3                        ),
    ("AuxChannelInfo",  UINT16                           )
    ]

class IPMI_GET_CHANNEL_INFO_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_CHANNEL_INFO_CHANNEL_NUMBER )
    ]

IPMI_APP_SET_USER_ACCESS  = 0x43

IPMI_APP_GET_USER_ACCESS  = 0x44

class IPMI_GET_USER_ACCESS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_GET_USER_ACCESS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",      UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_USER_ACCESS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_GET_USER_ACCESS_CHANNEL_NUMBER),
    ("UserId",          IPMI_USER_ID)
    ]

class IPMI_GET_USER_ACCESS_MAX_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxUserId",   UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_MAX_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_MAX_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_USER_ACCESS_CURRENT_USER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentUserId",       UINT8, 6),
    ("UserIdEnableStatus",  UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_CURRENT_USER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CURRENT_USER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_USER_ACCESS_FIXED_NAME_USER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FixedUserId", UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_FIXED_NAME_USER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_FIXED_NAME_USER_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_USER_ACCESS_CHANNEL_ACCESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserPrivilegeLimit",          UINT8, 4),
    ("EnableIpmiMessaging",         UINT8, 1),
    ("EnableUserLinkAuthetication", UINT8, 1),
    ("UserAccessAvailable",         UINT8, 1),
    ("Reserved",                    UINT8, 1)
    ]

class IPMI_GET_USER_ACCESS_CHANNEL_ACCESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CHANNEL_ACCESS_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_USER_ACCESS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCod",   UINT8                               ),
    ("MaxUserId",       IPMI_GET_USER_ACCESS_MAX_USER_ID    ),
    ("CurrentUser",     IPMI_GET_USER_ACCESS_CURRENT_USER   ),
    ("FixedNameUser",   IPMI_GET_USER_ACCESS_FIXED_NAME_USER),
    ("ChannelAccess",   IPMI_GET_USER_ACCESS_CHANNEL_ACCESS )
    ]

IPMI_APP_SET_USER_NAME  = 0x45

class IPMI_SET_USER_NAME_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",   IPMI_USER_ID),
    ("UserName", UINT8 * 16)
    ]

IPMI_APP_GET_USER_NAME  = 0x46

class IPMI_GET_USER_NAME_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",   IPMI_USER_ID)
    ]

class IPMI_GET_USER_NAME_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("UserName",        UINT8 * 16)
    ]

IPMI_APP_SET_USER_PASSWORD  = 0x47

IPMI_SET_USER_PASSWORD_OPERATION_TYPE_DISABLE_USER   = 0x0
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_ENABLE_USER    = 0x1
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_SET_PASSWORD   = 0x2
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_TEST_PASSWORD  = 0x3

IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_16  = 0x0
IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_20  = 0x1

class IPMI_SET_USER_PASSWORD_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",          UINT8, 6),
    ("Reserved",        UINT8, 1),
    ("PasswordSize",    UINT8, 1),
    ]

class IPMI_SET_USER_PASSWORD_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_USER_PASSWORD_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_USER_PASSWORD_OPERATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Operation",   UINT8, 6),
    ("Reserved",    UINT8, 1)
    ]

class IPMI_SET_USER_PASSWORD_OPERATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_USER_PASSWORD_OPERATION_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SET_USER_PASSWORD_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",          IPMI_SET_USER_PASSWORD_USER_ID),
    ("Operation",       IPMI_SET_USER_PASSWORD_OPERATION),
    ("PasswordData",    UINT8 * 0)
    ]

IPMI_APP_ACTIVATE_PAYLOAD  = 0x48

IPMI_APP_DEACTIVATE_PAYLOAD  = 0x49

IPMI_APP_GET_PAYLOAD_ACTIVATION_STATUS  = 0x4a

IPMI_APP_GET_PAYLOAD_INSTANCE_INFO  = 0x4b

IPMI_APP_SET_USER_PAYLOAD_ACCESS  = 0x4C

IPMI_APP_GET_USER_PAYLOAD_ACCESS  = 0x4D

IPMI_APP_GET_CHANNEL_PAYLOAD_SUPPORT  = 0x4E

IPMI_APP_GET_CHANNEL_PAYLOAD_VERSION  = 0x4F

IPMI_APP_GET_CHANNEL_OEM_PAYLOAD_INFO  = 0x50

IPMI_APP_MASTER_WRITE_READ  = 0x52

IPMI_APP_GET_CHANNEL_CIPHER_SUITES  = 0x54

IPMI_APP_SUSPEND_RESUME_PAYLOAD_ENCRYPTION  = 0x55

IPMI_APP_SET_CHANNEL_SECURITY_KEYS  = 0x56

IPMI_APP_GET_SYSTEM_INTERFACE_CAPABILITIES  = 0x57

IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SSIF  = 0x0
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_KCS   = 0x1
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SMIC  = 0x2

class IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterfaceType",   UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",             UINT8, 3),
    ("PecSupport",          UINT8, 1),
    ("Reserved",            UINT8, 2),
    ("TransactionSupport",  UINT8, 2)
    ]

class IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemInterfaceVersion",  UINT8, 3),
    ("Reserved",                UINT8, 5)
    ]

class IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_Bits),
    ("Uint8",   UINT8)
    ]

class IPMI_GET_SYSTEM_INTERFACE_SSIF_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCod",   UINT8                                  ),
    ("Reserved",        UINT8                                  ),
    ("InterfaceCap",    IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES),
    ("InputMsgSize",    UINT8                                  ),
    ("OutputMsgSize",   UINT8                                  )
    ]

class IPMI_GET_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8                                      ),
    ("Reserved",        UINT8                                      ),
    ("InterfaceCap",    IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES),
    ("InputMaxMsgSize", UINT8                                      )
    ]

class IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("InterfaceSsifCapability",     POINTER(IPMI_GET_SYSTEM_INTERFACE_SSIF_CAPABILITIES_RESPONSE)),
    ("InterfaceKcsSmicCapability",  POINTER(IPMI_GET_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_RESPONSE))
    ]

IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_SINGLE_PARTITION_RW             = 0x0
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW              = 0x1
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW_WITH_MIDDLE  = 0x2
