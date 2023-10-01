# Tpm12.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm12
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

class TPM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  pass

TPM_BASE                    = 0

TPM_AUTH_DATA_USAGE                 = UINT8
TPM_PAYLOAD_TYPE                    = UINT8
TPM_VERSION_BYTE                    = UINT8
TPM_DA_STATE                        = UINT8
TPM_TAG                             = UINT16
TPM_PROTOCOL_ID                     = UINT16
TPM_STARTUP_TYPE                    = UINT16
TPM_ENC_SCHEME                      = UINT16
TPM_SIG_SCHEME                      = UINT16
TPM_MIGRATE_SCHEME                  = UINT16
TPM_PHYSICAL_PRESENCE               = UINT16
TPM_ENTITY_TYPE                     = UINT16
TPM_KEY_USAGE                       = UINT16
TPM_EK_TYPE                         = UINT16
TPM_STRUCTURE_TAG                   = UINT16
TPM_PLATFORM_SPECIFIC               = UINT16
TPM_COMMAND_CODE                    = UINT32
TPM_CAPABILITY_AREA                 = UINT32
TPM_KEY_FLAGS                       = UINT32
TPM_ALGORITHM_ID                    = UINT32
TPM_MODIFIER_INDICATOR              = UINT32
TPM_ACTUAL_COUNT                    = UINT32
TPM_TRANSPORT_ATTRIBUTES            = UINT32
TPM_AUTHHANDLE                      = UINT32
TPM_DIRINDEX                        = UINT32
TPM_KEY_HANDLE                      = UINT32
TPM_PCRINDEX                        = UINT32
TPM_RESULT                          = UINT32
TPM_RESOURCE_TYPE                   = UINT32
TPM_KEY_CONTROL                     = UINT32
TPM_NV_INDEX                        = UINT32
TPM_FAMILY_ID                       = UINT32
TPM_FAMILY_VERIFICATION             = UINT32
TPM_STARTUP_EFFECTS                 = UINT32
TPM_SYM_MODE                        = UINT32
TPM_FAMILY_FLAGS                    = UINT32
TPM_DELEGATE_INDEX                  = UINT32
TPM_CMK_DELEGATE                    = UINT32
TPM_COUNT_ID                        = UINT32
TPM_REDIT_COMMAND                   = UINT32
TPM_TRANSHANDLE                     = UINT32
TPM_HANDLE                          = UINT32
TPM_FAMILY_OPERATION                = UINT32

TPM_Vendor_Specific32       = 0x00000400
TPM_Vendor_Specific8        = 0x80

TPM_TAG_CONTEXTBLOB         = 0x0001
TPM_TAG_CONTEXT_SENSITIVE   = 0x0002
TPM_TAG_CONTEXTPOINTER      = 0x0003
TPM_TAG_CONTEXTLIST         = 0x0004
TPM_TAG_SIGNINFO            = 0x0005
TPM_TAG_PCR_INFO_LONG       = 0x0006
TPM_TAG_PERSISTENT_FLAGS    = 0x0007
TPM_TAG_VOLATILE_FLAGS      = 0x0008
TPM_TAG_PERSISTENT_DATA     = 0x0009
TPM_TAG_VOLATILE_DATA       = 0x000A
TPM_TAG_SV_DATA             = 0x000B
TPM_TAG_EK_BLOB             = 0x000C
TPM_TAG_EK_BLOB_AUTH        = 0x000D
TPM_TAG_COUNTER_VALUE       = 0x000E
TPM_TAG_TRANSPORT_INTERNAL  = 0x000F
TPM_TAG_TRANSPORT_LOG_IN    = 0x0010
TPM_TAG_TRANSPORT_LOG_OUT   = 0x0011
TPM_TAG_AUDIT_EVENT_IN      = 0x0012
TPM_TAG_AUDIT_EVENT_OUT     = 0x0013
TPM_TAG_CURRENT_TICKS       = 0x0014
TPM_TAG_KEY                 = 0x0015
TPM_TAG_STORED_DATA12       = 0x0016
TPM_TAG_NV_ATTRIBUTES       = 0x0017
TPM_TAG_NV_DATA_PUBLIC      = 0x0018
TPM_TAG_NV_DATA_SENSITIVE   = 0x0019
TPM_TAG_DELEGATIONS         = 0x001A
TPM_TAG_DELEGATE_PUBLIC     = 0x001B
TPM_TAG_DELEGATE_TABLE_ROW  = 0x001C
TPM_TAG_TRANSPORT_AUTH      = 0x001D
TPM_TAG_TRANSPORT_PUBLIC    = 0x001E
TPM_TAG_PERMANENT_FLAGS     = 0x001F
TPM_TAG_STCLEAR_FLAGS       = 0x0020
TPM_TAG_STANY_FLAGS         = 0x0021
TPM_TAG_PERMANENT_DATA      = 0x0022
TPM_TAG_STCLEAR_DATA        = 0x0023
TPM_TAG_STANY_DATA          = 0x0024
TPM_TAG_FAMILY_TABLE_ENTRY  = 0x0025
TPM_TAG_DELEGATE_SENSITIVE  = 0x0026
TPM_TAG_DELG_KEY_BLOB       = 0x0027
TPM_TAG_KEY12               = 0x0028
TPM_TAG_CERTIFY_INFO2       = 0x0029
TPM_TAG_DELEGATE_OWNER_BLOB = 0x002A
TPM_TAG_EK_BLOB_ACTIVATE    = 0x002B
TPM_TAG_DAA_BLOB            = 0x002C
TPM_TAG_DAA_CONTEXT         = 0x002D
TPM_TAG_DAA_ENFORCE         = 0x002E
TPM_TAG_DAA_ISSUER          = 0x002F
TPM_TAG_CAP_VERSION_INFO    = 0x0030
TPM_TAG_DAA_SENSITIVE       = 0x0031
TPM_TAG_DAA_TPM             = 0x0032
TPM_TAG_CMK_MIGAUTH         = 0x0033
TPM_TAG_CMK_SIGTICKET       = 0x0034
TPM_TAG_CMK_MA_APPROVAL     = 0x0035
TPM_TAG_QUOTE_INFO2         = 0x0036
TPM_TAG_DA_INFO             = 0x0037
TPM_TAG_DA_LIMITED          = 0x0038
TPM_TAG_DA_ACTION_TYPE      = 0x0039

TPM_RT_KEY                  = 0x00000001
TPM_RT_AUTH                 = 0x00000002
TPM_RT_HASH                 = 0x00000003
TPM_RT_TRANS                = 0x00000004
TPM_RT_CONTEXT              = 0x00000005
TPM_RT_COUNTER              = 0x00000006
TPM_RT_DELEGATE             = 0x00000007
TPM_RT_DAA_TPM              = 0x00000008
TPM_RT_DAA_V0               = 0x00000009
TPM_RT_DAA_V1               = 0x0000000A

TPM_PT_ASYM                 = 0x01
TPM_PT_BIND                 = 0x02
TPM_PT_MIGRATE              = 0x03
TPM_PT_MAINT                = 0x04
TPM_PT_SEAL                 = 0x05
TPM_PT_MIGRATE_RESTRICTED   = 0x06
TPM_PT_MIGRATE_EXTERNAL     = 0x07
TPM_PT_CMK_MIGRATE          = 0x08
TPM_PT_VENDOR_SPECIFIC      = 0x80

TPM_ET_KEYHANDLE            = 0x0001
TPM_ET_OWNER                = 0x0002
TPM_ET_DATA                 = 0x0003
TPM_ET_SRK                  = 0x0004
TPM_ET_KEY                  = 0x0005
TPM_ET_REVOKE               = 0x0006
TPM_ET_DEL_OWNER_BLOB       = 0x0007
TPM_ET_DEL_ROW              = 0x0008
TPM_ET_DEL_KEY_BLOB         = 0x0009
TPM_ET_COUNTER              = 0x000A
TPM_ET_NV                   = 0x000B
TPM_ET_OPERATOR             = 0x000C
TPM_ET_RESERVED_HANDLE      = 0x0040

