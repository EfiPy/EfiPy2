import EfiPy2 as EfiPy
from EfiPy2.MdePkg.Protocol.Tcg2Protocol import gEfiTcg2ProtocolGuid,               \
                                                EFI_TCG2_PROTOCOL,                  \
                                                EFI_TCG2_EVENT_LOG_FORMAT_TCG_2,    \
                                                EFI_TCG2_FINAL_EVENTS_TABLE,        \
                                                gEfiTcg2FinalEventsTableGuid,       \
                                                MAX_PCR_INDEX

from EfiPy2.MdePkg.IndustryStandard      import EFIPY_INDUSTRY_STRUCTURE, UefiTcgPlatform, Tpm20
from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL

def EfiGetSystemConfigurationTable (TargetGuid):

    TargetTable = None

    for Index in range (EfiPy.gST.NumberOfTableEntries):
        if TargetGuid == EfiPy.gST.ConfigurationTable[Index].VendorGuid:
            TargetTable = EfiPy.gST.ConfigurationTable[Index].VendorTable
            break;

    return TargetTable

def Parse_TodoList (EventType, EventBuffer, EventAddress, EventSize):
  print (f'    EventData - Type: Unknown Event Type')

def Parse_EV_NO_ACTION (EventType, EventBuffer, EventAddress, EventSize):

  print(f"    EventData - Type: EV_NO_ACTION");

  if EventSize >= EfiPy.sizeof (UefiTcgPlatform.TCG_Sp800_155_PlatformId_Event2) and \
     UefiTcgPlatform.TCG_Sp800_155_PlatformId_Event2_SIGNATURE in EventBuffer:

    print(f"  EV_NO_ACTION (TCG_Sp800_155_PlatformId_Event2_SIGNATURE todo)");

  elif EventSize >= EfiPy.sizeof (UefiTcgPlatform.TCG_EfiStartupLocalityEvent) and \
       UefiTcgPlatform.TCG_EfiStartupLocalityEvent_SIGNATURE in EventBuffer:

    print(f"  EV_NO_ACTION (TCG_EfiStartupLocalityEvent_SIGNATURE todo)");

  else:
    print(f"  Unknown EV_NO_ACTION");

def Parse_EV_S_CRTM_VERSION (EventType, EventBuffer, EventAddress, EventSize):

  print(f"    EventData - Type: EV_S_CRTM_VERSION");
  print(f"      CRTM VERSION - {bytes (EventBuffer)}");

def Parse_EV_EFI_PLATFORM_FIRMWARE_BLOB2 (EventType, EventBuffer, EventAddress, EventSize):

  UefiPlatformFirmwareBlob2 = UefiTcgPlatform.UEFI_PLATFORM_FIRMWARE_BLOB2.from_address (EventAddress)
  class UEFI_PLATFORM_FIRMWARE_BLOB2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("BlobDescriptionSize", EfiPy.UINT8),
      ("BlobDescription",     EfiPy.UINT8 * UefiPlatformFirmwareBlob2.BlobDescriptionSize),
      ("BlobBase",            EfiPy.EFI_PHYSICAL_ADDRESS),
      ("BlobLength",          EfiPy.UINT64)
    ]
  UefiPlatformFirmwareBlob2 = UEFI_PLATFORM_FIRMWARE_BLOB2.from_address (EventAddress)

  print(f'''    EventData - Type: EV_EFI_PLATFORM_FIRMWARE_BLOB2
      BlobDescriptionSize - 0x{UefiPlatformFirmwareBlob2.BlobDescriptionSize:02X}
      BlobDescription     - {bytes (UefiPlatformFirmwareBlob2.BlobDescription)}
      BlobBase   - 0x{UefiPlatformFirmwareBlob2.BlobBase:016X}
      BlobLength - 0x{UefiPlatformFirmwareBlob2.BlobLength:016X}''')

