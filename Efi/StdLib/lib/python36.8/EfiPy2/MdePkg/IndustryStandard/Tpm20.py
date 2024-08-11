# Tpm20.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm20
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard    import *
from EfiPy2.MdePkg.IndustryStandard   import Tpm12

SHA1_DIGEST_SIZE = 20
SHA1_BLOCK_SIZE  = 64

SHA256_DIGEST_SIZE = 32
SHA256_BLOCK_SIZE  = 64

SHA384_DIGEST_SIZE = 48
SHA384_BLOCK_SIZE  = 128

SHA512_DIGEST_SIZE = 64
SHA512_BLOCK_SIZE  = 128

SM3_256_DIGEST_SIZE = 32
SM3_256_BLOCK_SIZE  = 64

MAX_SESSION_NUMBER = 3

YES   = 1
NO    = 0
SET   = 1
CLEAR = 0

MAX_RSA_KEY_BITS  = 2048
MAX_RSA_KEY_BYTES = ((MAX_RSA_KEY_BITS + 7) // 8)

MAX_ECC_KEY_BITS  = 256
MAX_ECC_KEY_BYTES = ((MAX_ECC_KEY_BITS + 7) // 8)

MAX_AES_KEY_BITS         = 128
MAX_AES_BLOCK_SIZE_BYTES = 16
MAX_AES_KEY_BYTES        = ((MAX_AES_KEY_BITS + 7) // 8)

MAX_SM4_KEY_BITS         = 128
MAX_SM4_BLOCK_SIZE_BYTES = 16
MAX_SM4_KEY_BYTES        = ((MAX_SM4_KEY_BITS + 7) // 8)

MAX_SYM_KEY_BITS   = MAX_AES_KEY_BITS
MAX_SYM_KEY_BYTES  = MAX_AES_KEY_BYTES
MAX_SYM_BLOCK_SIZE = MAX_AES_BLOCK_SIZE_BYTES

BSIZE               = UINT16
BUFFER_ALIGNMENT    = 4
IMPLEMENTATION_PCR  = 24
PLATFORM_PCR        = 24
DRTM_PCR            = 17
NUM_LOCALITIES      = 5
MAX_HANDLE_NUM      = 3
MAX_ACTIVE_SESSIONS = 64
CONTEXT_SLOT        = UINT16
CONTEXT_COUNTER     = UINT64
MAX_LOADED_SESSIONS           = 3
MAX_SESSION_NUM               = 3
MAX_LOADED_OBJECTS            = 3
MIN_EVICT_OBJECTS             = 2
PCR_SELECT_MIN                = ((PLATFORM_PCR + 7) // 8)
PCR_SELECT_MAX                = ((IMPLEMENTATION_PCR + 7) // 8)
NUM_POLICY_PCR_GROUP          = 1
NUM_AUTHVALUE_PCR_GROUP       = 1
MAX_CONTEXT_SIZE              = 4000
MAX_DIGEST_BUFFER             = 1024
MAX_NV_INDEX_SIZE             = 1024
MAX_CAP_BUFFER                = 1024
NV_MEMORY_SIZE                = 16384
NUM_STATIC_PCR                = 16
MAX_ALG_LIST_SIZE             = 64
TIMER_PRESCALE                = 100000
PRIMARY_SEED_SIZE             = 32
TPM_ALG_AES                   = 0x0006
CONTEXT_ENCRYPT_ALG           = TPM_ALG_AES
CONTEXT_ENCRYPT_KEY_BITS      = MAX_SYM_KEY_BITS
CONTEXT_ENCRYPT_KEY_BYTES     = ((CONTEXT_ENCRYPT_KEY_BITS + 7) // 8)
TPM_ALG_SHA256                = 0x000B
CONTEXT_INTEGRITY_HASH_ALG    = TPM_ALG_SHA256
CONTEXT_INTEGRITY_HASH_SIZE   = SHA256_DIGEST_SIZE
PROOF_SIZE                    = CONTEXT_INTEGRITY_HASH_SIZE
NV_CLOCK_UPDATE_INTERVAL      = 12
NUM_POLICY_PCR                = 1
MAX_COMMAND_SIZE              = 4096
MAX_RESPONSE_SIZE             = 4096
ORDERLY_BITS                  = 8
MAX_ORDERLY_COUNT             = ((1 << ORDERLY_BITS) - 1)
TPM_ALG_FIRST                 = 0x0001
ALG_ID_FIRST                  = TPM_ALG_FIRST
TPM_ALG_LAST                  = 0x0044
ALG_ID_LAST                   = TPM_ALG_LAST
MAX_SYM_DATA                  = 128
MAX_RNG_ENTROPY_SIZE          = 64
RAM_INDEX_SPACE               = 512
RSA_DEFAULT_PUBLIC_EXPONENT   = 0x00010001
CRT_FORMAT_RSA                = YES
PRIVATE_VENDOR_SPECIFIC_BYTES = ((MAX_RSA_KEY_BYTES // 2) * ( 3 + CRT_FORMAT_RSA * 2))

# MAX_CAP_DATA        = (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))
# MAX_CAP_ALGS        = (MAX_CAP_DATA // sizeof(TPMS_ALG_PROPERTY))
# MAX_CAP_HANDLES     = (MAX_CAP_DATA // sizeof(Tpm12.TPM_HANDLE))
# MAX_CAP_CC          = (MAX_CAP_DATA // sizeof(TPM_CC))
# MAX_TPM_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PROPERTY))
# MAX_PCR_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PCR_SELECT))
# MAX_ECC_CURVES      = (MAX_CAP_DATA // sizeof(TPM_ECC_CURVE))

HASH_COUNT  = 5

BYTE = UINT8

TPM_AUTHORIZATION_SIZE  = UINT32
TPM_PARAMETER_SIZE      = UINT32
TPM_KEY_SIZE            = UINT16
TPM_KEY_BITS            = UINT16

TPM_GENERATED       = UINT32
TPM_GENERATED_VALUE = 0xff544347

TPM_ALG_ID          = UINT16

TPM_ALG_ERROR       = 0x0000
TPM_ALG_SHA1        = 0x0004
TPM_ALG_KEYEDHASH   = 0x0008
# TPM_ALG_SHA256          = 0x000B
TPM_ALG_SHA384          = 0x000C
TPM_ALG_SHA512          = 0x000D
TPM_ALG_NULL            = 0x0010
TPM_ALG_SM3_256         = 0x0012
TPM_ALG_SM4             = 0x0013
TPM_ALG_RSASSA          = 0x0014
TPM_ALG_RSAES           = 0x0015
TPM_ALG_RSAPSS          = 0x0016
TPM_ALG_OAEP            = 0x0017
TPM_ALG_ECDSA           = 0x0018
TPM_ALG_ECDH            = 0x0019
TPM_ALG_ECDAA           = 0x001A
TPM_ALG_SM2             = 0x001B
TPM_ALG_ECSCHNORR       = 0x001C
TPM_ALG_ECMQV           = 0x001D
TPM_ALG_KDF1_SP800_56a  = 0x0020
TPM_ALG_KDF2            = 0x0021
TPM_ALG_KDF1_SP800_108  = 0x0022
TPM_ALG_ECC             = 0x0023
TPM_ALG_SYMCIPHER       = 0x0025
TPM_ALG_CTR             = 0x0040
TPM_ALG_OFB             = 0x0041
TPM_ALG_CBC             = 0x0042
TPM_ALG_CFB             = 0x0043
TPM_ALG_ECB             = 0x0044
# TPM_ALG_LAST            = 0x0044

TPM_ECC_CURVE = UINT16
TPM_ECC_NONE       = 0x0000
TPM_ECC_NIST_P192  = 0x0001
TPM_ECC_NIST_P224  = 0x0002
TPM_ECC_NIST_P256  = 0x0003
TPM_ECC_NIST_P384  = 0x0004
TPM_ECC_NIST_P521  = 0x0005
TPM_ECC_BN_P256    = 0x0010
TPM_ECC_BN_P638    = 0x0011
TPM_ECC_SM2_P256   = 0x0020

TPM_CC                            = UINT32

TPM_CC_FIRST                      = 0x0000011F
TPM_CC_PP_FIRST                   = 0x0000011F
TPM_CC_NV_UndefineSpaceSpecial    = 0x0000011F
TPM_CC_EvictControl               = 0x00000120
TPM_CC_HierarchyControl           = 0x00000121
TPM_CC_NV_UndefineSpace           = 0x00000122
TPM_CC_ChangeEPS                  = 0x00000124
TPM_CC_ChangePPS                  = 0x00000125
TPM_CC_Clear                      = 0x00000126
TPM_CC_ClearControl               = 0x00000127
TPM_CC_ClockSet                   = 0x00000128
TPM_CC_HierarchyChangeAuth        = 0x00000129
TPM_CC_NV_DefineSpace             = 0x0000012A
TPM_CC_PCR_Allocate               = 0x0000012B
TPM_CC_PCR_SetAuthPolicy          = 0x0000012C
TPM_CC_PP_Commands                = 0x0000012D
TPM_CC_SetPrimaryPolicy           = 0x0000012E
TPM_CC_FieldUpgradeStart          = 0x0000012F
TPM_CC_ClockRateAdjust            = 0x00000130
TPM_CC_CreatePrimary              = 0x00000131
TPM_CC_NV_GlobalWriteLock         = 0x00000132
TPM_CC_PP_LAST                    = 0x00000132
TPM_CC_GetCommandAuditDigest      = 0x00000133
TPM_CC_NV_Increment               = 0x00000134
TPM_CC_NV_SetBits                 = 0x00000135
TPM_CC_NV_Extend                  = 0x00000136
TPM_CC_NV_Write                   = 0x00000137
TPM_CC_NV_WriteLock               = 0x00000138
TPM_CC_DictionaryAttackLockReset  = 0x00000139
TPM_CC_DictionaryAttackParameters = 0x0000013A
TPM_CC_NV_ChangeAuth              = 0x0000013B
TPM_CC_PCR_Event                  = 0x0000013C
TPM_CC_PCR_Reset                  = 0x0000013D
TPM_CC_SequenceComplete           = 0x0000013E
TPM_CC_SetAlgorithmSet            = 0x0000013F
TPM_CC_SetCommandCodeAuditStatus  = 0x00000140
TPM_CC_FieldUpgradeData           = 0x00000141
TPM_CC_IncrementalSelfTest        = 0x00000142
TPM_CC_SelfTest                   = 0x00000143
TPM_CC_Startup                    = 0x00000144
TPM_CC_Shutdown                   = 0x00000145
TPM_CC_StirRandom                 = 0x00000146
TPM_CC_ActivateCredential         = 0x00000147
TPM_CC_Certify                    = 0x00000148
TPM_CC_PolicyNV                   = 0x00000149
TPM_CC_CertifyCreation            = 0x0000014A
TPM_CC_Duplicate                  = 0x0000014B
TPM_CC_GetTime                    = 0x0000014C
TPM_CC_GetSessionAuditDigest      = 0x0000014D
TPM_CC_NV_Read                    = 0x0000014E
TPM_CC_NV_ReadLock                = 0x0000014F
TPM_CC_ObjectChangeAuth           = 0x00000150
TPM_CC_PolicySecret               = 0x00000151
TPM_CC_Rewrap                     = 0x00000152
TPM_CC_Create                     = 0x00000153
TPM_CC_ECDH_ZGen                  = 0x00000154
TPM_CC_HMAC                       = 0x00000155
TPM_CC_Import                     = 0x00000156
TPM_CC_Load                       = 0x00000157
TPM_CC_Quote                      = 0x00000158
TPM_CC_RSA_Decrypt                = 0x00000159
TPM_CC_HMAC_Start                 = 0x0000015B
TPM_CC_SequenceUpdate             = 0x0000015C
TPM_CC_Sign                       = 0x0000015D
TPM_CC_Unseal                     = 0x0000015E
TPM_CC_PolicySigned               = 0x00000160
TPM_CC_ContextLoad                = 0x00000161
TPM_CC_ContextSave                = 0x00000162
TPM_CC_ECDH_KeyGen                = 0x00000163
TPM_CC_EncryptDecrypt             = 0x00000164
TPM_CC_FlushContext               = 0x00000165
TPM_CC_LoadExternal               = 0x00000167
TPM_CC_MakeCredential             = 0x00000168
TPM_CC_NV_ReadPublic              = 0x00000169
TPM_CC_PolicyAuthorize            = 0x0000016A
TPM_CC_PolicyAuthValue            = 0x0000016B
TPM_CC_PolicyCommandCode          = 0x0000016C
TPM_CC_PolicyCounterTimer         = 0x0000016D
TPM_CC_PolicyCpHash               = 0x0000016E
TPM_CC_PolicyLocality             = 0x0000016F
TPM_CC_PolicyNameHash             = 0x00000170
TPM_CC_PolicyOR                   = 0x00000171
TPM_CC_PolicyTicket               = 0x00000172
TPM_CC_ReadPublic                 = 0x00000173
TPM_CC_RSA_Encrypt                = 0x00000174
TPM_CC_StartAuthSession           = 0x00000176
TPM_CC_VerifySignature            = 0x00000177
TPM_CC_ECC_Parameters             = 0x00000178
TPM_CC_FirmwareRead               = 0x00000179
TPM_CC_GetCapability              = 0x0000017A
TPM_CC_GetRandom                  = 0x0000017B
TPM_CC_GetTestResult              = 0x0000017C
TPM_CC_Hash                       = 0x0000017D
TPM_CC_PCR_Read                   = 0x0000017E
TPM_CC_PolicyPCR                  = 0x0000017F
TPM_CC_PolicyRestart              = 0x00000180
TPM_CC_ReadClock                  = 0x00000181
TPM_CC_PCR_Extend                 = 0x00000182
TPM_CC_PCR_SetAuthValue           = 0x00000183
TPM_CC_NV_Certify                 = 0x00000184
TPM_CC_EventSequenceComplete      = 0x00000185
TPM_CC_HashSequenceStart          = 0x00000186
TPM_CC_PolicyPhysicalPresence     = 0x00000187
TPM_CC_PolicyDuplicationSelect    = 0x00000188
TPM_CC_PolicyGetDigest            = 0x00000189
TPM_CC_TestParms                  = 0x0000018A
TPM_CC_Commit                     = 0x0000018B
TPM_CC_PolicyPassword             = 0x0000018C
TPM_CC_ZGen_2Phase                = 0x0000018D
TPM_CC_EC_Ephemeral               = 0x0000018E
TPM_CC_LAST                       = 0x0000018E

TPM_RC                   = UINT32
TPM_RC_SUCCESS           = 0x000
TPM_RC_BAD_TAG           = 0x030
RC_VER1                  = 0x100
TPM_RC_INITIALIZE        = RC_VER1 + 0x000
TPM_RC_FAILURE           = RC_VER1 + 0x001
TPM_RC_SEQUENCE          = RC_VER1 + 0x003
TPM_RC_PRIVATE           = RC_VER1 + 0x00B
TPM_RC_HMAC              = RC_VER1 + 0x019
TPM_RC_DISABLED          = RC_VER1 + 0x020
TPM_RC_EXCLUSIVE         = RC_VER1 + 0x021
TPM_RC_AUTH_TYPE         = RC_VER1 + 0x024
TPM_RC_AUTH_MISSING      = RC_VER1 + 0x025
TPM_RC_POLICY            = RC_VER1 + 0x026
TPM_RC_PCR               = RC_VER1 + 0x027
TPM_RC_PCR_CHANGED       = RC_VER1 + 0x028
TPM_RC_UPGRADE           = RC_VER1 + 0x02D
TPM_RC_TOO_MANY_CONTEXTS = RC_VER1 + 0x02E
TPM_RC_AUTH_UNAVAILABLE  = RC_VER1 + 0x02F
TPM_RC_REBOOT            = RC_VER1 + 0x030
TPM_RC_UNBALANCED        = RC_VER1 + 0x031
TPM_RC_COMMAND_SIZE      = RC_VER1 + 0x042
TPM_RC_COMMAND_CODE      = RC_VER1 + 0x043
TPM_RC_AUTHSIZE          = RC_VER1 + 0x044
TPM_RC_AUTH_CONTEXT      = RC_VER1 + 0x045
TPM_RC_NV_RANGE          = RC_VER1 + 0x046
TPM_RC_NV_SIZE           = RC_VER1 + 0x047
TPM_RC_NV_LOCKED         = RC_VER1 + 0x048
TPM_RC_NV_AUTHORIZATION  = RC_VER1 + 0x049
TPM_RC_NV_UNINITIALIZED  = RC_VER1 + 0x04A
TPM_RC_NV_SPACE          = RC_VER1 + 0x04B
TPM_RC_NV_DEFINED        = RC_VER1 + 0x04C
TPM_RC_BAD_CONTEXT       = RC_VER1 + 0x050
TPM_RC_CPHASH            = RC_VER1 + 0x051
TPM_RC_PARENT            = RC_VER1 + 0x052
TPM_RC_NEEDS_TEST        = RC_VER1 + 0x053
TPM_RC_NO_RESULT         = RC_VER1 + 0x054
TPM_RC_SENSITIVE         = RC_VER1 + 0x055
RC_MAX_FM0               = RC_VER1 + 0x07F
RC_FMT1                  = 0x080
TPM_RC_ASYMMETRIC        = RC_FMT1 + 0x001
TPM_RC_ATTRIBUTES        = RC_FMT1 + 0x002
TPM_RC_HASH              = RC_FMT1 + 0x003
TPM_RC_VALUE             = RC_FMT1 + 0x004
TPM_RC_HIERARCHY         = RC_FMT1 + 0x005
TPM_RC_KEY_SIZE          = RC_FMT1 + 0x007
TPM_RC_MGF               = RC_FMT1 + 0x008
TPM_RC_MODE              = RC_FMT1 + 0x009
TPM_RC_TYPE              = RC_FMT1 + 0x00A
TPM_RC_HANDLE            = RC_FMT1 + 0x00B
TPM_RC_KDF               = RC_FMT1 + 0x00C
TPM_RC_RANGE             = RC_FMT1 + 0x00D
TPM_RC_AUTH_FAIL         = RC_FMT1 + 0x00E
TPM_RC_NONCE             = RC_FMT1 + 0x00F
TPM_RC_PP                = RC_FMT1 + 0x010
TPM_RC_SCHEME            = RC_FMT1 + 0x012
TPM_RC_SIZE              = RC_FMT1 + 0x015
TPM_RC_SYMMETRIC         = RC_FMT1 + 0x016
TPM_RC_TAG               = RC_FMT1 + 0x017
TPM_RC_SELECTOR          = RC_FMT1 + 0x018
TPM_RC_INSUFFICIENT      = RC_FMT1 + 0x01A
TPM_RC_SIGNATURE         = RC_FMT1 + 0x01B
TPM_RC_KEY               = RC_FMT1 + 0x01C
TPM_RC_POLICY_FAIL       = RC_FMT1 + 0x01D
TPM_RC_INTEGRITY         = RC_FMT1 + 0x01F
TPM_RC_TICKET            = RC_FMT1 + 0x020
TPM_RC_RESERVED_BITS     = RC_FMT1 + 0x021
TPM_RC_BAD_AUTH          = RC_FMT1 + 0x022
TPM_RC_EXPIRED           = RC_FMT1 + 0x023
TPM_RC_POLICY_CC         = RC_FMT1 + 0x024e
TPM_RC_BINDING           = RC_FMT1 + 0x025
TPM_RC_CURVE             = RC_FMT1 + 0x026
TPM_RC_ECC_POINT         = RC_FMT1 + 0x027
RC_WARN                  = 0x900
TPM_RC_CONTEXT_GAP       = RC_WARN + 0x001
TPM_RC_OBJECT_MEMORY     = RC_WARN + 0x002
TPM_RC_SESSION_MEMORY    = RC_WARN + 0x003
TPM_RC_MEMORY            = RC_WARN + 0x004
TPM_RC_SESSION_HANDLES   = RC_WARN + 0x005
TPM_RC_OBJECT_HANDLES    = RC_WARN + 0x006
TPM_RC_LOCALITY          = RC_WARN + 0x007
TPM_RC_YIELDED           = RC_WARN + 0x008
TPM_RC_CANCELED          = RC_WARN + 0x009
TPM_RC_TESTING           = RC_WARN + 0x00A
TPM_RC_REFERENCE_H0      = RC_WARN + 0x010
TPM_RC_REFERENCE_H1      = RC_WARN + 0x011
TPM_RC_REFERENCE_H2      = RC_WARN + 0x012
TPM_RC_REFERENCE_H3      = RC_WARN + 0x013
TPM_RC_REFERENCE_H4      = RC_WARN + 0x014
TPM_RC_REFERENCE_H5      = RC_WARN + 0x015
TPM_RC_REFERENCE_H6      = RC_WARN + 0x016
TPM_RC_REFERENCE_S0      = RC_WARN + 0x018
TPM_RC_REFERENCE_S1      = RC_WARN + 0x019
TPM_RC_REFERENCE_S2      = RC_WARN + 0x01A
TPM_RC_REFERENCE_S3      = RC_WARN + 0x01B
TPM_RC_REFERENCE_S4      = RC_WARN + 0x01C
TPM_RC_REFERENCE_S5      = RC_WARN + 0x01D
TPM_RC_REFERENCE_S6      = RC_WARN + 0x01E
TPM_RC_NV_RATE           = RC_WARN + 0x020
TPM_RC_LOCKOUT           = RC_WARN + 0x021
TPM_RC_RETRY             = RC_WARN + 0x022
TPM_RC_NV_UNAVAILABLE    = RC_WARN + 0x023
TPM_RC_NOT_USED          = RC_WARN + 0x7F
TPM_RC_H                 = 0x000
TPM_RC_P                 = 0x040
TPM_RC_S                 = 0x800
TPM_RC_1                 = 0x100
TPM_RC_2                 = 0x200
TPM_RC_3                 = 0x300
TPM_RC_4                 = 0x400
TPM_RC_5                 = 0x500
TPM_RC_6                 = 0x600
TPM_RC_7                 = 0x700
TPM_RC_8                 = 0x800
TPM_RC_9                 = 0x900
TPM_RC_A                 = 0xA00
TPM_RC_B                 = 0xB00
TPM_RC_C                 = 0xC00
TPM_RC_D                 = 0xD00
TPM_RC_E                 = 0xE00
TPM_RC_F                 = 0xF00
TPM_RC_N_MASK            = 0xF00

TPM_CLOCK_ADJUST        = INT8
TPM_CLOCK_COARSE_SLOWER = -3
TPM_CLOCK_MEDIUM_SLOWER = -2
TPM_CLOCK_FINE_SLOWER   = -1
TPM_CLOCK_NO_CHANGE     = 0
TPM_CLOCK_FINE_FASTER   = 1
TPM_CLOCK_MEDIUM_FASTER = 2
TPM_CLOCK_COARSE_FASTER = 3

TPM_EO             = UINT16
TPM_EO_EQ          = 0x0000
TPM_EO_NEQ         = 0x0001
TPM_EO_SIGNED_GT   = 0x0002
TPM_EO_UNSIGNED_GT = 0x0003
TPM_EO_SIGNED_LT   = 0x0004
TPM_EO_UNSIGNED_LT = 0x0005
TPM_EO_SIGNED_GE   = 0x0006
TPM_EO_UNSIGNED_GE = 0x0007
TPM_EO_SIGNED_LE   = 0x0008
TPM_EO_UNSIGNED_LE = 0x0009
TPM_EO_BITSET      = 0x000A
TPM_EO_BITCLEAR    = 0x000B

TPM_ST                      = UINT16
TPM_ST_RSP_COMMAND          = 0x00C4
TPM_ST_NULL                 = 0X8000
TPM_ST_NO_SESSIONS          = 0x8001
TPM_ST_SESSIONS             = 0x8002
TPM_ST_ATTEST_NV            = 0x8014
TPM_ST_ATTEST_COMMAND_AUDIT = 0x8015
TPM_ST_ATTEST_SESSION_AUDIT = 0x8016
TPM_ST_ATTEST_CERTIFY       = 0x8017
TPM_ST_ATTEST_QUOTE         = 0x8018
TPM_ST_ATTEST_TIME          = 0x8019
TPM_ST_ATTEST_CREATION      = 0x801A
TPM_ST_CREATION             = 0x8021
TPM_ST_VERIFIED             = 0x8022
TPM_ST_AUTH_SECRET          = 0x8023
TPM_ST_HASHCHECK            = 0x8024
TPM_ST_AUTH_SIGNED          = 0x8025
TPM_ST_FU_MANIFEST          = 0x8029

TPM_SU       = UINT16
TPM_SU_CLEAR = 0x0000
TPM_SU_STATE = 0x0001

TPM_SE        = UINT8
TPM_SE_HMAC   = 0x00
TPM_SE_POLICY = 0x01
TPM_SE_TRIAL  = 0x03

TPM_CAP                 = UINT32

TPM_CAP_FIRST           = 0x00000000
TPM_CAP_ALGS            = 0x00000000
TPM_CAP_HANDLES         = 0x00000001
TPM_CAP_COMMANDS        = 0x00000002
TPM_CAP_PP_COMMANDS     = 0x00000003
TPM_CAP_AUDIT_COMMANDS  = 0x00000004
TPM_CAP_PCRS            = 0x00000005
TPM_CAP_TPM_PROPERTIES  = 0x00000006
TPM_CAP_PCR_PROPERTIES  = 0x00000007
TPM_CAP_ECC_CURVES      = 0x00000008
TPM_CAP_LAST            = 0x00000008
TPM_CAP_VENDOR_PROPERTY = 0x00000100

TPM_PT                     = UINT32
TPM_PT_NONE                = 0x00000000
PT_GROUP                   = 0x00000100
PT_FIXED                   = PT_GROUP * 1
TPM_PT_FAMILY_INDICATOR    = PT_FIXED + 0
TPM_PT_LEVEL               = PT_FIXED + 1
TPM_PT_REVISION            = PT_FIXED + 2
TPM_PT_DAY_OF_YEAR         = PT_FIXED + 3
TPM_PT_YEAR                = PT_FIXED + 4
TPM_PT_MANUFACTURER        = PT_FIXED + 5
TPM_PT_VENDOR_STRING_1     = PT_FIXED + 6
TPM_PT_VENDOR_STRING_2     = PT_FIXED + 7
TPM_PT_VENDOR_STRING_3     = PT_FIXED + 8
TPM_PT_VENDOR_STRING_4     = PT_FIXED + 9
TPM_PT_VENDOR_TPM_TYPE     = PT_FIXED + 10
TPM_PT_FIRMWARE_VERSION_1  = PT_FIXED + 11
TPM_PT_FIRMWARE_VERSION_2  = PT_FIXED + 12
TPM_PT_INPUT_BUFFER        = PT_FIXED + 13
TPM_PT_HR_TRANSIENT_MIN    = PT_FIXED + 14
TPM_PT_HR_PERSISTENT_MIN   = PT_FIXED + 15
TPM_PT_HR_LOADED_MIN       = PT_FIXED + 16
TPM_PT_ACTIVE_SESSIONS_MAX = PT_FIXED + 17
TPM_PT_PCR_COUNT           = PT_FIXED + 18
TPM_PT_PCR_SELECT_MIN      = PT_FIXED + 19
TPM_PT_CONTEXT_GAP_MAX     = PT_FIXED + 20
TPM_PT_NV_COUNTERS_MAX     = PT_FIXED + 22
TPM_PT_NV_INDEX_MAX        = PT_FIXED + 23
TPM_PT_MEMORY              = PT_FIXED + 24
TPM_PT_CLOCK_UPDATE        = PT_FIXED + 25
TPM_PT_CONTEXT_HASH        = PT_FIXED + 26
TPM_PT_CONTEXT_SYM         = PT_FIXED + 27
TPM_PT_CONTEXT_SYM_SIZE    = PT_FIXED + 28
TPM_PT_ORDERLY_COUNT       = PT_FIXED + 29
TPM_PT_MAX_COMMAND_SIZE    = PT_FIXED + 30
TPM_PT_MAX_RESPONSE_SIZE   = PT_FIXED + 31
TPM_PT_MAX_DIGEST          = PT_FIXED + 32
TPM_PT_MAX_OBJECT_CONTEXT  = PT_FIXED + 33
TPM_PT_MAX_SESSION_CONTEXT = PT_FIXED + 34
TPM_PT_PS_FAMILY_INDICATOR = PT_FIXED + 35
TPM_PT_PS_LEVEL            = PT_FIXED + 36
TPM_PT_PS_REVISION         = PT_FIXED + 37
TPM_PT_PS_DAY_OF_YEAR      = PT_FIXED + 38
TPM_PT_PS_YEAR             = PT_FIXED + 39
TPM_PT_SPLIT_MAX           = PT_FIXED + 40
TPM_PT_TOTAL_COMMANDS      = PT_FIXED + 41
TPM_PT_LIBRARY_COMMANDS    = PT_FIXED + 42
TPM_PT_VENDOR_COMMANDS     = PT_FIXED + 43
PT_VAR                     = PT_GROUP * 2
TPM_PT_PERMANENT           = PT_VAR + 0
TPM_PT_STARTUP_CLEAR       = PT_VAR + 1
TPM_PT_HR_NV_INDEX         = PT_VAR + 2
TPM_PT_HR_LOADED           = PT_VAR + 3
TPM_PT_HR_LOADED_AVAIL     = PT_VAR + 4
TPM_PT_HR_ACTIVE           = PT_VAR + 5
TPM_PT_HR_ACTIVE_AVAIL     = PT_VAR + 6
TPM_PT_HR_TRANSIENT_AVAIL  = PT_VAR + 7
TPM_PT_HR_PERSISTENT       = PT_VAR + 8
TPM_PT_HR_PERSISTENT_AVAIL = PT_VAR + 9
TPM_PT_NV_COUNTERS         = PT_VAR + 10
TPM_PT_NV_COUNTERS_AVAIL   = PT_VAR + 11
TPM_PT_ALGORITHM_SET       = PT_VAR + 12
TPM_PT_LOADED_CURVES       = PT_VAR + 13
TPM_PT_LOCKOUT_COUNTER     = PT_VAR + 14
TPM_PT_MAX_AUTH_FAIL       = PT_VAR + 15
TPM_PT_LOCKOUT_INTERVAL    = PT_VAR + 16
TPM_PT_LOCKOUT_RECOVERY    = PT_VAR + 17
TPM_PT_NV_WRITE_RECOVERY   = PT_VAR + 18
TPM_PT_AUDIT_COUNTER_0     = PT_VAR + 19
TPM_PT_AUDIT_COUNTER_1     = PT_VAR + 20

TPM_PT_PCR              = UINT32
TPM_PT_PCR_FIRST        = 0x00000000
TPM_PT_PCR_SAVE         = 0x00000000
TPM_PT_PCR_EXTEND_L0    = 0x00000001
TPM_PT_PCR_RESET_L0     = 0x00000002
TPM_PT_PCR_EXTEND_L1    = 0x00000003
TPM_PT_PCR_RESET_L1     = 0x00000004
TPM_PT_PCR_EXTEND_L2    = 0x00000005
TPM_PT_PCR_RESET_L2     = 0x00000006
TPM_PT_PCR_EXTEND_L3    = 0x00000007
TPM_PT_PCR_RESET_L3     = 0x00000008
TPM_PT_PCR_EXTEND_L4    = 0x00000009
TPM_PT_PCR_RESET_L4     = 0x0000000A
TPM_PT_PCR_NO_INCREMENT = 0x00000011
TPM_PT_PCR_DRTM_RESET   = 0x00000012
TPM_PT_PCR_POLICY       = 0x00000013
TPM_PT_PCR_AUTH         = 0x00000014
TPM_PT_PCR_LAST         = 0x00000014

TPM_PS                = UINT32
TPM_PS_MAIN           = 0x00000000
TPM_PS_PC             = 0x00000001
TPM_PS_PDA            = 0x00000002
TPM_PS_CELL_PHONE     = 0x00000003
TPM_PS_SERVER         = 0x00000004
TPM_PS_PERIPHERAL     = 0x00000005
TPM_PS_TSS            = 0x00000006
TPM_PS_STORAGE        = 0x00000007
TPM_PS_AUTHENTICATION = 0x00000008
TPM_PS_EMBEDDED       = 0x00000009
TPM_PS_HARDCOPY       = 0x0000000A
TPM_PS_INFRASTRUCTURE = 0x0000000B
TPM_PS_VIRTUALIZATION = 0x0000000C
TPM_PS_TNC            = 0x0000000D
TPM_PS_MULTI_TENANT   = 0x0000000E
TPM_PS_TC             = 0x0000000F

TPM_HT                = UINT8
TPM_HT_PCR            = 0x00
TPM_HT_NV_INDEX       = 0x01
TPM_HT_HMAC_SESSION   = 0x02
TPM_HT_LOADED_SESSION = 0x02
TPM_HT_POLICY_SESSION = 0x03
TPM_HT_ACTIVE_SESSION = 0x03
TPM_HT_PERMANENT      = 0x40
TPM_HT_TRANSIENT      = 0x80
TPM_HT_PERSISTENT     = 0x81

TPM_RH             = UINT32
TPM_RH_FIRST       = 0x40000000
TPM_RH_SRK         = 0x40000000
TPM_RH_OWNER       = 0x40000001
TPM_RH_REVOKE      = 0x40000002
TPM_RH_TRANSPORT   = 0x40000003
TPM_RH_OPERATOR    = 0x40000004
TPM_RH_ADMIN       = 0x40000005
TPM_RH_EK          = 0x40000006
TPM_RH_NULL        = 0x40000007
TPM_RH_UNASSIGNED  = 0x40000008
TPM_RS_PW          = 0x40000009
TPM_RH_LOCKOUT     = 0x4000000A
TPM_RH_ENDORSEMENT = 0x4000000B
TPM_RH_PLATFORM    = 0x4000000C
TPM_RH_LAST        = 0x4000000C

TPM_HC               = Tpm12.TPM_HANDLE
HR_HANDLE_MASK       = 0x00FFFFFF
HR_RANGE_MASK        = 0xFF000000
HR_SHIFT             = 24
HR_PCR               = TPM_HT_PCR << HR_SHIFT
HR_HMAC_SESSION      = TPM_HT_HMAC_SESSION << HR_SHIFT
HR_POLICY_SESSION    = TPM_HT_POLICY_SESSION << HR_SHIFT
HR_TRANSIENT         = TPM_HT_TRANSIENT << HR_SHIFT
HR_PERSISTENT        = TPM_HT_PERSISTENT << HR_SHIFT
HR_NV_INDEX          = TPM_HT_NV_INDEX << HR_SHIFT
HR_PERMANENT         = TPM_HT_PERMANENT << HR_SHIFT
PCR_FIRST            = HR_PCR + 0
PCR_LAST             = PCR_FIRST + IMPLEMENTATION_PCR - 1
HMAC_SESSION_FIRST   = HR_HMAC_SESSION + 0
HMAC_SESSION_LAST    = HMAC_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1
LOADED_SESSION_FIRST = HMAC_SESSION_FIRST
LOADED_SESSION_LAST  = HMAC_SESSION_LAST
POLICY_SESSION_FIRST = HR_POLICY_SESSION + 0
POLICY_SESSION_LAST  = POLICY_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1
TRANSIENT_FIRST      = HR_TRANSIENT + 0
ACTIVE_SESSION_FIRST = POLICY_SESSION_FIRST
ACTIVE_SESSION_LAST  = POLICY_SESSION_LAST
TRANSIENT_LAST       = TRANSIENT_FIRST+MAX_LOADED_OBJECTS - 1
PERSISTENT_FIRST     = HR_PERSISTENT + 0
PERSISTENT_LAST      = PERSISTENT_FIRST + 0x00FFFFFF
PLATFORM_PERSISTENT  = PERSISTENT_FIRST + 0x00800000
NV_INDEX_FIRST       = HR_NV_INDEX + 0
NV_INDEX_LAST        = NV_INDEX_FIRST + 0x00FFFFFF
PERMANENT_FIRST      = TPM_RH_FIRST
PERMANENT_LAST       = TPM_RH_LAST

class TPMA_ALGORITHM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymmetric",    UINT32, 1),
    ("symmetric",     UINT32, 1),
    ("hash",          UINT32, 1),
    ("object",        UINT32, 1),
    ("reserved4_7",   UINT32, 4),
    ("signing",       UINT32, 1),
    ("encrypting",    UINT32, 1),
    ("method",        UINT32, 1),
    ("reserved11_31", UINT32, 21)
  ]

class TPMA_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("reserved1",             UINT32, 1),
    ("fixedTPM",              UINT32, 1),
    ("stClear",               UINT32, 1),
    ("reserved4",             UINT32, 1),
    ("fixedParent",           UINT32, 1),
    ("sensitiveDataOrigin",   UINT32, 1),
    ("userWithAuth",          UINT32, 1),
    ("adminWithPolicy",       UINT32, 1),
    ("reserved8_9",           UINT32, 2),
    ("noDA",                  UINT32, 1),
    ("encryptedDuplication",  UINT32, 1),
    ("reserved12_15",         UINT32, 4),
    ("restricted",            UINT32, 1),
    ("decrypt",               UINT32, 1),
    ("sign",                  UINT32, 1),
    ("reserved19_31",         UINT32, 13)
  ]

class TPMA_SESSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("continueSession", UINT8, 1),
    ("auditExclusive",  UINT8, 1),
    ("auditReset",      UINT8, 1),
    ("reserved3_4",     UINT8, 2),
    ("decrypt",         UINT8, 1),
    ("encrypt",         UINT8, 1),
    ("audit",           UINT8, 1)
  ]

class TPMA_LOCALITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("locZero",   UINT8, 1),
    ("locOne",    UINT8, 1),
    ("locTwo",    UINT8, 1),
    ("locThree",  UINT8, 1),
    ("locFour",   UINT8, 1),
    ("Extended",  UINT8, 3)
  ]

class TPMA_PERMANENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ownerAuthSet",        UINT32, 1),
    ("endorsementAuthSet",  UINT32, 1),
    ("lockoutAuthSet",      UINT32, 1),
    ("reserved3_7",         UINT32, 5),
    ("disableClear",        UINT32, 1),
    ("inLockout",           UINT32, 1),
    ("tpmGeneratedEPS",     UINT32, 1),
    ("reserved11_31",       UINT32, 21)
  ]

class TPMA_STARTUP_CLEAR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("phEnable",      UINT32, 1),
    ("shEnable",      UINT32, 1),
    ("ehEnable",      UINT32, 1),
    ("reserved3_30",  UINT32, 28),
    ("orderly",       UINT32, 1)
  ]

class TPMA_MEMORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sharedRAM",         UINT32, 1),
    ("sharedNV",          UINT32, 1),
    ("objectCopiedToRam", UINT32, 1),
    ("reserved3_31",      UINT32, 29)
  ]

class TPMA_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("commandIndex",      UINT32, 16),
    ("reserved16_21",     UINT32, 6),
    ("nv",                UINT32, 1),
    ("extensive",         UINT32, 1),
    ("flushed",           UINT32, 1),
    ("cHandles",          UINT32, 3),
    ("rHandle",           UINT32, 1),
    ("V",                 UINT32, 1),
    ("Res",               UINT32, 2)
  ]

TPMI_YES_NO = BYTE

TPMI_DH_OBJECT = Tpm12.TPM_HANDLE
TPMI_DH_PERSISTENT = Tpm12.TPM_HANDLE
TPMI_DH_ENTITY = Tpm12.TPM_HANDLE
TPMI_DH_PCR = Tpm12.TPM_HANDLE
TPMI_SH_AUTH_SESSION = Tpm12.TPM_HANDLE
TPMI_SH_HMAC = Tpm12.TPM_HANDLE
TPMI_SH_POLICY = Tpm12.TPM_HANDLE
TPMI_DH_CONTEXT = Tpm12.TPM_HANDLE
TPMI_RH_HIERARCHY = Tpm12.TPM_HANDLE
TPMI_RH_HIERARCHY_AUTH = Tpm12.TPM_HANDLE
TPMI_RH_PLATFORM = Tpm12.TPM_HANDLE
TPMI_RH_OWNER = Tpm12.TPM_HANDLE
TPMI_RH_ENDORSEMENT = Tpm12.TPM_HANDLE
TPMI_RH_PROVISION = Tpm12.TPM_HANDLE
TPMI_RH_CLEAR = Tpm12.TPM_HANDLE
TPMI_RH_NV_AUTH = Tpm12.TPM_HANDLE
TPMI_RH_LOCKOUT = Tpm12.TPM_HANDLE
TPMI_RH_NV_INDEX = Tpm12.TPM_HANDLE
TPMI_ALG_HASH = TPM_ALG_ID
TPMI_ALG_ASYM = TPM_ALG_ID
TPMI_ALG_SYM = TPM_ALG_ID
TPMI_ALG_SYM_OBJECT = TPM_ALG_ID
TPMI_ALG_SYM_MODE = TPM_ALG_ID
TPMI_ALG_KDF = TPM_ALG_ID
TPMI_ALG_SIG_SCHEME = TPM_ALG_ID
TPMI_ECC_KEY_EXCHANGE = TPM_ALG_ID
TPMI_ST_COMMAND_TAG = TPM_ST

class TPMS_ALGORITHM_DESCRIPTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",         TPM_ALG_ID),
    ("attributes",  TPMA_ALGORITHM)
  ]