TPM_ET_XOR                  = 0x0000
TPM_ET_AES128               = 0x0006

TPM_KH_SRK                  = 0x40000000
TPM_KH_OWNER                = 0x40000001
TPM_KH_REVOKE               = 0x40000002
TPM_KH_TRANSPORT            = 0x40000003
TPM_KH_OPERATOR             = 0x40000004
TPM_KH_ADMIN                = 0x40000005
TPM_KH_EK                   = 0x40000006

TPM_ST_CLEAR                = 0x0001
TPM_ST_STATE                = 0x0002
TPM_ST_DEACTIVATED          = 0x0003

TPM_PID_OIAP                = 0x0001
TPM_PID_OSAP                = 0x0002
TPM_PID_ADIP                = 0x0003
TPM_PID_ADCP                = 0x0004
TPM_PID_OWNER               = 0x0005
TPM_PID_DSAP                = 0x0006
TPM_PID_TRANSPORT           = 0x0007

TPM_ALG_RSA                 = 0x00000001
TPM_ALG_DES                 = 0x00000002
TPM_ALG_3DES                = 0x00000003
TPM_ALG_SHA                 = 0x00000004
TPM_ALG_HMAC                = 0x00000005
TPM_ALG_AES128              = 0x00000006
TPM_ALG_MGF1                = 0x00000007
TPM_ALG_AES192              = 0x00000008
TPM_ALG_AES256              = 0x00000009
TPM_ALG_XOR                 = 0x0000000A

TPM_PHYSICAL_PRESENCE_HW_DISABLE    = 0x0200
TPM_PHYSICAL_PRESENCE_CMD_DISABLE   = 0x0100
TPM_PHYSICAL_PRESENCE_LIFETIME_LOCK = 0x0080
TPM_PHYSICAL_PRESENCE_HW_ENABLE     = 0x0040
TPM_PHYSICAL_PRESENCE_CMD_ENABLE    = 0x0020
TPM_PHYSICAL_PRESENCE_NOTPRESENT    = 0x0010
TPM_PHYSICAL_PRESENCE_PRESENT       = 0x0008
TPM_PHYSICAL_PRESENCE_LOCK          = 0x0004

TPM_MS_MIGRATE                      = 0x0001
TPM_MS_REWRAP                       = 0x0002
TPM_MS_MAINT                        = 0x0003
TPM_MS_RESTRICT_MIGRATE             = 0x0004
TPM_MS_RESTRICT_APPROVE_DOUBLE      = 0x0005

TPM_EK_TYPE_ACTIVATE        = 0x0001
TPM_EK_TYPE_AUTH            = 0x0002

TPM_PS_PC_11                = 0x0001
TPM_PS_PC_12                = 0x0002
TPM_PS_PDA_12               = 0x0003
TPM_PS_Server_12            = 0x0004
TPM_PS_Mobile_12            = 0x0005

class TPM_STRUCT_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     UINT8),
    ("minor",     UINT8),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

class TPM_VERSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     TPM_VERSION_BYTE),
    ("minor",     TPM_VERSION_BYTE),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

TPM_SHA1_160_HASH_LEN       = 0x14
TPM_SHA1BASED_NONCE_LEN     = TPM_SHA1_160_HASH_LEN

class TPM_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("digest",  UINT8 * TPM_SHA1_160_HASH_LEN)
  ]

TPM_CHOSENID_HASH                   = TPM_DIGEST
TPM_COMPOSITE_HASH                  = TPM_DIGEST
TPM_DIRVALUE                        = TPM_DIGEST
TPM_HMAC                            = TPM_DIGEST
TPM_PCRVALUE                        = TPM_DIGEST
TPM_AUDITDIGEST                     = TPM_DIGEST

class TPM_NONCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",  UINT8 * 20)
  ]

TPM_DAA_TPM_SEED                  = TPM_NONCE
TPM_DAA_CONTEXT_SEED              = TPM_NONCE

tdTPM_AUTHDATA                    = UINT8 * 20
TPM_AUTHDATA                      = tdTPM_AUTHDATA
TPM_SECRET                        = TPM_AUTHDATA
TPM_ENCAUTH                       = TPM_AUTHDATA

class TPM_KEY_HANDLE_LIST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("loaded",  UINT16),
    ("handle",  TPM_KEY_HANDLE * 1)
  ]

TPM_KEY_SIGNING             = 0x0010
TPM_KEY_STORAGE             = 0x0011
TPM_KEY_IDENTITY            = 0x0012
TPM_KEY_AUTHCHANGE          = 0x0013
TPM_KEY_BIND                = 0x0014
TPM_KEY_LEGACY              = 0x0015
TPM_KEY_MIGRATE             = 0x0016

TPM_ES_NONE                 = 0x0001
TPM_ES_RSAESPKCSv15         = 0x0002
TPM_ES_RSAESOAEP_SHA1_MGF1  = 0x0003
TPM_ES_SYM_CNT              = 0x0004
TPM_ES_SYM_CTR              = 0x0004
TPM_ES_SYM_OFB              = 0x0005

TPM_SS_NONE                 = 0x0001
TPM_SS_RSASSAPKCS1v15_SHA1  = 0x0002
TPM_SS_RSASSAPKCS1v15_DER   = 0x0003
TPM_SS_RSASSAPKCS1v15_INFO  = 0x0004

TPM_AUTH_NEVER              = 0x00
TPM_AUTH_ALWAYS             = 0x01
TPM_AUTH_PRIV_USE_ONLY      = 0x03

TpmKeyFlagsRedirection                       = 0x00000001
TpmKeyFlagsMigratable                        = 0x00000002
TpmKeyFlagsIsVolatile                        = 0x00000004
TpmKeyFlagsPcrIgnoredOnRead                  = 0x00000008
TpmKeyFlagsMigrateAuthority                  = 0x00000010
TPM_KEY_FLAGS_BITS = ENUM

class TPM_CHANGEAUTH_VALIDATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("newAuthSecret", TPM_SECRET),
    ("n1",            TPM_NONCE)
  ]

class TPM_KEY_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmID", TPM_ALGORITHM_ID),
    ("encScheme",   TPM_ENC_SCHEME),
    ("sigScheme",   TPM_SIG_SCHEME),
    ("parmSize",    UINT32),
    ("parms",       POINTER (UINT8))
  ]

class TPM_STORE_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       UINT8 * 1)
  ]

class TPM_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubKey",          TPM_STORE_PUBKEY)
  ]

class TPM_MIGRATIONKEYAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationKey",    TPM_PUBKEY),
    ("migrationScheme", TPM_MIGRATE_SCHEME),
    ("digest",          TPM_DIGEST)
  ]

class TPM_COUNTER_VALUE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("label",   UINT8 * 4),
    ("counter", TPM_ACTUAL_COUNT)
  ]

class TPM_SIGN_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("fixed",   UINT8 * 4),
    ("replay",  TPM_NONCE),
    ("dataLen", UINT32),
    ("data",    POINTER (UINT8))
  ]

class TPM_MSA_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MSAlist",       UINT32),
    ("migAuthDigest", TPM_DIGEST * 1)
  ]

class TPM_CMK_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationAuthorityDigest",  TPM_DIGEST),
    ("destinationKeyDigest",      TPM_DIGEST),
    ("sourceKeyDigest",           TPM_DIGEST)
  ]