def Parse_EV_EFI_VARIABLE (EventType, EventBuffer, EventAddress, EventSize):

    UefiVariableData = UefiTcgPlatform.UEFI_VARIABLE_DATA.from_address (EventAddress)

    class UEFI_VARIABLE_DATA (EFIPY_INDUSTRY_STRUCTURE):
      _fields_ = [
        ("VariableName",        EfiPy.EFI_GUID),
        ("UnicodeNameLength",   EfiPy.UINT64),
        ("VariableDataLength",  EfiPy.UINT64),
        ("UnicodeName",         EfiPy.CHAR16 * UefiVariableData.UnicodeNameLength),
        ("VariableData",        EfiPy.INT8 * UefiVariableData.VariableDataLength)
      ]

    UefiVariableData = UEFI_VARIABLE_DATA.from_address (EventAddress)
    print(f'''      VariableName       - {UefiVariableData.VariableName}
      UnicodeNameLength  - 0x{UefiVariableData.UnicodeNameLength:016X}
      VariableDataLength - 0x{UefiVariableData.VariableDataLength:016X}
      UnicodeName        - {UefiVariableData.UnicodeName}
      VariableData       - {bytes (UefiVariableData.VariableData)}''')

def Parse_EV_EFI_VARIABLE_BOOT (EventType, EventBuffer, EventAddress, EventSize):

  print(f"    EventData - Type: EV_EFI_VARIABLE_BOOT")
  Parse_EV_EFI_VARIABLE (EventType, EventBuffer, EventAddress, EventSize)

def Parse_EV_EFI_VARIABLE_DRIVER_CONFIG (EventType, EventBuffer, EventAddress, EventSize):

  print(f"    EventData - Type: EV_EFI_VARIABLE_DRIVER_CONFIG")
  Parse_EV_EFI_VARIABLE (EventType, EventBuffer, EventAddress, EventSize)

def Parse_EV_SEPARATOR (EventType, EventBuffer, EventAddress, EventSize):

  print(f'''    EventData - Type: EV_SEPARATOR
      SEPARATOR - 0x{EfiPy.UINT32.from_address(EventAddress).value:08X}''')

def Parse_EV_EFI_HANDOFF_TABLES2 (EventType, EventBuffer, EventAddress, EventSize):

  from EfiPy2.MdePkg.Uefi.UefiSpec             import EFI_CONFIGURATION_TABLE

  class UEFI_HANDOFF_TABLE_POINTERS2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("TableDescriptionSize",    EfiPy.UINT8)
    ]

  UefiHandoffTablePointers2 = UEFI_HANDOFF_TABLE_POINTERS2.from_address (EventAddress)
  class UEFI_HANDOFF_TABLE_POINTERS2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("TableDescriptionSize",    EfiPy.UINT8),
      ("TableDescription",        EfiPy.UINT8 * UefiHandoffTablePointers2.TableDescriptionSize),
      ("NumberOfTables",          EfiPy.UINT64)
    ]
  UefiHandoffTablePointers2 = UEFI_HANDOFF_TABLE_POINTERS2.from_address (EventAddress)
  class UEFI_HANDOFF_TABLE_POINTERS2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("TableDescriptionSize",    EfiPy.UINT8),
      ("TableDescription",        EfiPy.UINT8 * UefiHandoffTablePointers2.TableDescriptionSize),
      ("NumberOfTables",          EfiPy.UINT64),
      ("TableEntry",              EFI_CONFIGURATION_TABLE * UefiHandoffTablePointers2.NumberOfTables)
    ]
  UefiHandoffTablePointers2 = UEFI_HANDOFF_TABLE_POINTERS2.from_address (EventAddress)

  print(f'''    EventData - Type: EV_EFI_HANDOFF_TABLES2
      TableDescriptionSize - 0x{UefiHandoffTablePointers2.TableDescriptionSize:02X}
      TableDescription     - {bytes (UefiHandoffTablePointers2.TableDescription)}

      NumberOfTables - 0x{UefiHandoffTablePointers2.NumberOfTables:016X}''')

  for Index in range (UefiHandoffTablePointers2.NumberOfTables):
    print (f'''      TableEntry ({Index}):
        VendorGuid  - {UefiHandoffTablePointers2.TableEntry[Index].VendorGuid}
        VendorTable - 0x{UefiHandoffTablePointers2.TableEntry[Index].VendorTable:016X}''')

