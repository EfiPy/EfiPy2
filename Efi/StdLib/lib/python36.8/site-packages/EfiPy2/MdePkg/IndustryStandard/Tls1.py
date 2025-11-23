# Tls1.py
#
# EfiPy2.MdePkg.IndustryStandard.Tls1
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2.MdePkg.IndustryStandard import *

TLS_RSA_WITH_NULL_MD5                    = (0x00, 0x01)
TLS_RSA_WITH_NULL_SHA                    = (0x00, 0x02)
TLS_RSA_WITH_RC4_128_MD5                 = (0x00, 0x04)
TLS_RSA_WITH_RC4_128_SHA                 = (0x00, 0x05)
TLS_RSA_WITH_IDEA_CBC_SHA                = (0x00, 0x07)
TLS_RSA_WITH_DES_CBC_SHA                 = (0x00, 0x09)
TLS_RSA_WITH_3DES_EDE_CBC_SHA            = (0x00, 0x0A)
TLS_DH_DSS_WITH_DES_CBC_SHA              = (0x00, 0x0C)
TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA         = (0x00, 0x0D)
TLS_DH_RSA_WITH_DES_CBC_SHA              = (0x00, 0x0F)
TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA         = (0x00, 0x10)
TLS_DHE_DSS_WITH_DES_CBC_SHA             = (0x00, 0x12)
TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA        = (0x00, 0x13)
TLS_DHE_RSA_WITH_DES_CBC_SHA             = (0x00, 0x15)
TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA        = (0x00, 0x16)
TLS_RSA_WITH_AES_128_CBC_SHA             = (0x00, 0x2F)
TLS_DH_DSS_WITH_AES_128_CBC_SHA          = (0x00, 0x30)
TLS_DH_RSA_WITH_AES_128_CBC_SHA          = (0x00, 0x31)
TLS_DHE_DSS_WITH_AES_128_CBC_SHA         = (0x00, 0x32)
TLS_DHE_RSA_WITH_AES_128_CBC_SHA         = (0x00, 0x33)
TLS_RSA_WITH_AES_256_CBC_SHA             = (0x00, 0x35)
TLS_DH_DSS_WITH_AES_256_CBC_SHA          = (0x00, 0x36)
TLS_DH_RSA_WITH_AES_256_CBC_SHA          = (0x00, 0x37)
TLS_DHE_DSS_WITH_AES_256_CBC_SHA         = (0x00, 0x38)
TLS_DHE_RSA_WITH_AES_256_CBC_SHA         = (0x00, 0x39)
TLS_RSA_WITH_NULL_SHA256                 = (0x00, 0x3B)
TLS_RSA_WITH_AES_128_CBC_SHA256          = (0x00, 0x3C)
TLS_RSA_WITH_AES_256_CBC_SHA256          = (0x00, 0x3D)
TLS_DH_DSS_WITH_AES_128_CBC_SHA256       = (0x00, 0x3E)
TLS_DH_RSA_WITH_AES_128_CBC_SHA256       = (0x00, 0x3F)
TLS_DHE_DSS_WITH_AES_128_CBC_SHA256      = (0x00, 0x40)
TLS_DHE_RSA_WITH_AES_128_CBC_SHA256      = (0x00, 0x67)
TLS_DH_DSS_WITH_AES_256_CBC_SHA256       = (0x00, 0x68)
TLS_DH_RSA_WITH_AES_256_CBC_SHA256       = (0x00, 0x69)
TLS_DHE_DSS_WITH_AES_256_CBC_SHA256      = (0x00, 0x6A)
TLS_DHE_RSA_WITH_AES_256_CBC_SHA256      = (0x00, 0x6B)
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384      = (0x00, 0x9F)
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  = (0xC0, 0x2B)
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  = (0xC0, 0x2C)
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384    = (0xC0, 0x30)

TLS10_PROTOCOL_VERSION_MAJOR  = 0x03
TLS10_PROTOCOL_VERSION_MINOR  = 0x01
TLS11_PROTOCOL_VERSION_MAJOR  = 0x03
TLS11_PROTOCOL_VERSION_MINOR  = 0x02
TLS12_PROTOCOL_VERSION_MAJOR  = 0x03
TLS12_PROTOCOL_VERSION_MINOR  = 0x03