TPM_CMK_DELEGATE_SIGNING    = BIT31
TPM_CMK_DELEGATE_STORAGE    = BIT30
TPM_CMK_DELEGATE_BIND       = BIT29
TPM_CMK_DELEGATE_LEGACY     = BIT28
TPM_CMK_DELEGATE_MIGRATE    = BIT27

class TPM_SELECT_SIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",   UINT8),
    ("minor",   UINT8),
    ("reqSize", UINT16)
  ]

class TPM_CMK_MIGAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("msaDigest",     TPM_DIGEST),
    ("pubKeyDigest",  TPM_DIGEST)
  ]

class TPM_CMK_SIGTICKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("verKeyDigest",  TPM_DIGEST),
    ("signedData",    TPM_DIGEST)
  ]

class TPM_CMK_MA_APPROVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("migrationAuthorityDigest",  TPM_DIGEST)
  ]

TPM_TAG_RQU_COMMAND         = 0x00C1
TPM_TAG_RQU_AUTH1_COMMAND   = 0x00C2
TPM_TAG_RQU_AUTH2_COMMAND   = 0x00C3
TPM_TAG_RSP_COMMAND         = 0x00C4
TPM_TAG_RSP_AUTH1_COMMAND   = 0x00C5
TPM_TAG_RSP_AUTH2_COMMAND   = 0x00C6

class TPM_PERMANENT_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                           TPM_STRUCTURE_TAG),
    ("disable",                       BOOLEAN),
    ("ownership",                     BOOLEAN),
    ("deactivated",                   BOOLEAN),
    ("readPubek",                     BOOLEAN),
    ("disableOwnerClear",             BOOLEAN),
    ("allowMaintenance",              BOOLEAN),
    ("physicalPresenceLifetimeLock",  BOOLEAN),
    ("physicalPresenceHWEnable",      BOOLEAN),
    ("physicalPresenceCMDEnable",     BOOLEAN),
    ("CEKPUsed",                      BOOLEAN),
    ("TPMpost",                       BOOLEAN),
    ("TPMpostLock",                   BOOLEAN),
    ("FIPS",                          BOOLEAN),
    ("operator",                      BOOLEAN),
    ("enableRevokeEK",                BOOLEAN),
    ("nvLocked",                      BOOLEAN),
    ("readSRKPub",                    BOOLEAN),
    ("tpmEstablished",                BOOLEAN),
    ("maintenanceDone",               BOOLEAN),
    ("disableFullDALogicInfo",        BOOLEAN)
  ]

TPM_PF_DISABLE                      = 1
TPM_PF_OWNERSHIP                    = 2
TPM_PF_DEACTIVATED                  = 3
TPM_PF_READPUBEK                    = 4
TPM_PF_DISABLEOWNERCLEAR            = 5
TPM_PF_ALLOWMAINTENANCE             = 6
TPM_PF_PHYSICALPRESENCELIFETIMELOCK = 7
TPM_PF_PHYSICALPRESENCEHWENABLE     = 8
TPM_PF_PHYSICALPRESENCECMDENABLE    = 9
TPM_PF_CEKPUSED                     = 10
TPM_PF_TPMPOST                      = 11
TPM_PF_TPMPOSTLOCK                  = 12
TPM_PF_FIPS                         = 13
TPM_PF_OPERATOR                     = 14
TPM_PF_ENABLEREVOKEEK               = 15
TPM_PF_NV_LOCKED                    = 16
TPM_PF_READSRKPUB                   = 17
TPM_PF_TPMESTABLISHED               = 18
TPM_PF_MAINTENANCEDONE              = 19
TPM_PF_DISABLEFULLDALOGICINFO       = 20

class TPM_STCLEAR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("deactivated",           BOOLEAN),
    ("disableForceClear",     BOOLEAN),
    ("physicalPresence",      BOOLEAN),
    ("physicalPresenceLock",  BOOLEAN),
    ("bGlobalLock",           BOOLEAN)
  ]

TPM_SF_DEACTIVATED          = 1
TPM_SF_DISABLEFORCECLEAR    = 2
TPM_SF_PHYSICALPRESENCE     = 3
TPM_SF_PHYSICALPRESENCELOCK = 4
TPM_SF_BGLOBALLOCK          = 5

class TPM_STANY_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("postInitialise",      BOOLEAN),
    ("localityModifier",    TPM_MODIFIER_INDICATOR),
    ("transportExclusive",  BOOLEAN),
    ("TOSPresent",          BOOLEAN)
  ]

TPM_AF_POSTINITIALISE       = 1
TPM_AF_LOCALITYMODIFIER     = 2
TPM_AF_TRANSPORTEXCLUSIVE   = 3
TPM_AF_TOSPRESENT           = 4

TPM_MIN_COUNTERS            = 4
TPM_DELEGATE_KEY            = TPM_KEY
TPM_NUM_PCR                 = 16
TPM_MAX_NV_WRITE_NOOWNER    = 64

TPM_PD_REVMAJOR               = 1
TPM_PD_REVMINOR               = 2
TPM_PD_TPMPROOF               = 3
TPM_PD_OWNERAUTH              = 4
TPM_PD_OPERATORAUTH           = 5
TPM_PD_MANUMAINTPUB           = 6
TPM_PD_ENDORSEMENTKEY         = 7
TPM_PD_SRK                    = 8
TPM_PD_DELEGATEKEY            = 9
TPM_PD_CONTEXTKEY             = 10
TPM_PD_AUDITMONOTONICCOUNTER  = 11
TPM_PD_MONOTONICCOUNTER       = 12
TPM_PD_PCRATTRIB              = 13
TPM_PD_ORDINALAUDITSTATUS     = 14
TPM_PD_AUTHDIR                = 15
TPM_PD_RNGSTATE               = 16
TPM_PD_FAMILYTABLE            = 17
TPM_DELEGATETABLE             = 18
TPM_PD_EKRESET                = 19
TPM_PD_MAXNVBUFSIZE           = 20
TPM_PD_LASTFAMILYID           = 21
TPM_PD_NOOWNERNVWRITE         = 22
TPM_PD_RESTRICTDELEGATE       = 23
TPM_PD_TPMDAASEED             = 24
TPM_PD_DAAPROOF               = 25

class TPM_STCLEAR_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("contextNonceKey",           TPM_NONCE),
    ("countID",                   TPM_COUNT_ID),
    ("ownerReference",            UINT32),
    ("disableResetLock",          BOOLEAN),
    ("PCR",                       TPM_PCRVALUE * TPM_NUM_PCR),
    ("deferredPhysicalPresence",  UINT32)
  ]

TPM_SD_CONTEXTNONCEKEY            = 0x00000001
TPM_SD_COUNTID                    = 0x00000002
TPM_SD_OWNERREFERENCE             = 0x00000003
TPM_SD_DISABLERESETLOCK           = 0x00000004
TPM_SD_PCR                        = 0x00000005
TPM_SD_DEFERREDPHYSICALPRESENCE   = 0x00000006

TPM_AD_CONTEXTNONCESESSION        = 1
TPM_AD_AUDITDIGEST                = 2
TPM_AD_CURRENTTICKS               = 3
TPM_AD_CONTEXTCOUNT               = 4
TPM_AD_CONTEXTLIST                = 5
TPM_AD_SESSIONS                   = 6

class TPM_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeOfSelect",  UINT16),
    ("pcrSelect",     UINT8 * 1)
  ]

class TPM_PCR_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("select",    TPM_PCR_SELECTION),
    ("valueSize", UINT32),
    ("pcrValue",  TPM_PCRVALUE * 1)
  ]

class TPM_PCR_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH),
    ("digestAtCreation",  TPM_COMPOSITE_HASH)
  ]

TPM_LOCALITY_SELECTION = UINT8