class TPMU_HA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("sha1",    BYTE * SHA1_DIGEST_SIZE),
    ("sha256",  BYTE * SHA256_DIGEST_SIZE),
    ("sm3_256", BYTE * SM3_256_DIGEST_SIZE),
    ("sha384",  BYTE * SHA384_DIGEST_SIZE),
    ("sha512",  BYTE * SHA512_DIGEST_SIZE)
  ]

class TPMT_HA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  TPMU_HA)
  ]

class TPMT_HA_SHA1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA1_DIGEST_SIZE)
  ]

class TPMT_HA_SHA256 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA256_DIGEST_SIZE)
  ]

class TPMT_HA_SM3_256 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SM3_256_DIGEST_SIZE)
  ]

class TPMT_HA_SHA384 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA384_DIGEST_SIZE)
  ]

class TPMT_HA_SHA512 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA512_DIGEST_SIZE)
  ]

class TPM2B_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMU_HA))
  ]

class TPM2B_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMT_HA))
  ]

TPM2B_NONCE = TPM2B_DIGEST
TPM2B_AUTH = TPM2B_DIGEST
TPM2B_OPERAND = TPM2B_DIGEST

class TPM2B_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * 1024)
  ]

class TPM2B_MAX_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_DIGEST_BUFFER)
  ]