def Parse_EV_EFI_ACTION (EventType, EventBuffer, EventAddress, EventSize):

  print(f'''    EventData - Type: EV_EFI_ACTION
      Action String - {bytes ((EfiPy.UINT8 * EventSize).from_address (EventAddress))}''')
def Parse_EV_EFI_SERVICES (EventType, EventBuffer, EventAddress, EventSize):

  class EFI_IMAGE_LOAD_EVENT (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("ImageLocationInMemory", EfiPy.EFI_PHYSICAL_ADDRESS),
      ("ImageLengthInMemory",   EfiPy.UINTN),
      ("ImageLinkTimeAddress",  EfiPy.UINTN),
      ("LengthOfDevicePath",    EfiPy.UINTN)
    ]
  EfiImageLoadEvent = UefiTcgPlatform.EFI_IMAGE_LOAD_EVENT.from_address (EventAddress)
  class EFI_IMAGE_LOAD_EVENT (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("ImageLocationInMemory", EfiPy.EFI_PHYSICAL_ADDRESS),
      ("ImageLengthInMemory",   EfiPy.UINTN),
      ("ImageLinkTimeAddress",  EfiPy.UINTN),
      ("LengthOfDevicePath",    EfiPy.UINTN),
      ("DevicePath",            EFI_DEVICE_PATH_PROTOCOL)
    ]
  EfiImageLoadEvent = EFI_IMAGE_LOAD_EVENT.from_address (EventAddress)

  DevicePath = EfiImageLoadEvent.DevicePath

  print(f'''
      ImageLocationInMemory - 0x{EfiImageLoadEvent.ImageLocationInMemory:016X}
      ImageLengthInMemory   - 0x{EfiImageLoadEvent.ImageLengthInMemory:016X}
      ImageLinkTimeAddress  - 0x{EfiImageLoadEvent.ImageLinkTimeAddress:016X}
      LengthOfDevicePath    - 0x{EfiImageLoadEvent.LengthOfDevicePath:016X}
      DevicePath:
        {EfiImageLoadEvent.DevicePath}''')

def Parse_EV_EFI_BOOT_SERVICES_APPLICATION (EventType, EventBuffer, EventAddress, EventSize):
  print(f'''    EventData - Type: EV_EFI_BOOT_SERVICES_APPLICATION''')
  Parse_EV_EFI_SERVICES (EventType, EventBuffer, EventAddress, EventSize)

def Parse_EV_EFI_BOOT_SERVICES_DRIVER (EventType, EventBuffer, EventAddress, EventSize):
  print(f'''    EventData - Type: EV_EFI_BOOT_SERVICES_DRIVER''')
  Parse_EV_EFI_SERVICES (EventType, EventBuffer, EventAddress, EventSize)

def Parse_EV_EFI_RUNTIME_SERVICES_DRIVER (EventType, EventBuffer, EventAddress, EventSize):
  print(f'''    EventData - Type: EV_EFI_RUNTIME_SERVICES_DRIVER''')
  Parse_EV_EFI_SERVICES (EventType, EventBuffer, EventAddress, EventSize)