TPM_LOC_FOUR                = 0x10
TPM_LOC_THREE               = 0x08
TPM_LOC_TWO                 = 0x04
TPM_LOC_ONE                 = 0x02
TPM_LOC_ZERO                = 0x01

class TPM_PCR_INFO_LONG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("localityAtCreation",    TPM_LOCALITY_SELECTION),
    ("localityAtRelease",     TPM_LOCALITY_SELECTION),
    ("creationPCRSelection",  TPM_PCR_SELECTION),
    ("releasePCRSelection",   TPM_PCR_SELECTION),
    ("digestAtCreation",      TPM_COMPOSITE_HASH),
    ("digestAtRelease",       TPM_COMPOSITE_HASH)
  ]

class TPM_PCR_INFO_SHORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("localityAtRelease", TPM_LOCALITY_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH)
  ]

class TPM_PCR_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrReset",        BOOLEAN),
    ("pcrExtendLocal",  TPM_LOCALITY_SELECTION),
    ("pcrResetLocal",   TPM_LOCALITY_SELECTION)
  ]

class TPM_STORED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",           TPM_STRUCT_VER),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

class TPM_STORED_DATA12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("et",            TPM_ENTITY_TYPE),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

class TPM_SEALED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("authData",      TPM_SECRET),
    ("tpmProof",      TPM_NONCE),
    ("storedDigest",  TPM_DIGEST),
    ("dataSize",      UINT32),
    ("data",          POINTER (UINT8))
  ]

class TPM_SYMMETRIC_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algId",     TPM_ALGORITHM_ID),
    ("encScheme", TPM_ENC_SCHEME),
    ("dataSize",  UINT16),
    ("data",      POINTER (UINT8))
  ]

class TPM_BOUND_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",         TPM_STRUCT_VER),
    ("payload",     TPM_PAYLOAD_TYPE),
    ("payloadData", UINT8 * 1)
  ]


TPM_KEY._fields_ = [
    ("ver",             TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

class TPM_KEY12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("fill",            UINT16),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

class TPM_STORE_PRIVKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       POINTER (UINT8))
  ]

class TPM_STORE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("usageAuth",     TPM_SECRET),
    ("migrationAuth", TPM_SECRET),
    ("pubDataDigest", TPM_DIGEST),
    ("privKey",       TPM_STORE_PRIVKEY)
  ]

class TPM_MIGRATE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",         TPM_PAYLOAD_TYPE),
    ("usageAuth",       TPM_SECRET),
    ("pubDataDigest",   TPM_DIGEST),
    ("partPrivKeyLen",  UINT32),
    ("partPrivKey",     POINTER (UINT8))
  ]

TPM_KEY_CONTROL_OWNER_EVICT = 0x00000001

class TPM_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",         TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubkeyDigest",    TPM_DIGEST),
    ("data",            TPM_NONCE),
    ("parentPCRStatus", BOOLEAN),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8))
  ]

class TPM_CERTIFY_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                     TPM_STRUCTURE_TAG),
    ("fill",                    UINT8),
    ("payloadType",             TPM_PAYLOAD_TYPE),
    ("keyUsage",                TPM_KEY_USAGE),
    ("keyFlags",                TPM_KEY_FLAGS),
    ("authDataUsage",           TPM_AUTH_DATA_USAGE),
    ("algorithmParms",          TPM_KEY_PARMS),
    ("pubkeyDigest",            TPM_DIGEST),
    ("data",                    TPM_NONCE),
    ("parentPCRStatus",         BOOLEAN),
    ("PCRInfoSize",             UINT32),
    ("PCRInfo",                 POINTER(UINT8)),
    ("migrationAuthoritySize",  UINT32),
    ("migrationAuthority",      POINTER (UINT8))
  ]

class TPM_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",       TPM_STRUCT_VER),
    ("fixed",         UINT8 * 4),
    ("digestValue",   TPM_COMPOSITE_HASH),
    ("externalData",  TPM_NONCE)
  ]

class TPM_QUOTE_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("fixed",         UINT8 * 4),
    ("externalData",  TPM_NONCE),
    ("infoShort",     TPM_PCR_INFO_SHORT)
  ]

class TPM_EK_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("ekType",    TPM_EK_TYPE),
    ("blobSize",  UINT32),
    ("blob",      POINTER (UINT8))
  ]

class TPM_EK_BLOB_ACTIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST),
    ("pcrInfo",     TPM_PCR_INFO_SHORT)
  ]

class TPM_EK_BLOB_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("authValue",   TPM_SECRET)
  ]

class TPM_IDENTITY_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",               TPM_STRUCT_VER),
    ("ordinal",           UINT32),
    ("labelPrivCADigest", TPM_CHOSENID_HASH),
    ("identityPubKey",    TPM_PUBKEY)
  ]

class TPM_IDENTITY_REQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymSize",      UINT32),
    ("symSize",       UINT32),
    ("asymAlgorithm", TPM_KEY_PARMS),
    ("symAlgorithm",  TPM_KEY_PARMS),
    ("asymBlob",      POINTER (UINT8)),
    ("symBlob",       POINTER (UINT8))
  ]

class TPM_IDENTITY_PROOF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",                   TPM_STRUCT_VER),
    ("labelSize",             UINT32),
    ("identityBindingSize",   UINT32),
    ("endorsementSize",       UINT32),
    ("platformSize",          UINT32),
    ("conformanceSize",       UINT32),
    ("identityKey",           TPM_PUBKEY),
    ("labelArea",             POINTER (UINT8)),
    ("identityBinding",       POINTER (UINT8)),
    ("endorsementCredential", POINTER (UINT8)),
    ("platformCredential",    POINTER (UINT8)),
    ("conformanceCredential", POINTER (UINT8))
  ]

class TPM_ASYM_CA_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST)
  ]

class TPM_SYM_CA_ATTESTATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("credSize",    UINT32),
    ("algorithm",   TPM_KEY_PARMS),
    ("credential",  POINTER (UINT8))
  ]

class TPM_CURRENT_TICKS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("currentTicks",  UINT64),
    ("tickRate",      UINT16),
    ("tickNonce",     TPM_NONCE)
  ]

class TPM_TRANSPORT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("transAttributes", TPM_TRANSPORT_ATTRIBUTES),
    ("algId",           TPM_ALGORITHM_ID),
    ("encScheme",       TPM_ENC_SCHEME)
  ]

TPM_TRANSPORT_ENCRYPT       = BIT0
TPM_TRANSPORT_LOG           = BIT1
TPM_TRANSPORT_EXCLUSIVE     = BIT2

class TPM_TRANSPORT_INTERNAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("authData",        TPM_AUTHDATA),
    ("transPublic",     TPM_TRANSPORT_PUBLIC),
    ("transHandle",     TPM_TRANSHANDLE),
    ("transNonceEven",  TPM_NONCE),
    ("transDigest",     TPM_DIGEST)
  ]

class TPM_TRANSPORT_LOG_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("parameters",      TPM_DIGEST),
    ("pubKeyHash",      TPM_DIGEST)
  ]

class TPM_TRANSPORT_LOG_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("currentTicks",    TPM_CURRENT_TICKS),
    ("parameters",      TPM_DIGEST),
    ("locality",        TPM_MODIFIER_INDICATOR)
  ]

class TPM_TRANSPORT_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authData",  TPM_AUTHDATA)
  ]

class TPM_AUDIT_EVENT_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("inputParms",  TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE)
  ]

class TPM_AUDIT_EVENT_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("ordinal",     TPM_COMMAND_CODE),
    ("outputParms", TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE),
    ("returnCode",  TPM_RESULT)
  ]