class TPM2B_MAX_NV_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_NV_INDEX_SIZE)
  ]

class TPM2B_TIMEOUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (UINT64))
  ]

class TPM2B_IV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_BLOCK_SIZE)
  ]

class TPMU_NAME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("digest",  TPMT_HA),
    ("handle",  Tpm12.TPM_HANDLE)
  ]

class TPM2B_NAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("name",  BYTE * sizeof(TPMU_NAME))
  ]

class TPMS_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeofSelect",  UINT16),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

class TPMS_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",          TPMI_ALG_HASH),
    ("sizeofSelect",  UINT8),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

class TPMT_TK_CREATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_ST),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

class TPMT_TK_VERIFIED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_ST),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

TPMT_TK_AUTH = TPMT_TK_VERIFIED

TPMT_TK_HASHCHECK = TPMT_TK_VERIFIED

class TPMS_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",           TPM_ALG_ID),
    ("algProperties", TPMA_ALGORITHM)
  ]

class TPMS_TAGGED_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("property",  TPM_PT),
    ("value",     UINT32)
  ]

class TPMS_TAGGED_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_PT),
    ("sizeofSelect",  UINT8),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

MAX_CAP_DATA        = (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))
MAX_CAP_ALGS        = (MAX_CAP_DATA // sizeof(TPMS_ALG_PROPERTY))
MAX_CAP_HANDLES     = (MAX_CAP_DATA // sizeof(Tpm12.TPM_HANDLE))
MAX_CAP_CC          = (MAX_CAP_DATA // sizeof(TPM_CC))
MAX_TPM_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PROPERTY))
MAX_PCR_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PCR_SELECT))
MAX_ECC_CURVES      = (MAX_CAP_DATA // sizeof(TPM_ECC_CURVE))

class TPML_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("commandCodes",  TPM_CC * MAX_CAP_CC)
  ]