ParseEventDict = {
  UefiTcgPlatform.EV_NO_ACTION:                     Parse_EV_NO_ACTION,
  UefiTcgPlatform.EV_S_CRTM_VERSION:                Parse_EV_S_CRTM_VERSION,
  UefiTcgPlatform.EV_EFI_PLATFORM_FIRMWARE_BLOB2:   Parse_EV_EFI_PLATFORM_FIRMWARE_BLOB2,
  UefiTcgPlatform.EV_EFI_VARIABLE_DRIVER_CONFIG:    Parse_EV_EFI_VARIABLE_DRIVER_CONFIG,
  UefiTcgPlatform.EV_EFI_VARIABLE_BOOT:             Parse_EV_EFI_VARIABLE_BOOT,
  UefiTcgPlatform.EV_SEPARATOR:                     Parse_EV_SEPARATOR,
  UefiTcgPlatform.EV_EFI_HANDOFF_TABLES2:           Parse_EV_EFI_HANDOFF_TABLES2,
  UefiTcgPlatform.EV_EFI_ACTION:                    Parse_EV_EFI_ACTION,
  UefiTcgPlatform.EV_EFI_BOOT_SERVICES_APPLICATION: Parse_EV_EFI_BOOT_SERVICES_APPLICATION,
  UefiTcgPlatform.EV_EFI_BOOT_SERVICES_DRIVER:      Parse_EV_EFI_BOOT_SERVICES_DRIVER,
  UefiTcgPlatform.EV_EFI_RUNTIME_SERVICES_DRIVER:   Parse_EV_EFI_RUNTIME_SERVICES_DRIVER,
}

def ParseEventData (EventType, EventBuffer, EventAddress, EventSize):
  # print (f'      {bytes (EventBuffer)}')

  ParseEventFunc = ParseEventDict.get (EventType, Parse_TodoList)
  ParseEventFunc (EventType, EventBuffer, EventAddress, EventSize)

def DumpEvent (EventLogLocation, PCRIndex):

  EventHdr = UefiTcgPlatform.TCG_PCR_EVENT_HDR.from_address (EventLogLocation.value)
  if PCRIndex != None and EventHdr.PCRIndex != PCRIndex:
    return

  print (f'''  Event:
    PCRIndex  - {EventHdr.PCRIndex}
    EventType - 0x{EventHdr.EventType:08X}
    Digest    - {bytes (EventHdr.Digest.digest)}
    EventSize - 0x{EventHdr.EventSize:08X}''');
  EventAddress = EventLogLocation.value + EfiPy.sizeof (UefiTcgPlatform.TCG_PCR_EVENT_HDR)
  EventBuffer  = (EfiPy.UINT8 * EventHdr.EventSize).from_address (EventAddress)
  ParseEventData (EventHdr.EventType, EventBuffer, EventAddress, EventHdr.EventSize)