TlsContentTypeChangeCipherSpec = 20
TlsContentTypeAlert            = 21
TlsContentTypeHandshake        = 22
TlsContentTypeApplicationData  = 23
TLS_CONTENT_TYPE               = ENUM

# 
# ///
# /// TLS Record Header, refers to A.1 of rfc-2246, rfc-4346 and rfc-5246.
# ///
# typedef struct {
#   UINT8              ContentType;
#   EFI_TLS_VERSION    Version;
#   UINT16             Length;
# } TLS_RECORD_HEADER;

#
# This is defined in Protocol/Tls.h, defined here for workaround
#
class EFI_TLS_VERSION (Structure):
  _fields_ = [
    ("Major", UINT8),
    ("Minor", UINT8)
    ]

class TLS_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContentType", UINT8),
    ("Version",     EFI_TLS_VERSION),
    ("Length",      UINT16),
    ]

# 
# #define TLS_RECORD_HEADER_LENGTH  5
TLS_RECORD_HEADER_LENGTH  = 5

# 
# //
# // The length (in bytes) of the TLSPlaintext records payload MUST NOT exceed 2^14.
# // Refers to section 6.2 of RFC5246.
# //
# #define TLS_PLAINTEXT_RECORD_MAX_PAYLOAD_LENGTH  16384
TLS_PLAINTEXT_RECORD_MAX_PAYLOAD_LENGTH  = 16384

# 
# //
# // The length (in bytes) of the TLSCiphertext records payload MUST NOT exceed 2^14 + 2048.
# // Refers to section 6.2 of RFC5246.
# //
# #define TLS_CIPHERTEXT_RECORD_MAX_PAYLOAD_LENGTH  18432
TLS_CIPHERTEXT_RECORD_MAX_PAYLOAD_LENGTH  = 18432

# 
# ///
# /// TLS Hash algorithm, refers to section 7.4.1.4.1. of rfc-5246.
# ///
# typedef enum {
#   TlsHashAlgoNone   = 0,
#   TlsHashAlgoMd5    = 1,
#   TlsHashAlgoSha1   = 2,
#   TlsHashAlgoSha224 = 3,
#   TlsHashAlgoSha256 = 4,
#   TlsHashAlgoSha384 = 5,
#   TlsHashAlgoSha512 = 6,
# } TLS_HASH_ALGO;
TlsHashAlgoNone   = 0
TlsHashAlgoMd5    = 1
TlsHashAlgoSha1   = 2
TlsHashAlgoSha224 = 3
TlsHashAlgoSha256 = 4
TlsHashAlgoSha384 = 5
TlsHashAlgoSha512 = 6
TLS_HASH_ALGO     = ENUM

# 
# ///
# /// TLS Signature algorithm, refers to section 7.4.1.4.1. of rfc-5246.
# ///
# typedef enum {
#   TlsSignatureAlgoAnonymous = 0,
#   TlsSignatureAlgoRsa       = 1,
#   TlsSignatureAlgoDsa       = 2,
#   TlsSignatureAlgoEcdsa     = 3,
# } TLS_SIGNATURE_ALGO;
TlsSignatureAlgoAnonymous = 0
TlsSignatureAlgoRsa       = 1
TlsSignatureAlgoDsa       = 2
TlsSignatureAlgoEcdsa     = 3
TLS_SIGNATURE_ALGO        = ENUM

# 
# ///
# /// TLS Supported Elliptic Curves Extensions, refers to section 5.1.1 of rfc-8422.
# ///
# typedef enum {
#   TlsEcNamedCurveSecp256r1 = 23,
#   TlsEcNamedCurveSecp384r1 = 24,
#   TlsEcNamedCurveSecp521r1 = 25,
#   TlsEcNamedCurveX25519    = 29,
#   TlsEcNamedCurveX448      = 30,
# } TLS_EC_NAMED_CURVE;
TlsEcNamedCurveSecp256r1 = 23
TlsEcNamedCurveSecp384r1 = 24
TlsEcNamedCurveSecp521r1 = 25
TlsEcNamedCurveX25519    = 29
TlsEcNamedCurveX448      = 30
TLS_EC_NAMED_CURVE       = ENUM

# 
# #pragma pack()
# 
# #endif
# 