class TPML_CCA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",             UINT32),
    ("commandAttributes", TPMA_CC * MAX_CAP_CC)
  ]

class TPML_ALG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("algorithms",  TPM_ALG_ID * MAX_ALG_LIST_SIZE)
  ]

class TPML_HANDLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("handle",  Tpm12.TPM_HANDLE * MAX_CAP_HANDLES)
  ]

class TPML_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPM2B_DIGEST * 8)
  ]

class TPML_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPMT_HA * HASH_COUNT)
  ]

class TPM2B_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",   UINT16),
    ("buffer", BYTE * sizeof (TPML_DIGEST_VALUES))
  ]

class TPML_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("pcrSelections", TPMS_PCR_SELECTION * HASH_COUNT)
  ]

class TPML_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("algProperties", TPMS_ALG_PROPERTY * MAX_CAP_ALGS)
  ]

class TPML_TAGGED_TPM_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("tpmProperty", TPMS_TAGGED_PROPERTY * MAX_TPM_PROPERTIES)
  ]

class TPML_TAGGED_PCR_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("pcrProperty", TPMS_TAGGED_PCR_SELECT * MAX_PCR_PROPERTIES)
  ]

class TPML_ECC_CURVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("eccCurves",   TPM_ECC_CURVE * MAX_ECC_CURVES)
  ]