def DumpTcgEfiSpecIdEventStruct (TcgEfiSpecIdEventAddress):

  TcgEfiSpecIdEventStruct = UefiTcgPlatform.TCG_EfiSpecIDEventStruct.from_address (TcgEfiSpecIdEventAddress)
  print (f'''  TCG_EfiSpecIDEventStruct:
    signature          - {bytes (TcgEfiSpecIdEventStruct.signature)}

    platformClass      - 0x{TcgEfiSpecIdEventStruct.platformClass:08X}
    specVersion        - {TcgEfiSpecIdEventStruct.specVersionMajor}.{TcgEfiSpecIdEventStruct.specVersionMinor}.{TcgEfiSpecIdEventStruct.specErrata}
    uintnSize          - 0x{TcgEfiSpecIdEventStruct.uintnSize:02X}''');

  class TCG_EfiSpecIDEventStruct (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("signature",           EfiPy.UINT8 * 16),
      ("platformClass",       EfiPy.UINT32),
      ("specVersionMinor",    EfiPy.UINT8),
      ("specVersionMajor",    EfiPy.UINT8),
      ("specErrata",          EfiPy.UINT8),
      ("uintnSize",           EfiPy.UINT8),
      ("numberOfAlgorithms",  EfiPy.UINT32)
      # ("digestSize",          TCG_EfiSpecIdEventAlgorithmSize * numberOfAlgorithms),
      # ("vendorInfoSize",      UINT8),
      # ("vendorInfo",          UINT8 * vendorInfoSize)
    ]
  TcgEfiSpecIdEventStruct = TCG_EfiSpecIDEventStruct.from_address (TcgEfiSpecIdEventAddress)
  class TCG_EfiSpecIDEventStruct (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("signature",           EfiPy.UINT8 * 16),
      ("platformClass",       EfiPy.UINT32),
      ("specVersionMinor",    EfiPy.UINT8),
      ("specVersionMajor",    EfiPy.UINT8),
      ("specErrata",          EfiPy.UINT8),
      ("uintnSize",           EfiPy.UINT8),
      ("numberOfAlgorithms",  EfiPy.UINT32),
      ("digestSize",          UefiTcgPlatform.TCG_EfiSpecIdEventAlgorithmSize * TcgEfiSpecIdEventStruct.numberOfAlgorithms),
      ("vendorInfoSize",      EfiPy.UINT8)
    ]
  TcgEfiSpecIdEventStruct = TCG_EfiSpecIDEventStruct.from_address (TcgEfiSpecIdEventAddress)
  class TCG_EfiSpecIDEventStruct (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("signature",           EfiPy.UINT8 * 16),
      ("platformClass",       EfiPy.UINT32),
      ("specVersionMinor",    EfiPy.UINT8),
      ("specVersionMajor",    EfiPy.UINT8),
      ("specErrata",          EfiPy.UINT8),
      ("uintnSize",           EfiPy.UINT8),
      ("numberOfAlgorithms",  EfiPy.UINT32),
      # ("digestSize",          UefiTcgPlatform.TCG_EfiSpecIdEventAlgorithmSize * TcgEfiSpecIdEventStruct2.numberOfAlgorithms),
      ("digestSize",          UefiTcgPlatform.TCG_EfiSpecIdEventAlgorithmSize * TcgEfiSpecIdEventStruct.numberOfAlgorithms),
      ("vendorInfoSize",      EfiPy.UINT8),
      # ("vendorInfo",          EfiPy.UINT8 * TcgEfiSpecIdEventStruct3.vendorInfoSize)
      ("vendorInfo",          EfiPy.UINT8 * TcgEfiSpecIdEventStruct.vendorInfoSize)
    ]
  TcgEfiSpecIdEventStruct = TCG_EfiSpecIDEventStruct.from_address (TcgEfiSpecIdEventAddress)

  print (f"    numberOfAlgorithms - 0x{TcgEfiSpecIdEventStruct.numberOfAlgorithms:08X}");
  for Index in range (TcgEfiSpecIdEventStruct.numberOfAlgorithms):
    print (f'''    digest({Index})
      algorithmId      - 0x{TcgEfiSpecIdEventStruct.digestSize[Index].algorithmId:04X}
      digestSize       - 0x{TcgEfiSpecIdEventStruct.digestSize[Index].digestSize:04X}''')
  print (f"    vendorInfoSize     - 0x{TcgEfiSpecIdEventStruct.vendorInfoSize:02X}");
  print (f"    vendorInfo         - {bytes (TcgEfiSpecIdEventStruct.vendorInfo)}");
  print (f"    TCG_EfiSpecIDEventStruct size - 0x{EfiPy.sizeof (TCG_EfiSpecIDEventStruct):08X}");

  return TcgEfiSpecIdEventAddress + EfiPy.sizeof (TCG_EfiSpecIDEventStruct)

mHashInfo = {
  Tpm20.TPM_ALG_SHA1:    (Tpm20.SHA1_DIGEST_SIZE,    "HASH_ALG_SHA1"   ),
  Tpm20.TPM_ALG_SHA256:  (Tpm20.SHA256_DIGEST_SIZE,  "HASH_ALG_SHA256" ),
  Tpm20.TPM_ALG_SM3_256: (Tpm20.SM3_256_DIGEST_SIZE, "HASH_ALG_SM3_256"),
  Tpm20.TPM_ALG_SHA384:  (Tpm20.SHA384_DIGEST_SIZE,  "HASH_ALG_SHA384" ),
  Tpm20.TPM_ALG_SHA512:  (Tpm20.SHA512_DIGEST_SIZE,  "HASH_ALG_SHA512" )
}

