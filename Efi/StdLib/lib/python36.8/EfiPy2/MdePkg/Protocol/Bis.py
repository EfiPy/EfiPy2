# Bis.py
#
# EfiPy2.MdePkg.Protocol.Bis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2 import *

gEfiBisProtocolGuid                     = \
  EFI_GUID (0x0b64aab0, 0x5429, 0x11d4, (0x98, 0x16, 0x00, 0xa0, 0xc9, 0x1f, 0xad, 0xcf ))

gBootObjectAuthorizationParmsetGuid     = \
  EFI_GUID (0xedd35e31, 0x7b9, 0x11d2, ( 0x83,0xa3,0x0,0xa0,0xc9,0x1f,0xad,0xcf ))

class EFI_BIS_PROTOCOL (Structure):
  pass

BIS_APPLICATION_HANDLE  = PVOID
BIS_ALG_ID              = UINT16
BIS_CERT_ID             = UINT32

class EFI_BIS_DATA (Structure):
  _fields_ = [
    ("Length",  UINT32),
    ("Data",    POINTER (UINT8))
  ]

class EFI_BIS_VERSION (Structure):
  _fields_ = [
    ("Major",  UINT32),
    ("Major",  UINT32)
  ]

BIS_VERSION_1             = 1
BIS_CURRENT_VERSION_MAJOR = BIS_VERSION_1

class EFI_BIS_SIGNATURE_INFO (Structure):
  _fields_ = [
    ("CertificateID", BIS_CERT_ID),
    ("AlgorithmID",   BIS_ALG_ID),
    ("KeyLength",     UINT16)
  ]

BIS_ALG_DSA     = 41
BIS_ALG_RSA_MD5 = 42

BIS_CERT_ID_DSA     = BIS_ALG_DSA    
BIS_CERT_ID_RSA_MD5 = BIS_ALG_RSA_MD5

BIS_CERT_ID_MASK  = 0xFF7F7FFF

def BIS_GET_SIGINFO_COUNT(BisDataPtr):
  return (BisDataPtr).Length // sizeof (EFI_BIS_SIGNATURE_INFO)

def BIS_GET_SIGINFO_ARRAY(BisDataPtr):
  return BisDataPtr.Data

BOOT_OBJECT_AUTHORIZATION_PARMSET_GUIDVALUE = gBootObjectAuthorizationParmsetGuid

EFI_BIS_INITIALIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_BIS_PROTOCOL)       , #IN     *This,              
  POINTER (BIS_APPLICATION_HANDLE) , #OUT    *AppHandle,         
  POINTER (EFI_BIS_VERSION)        , #IN OUT *InterfaceVersion,  
  POINTER (EFI_BIS_DATA)             #IN     *TargetAddress      
  )

EFI_BIS_FREE = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE, # IN  AppHandle,               
  POINTER (EFI_BIS_DATA)  # IN  *ToFree                  
  )

EFI_BIS_SHUTDOWN = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE  # IN  AppHandle
  )

EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_CERTIFICATE = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,           # IN  AppHandle,               
  POINTER (POINTER (EFI_BIS_DATA))  # OUT **Certificate
  )

EFI_BIS_VERIFY_BOOT_OBJECT = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,           # IN  AppHandle,               
  EFI_BIS_DATA,                     # IN  *Credentials,
  EFI_BIS_DATA,                     # IN  *DataObject,
  BOOLEAN                           # OUT *IsVerified
  )

EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_CHECKFLAG = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE, # IN  AppHandle,               
  POINTER (BOOLEAN)       # OUT *CheckIsRequired               
  )

EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_UPDATE_TOKEN = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,           # IN  AppHandle,               
  POINTER (POINTER (EFI_BIS_DATA))  # OUT **UpdateToken               
  )

EFI_BIS_UPDATE_BOOT_OBJECT_AUTHORIZATION = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,           # IN  AppHandle,               
  POINTER (EFI_BIS_DATA),           # IN *RequestCredential               
  POINTER (POINTER (EFI_BIS_DATA))  # OUT **NewUpdateToken               
  )

EFI_BIS_VERIFY_OBJECT_WITH_CREDENTIAL = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,               # IN  AppHandle,               
  POINTER (EFI_BIS_DATA),               # IN  *Credentials               
  POINTER (EFI_BIS_DATA),               # IN  *DataObject               
  POINTER (EFI_BIS_DATA),               # IN  *SectionName               
  POINTER (EFI_BIS_DATA),               # IN  *AuthorityCertificate               
  POINTER (BOOLEAN)                     # OUT *IsVerified              
  )

EFI_BIS_GET_SIGNATURE_INFO = CFUNCTYPE (
  EFI_STATUS,
  BIS_APPLICATION_HANDLE,               # IN  AppHandle,               
  POINTER (POINTER (EFI_BIS_DATA))      # OUT **SignatureInfo               
  )

EFI_BIS_PROTOCOL._fields_ = [
    ("Initialize",                            EFI_BIS_INITIALIZE),
    ("Shutdown",                              EFI_BIS_SHUTDOWN),
    ("Free",                                  EFI_BIS_FREE),
    ("GetBootObjectAuthorizationCertificate", EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_CERTIFICATE ),
    ("GetBootObjectAuthorizationCheckFlag",   EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_CHECKFLAG),
    ("GetBootObjectAuthorizationUpdateToken", EFI_BIS_GET_BOOT_OBJECT_AUTHORIZATION_UPDATE_TOKEN),
    ("GetSignatureInfo",                      EFI_BIS_GET_SIGNATURE_INFO),
    ("UpdateBootObjectAuthorization",         EFI_BIS_UPDATE_BOOT_OBJECT_AUTHORIZATION),
    ("VerifyBootObject",                      EFI_BIS_VERIFY_BOOT_OBJECT),
    ("VerifyObjectWithCredential",            EFI_BIS_VERIFY_OBJECT_WITH_CREDENTIAL)
  ]

