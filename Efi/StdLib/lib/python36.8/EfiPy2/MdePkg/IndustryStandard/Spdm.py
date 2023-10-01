# Spdm.py
#
# EfiPy2.MdePkg.IndustryStandard.Spdm
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

SPDM_DIGESTS            = 0x01
SPDM_CERTIFICATE        = 0x02
SPDM_CHALLENGE_AUTH     = 0x03
SPDM_VERSION            = 0x04
SPDM_MEASUREMENTS       = 0x60
SPDM_CAPABILITIES       = 0x61
SPDM_SET_CERT_RESPONSE  = 0x62
SPDM_ALGORITHMS         = 0x63
SPDM_ERROR              = 0x7F

SPDM_GET_DIGESTS           = 0x81
SPDM_GET_CERTIFICATE       = 0x82
SPDM_CHALLENGE             = 0x83
SPDM_GET_VERSION           = 0x84
SPDM_GET_MEASUREMENTS      = 0xE0
SPDM_GET_CAPABILITIES      = 0xE1
SPDM_NEGOTIATE_ALGORITHMS  = 0xE3
SPDM_RESPOND_IF_READY      = 0xFF

class SPDM_MESSAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SPDMVersion",         UINT8),
    ("RequestResponseCode", UINT8),
    ("Param1",              UINT8),
    ("Param2",              UINT8)
    ]

SPDM_MESSAGE_VERSION  = 0x10
class SPDM_GET_VERSION_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER)
    ]

class SPDM_VERSION_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  SPDM_MESSAGE_HEADER),
    ("Reserved",                UINT8),
    ("VersionNumberEntryCount", UINT8)
    # ("VersionNumberEntry",      SPDM_VERSION_NUMBER * VersionNumberEntryCount)
    ]

class SPDM_VERSION_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Alpha",               UINT16, 4),
    ("UpdateVersionNumber", UINT16, 4),
    ("MinorVersion",        UINT16, 4),
    ("MajorVersion",        UINT16, 4)
    ]

class SPDM_GET_CAPABILITIES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER)
    ]

class SPDM_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      SPDM_MESSAGE_HEADER),
    ("Reserved",    UINT8 ),
    ("CTExponent",  UINT8 ),
    ("Reserved2",   UINT16),
    ("Flags",       UINT32)
    ]

SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_CACHE_CAP        = BIT0
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_CERT_CAP         = BIT1
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_CHAL_CAP         = BIT2
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_MEAS_CAP         = (BIT3 | BIT4)
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_MEAS_CAP_NO_SIG  = BIT3
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_MEAS_CAP_SIG     = BIT4
SPDM_GET_CAPABILITIES_RESPONSE_FLAGS_MEAS_FRESH_CAP   = BIT5

class SPDM_NEGOTIATE_ALGORITHMS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      SPDM_MESSAGE_HEADER),
    ("Length",                      UINT16),
    ("MeasurementSpecification",    UINT8 ),
    ("Reserved",                    UINT8 ),
    ("BaseAsymAlgo",                UINT32),
    ("BaseHashAlgo",                UINT32),
    ("Reserved2",                   UINT8 * 12),
    ("ExtAsymCount",                UINT8 ),
    ("ExtHashCount",                UINT8 ),
    ("Reserved3",                   UINT16)
    # ("ExtAsym",                   UINT32 * ExtAsymCount),
    # ("ExtHash",                   UINT32 * ExtHashCount)
    ]

SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSASSA_2048          = BIT0
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSAPSS_2048          = BIT1
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSASSA_3072          = BIT2
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSAPSS_3072          = BIT3
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_ECDSA_ECC_NIST_P256  = BIT4
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSASSA_4096          = BIT5
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_RSAPSS_4096          = BIT6
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_ECDSA_ECC_NIST_P384  = BIT7
SPDM_ALGORITHMS_BASE_ASYM_ALGO_TPM_ALG_ECDSA_ECC_NIST_P521  = BIT8

SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA_256   = BIT0
SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA_384   = BIT1
SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA_512   = BIT2
SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA3_256  = BIT3
SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA3_384  = BIT4
SPDM_ALGORITHMS_BASE_HASH_ALGO_TPM_ALG_SHA3_512  = BIT5

class SPDM_ALGORITHMS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      SPDM_MESSAGE_HEADER),

    ("Length",                      UINT16),
    ("MeasurementSpecificationSel", UINT8 ),
    ("Reserved",                    UINT8 ),
    ("MeasurementHashAlgo",         UINT32),
    ("BaseAsymSel",                 UINT32),
    ("BaseHashSel",                 UINT32),
    ("Reserved2",                   UINT8 * 12),
    ("ExtAsymSelCount",             UINT8 ),
    ("ExtHashSelCount",             UINT8 ),
    ("Reserved3",                   UINT16)

    # ("ExtAsymSel",                   UINT32 * ExtAsymSelCount),
    # ("ExtHashSel",                   UINT32 * ExtHashSelCount)
    ]

SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_RAW_BIT_STREAM_ONLY  = BIT0
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA_256      = BIT1
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA_384      = BIT2
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA_512      = BIT3
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA3_256     = BIT4
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA3_384     = BIT5
SPDM_ALGORITHMS_MEASUREMENT_HASH_ALGO_TPM_ALG_SHA3_512     = BIT6

class SPDM_GET_DIGESTS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                      SPDM_MESSAGE_HEADER)
    ]

class SPDM_DIGESTS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER)
    # ("Digest",  UINT8 * DigestSize)
    ]

class SPDM_GET_CERTIFICATE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER),
    ("Offset",  UINT16),
    ("Length",  UINT16)
    ]

class SPDM_CERTIFICATE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          SPDM_MESSAGE_HEADER),
    ("PortionLength",   UINT16),
    ("RemainderLength", UINT16)
    # ("CertChain",       UINT8 * CertChainSize)
    ]

class SPDM_CHALLENGE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER),
    ("Nonce",   UINT8 * 32)
    ]

class SPDM_CHALLENGE_AUTH_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER)
    # ("CertChainHash",           UINT8 * DigestSize),
    # ("Nonce",                   UINT8 * 32),
    # ("MeasurementSummaryHash",  UINT8 * DigestSize),
    # ("OpaqueLength",            UINT16),
    # ("OpaqueData",              UINT8 * OpaqueLength),
    # ("Signature",               UINT8 * KeySize)
    ]

class SPDM_GET_MEASUREMENTS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",  SPDM_MESSAGE_HEADER),
    ("Nonce",   UINT8 * 32)
    ]

class SPDM_MEASUREMENT_BLOCK_COMMON_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Index",                       UINT8),
    ("MeasurementSpecification",    UINT8),
    ("MeasurementSize",             UINT16)
    # ("Measurement",    UINT8 * MeasurementSize),
    ]

SPDM_MEASUREMENT_BLOCK_HEADER_SPECIFICATION_DMTF  = BIT0

class SPDM_MEASUREMENT_BLOCK_DMTF_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DMTFSpecMeasurementValueType",    UINT8),
    ("DMTFSpecMeasurementValueSize",    UINT16)
    # ("DMTFSpecMeasurementValue",    UINT8 * DMTFSpecMeasurementValueSize),
    ]

SPDM_MEASUREMENT_BLOCK_MEASUREMENT_TYPE_IMMUTABLE_ROM           = 0
SPDM_MEASUREMENT_BLOCK_MEASUREMENT_TYPE_MUTABLE_FIRMWARE        = 1
SPDM_MEASUREMENT_BLOCK_MEASUREMENT_TYPE_HARDWARE_CONFIGURATION  = 2
SPDM_MEASUREMENT_BLOCK_MEASUREMENT_TYPE_FIRMWARE_CONFIGURATION  = 3
SPDM_MEASUREMENT_BLOCK_MEASUREMENT_TYPE_RAW_BIT_STREAM          = BIT7

class SPDM_MEASUREMENTS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  SPDM_MESSAGE_HEADER),
    ("NumberOfBlocks",          UINT8),
    ("MeasurementRecordLength", UINT8 * 3)
    # ("MeasurementRecord",     UINT8 * MeasurementRecordLength),
    # ("Nonce",                 UINT8 * 32),
    # ("OpaqueLength",          UINT8 * UINT16),
    # ("OpaqueData",            UINT8 * OpaqueLength),
    # ("Signature",             UINT8 * KeySize)
    ]

class SPDM_ERROR_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              SPDM_MESSAGE_HEADER)
    # ("ExtendedErrorData", UINT8 * N)
    ]

SPDM_ERROR_CODE_INVALID_REQUEST         = 0x01
SPDM_ERROR_CODE_BUSY                    = 0x03
SPDM_ERROR_CODE_UNEXPECTED_REQUEST      = 0x04
SPDM_ERROR_CODE_UNSPECIFIED             = 0x05
SPDM_ERROR_CODE_UNSUPPORTED_REQUEST     = 0x07
SPDM_ERROR_CODE_MAJOR_VERSION_MISMATCH  = 0x41
SPDM_ERROR_CODE_RESPONSE_NOT_READY      = 0x42
SPDM_ERROR_CODE_REQUEST_RESYNCH         = 0x43

class SPDM_RESPONSE_IF_READY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              SPDM_MESSAGE_HEADER)
    ]