mHashClass = {
  Tpm20.TPM_ALG_SHA1:    ("HASH_ALG_SHA1",      Tpm20.SHA1_DIGEST_SIZE,    Tpm20.TPMT_HA_SHA1   ),
  Tpm20.TPM_ALG_SHA256:  ("HASH_ALG_SHA256",    Tpm20.SHA256_DIGEST_SIZE,  Tpm20.TPMT_HA_SHA256 ),
  Tpm20.TPM_ALG_SM3_256: ("HASH_ALG_SM3_256",   Tpm20.SM3_256_DIGEST_SIZE, Tpm20.TPMT_HA_SM3_256),
  Tpm20.TPM_ALG_SHA384:  ("HASH_ALG_SHA384",    Tpm20.SHA384_DIGEST_SIZE,  Tpm20.TPMT_HA_SHA384 ),
  Tpm20.TPM_ALG_SHA512:  ("HASH_ALG_SHA512",    Tpm20.SHA512_DIGEST_SIZE,  Tpm20.TPMT_HA_SHA512 )
}

def DumpEvent2 (TcgPcrEvent2Address, PCRIndex):

  TcgPcrEvent2 = UefiTcgPlatform.TCG_PCR_EVENT2.from_address (TcgPcrEvent2Address)

  class TPMT_HA (EFIPY_INDUSTRY_STRUCTURE):
    pass

  HashAlgoAddress = EfiPy.addressof (TcgPcrEvent2.Digest.digests[0])
  TPMT_HA_fields = []

  for i in range (TcgPcrEvent2.Digest.count):

    HashAlgo = Tpm20.TPMI_ALG_HASH.from_address (HashAlgoAddress)
    hashAlgName, digestSize, digestClass = mHashClass[HashAlgo.value]

    TPMT_HA_fields.append (
      (hashAlgName, digestClass)
    )

    HashAlgoAddress += EfiPy.sizeof (digestClass)

  class TPMT_HA (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = TPMT_HA_fields

  class TPML_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("count",   EfiPy.UINT32),
      ("digests", TPMT_HA)
    ]

  class TCG_PCR_EVENT2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("PCRIndex",  UefiTcgPlatform.TCG_PCRINDEX),
      ("EventType", UefiTcgPlatform.TCG_EVENTTYPE),
      ("Digest",    TPML_DIGEST_VALUES),
      ("EventSize", EfiPy.UINT32)
    ]
  TcgPcrEvent2 = TCG_PCR_EVENT2.from_address (TcgPcrEvent2Address)

  class TCG_PCR_EVENT2 (EFIPY_INDUSTRY_STRUCTURE):
    _fields_ = [
      ("PCRIndex",  UefiTcgPlatform.TCG_PCRINDEX),
      ("EventType", UefiTcgPlatform.TCG_EVENTTYPE),
      ("Digest",    TPML_DIGEST_VALUES),
      ("EventSize", EfiPy.UINT32),
      ("Event", EfiPy.UINT8 * TcgPcrEvent2.EventSize)
    ]
  TcgPcrEvent2 = TCG_PCR_EVENT2.from_address (TcgPcrEvent2Address)

  if PCRIndex != None and TcgPcrEvent2.PCRIndex != PCRIndex:
    return EfiPy.sizeof (TCG_PCR_EVENT2)

  print (f'''  Event:
    PCRIndex  - {TcgPcrEvent2.PCRIndex}
    EventType - 0x{TcgPcrEvent2.EventType:08X}
    DigestCount: 0x{TcgPcrEvent2.Digest.count:08X}''')

  Digest = TcgPcrEvent2.Digest
  for Index in range (Digest.count):

    hashAlgName, digestClass = Digest.digests._fields_ [Index]
    digestObj = getattr (Digest.digests, hashAlgName)

    print (f'''    HashAlgo : 0x{digestObj.hashAlg:04X} {hashAlgName}
    Digest({Index}, {len(digestObj.digest)}): {''.join (f'{v:02X}' for v in bytes (digestObj.digest))}
      {bytes (digestObj.digest)}''')

  print (f'''    EventSize - 0x{TcgPcrEvent2.EventSize:08X}''')

  ParseEventData (TcgPcrEvent2.EventType, bytes (TcgPcrEvent2.Event), EfiPy.addressof (TcgPcrEvent2.Event), TcgPcrEvent2.EventSize)

  return EfiPy.sizeof (TCG_PCR_EVENT2)

