# LocalApic.py
#
# EfiPy2.MdePkg.Register.Intel.LocalApic
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

XAPIC_ID_OFFSET                          = 0x20
XAPIC_VERSION_OFFSET                     = 0x30
XAPIC_EOI_OFFSET                         = 0x0b0
XAPIC_ICR_DFR_OFFSET                     = 0x0e0
XAPIC_SPURIOUS_VECTOR_OFFSET             = 0x0f0
XAPIC_ICR_LOW_OFFSET                     = 0x300
XAPIC_ICR_HIGH_OFFSET                    = 0x310
XAPIC_LVT_TIMER_OFFSET                   = 0x320
XAPIC_LVT_LINT0_OFFSET                   = 0x350
XAPIC_LVT_LINT1_OFFSET                   = 0x360
XAPIC_TIMER_INIT_COUNT_OFFSET            = 0x380
XAPIC_TIMER_CURRENT_COUNT_OFFSET         = 0x390
XAPIC_TIMER_DIVIDE_CONFIGURATION_OFFSET  = 0x3E0

X2APIC_MSR_BASE_ADDRESS  = 0x800
X2APIC_MSR_ICR_ADDRESS   = 0x830

LOCAL_APIC_DELIVERY_MODE_FIXED            = 0
LOCAL_APIC_DELIVERY_MODE_LOWEST_PRIORITY  = 1
LOCAL_APIC_DELIVERY_MODE_SMI              = 2
LOCAL_APIC_DELIVERY_MODE_NMI              = 4
LOCAL_APIC_DELIVERY_MODE_INIT             = 5
LOCAL_APIC_DELIVERY_MODE_STARTUP          = 6
LOCAL_APIC_DELIVERY_MODE_EXTINT           = 7

LOCAL_APIC_DESTINATION_SHORTHAND_NO_SHORTHAND        = 0
LOCAL_APIC_DESTINATION_SHORTHAND_SELF                = 1
LOCAL_APIC_DESTINATION_SHORTHAND_ALL_INCLUDING_SELF  = 2
LOCAL_APIC_DESTINATION_SHORTHAND_ALL_EXCLUDING_SELF  = 3

class LOCAL_APIC_VERSION_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",                 UINT32, 8),
    ("Reserved0",               UINT32, 8),
    ("MaxLvtEntry",             UINT32, 8),
    ("EoiBroadcastSuppression", UINT32, 1),
    ("Reserved1",               UINT32, 7)
  ]

class LOCAL_APIC_VERSION (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_VERSION_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_ICR_LOW_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",                  UINT32, 8),
    ("DeliveryMode",            UINT32, 3),
    ("DestinationMode",         UINT32, 1),
    ("DeliveryStatus",          UINT32, 1),
    ("Reserved0",               UINT32, 1),
    ("Level",                   UINT32, 1),
    ("TriggerMode",             UINT32, 1),
    ("Reserved1",               UINT32, 2),
    ("DestinationShorthand",    UINT32, 2),
    ("Reserved2",               UINT32, 12)
  ]

class LOCAL_APIC_ICR_LOW (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_ICR_LOW_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_ICR_HIGH_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved0",       UINT32, 24),
    ("Destination",     UINT32, 8)
  ]

class LOCAL_APIC_ICR_HIGH (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_ICR_HIGH_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_SVR_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SpuriousVector",          UINT32, 8),
    ("SoftwareEnable",          UINT32, 1),
    ("FocusProcessorChecking",  UINT32, 1),
    ("Reserved0",               UINT32, 2),
    ("EoiBroadcastSuppression", UINT32, 1),
    ("Reserved1",               UINT32, 19)
  ]

class LOCAL_APIC_SVR (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_SVR_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_DCR_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DivideValue1",    UINT32, 2),
    ("Reserved0",       UINT32, 1),
    ("DivideValue2",    UINT32, 1),
    ("Reserved1",       UINT32, 28)
  ]

class LOCAL_APIC_DCR (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_DCR_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_LVT_TIMER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",          UINT32, 8),
    ("Reserved0",       UINT32, 4),
    ("DeliveryStatus",  UINT32, 1),
    ("Reserved1",       UINT32, 3),
    ("Mask",            UINT32, 1),
    ("TimerMode",       UINT32, 1),
    ("Reserved2",       UINT32, 14)
  ]

class LOCAL_APIC_LVT_TIMER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_LVT_TIMER_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_LVT_LINT_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",              UINT32, 8),
    ("DeliveryMode",        UINT32, 3),
    ("Reserved0",           UINT32, 1),
    ("DeliveryStatus",      UINT32, 1),
    ("InputPinPolarity",    UINT32, 1),
    ("RemoteIrr",           UINT32, 1),
    ("TriggerMode",         UINT32, 1),
    ("Mask",                UINT32, 1),
    ("Reserved1",           UINT32, 15)
  ]

class LOCAL_APIC_LVT_LINT (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_LVT_LINT_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_MSI_ADDRESS_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved0",       UINT32, 2),
    ("DestinationMode", UINT32, 1),
    ("RedirectionHint", UINT32, 1),
    ("Reserved1",       UINT32, 8),
    ("DestinationId",   UINT32, 8),
    ("BaseAddress",     UINT32, 12)
  ]

class LOCAL_APIC_MSI_ADDRESS (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_MSI_ADDRESS_Bits),
    ("Uint32",  UINT32)
  ]

class LOCAL_APIC_MSI_DATA_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",          UINT32, 8),
    ("DeliveryMode",    UINT32, 3),
    ("Reserved0",       UINT32, 3),
    ("Level",           UINT32, 1),
    ("TriggerMode",     UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class LOCAL_APIC_MSI_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_MSI_DATA_Bits),
    ("Uint64",  UINT64)
  ]