class TPMU_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("algorithms",    TPML_ALG_PROPERTY),
    ("handles",       TPML_HANDLE),
    ("command",       TPML_CCA),
    ("ppCommands",    TPML_CC),
    ("auditCommands", TPML_CC),
    ("assignedPCR",   TPML_PCR_SELECTION),
    ("tpmProperties", TPML_TAGGED_TPM_PROPERTY),
    ("pcrProperties", TPML_TAGGED_PCR_PROPERTY),
    ("eccCurves",     TPML_ECC_CURVE)
  ]

class TPMS_CAPABILITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("capability",  TPM_CAP),
    ("data",        TPMU_CAPABILITIES)
  ]

class TPMS_CLOCK_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("clock",         UINT64),
    ("resetCount",    UINT32),
    ("restartCount",  UINT32),
    ("safe",          TPMI_YES_NO)
  ]

class TPMS_TIME_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",      UINT64),
    ("clockInfo", TPMS_CLOCK_INFO)
  ]

class TPMS_TIME_ATTEST_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",            TPMS_TIME_INFO),
    ("firmwareVersion", UINT64)
  ]

class TPMS_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("name",          TPM2B_NAME),
    ("qualifiedName", TPM2B_NAME)
  ]

class TPMS_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect", TPML_PCR_SELECTION),
    ("pcrDigest", TPM2B_DIGEST)
  ]