TPM_VENDOR_ERROR            = TPM_Vendor_Specific32
TPM_NON_FATAL               = 0x00000800
TPM_SUCCESS                 = TPM_BASE
TPM_AUTHFAIL                = TPM_BASE + 1
TPM_BADINDEX                = TPM_BASE + 2
TPM_BAD_PARAMETER           = TPM_BASE + 3
TPM_AUDITFAILURE            = TPM_BASE + 4
TPM_CLEAR_DISABLED          = TPM_BASE + 5
TPM_DEACTIVATED             = TPM_BASE + 6
TPM_DISABLED                = TPM_BASE + 7
TPM_DISABLED_CMD            = TPM_BASE + 8
TPM_FAIL                    = TPM_BASE + 9
TPM_BAD_ORDINAL             = TPM_BASE + 10
TPM_INSTALL_DISABLED        = TPM_BASE + 11
TPM_INVALID_KEYHANDLE       = TPM_BASE + 12
TPM_KEYNOTFOUND             = TPM_BASE + 13
TPM_INAPPROPRIATE_ENC       = TPM_BASE + 14
TPM_MIGRATEFAIL             = TPM_BASE + 15
TPM_INVALID_PCR_INFO        = TPM_BASE + 16
TPM_NOSPACE                 = TPM_BASE + 17
TPM_NOSRK                   = TPM_BASE + 18
TPM_NOTSEALED_BLOB          = TPM_BASE + 19
TPM_OWNER_SET               = TPM_BASE + 20
TPM_RESOURCES               = TPM_BASE + 21
TPM_SHORTRANDOM             = TPM_BASE + 22
TPM_SIZE                    = TPM_BASE + 23
TPM_WRONGPCRVAL             = TPM_BASE + 24
TPM_BAD_PARAM_SIZE          = TPM_BASE + 25
TPM_SHA_THREAD              = TPM_BASE + 26
TPM_SHA_ERROR               = TPM_BASE + 27
TPM_FAILEDSELFTEST          = TPM_BASE + 28
TPM_AUTH2FAIL               = TPM_BASE + 29
TPM_BADTAG                  = TPM_BASE + 30
TPM_IOERROR                 = TPM_BASE + 31
TPM_ENCRYPT_ERROR           = TPM_BASE + 32
TPM_DECRYPT_ERROR           = TPM_BASE + 33
TPM_INVALID_AUTHHANDLE      = TPM_BASE + 34
TPM_NO_ENDORSEMENT          = TPM_BASE + 35
TPM_INVALID_KEYUSAGE        = TPM_BASE + 36
TPM_WRONG_ENTITYTYPE        = TPM_BASE + 37
TPM_INVALID_POSTINIT        = TPM_BASE + 38
TPM_INAPPROPRIATE_SIG       = TPM_BASE + 39
TPM_BAD_KEY_PROPERTY        = TPM_BASE + 40
TPM_BAD_MIGRATION           = TPM_BASE + 41
TPM_BAD_SCHEME              = TPM_BASE + 42
TPM_BAD_DATASIZE            = TPM_BASE + 43
TPM_BAD_MODE                = TPM_BASE + 44
TPM_BAD_PRESENCE            = TPM_BASE + 45
TPM_BAD_VERSION             = TPM_BASE + 46
TPM_NO_WRAP_TRANSPORT       = TPM_BASE + 47
TPM_AUDITFAIL_UNSUCCESSFUL  = TPM_BASE + 48
TPM_AUDITFAIL_SUCCESSFUL    = TPM_BASE + 49
TPM_NOTRESETABLE            = TPM_BASE + 50
TPM_NOTLOCAL                = TPM_BASE + 51
TPM_BAD_TYPE                = TPM_BASE + 52
TPM_INVALID_RESOURCE        = TPM_BASE + 53
TPM_NOTFIPS                 = TPM_BASE + 54
TPM_INVALID_FAMILY          = TPM_BASE + 55
TPM_NO_NV_PERMISSION        = TPM_BASE + 56
TPM_REQUIRES_SIGN           = TPM_BASE + 57
TPM_KEY_NOTSUPPORTED        = TPM_BASE + 58
TPM_AUTH_CONFLICT           = TPM_BASE + 59
TPM_AREA_LOCKED             = TPM_BASE + 60
TPM_BAD_LOCALITY            = TPM_BASE + 61
TPM_READ_ONLY               = TPM_BASE + 62
TPM_PER_NOWRITE             = TPM_BASE + 63
TPM_FAMILYCOUNT             = TPM_BASE + 64
TPM_WRITE_LOCKED            = TPM_BASE + 65
TPM_BAD_ATTRIBUTES          = TPM_BASE + 66
TPM_INVALID_STRUCTURE       = TPM_BASE + 67
TPM_KEY_OWNER_CONTROL       = TPM_BASE + 68
TPM_BAD_COUNTER             = TPM_BASE + 69
TPM_NOT_FULLWRITE           = TPM_BASE + 70
TPM_CONTEXT_GAP             = TPM_BASE + 71
TPM_MAXNVWRITES             = TPM_BASE + 72
TPM_NOOPERATOR              = TPM_BASE + 73
TPM_RESOURCEMISSING         = TPM_BASE + 74
TPM_DELEGATE_LOCK           = TPM_BASE + 75
TPM_DELEGATE_FAMILY         = TPM_BASE + 76
TPM_DELEGATE_ADMIN          = TPM_BASE + 77
TPM_TRANSPORT_NOTEXCLUSIVE  = TPM_BASE + 78
TPM_OWNER_CONTROL           = TPM_BASE + 79
TPM_DAA_RESOURCES           = TPM_BASE + 80
TPM_DAA_INPUT_DATA0         = TPM_BASE + 81
TPM_DAA_INPUT_DATA1         = TPM_BASE + 82
TPM_DAA_ISSUER_SETTINGS     = TPM_BASE + 83
TPM_DAA_TPM_SETTINGS        = TPM_BASE + 84
TPM_DAA_STAGE               = TPM_BASE + 85
TPM_DAA_ISSUER_VALIDITY     = TPM_BASE + 86
TPM_DAA_WRONG_W             = TPM_BASE + 87
TPM_BAD_HANDLE              = TPM_BASE + 88
TPM_BAD_DELEGATE            = TPM_BASE + 89
TPM_BADCONTEXT              = TPM_BASE + 90
TPM_TOOMANYCONTEXTS         = TPM_BASE + 91
TPM_MA_TICKET_SIGNATURE     = TPM_BASE + 92
TPM_MA_DESTINATION          = TPM_BASE + 93
TPM_MA_SOURCE               = TPM_BASE + 94
TPM_MA_AUTHORITY            = TPM_BASE + 95
TPM_PERMANENTEK             = TPM_BASE + 97
TPM_BAD_SIGNATURE           = TPM_BASE + 98
TPM_NOCONTEXTSPACE          = TPM_BASE + 99

TPM_RETRY                   = TPM_BASE + TPM_NON_FATAL
TPM_NEEDS_SELFTEST          = TPM_BASE + TPM_NON_FATAL + 1
TPM_DOING_SELFTEST          = TPM_BASE + TPM_NON_FATAL + 2
TPM_DEFEND_LOCK_RUNNING     = TPM_BASE + TPM_NON_FATAL + 3

