# BlockIoCrypto.py
#
# EfiPy2.MdePkg.Protocol.BlockIoCrypto
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

from EfiPy2.MdePkg.Protocol import BlockIo

gEfiBlockIoCryptoProtocolGuid           = \
  EFI_GUID (0xa00490ba, 0x3f1a, 0x4b4c, (0xab, 0x90, 0x4f, 0xa9, 0x97, 0x26, 0xa1, 0xe8))

class EFI_BLOCK_IO_CRYPTO_PROTOCOL (Structure):
  pass

class EFI_BLOCK_IO_CRYPTO_TOKEN (Structure):
  _fields_ = [
    ("Event",               EFI_EVENT),
    ("TransactionStatus",   EFI_STATUS)
  ]

class EFI_BLOCK_IO_CRYPTO_CAPABILITY (Structure):
  _fields_ = [
    ("Algorithm",               EFI_GUID),
    ("KeySize",                 UINT64),
    ("CryptoBlockSizeBitMask",  UINT64)
  ]

class EFI_BLOCK_IO_CRYPTO_IV_INPUT (Structure):
  _fields_ = [
    ("InputSize",               UINT64)
  ]

gEfiBlockIoCryptoAlgoAesXtsGuid         = \
  EFI_GUID (0x2f87ba6a, 0x5c04, 0x4385, (0xa7, 0x80, 0xf3, 0xbf, 0x78, 0xa9, 0x7b, 0xec))

class EFI_BLOCK_IO_CRYPTO_IV_INPUT_AES_XTS (Structure):
  _fields_ = [
    ("Header",              EFI_BLOCK_IO_CRYPTO_IV_INPUT),
    ("CryptoBlockNumber",   UINT64),
    ("CryptoBlockByteSize", UINT64)
  ]

gEfiBlockIoCryptoAlgoAesCbcMsBitlockerGuid  = \
  EFI_GUID (0x689e4c62, 0x70bf, 0x4cf3, (0x88, 0xbb, 0x33, 0xb3, 0x18, 0x26, 0x86, 0x70))

class EFI_BLOCK_IO_CRYPTO_IV_INPUT_AES_CBC_MICROSOFT_BITLOCKER (Structure):
  _fields_ = [
    ("Header",                EFI_BLOCK_IO_CRYPTO_IV_INPUT),
    ("CryptoBlockByteOffset", UINT64),
    ("CryptoBlockByteSize",   UINT64)
  ]

EFI_BLOCK_IO_CRYPTO_INDEX_ANY = 0xFFFFFFFFFFFFFFFF

class EFI_BLOCK_IO_CRYPTO_CAPABILITIES (Structure):
  _fields_ = [
    ("Supported",        BOOLEAN),
    ("KeyCount",         UINT64),
    ("CapabilityCount",  UINT64),
    ("Capabilities",     EFI_BLOCK_IO_CRYPTO_CAPABILITY * 1)
  ]

class EFI_BLOCK_IO_CRYPTO_CONFIGURATION_TABLE_ENTRY (Structure):
  _fields_ = [
    ("Index",         UINT64),
    ("KeyOwnerGuid",  EFI_GUID),
    ("Capability",    EFI_BLOCK_IO_CRYPTO_CAPABILITY),
    ("CryptoKey",     PVOID)
  ]

class EFI_BLOCK_IO_CRYPTO_RESPONSE_CONFIGURATION_ENTRY (Structure):
  _fields_ = [
    ("Index",         UINT64),
    ("KeyOwnerGuid",  EFI_GUID),
    ("Capability",    EFI_BLOCK_IO_CRYPTO_CAPABILITY)
  ]

EFI_BLOCK_IO_CRYPTO_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL), # IN  *This,              
  BOOLEAN                                 # IN  ExtendedVerification         
  )

EFI_BLOCK_IO_CRYPTO_GET_CAPABILITIES = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL),     # IN     *This,              
  POINTER (EFI_BLOCK_IO_CRYPTO_CAPABILITIES)  #    OUT *Capabilities         
  )

EFI_BLOCK_IO_CRYPTO_SET_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL),                     # IN     *This,              
  UINT64,                                                     # IN     ConfigurationCount,
  POINTER (EFI_BLOCK_IO_CRYPTO_CONFIGURATION_TABLE_ENTRY),    # IN     *ConfigurationTable,
  POINTER (EFI_BLOCK_IO_CRYPTO_RESPONSE_CONFIGURATION_ENTRY)  #    OUT *ResultingTable OPTIONAL
  )

EFI_BLOCK_IO_CRYPTO_GET_CONFIGURATION = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL),                     # IN     *This,
  UINT64,                                                     # IN     StartIndex,
  UINT64,                                                     # IN     ConfigurationCount,
  POINTER (EFI_GUID),                                         # IN     *KeyOwnerGuid        OPTIONAL,
  POINTER (EFI_BLOCK_IO_CRYPTO_RESPONSE_CONFIGURATION_ENTRY)  #    OUT *ConfigurationTable
  )

EFI_BLOCK_IO_CRYPTO_READ_EXTENDED = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL), # IN     *This,
  UINT32,                                 # IN     MediaId,
  EFI_LBA,                                # IN     LBA,
  POINTER (EFI_BLOCK_IO_CRYPTO_TOKEN),    # IN OUT *Token,
  UINT64,                                 # IN     BufferSize,
  PVOID,                                  #    OUT *Buffer,
  POINTER (UINT64),                       # IN     *Index OPTIONAL,
  PVOID,                                  # IN     *CryptoIvInput OPTIONAL
  )

EFI_BLOCK_IO_CRYPTO_WRITE_EXTENDED = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL), # IN     *This,
  UINT32,                                 # IN     MediaId,
  EFI_LBA,                                # IN     LBA,
  POINTER (EFI_BLOCK_IO_CRYPTO_TOKEN),    # IN OUT *Token,
  UINT64,                                 # IN     BufferSize,
  PVOID,                                  # IN     *Buffer,
  POINTER (UINT64),                       # IN     *Index OPTIONAL,
  PVOID,                                  # IN     *CryptoIvInput OPTIONAL
  )

EFI_BLOCK_IO_CRYPTO_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BLOCK_IO_CRYPTO_PROTOCOL), # IN     *This,
  POINTER (EFI_BLOCK_IO_CRYPTO_TOKEN)     # IN OUT *Token,
  )

EFI_BLOCK_IO_CRYPTO_PROTOCOL._fields_ = [
    ("Media",             POINTER (BlockIo.EFI_BLOCK_IO_MEDIA)),
    ("Reset",             EFI_BLOCK_IO_CRYPTO_RESET),
    ("GetCapabilities",   EFI_BLOCK_IO_CRYPTO_GET_CAPABILITIES),
    ("SetConfiguration",  EFI_BLOCK_IO_CRYPTO_SET_CONFIGURATION),
    ("GetConfiguration",  EFI_BLOCK_IO_CRYPTO_GET_CONFIGURATION),
    ("ReadExtended",      EFI_BLOCK_IO_CRYPTO_READ_EXTENDED),
    ("WriteExtended",     EFI_BLOCK_IO_CRYPTO_WRITE_EXTENDED),
    ("FlushBlocks",       EFI_BLOCK_IO_CRYPTO_FLUSH)
  ]