class TPMS_COMMAND_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("auditCounter",  UINT64),
    ("digestAlg",     TPM_ALG_ID),
    ("auditDigest",   TPM2B_DIGEST),
    ("commandDigest", TPM2B_DIGEST)
  ]

class TPMS_SESSION_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("exclusiveSession",  TPMI_YES_NO),
    ("sessionDigest",     TPM2B_DIGEST)
  ]

class TPMS_CREATION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("objectName",    TPM2B_NAME),
    ("creationHash",  TPM2B_DIGEST)
  ]

class TPMS_NV_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("indexName",   TPM2B_NAME),
    ("offset",      UINT16),
    ("nvContents",  TPM2B_MAX_NV_BUFFER),
  ]

TPMI_ST_ATTEST = TPM_ST
class TPMU_ATTEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("certify",       TPMS_CERTIFY_INFO),
    ("creation",      TPMS_CREATION_INFO),
    ("quote",         TPMS_QUOTE_INFO),
    ("commandAudit",  TPMS_COMMAND_AUDIT_INFO),
    ("sessionAudit",  TPMS_SESSION_AUDIT_INFO),
    ("time",          TPMS_TIME_ATTEST_INFO),
    ("nv",            TPMS_NV_CERTIFY_INFO)
  ]

class TPMS_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("magic",           TPM_GENERATED),
    ("type",            TPMI_ST_ATTEST),
    ("qualifiedSigner", TPM2B_NAME),
    ("extraData",       TPM2B_DATA),
    ("clockInfo",       TPMS_CLOCK_INFO),
    ("firmwareVersion", UINT64),
    ("attested",        TPMU_ATTEST)
  ]