TPM_ORD_ActivateIdentity                  = 0x0000007A
TPM_ORD_AuthorizeMigrationKey             = 0x0000002B
TPM_ORD_CertifyKey                        = 0x00000032
TPM_ORD_CertifyKey2                       = 0x00000033
TPM_ORD_CertifySelfTest                   = 0x00000052
TPM_ORD_ChangeAuth                        = 0x0000000C
TPM_ORD_ChangeAuthAsymFinish              = 0x0000000F
TPM_ORD_ChangeAuthAsymStart               = 0x0000000E
TPM_ORD_ChangeAuthOwner                   = 0x00000010
TPM_ORD_CMK_ApproveMA                     = 0x0000001D
TPM_ORD_CMK_ConvertMigration              = 0x00000024
TPM_ORD_CMK_CreateBlob                    = 0x0000001B
TPM_ORD_CMK_CreateKey                     = 0x00000013
TPM_ORD_CMK_CreateTicket                  = 0x00000012
TPM_ORD_CMK_SetRestrictions               = 0x0000001C
TPM_ORD_ContinueSelfTest                  = 0x00000053
TPM_ORD_ConvertMigrationBlob              = 0x0000002A
TPM_ORD_CreateCounter                     = 0x000000DC
TPM_ORD_CreateEndorsementKeyPair          = 0x00000078
TPM_ORD_CreateMaintenanceArchive          = 0x0000002C
TPM_ORD_CreateMigrationBlob               = 0x00000028
TPM_ORD_CreateRevocableEK                 = 0x0000007F
TPM_ORD_CreateWrapKey                     = 0x0000001F
TPM_ORD_DAA_JOIN                          = 0x00000029
TPM_ORD_DAA_SIGN                          = 0x00000031
TPM_ORD_Delegate_CreateKeyDelegation      = 0x000000D4
TPM_ORD_Delegate_CreateOwnerDelegation    = 0x000000D5
TPM_ORD_Delegate_LoadOwnerDelegation      = 0x000000D8
TPM_ORD_Delegate_Manage                   = 0x000000D2
TPM_ORD_Delegate_ReadTable                = 0x000000DB
TPM_ORD_Delegate_UpdateVerification       = 0x000000D1
TPM_ORD_Delegate_VerifyDelegation         = 0x000000D6
TPM_ORD_DirRead                           = 0x0000001A
TPM_ORD_DirWriteAuth                      = 0x00000019
TPM_ORD_DisableForceClear                 = 0x0000005E
TPM_ORD_DisableOwnerClear                 = 0x0000005C
TPM_ORD_DisablePubekRead                  = 0x0000007E
TPM_ORD_DSAP                              = 0x00000011
TPM_ORD_EstablishTransport                = 0x000000E6
TPM_ORD_EvictKey                          = 0x00000022
TPM_ORD_ExecuteTransport                  = 0x000000E7
TPM_ORD_Extend                            = 0x00000014
TPM_ORD_FieldUpgrade                      = 0x000000AA
TPM_ORD_FlushSpecific                     = 0x000000BA
TPM_ORD_ForceClear                        = 0x0000005D
TPM_ORD_GetAuditDigest                    = 0x00000085
TPM_ORD_GetAuditDigestSigned              = 0x00000086
TPM_ORD_GetAuditEvent                     = 0x00000082
TPM_ORD_GetAuditEventSigned               = 0x00000083
TPM_ORD_GetCapability                     = 0x00000065
TPM_ORD_GetCapabilityOwner                = 0x00000066
TPM_ORD_GetCapabilitySigned               = 0x00000064
TPM_ORD_GetOrdinalAuditStatus             = 0x0000008C
TPM_ORD_GetPubKey                         = 0x00000021
TPM_ORD_GetRandom                         = 0x00000046
TPM_ORD_GetTestResult                     = 0x00000054
TPM_ORD_GetTicks                          = 0x000000F1
TPM_ORD_IncrementCounter                  = 0x000000DD
TPM_ORD_Init                              = 0x00000097
TPM_ORD_KeyControlOwner                   = 0x00000023
TPM_ORD_KillMaintenanceFeature            = 0x0000002E
TPM_ORD_LoadAuthContext                   = 0x000000B7
TPM_ORD_LoadContext                       = 0x000000B9
TPM_ORD_LoadKey                           = 0x00000020
TPM_ORD_LoadKey2                          = 0x00000041
TPM_ORD_LoadKeyContext                    = 0x000000B5
TPM_ORD_LoadMaintenanceArchive            = 0x0000002D
TPM_ORD_LoadManuMaintPub                  = 0x0000002F
TPM_ORD_MakeIdentity                      = 0x00000079
TPM_ORD_MigrateKey                        = 0x00000025
TPM_ORD_NV_DefineSpace                    = 0x000000CC
TPM_ORD_NV_ReadValue                      = 0x000000CF
TPM_ORD_NV_ReadValueAuth                  = 0x000000D0
TPM_ORD_NV_WriteValue                     = 0x000000CD
TPM_ORD_NV_WriteValueAuth                 = 0x000000CE
TPM_ORD_OIAP                              = 0x0000000A
TPM_ORD_OSAP                              = 0x0000000B
TPM_ORD_OwnerClear                        = 0x0000005B
TPM_ORD_OwnerReadInternalPub              = 0x00000081
TPM_ORD_OwnerReadPubek                    = 0x0000007D
TPM_ORD_OwnerSetDisable                   = 0x0000006E
TPM_ORD_PCR_Reset                         = 0x000000C8
TPM_ORD_PcrRead                           = 0x00000015
TPM_ORD_PhysicalDisable                   = 0x00000070
TPM_ORD_PhysicalEnable                    = 0x0000006F
TPM_ORD_PhysicalSetDeactivated            = 0x00000072
TPM_ORD_Quote                             = 0x00000016
TPM_ORD_Quote2                            = 0x0000003E
TPM_ORD_ReadCounter                       = 0x000000DE
TPM_ORD_ReadManuMaintPub                  = 0x00000030
TPM_ORD_ReadPubek                         = 0x0000007C
TPM_ORD_ReleaseCounter                    = 0x000000DF
TPM_ORD_ReleaseCounterOwner               = 0x000000E0
TPM_ORD_ReleaseTransportSigned            = 0x000000E8
TPM_ORD_Reset                             = 0x0000005A
TPM_ORD_ResetLockValue                    = 0x00000040
TPM_ORD_RevokeTrust                       = 0x00000080
TPM_ORD_SaveAuthContext                   = 0x000000B6
TPM_ORD_SaveContext                       = 0x000000B8
TPM_ORD_SaveKeyContext                    = 0x000000B4
TPM_ORD_SaveState                         = 0x00000098
TPM_ORD_Seal                              = 0x00000017
TPM_ORD_Sealx                             = 0x0000003D
TPM_ORD_SelfTestFull                      = 0x00000050
TPM_ORD_SetCapability                     = 0x0000003F
TPM_ORD_SetOperatorAuth                   = 0x00000074
TPM_ORD_SetOrdinalAuditStatus             = 0x0000008D
TPM_ORD_SetOwnerInstall                   = 0x00000071
TPM_ORD_SetOwnerPointer                   = 0x00000075
TPM_ORD_SetRedirection                    = 0x0000009A
TPM_ORD_SetTempDeactivated                = 0x00000073
TPM_ORD_SHA1Complete                      = 0x000000A2
TPM_ORD_SHA1CompleteExtend                = 0x000000A3
TPM_ORD_SHA1Start                         = 0x000000A0
TPM_ORD_SHA1Update                        = 0x000000A1
TPM_ORD_Sign                              = 0x0000003C
TPM_ORD_Startup                           = 0x00000099
TPM_ORD_StirRandom                        = 0x00000047
TPM_ORD_TakeOwnership                     = 0x0000000D
TPM_ORD_Terminate_Handle                  = 0x00000096
TPM_ORD_TickStampBlob                     = 0x000000F2
TPM_ORD_UnBind                            = 0x0000001E
TPM_ORD_Unseal                            = 0x00000018
TSC_ORD_PhysicalPresence                  = 0x4000000A
TSC_ORD_ResetEstablishmentBit             = 0x4000000B

class TPM_CONTEXT_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("handle",          TPM_HANDLE),
    ("label",           UINT8 * 16),
    ("contextCount",    UINT32),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

class TPM_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("contextNonce",  TPM_NONCE),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