def DumpEventLogV2 (EventLogLocation, EventLogLastEntry, FinalEventsTable, PCRIndex):

  DumpEvent (EventLogLocation, PCRIndex)
  TcgPcrEvent2Address = DumpTcgEfiSpecIdEventStruct (EventLogLocation.value + EfiPy.sizeof (UefiTcgPlatform.TCG_PCR_EVENT_HDR))

  while TcgPcrEvent2Address <= EventLogLastEntry.value:
    TcgPcrEvent2Address += DumpEvent2 (TcgPcrEvent2Address, PCRIndex)

  if (FinalEventsTable == None):
    print ("FinalEventsTable: NOT FOUND")
    return

  FinalEventsTable = EfiPy.cast (
                             FinalEventsTable,
                             EfiPy.POINTER(EFI_TCG2_FINAL_EVENTS_TABLE)
                             )
  print (f'''FinalEventsTable:    (0x{EfiPy.addressof (FinalEventsTable[0]):X})
  Version:           (0x{FinalEventsTable[0].Version:X})
  NumberOfEvents:    (0x{FinalEventsTable[0].NumberOfEvents:X})''')

  TcgPcrEvent2 = EfiPy.addressof (FinalEventsTable[0]) + EfiPy.sizeof (EFI_TCG2_FINAL_EVENTS_TABLE)
  for Index in range (FinalEventsTable[0].NumberOfEvents):
    TcgPcrEvent2 += DumpEvent2 (TcgPcrEvent2, PCRIndex)

if __name__ == '__main__':
  Interface = EfiPy.PVOID ()
  Status = EfiPy.gBS.LocateProtocol (
             EfiPy.byref (gEfiTcg2ProtocolGuid),
             None,
             EfiPy.byref (Interface)
             )

  if (EfiPy.EFI_ERROR (Status)):
    import sys
    print ("Locate protocol.(Status:0x%016X)" % Status)
    sys.exit(Status)

  Tcg2Protocol = EfiPy.cast (
                   Interface,
                   EfiPy.POINTER(EFI_TCG2_PROTOCOL)
                   )

  LogFormat         = EFI_TCG2_EVENT_LOG_FORMAT_TCG_2
  EventLogLocation  = EfiPy.EFI_PHYSICAL_ADDRESS ()
  EventLogLastEntry = EfiPy.EFI_PHYSICAL_ADDRESS ()
  EventLogTruncated = EfiPy.BOOLEAN ()

  Status = Tcg2Protocol[0].GetEventLog (
                             Tcg2Protocol,
                             LogFormat,
                             EfiPy.pointer (EventLogLocation),
                             EfiPy.pointer (EventLogLastEntry),
                             EfiPy.pointer (EventLogTruncated)
                             )
  if EfiPy.EFI_ERROR (Status):
    import sys
    print ("ERROR: Tcg2Protocol->GetEventLog (Status:0x%016X)" % Status)
    sys.exit(Status)

  print (f'EventLogLocation: 0x{EventLogLocation.value:X}')
  print (f'EventLogLastEntry: 0x{EventLogLastEntry.value:X}')
  print (f'EventLogTruncated: {EventLogTruncated.value}')

  if EventLogTruncated.value:
    print ("WARNING: EventLogTruncated")

  FinalEventsTable = EfiGetSystemConfigurationTable (gEfiTcg2FinalEventsTableGuid)
  print (f'gEfiTcg2FinalEventsTableGuid: {gEfiTcg2FinalEventsTableGuid}, FinalEventsTable')

  DumpEventLogV2 (EventLogLocation, EventLogLastEntry, FinalEventsTable, None)