class TPM2B_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",            UINT16),
    ("attestationData", BYTE * sizeof (TPMS_ATTEST))
  ]

class TPMS_AUTH_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionHandle",     TPMI_SH_AUTH_SESSION),
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

class TPMS_AUTH_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

TPMI_AES_KEY_BITS = TPM_KEY_BITS
TPMI_SM4_KEY_BITS = TPM_KEY_BITS

class TPMU_SYM_KEY_BITS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_AES_KEY_BITS),
    ("SM4", TPMI_SM4_KEY_BITS),
    ("sym", TPM_KEY_BITS),
    ("xor", TPMI_ALG_HASH)
  ]

class TPMU_SYM_MODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_ALG_SYM_MODE),
    ("SM4", TPMI_ALG_SYM_MODE),
    ("sym", TPMI_ALG_SYM_MODE)
  ]

class TPMT_SYM_DEF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

class TPMT_SYM_DEF_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM_OBJECT),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

class TPM2B_SYM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_KEY_BYTES)
  ]

class TPMS_SYMCIPHER_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sym",    TPMT_SYM_DEF_OBJECT)
  ]

class TPM2B_SENSITIVE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_DATA)
  ]

class TPMS_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("userAuth",    TPM2B_AUTH),
    ("data",        TPM2B_SENSITIVE_DATA)
  ]

class TPM2B_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("sensitive", TPMS_SENSITIVE_CREATE)
  ]

class TPMS_SCHEME_SIGHASH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

TPMI_ALG_KEYEDHASH_SCHEME = TPM_ALG_ID
TPMS_SCHEME_HMAC = TPMS_SCHEME_SIGHASH

class TPMS_SCHEME_XOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("kdf",     TPMI_ALG_KDF)
  ]

class TPMU_SCHEME_KEYEDHASH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("hmac",  TPMS_SCHEME_HMAC),
    ("xor",   TPMS_SCHEME_XOR)
  ]

class TPMT_KEYEDHASH_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KEYEDHASH_SCHEME),
    ("details", TPMU_SCHEME_KEYEDHASH)
  ]

TPMS_SCHEME_RSASSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_RSAPSS = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECDSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_SM2 = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECSCHNORR = TPMS_SCHEME_SIGHASH

class TPMS_SCHEME_ECDAA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("count",   UINT16)
  ]

class TPMU_SIG_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("hmac",      TPMS_SCHEME_HMAC),
    ("any",       TPMS_SCHEME_SIGHASH),
  ]

class TPMT_SIG_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_SIG_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

class TPMS_SCHEME_OAEP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

TPMS_SCHEME_ECDH = TPMS_SCHEME_OAEP

TPMS_SCHEME_MGF1 = TPMS_SCHEME_OAEP

TPMS_SCHEME_KDF1_SP800_56a = TPMS_SCHEME_OAEP

TPMS_SCHEME_KDF2 = TPMS_SCHEME_OAEP

TPMS_SCHEME_KDF1_SP800_108 = TPMS_SCHEME_OAEP

class TPMU_KDF_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("mgf1",            TPMS_SCHEME_MGF1),
    ("kdf1_SP800_56a",  TPMS_SCHEME_KDF1_SP800_56a),
    ("kdf2",            TPMS_SCHEME_KDF2),
    ("kdf1_sp800_108",  TPMS_SCHEME_KDF1_SP800_108),
  ]

class TPMT_KDF_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KDF),
    ("details", TPMU_KDF_SCHEME)
  ]

TPMI_ALG_ASYM_SCHEME = TPM_ALG_ID

class TPMU_ASYM_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("oaep",      TPMS_SCHEME_OAEP),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("anySig",    TPMS_SCHEME_SIGHASH)
  ]

class TPMT_ASYM_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ASYM_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

TPMI_ALG_RSA_SCHEME = TPM_ALG_ID

class TPMT_RSA_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

TPMI_ALG_RSA_DECRYPT = TPM_ALG_ID

class TPMT_RSA_DECRYPT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_DECRYPT),
    ("details", TPMU_ASYM_SCHEME)
  ]

class TPM2B_PUBLIC_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_RSA_KEY_BYTES)
  ]

TPMI_RSA_KEY_BITS = TPM_KEY_BITS

class TPM2B_PRIVATE_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * (MAX_RSA_KEY_BYTES // 2))
  ]

class TPM2B_ECC_PARAMETER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_ECC_KEY_BYTES)
  ]

class TPMS_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("x", TPM2B_ECC_PARAMETER),
    ("y", TPM2B_ECC_PARAMETER)
  ]

class TPM2B_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("point", TPMS_ECC_POINT)
  ]

TPMI_ALG_ECC_SCHEME = TPM_ALG_ID
TPMI_ECC_CURVE = TPM_ECC_CURVE

class TPMT_ECC_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ECC_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

class TPMS_ALGORITHM_DETAIL_ECC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("curveID", TPM_ECC_CURVE),
    ("keySize", UINT16),
    ("kdf",     TPMT_KDF_SCHEME),
    ("sign",    TPMT_ECC_SCHEME),
    ("p",       TPM2B_ECC_PARAMETER),
    ("a",       TPM2B_ECC_PARAMETER),
    ("b",       TPM2B_ECC_PARAMETER),
    ("gX",      TPM2B_ECC_PARAMETER),
    ("gY",      TPM2B_ECC_PARAMETER),
    ("n",       TPM2B_ECC_PARAMETER),
    ("h",       TPM2B_ECC_PARAMETER)
  ]

class TPMS_SIGNATURE_RSASSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",    TPMI_ALG_HASH),
    ("sig",     TPM2B_PUBLIC_KEY_RSA)
  ]

class TPMS_SIGNATURE_RSAPSS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",    TPMI_ALG_HASH),
    ("sig",     TPM2B_PUBLIC_KEY_RSA)
  ]

class TPMS_SIGNATURE_ECDSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",        TPMI_ALG_HASH),
    ("signatureR",  TPM2B_ECC_PARAMETER),
    ("signatureS",  TPM2B_ECC_PARAMETER)
  ]