TPM_NV_INDEX_LOCK              = 0xffffffff
TPM_NV_INDEX0                  = 0x00000000
TPM_NV_INDEX_DIR               = 0x10000001
TPM_NV_INDEX_EKCert            = 0x0000f000
TPM_NV_INDEX_TPM_CC            = 0x0000f001
TPM_NV_INDEX_PlatformCert      = 0x0000f002
TPM_NV_INDEX_Platform_CC       = 0x0000f003

TPM_NV_INDEX_TSS_BASE          = 0x00011100
TPM_NV_INDEX_PC_BASE           = 0x00011200
TPM_NV_INDEX_SERVER_BASE       = 0x00011300
TPM_NV_INDEX_MOBILE_BASE       = 0x00011400
TPM_NV_INDEX_PERIPHERAL_BASE   = 0x00011500
TPM_NV_INDEX_GROUP_RESV_BASE   = 0x00010000

class TPM_NV_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("attributes",  UINT32)
  ]

TPM_NV_PER_READ_STCLEAR        = BIT31
TPM_NV_PER_AUTHREAD            = BIT18
TPM_NV_PER_OWNERREAD           = BIT17
TPM_NV_PER_PPREAD              = BIT16
TPM_NV_PER_GLOBALLOCK          = BIT15
TPM_NV_PER_WRITE_STCLEAR       = BIT14
TPM_NV_PER_WRITEDEFINE         = BIT13
TPM_NV_PER_WRITEALL            = BIT12
TPM_NV_PER_AUTHWRITE           = BIT2
TPM_NV_PER_OWNERWRITE          = BIT1
TPM_NV_PER_PPWRITE             = BIT0

class TPM_NV_DATA_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("nvIndex",       TPM_NV_INDEX),
    ("pcrInfoRead",   TPM_PCR_INFO_SHORT),
    ("pcrInfoWrite",  TPM_PCR_INFO_SHORT),
    ("permission",    TPM_NV_ATTRIBUTES),
    ("bReadSTClear",  BOOLEAN),
    ("bWriteSTClear", BOOLEAN),
    ("bWriteDefine",  BOOLEAN),
    ("dataSize",      UINT32)
  ]

TPM_DEL_OWNER_BITS          = 0x00000001
TPM_DEL_KEY_BITS            = 0x00000002

class TPM_DELEGATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("delegateType",  UINT32),
    ("per1",          UINT32),
    ("per2",          UINT32)
  ]

TPM_DELEGATE_SetOrdinalAuditStatus          = BIT30
TPM_DELEGATE_DirWriteAuth                   = BIT29
TPM_DELEGATE_CMK_ApproveMA                  = BIT28
TPM_DELEGATE_NV_WriteValue                  = BIT27
TPM_DELEGATE_CMK_CreateTicket               = BIT26
TPM_DELEGATE_NV_ReadValue                   = BIT25
TPM_DELEGATE_Delegate_LoadOwnerDelegation   = BIT24
TPM_DELEGATE_DAA_Join                       = BIT23
TPM_DELEGATE_AuthorizeMigrationKey          = BIT22
TPM_DELEGATE_CreateMaintenanceArchive       = BIT21
TPM_DELEGATE_LoadMaintenanceArchive         = BIT20
TPM_DELEGATE_KillMaintenanceFeature         = BIT19
TPM_DELEGATE_OwnerReadInteralPub            = BIT18
TPM_DELEGATE_ResetLockValue                 = BIT17
TPM_DELEGATE_OwnerClear                     = BIT16
TPM_DELEGATE_DisableOwnerClear              = BIT15
TPM_DELEGATE_NV_DefineSpace                 = BIT14
TPM_DELEGATE_OwnerSetDisable                = BIT13
TPM_DELEGATE_SetCapability                  = BIT12
TPM_DELEGATE_MakeIdentity                   = BIT11
TPM_DELEGATE_ActivateIdentity               = BIT10
TPM_DELEGATE_OwnerReadPubek                 = BIT9
TPM_DELEGATE_DisablePubekRead               = BIT8
TPM_DELEGATE_SetRedirection                 = BIT7
TPM_DELEGATE_FieldUpgrade                   = BIT6
TPM_DELEGATE_Delegate_UpdateVerification    = BIT5
TPM_DELEGATE_CreateCounter                  = BIT4
TPM_DELEGATE_ReleaseCounterOwner            = BIT3
TPM_DELEGATE_DelegateManage                 = BIT2
TPM_DELEGATE_Delegate_CreateOwnerDelegation = BIT1
TPM_DELEGATE_DAA_Sign                       = BIT0

TPM_KEY_DELEGATE_CMK_ConvertMigration       = BIT28
TPM_KEY_DELEGATE_TickStampBlob              = BIT27
TPM_KEY_DELEGATE_ChangeAuthAsymStart        = BIT26
TPM_KEY_DELEGATE_ChangeAuthAsymFinish       = BIT25
TPM_KEY_DELEGATE_CMK_CreateKey              = BIT24
TPM_KEY_DELEGATE_MigrateKey                 = BIT23
TPM_KEY_DELEGATE_LoadKey2                   = BIT22
TPM_KEY_DELEGATE_EstablishTransport         = BIT21
TPM_KEY_DELEGATE_ReleaseTransportSigned     = BIT20
TPM_KEY_DELEGATE_Quote2                     = BIT19
TPM_KEY_DELEGATE_Sealx                      = BIT18
TPM_KEY_DELEGATE_MakeIdentity               = BIT17
TPM_KEY_DELEGATE_ActivateIdentity           = BIT16
TPM_KEY_DELEGATE_GetAuditDigestSigned       = BIT15
TPM_KEY_DELEGATE_Sign                       = BIT14
TPM_KEY_DELEGATE_CertifyKey2                = BIT13
TPM_KEY_DELEGATE_CertifyKey                 = BIT12
TPM_KEY_DELEGATE_CreateWrapKey              = BIT11
TPM_KEY_DELEGATE_CMK_CreateBlob             = BIT10
TPM_KEY_DELEGATE_CreateMigrationBlob        = BIT9
TPM_KEY_DELEGATE_ConvertMigrationBlob       = BIT8
TPM_KEY_DELEGATE_CreateKeyDelegation        = BIT7
TPM_KEY_DELEGATE_ChangeAuth                 = BIT6
TPM_KEY_DELEGATE_GetPubKey                  = BIT5
TPM_KEY_DELEGATE_UnBind                     = BIT4
TPM_KEY_DELEGATE_Quote                      = BIT3
TPM_KEY_DELEGATE_Unseal                     = BIT2
TPM_KEY_DELEGATE_Seal                       = BIT1
TPM_KEY_DELEGATE_LoadKey                    = BIT0

TPM_DELEGATE_ADMIN_LOCK           = BIT1
TPM_FAMFLAG_ENABLE                = BIT0

class TPM_FAMILY_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

class TPM_FAMILY_TABLE_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_FAMILY_LABEL),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
    ("flags",             TPM_FAMILY_FLAGS)
  ]

TPM_NUM_FAMILY_TABLE_ENTRY_MIN = 8

class TPM_FAMILY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("famTableRow",     TPM_FAMILY_TABLE_ENTRY * TPM_NUM_FAMILY_TABLE_ENTRY_MIN)
  ]

class TPM_DELEGATE_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

class TPM_DELEGATE_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_DELEGATE_LABEL),
    ("pcrInfo",           TPM_PCR_INFO_SHORT),
    ("permissions",       TPM_DELEGATIONS),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
  ]

class TPM_DELEGATE_TABLE_ROW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("pub",       TPM_DELEGATE_PUBLIC),
    ("authValue", TPM_SECRET)
  ]

TPM_NUM_DELEGATE_TABLE_ENTRY_MIN = 2