class TPMU_SIGNATURE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SIGNATURE_RSASSA),
    ("rsapss",    TPMS_SIGNATURE_RSAPSS),
    ("ecdsa",     TPMS_SIGNATURE_ECDSA),
    ("sm2",       TPMS_SIGNATURE_ECDSA),
    ("ecdaa",     TPMS_SIGNATURE_ECDSA),
    ("ecschnorr", TPMS_SIGNATURE_ECDSA),
    ("hmac",      TPMT_HA),
    ("any",       TPMS_SCHEME_SIGHASH)
  ]

class TPMT_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sigAlg",    TPMI_ALG_SIG_SCHEME),
    ("signature", TPMU_SIGNATURE)
  ]

class TPMU_ENCRYPTED_SECRET (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("ecc",       BYTE * sizeof (TPMS_ECC_POINT)),
    ("rsa",       BYTE * MAX_RSA_KEY_BYTES),
    ("symmetric", BYTE * sizeof (TPM2B_DIGEST)),
    ("keyedHash", BYTE * sizeof (TPM2B_DIGEST))
  ]

class TPM2B_ENCRYPTED_SECRET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("secret",  BYTE * sizeof (TPMU_ENCRYPTED_SECRET))
  ]

TPMI_ALG_PUBLIC = TPM_ALG_ID

class TPMU_PUBLIC_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHash", TPM2B_DIGEST),
    ("sym",       TPM2B_DIGEST),
    ("rsa",       TPM2B_PUBLIC_KEY_RSA),
    ("ecc",       TPMS_ECC_POINT)
  ]

class TPMS_KEYEDHASH_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMT_KEYEDHASH_SCHEME)
  ]

class TPMS_ASYM_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ASYM_SCHEME)
  ]

class TPMS_RSA_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_RSA_SCHEME),
    ("keyBits",   TPMI_RSA_KEY_BITS),
    ("exponent",  UINT32)
  ]

class TPMS_ECC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ECC_SCHEME),
    ("curveID",   TPMI_ECC_CURVE),
    ("kdf",       TPMT_KDF_SCHEME)
  ]

class TPMU_PUBLIC_PARMS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHashDetail", TPMS_KEYEDHASH_PARMS),
    ("symDetail",       TPMT_SYM_DEF_OBJECT),
    ("rsaDetail",       TPMS_RSA_PARMS),
    ("eccDetail",       TPMS_ECC_PARMS),
    ("asymDetail",      TPMS_ASYM_PARMS)
  ]

class TPMT_PUBLIC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",        TPMI_ALG_PUBLIC),
    ("parameters",  TPMU_PUBLIC_PARMS)
  ]

class TPMT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",              TPMI_ALG_PUBLIC),
    ("nameAlg",           TPMI_ALG_HASH),
    ("objectAttributes",  TPMA_OBJECT),
    ("authPolicy",        TPM2B_DIGEST),
    ("parameters",        TPMU_PUBLIC_PARMS),
    ("unique",            TPMU_PUBLIC_ID)
  ]

class TPM2B_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("publicArea",  TPMT_PUBLIC)
  ]

class TPM2B_PRIVATE_VENDOR_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * PRIVATE_VENDOR_SPECIFIC_BYTES)
  ]

class TPMU_SENSITIVE_COMPOSITE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsa",   TPM2B_PRIVATE_KEY_RSA),
    ("ecc",   TPM2B_ECC_PARAMETER),
    ("bits",  TPM2B_SENSITIVE_DATA),
    ("sym",   TPM2B_SYM_KEY),
    ("any",   TPM2B_PRIVATE_VENDOR_SPECIFIC)
  ]

class TPMT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sensitiveType", TPMI_ALG_PUBLIC),
    ("authValue",     TPM2B_AUTH),
    ("seedValue",     TPM2B_DIGEST),
    ("sensitive",     TPMU_SENSITIVE_COMPOSITE)
  ]

class TPM2B_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",          UINT16),
    ("sensitiveArea", TPMT_SENSITIVE)
  ]

class _PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityOuter",  TPM2B_DIGEST),
    ("integrityInner",  TPM2B_DIGEST),
    ("sensitive",       TPMT_SENSITIVE)
  ]

class TPM2B_PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (_PRIVATE))
  ]

class _ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityHMAC", TPM2B_DIGEST),
    ("encIdentity",   TPM2B_DIGEST)
  ]

class TPM2B_ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("credential",  BYTE * sizeof (_ID_OBJECT))
  ]

class TPMA_NV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TPMA_NV_PPWRITE",         UINT32, 1),
    ("TPMA_NV_OWNERWRITE ",     UINT32, 1),
    ("TPMA_NV_AUTHWRITE",       UINT32, 1),
    ("TPMA_NV_POLICYWRITE",     UINT32, 1),
    ("TPMA_NV_COUNTER",         UINT32, 1),
    ("TPMA_NV_BITS",            UINT32, 1),
    ("TPMA_NV_EXTEND",          UINT32, 1),
    ("reserved7_9",             UINT32, 3),
    ("TPMA_NV_POLICY_DELETE ",  UINT32, 1),
    ("TPMA_NV_WRITELOCKED",     UINT32, 1),
    ("TPMA_NV_WRITEALL",        UINT32, 1),
    ("TPMA_NV_WRITEDEFINE",     UINT32, 1),
    ("TPMA_NV_WRITE_STCLEAR ",  UINT32, 1),
    ("TPMA_NV_GLOBALLOCK",      UINT32, 1),
    ("TPMA_NV_PPREAD",          UINT32, 1),
    ("TPMA_NV_OWNERREAD",       UINT32, 1),
    ("TPMA_NV_AUTHREAD",        UINT32, 1),
    ("TPMA_NV_POLICYREAD",      UINT32, 1),
    ("reserved20_24",           UINT32, 5),
    ("TPMA_NV_NO_DA",           UINT32, 1),
    ("TPMA_NV_ORDERLY",         UINT32, 1),
    ("TPMA_NV_CLEAR_STCLEAR",   UINT32, 1),
    ("TPMA_NV_READLOCKED",      UINT32, 1),
    ("TPMA_NV_WRITTEN",         UINT32, 1),
    ("TPMA_NV_PLATFORMCREATE",  UINT32, 1),
    ("TPMA_NV_READ_STCLEAR",    UINT32, 1)
  ]

class TPMS_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nvIndex",     TPMI_RH_NV_INDEX),
    ("nameAlg",     TPMI_ALG_HASH),
    ("attributes",  TPMA_NV),
    ("authPolicy",  TPM2B_DIGEST),
    ("dataSize",    UINT16)
  ]

class TPM2B_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("nvPublic",  TPMS_NV_PUBLIC)
  ]

class TPM2B_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_CONTEXT_SIZE)
  ]

class TPMS_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrity", TPM2B_DIGEST),
    ("encrypted", TPM2B_CONTEXT_SENSITIVE)
  ]

class TPM2B_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof(TPMS_CONTEXT_DATA))
  ]

class TPMS_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sequence",    UINT64),
    ("savedHandle", TPMI_DH_CONTEXT),
    ("hierarchy",   TPMI_RH_HIERARCHY),
    ("contextBlob", TPM2B_CONTEXT_DATA)
  ]

class TPMS_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect",           TPML_PCR_SELECTION),
    ("pcrDigest",           TPM2B_DIGEST),
    ("locality",            TPMA_LOCALITY),
    ("parentNameAlg",       TPM_ALG_ID),
    ("parentName",          TPM2B_NAME),
    ("parentQualifiedName", TPM2B_NAME),
    ("outsideInfo",         TPM2B_DATA)
  ]

class TPM2B_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",            UINT16),
    ("creationData",    TPMS_CREATION_DATA)
  ]

class TPM2_COMMAND_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_ST),
    ("paramSize",   UINT32),
    ("commandCode", TPM_CC)
  ]

class TPM2_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_ST),
    ("paramSize",     UINT32),
    ("responseCode",  TPM_RC)
  ]

HASH_ALG_SHA1     = 0x00000001
HASH_ALG_SHA256   = 0x00000002
HASH_ALG_SHA384   = 0x00000004
HASH_ALG_SHA512   = 0x00000008
HASH_ALG_SM3_256  = 0x00000010