class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("delRow", TPM_DELEGATE_TABLE_ROW * TPM_NUM_DELEGATE_TABLE_ENTRY_MIN)
  ]

class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authValue", TPM_SECRET)
  ]

class TPM_DELEGATE_OWNER_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

class TPM_DELEGATE_KEY_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("pubKeyDigest",    TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

TPM_FAMILY_CREATE                 = 0x00000001
TPM_FAMILY_ENABLE                 = 0x00000002
TPM_FAMILY_ADMIN                  = 0x00000003
TPM_FAMILY_INVALIDATE             = 0x00000004

TPM_CAP_ORD                     = 0x00000001
TPM_CAP_ALG                     = 0x00000002
TPM_CAP_PID                     = 0x00000003
TPM_CAP_FLAG                    = 0x00000004
TPM_CAP_PROPERTY                = 0x00000005
TPM_CAP_VERSION                 = 0x00000006
TPM_CAP_KEY_HANDLE              = 0x00000007
TPM_CAP_CHECK_LOADED            = 0x00000008
TPM_CAP_SYM_MODE                = 0x00000009
TPM_CAP_KEY_STATUS              = 0x0000000C
TPM_CAP_NV_LIST                 = 0x0000000D
TPM_CAP_MFR                     = 0x00000010
TPM_CAP_NV_INDEX                = 0x00000011
TPM_CAP_TRANS_ALG               = 0x00000012
TPM_CAP_HANDLE                  = 0x00000014
TPM_CAP_TRANS_ES                = 0x00000015
TPM_CAP_AUTH_ENCRYPT            = 0x00000017
TPM_CAP_SELECT_SIZE             = 0x00000018
TPM_CAP_VERSION_VAL             = 0x0000001A

TPM_CAP_FLAG_PERMANENT          = 0x00000108
TPM_CAP_FLAG_VOLATILE           = 0x00000109

TPM_CAP_PROP_PCR                = 0x00000101
TPM_CAP_PROP_DIR                = 0x00000102
TPM_CAP_PROP_MANUFACTURER       = 0x00000103
TPM_CAP_PROP_KEYS               = 0x00000104
TPM_CAP_PROP_MIN_COUNTER        = 0x00000107
TPM_CAP_PROP_AUTHSESS           = 0x0000010A
TPM_CAP_PROP_TRANSESS           = 0x0000010B
TPM_CAP_PROP_COUNTERS           = 0x0000010C
TPM_CAP_PROP_MAX_AUTHSESS       = 0x0000010D
TPM_CAP_PROP_MAX_TRANSESS       = 0x0000010E
TPM_CAP_PROP_MAX_COUNTERS       = 0x0000010F
TPM_CAP_PROP_MAX_KEYS           = 0x00000110
TPM_CAP_PROP_OWNER              = 0x00000111
TPM_CAP_PROP_CONTEXT            = 0x00000112
TPM_CAP_PROP_MAX_CONTEXT        = 0x00000113
TPM_CAP_PROP_FAMILYROWS         = 0x00000114
TPM_CAP_PROP_TIS_TIMEOUT        = 0x00000115
TPM_CAP_PROP_STARTUP_EFFECT     = 0x00000116
TPM_CAP_PROP_DELEGATE_ROW       = 0x00000117
TPM_CAP_PROP_DAA_MAX            = 0x00000119
CAP_PROP_SESSION_DAA            = 0x0000011A
TPM_CAP_PROP_CONTEXT_DIST       = 0x0000011B
TPM_CAP_PROP_DAA_INTERRUPT      = 0x0000011C
TPM_CAP_PROP_SESSIONS           = 0x0000011D
TPM_CAP_PROP_MAX_SESSIONS       = 0x0000011E
TPM_CAP_PROP_CMK_RESTRICTION    = 0x0000011F
TPM_CAP_PROP_DURATION           = 0x00000120
TPM_CAP_PROP_ACTIVE_COUNTER     = 0x00000122
TPM_CAP_PROP_MAX_NV_AVAILABLE   = 0x00000123
TPM_CAP_PROP_INPUT_BUFFER       = 0x00000124

TPM_SET_PERM_FLAGS              = 0x00000001
TPM_SET_PERM_DATA               = 0x00000002
TPM_SET_STCLEAR_FLAGS           = 0x00000003
TPM_SET_STCLEAR_DATA            = 0x00000004
TPM_SET_STANY_FLAGS             = 0x00000005
TPM_SET_STANY_DATA              = 0x00000006

class TPM_CAP_VERSION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("version",             TPM_VERSION),
    ("specLevel",           UINT16),
    ("errataRev",           UINT8),
    ("tpmVendorID",         UINT8 * 4),
    ("vendorSpecificSize",  UINT16),
    ("vendorSpecific",      POINTER (UINT8))
  ]

class TPM_DA_ACTION_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("actions", UINT32)
  ]

TPM_DA_ACTION_FAILURE_MODE     = 1 << 3
TPM_DA_ACTION_DEACTIVATE       = 1 << 2
TPM_DA_ACTION_DISABLE          = 1 << 1
TPM_DA_ACTION_TIMEOUT          = 1 << 0

class TPM_DA_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("currentCount",      UINT16),
    ("thresholdCount",    UINT16),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("actionDependValue", UINT32),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

class TPM_DA_INFO_LIMITED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

TPM_DA_STATE_INACTIVE          = UINT8(0x00).value
TPM_DA_STATE_ACTIVE            = UINT8(0x01).value

TPM_DAA_SIZE_r0                = 43
TPM_DAA_SIZE_r1                = 43
TPM_DAA_SIZE_r2                = 128
TPM_DAA_SIZE_r3                = 168
TPM_DAA_SIZE_r4                = 219
TPM_DAA_SIZE_NT                = 20
TPM_DAA_SIZE_v0                = 128
TPM_DAA_SIZE_v1                = 192
TPM_DAA_SIZE_NE                = 256
TPM_DAA_SIZE_w                 = 256
TPM_DAA_SIZE_issuerModulus     = 256

TPM_DAA_power0                 = 104
TPM_DAA_power1                 = 1024

class TPM_DAA_ISSUER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digest_R0",     TPM_DIGEST),
    ("DAA_digest_R1",     TPM_DIGEST),
    ("DAA_digest_S0",     TPM_DIGEST),
    ("DAA_digest_S1",     TPM_DIGEST),
    ("DAA_digest_n",      TPM_DIGEST),
    ("DAA_digest_gamma",  TPM_DIGEST),
    ("DAA_generic_q",     UINT8 * 26)
  ]

class TPM_DAA_TPM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestIssuer",  TPM_DIGEST),
    ("DAA_digest_v0",     TPM_DIGEST),
    ("DAA_digest_v1",     TPM_DIGEST),
    ("DAA_rekey",         TPM_DIGEST),
    ("DAA_count",         UINT32)
  ]

class TPM_DAA_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestContext", TPM_DIGEST),
    ("DAA_digest",        TPM_DIGEST),
    ("DAA_contextSeed",   TPM_DAA_CONTEXT_SEED),
    ("DAA_scratch",       UINT8 * 256),
    ("DAA_stage",         UINT8)
  ]

class TPM_DAA_JOINDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DAA_join_u0",   UINT8 * 128),
    ("DAA_join_u1",   UINT8 * 138),
    ("DAA_digest_n0", TPM_DIGEST)
  ]

class TPM_DAA_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("label",           UINT8 * 16),
    ("blobIntegrity",   TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

class TPM_DAA_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

TPM_REDIR_GPIO              = 0x00000001

class TPM_RQU_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("paramSize", UINT32),
    ("ordinal",   TPM_COMMAND_CODE)
  ]

class TPM_RSP_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("paramSize",   UINT32),
    ("returnCode",  TPM_RESULT)
  ]
 