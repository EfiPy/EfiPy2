# UefiInternalFormRepresentation.py
#
# EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

EFI_HII_HANDLE    = PVOID
EFI_STRING        = PCHAR16
EFI_IMAGE_ID      = UINT16
EFI_QUESTION_ID   = UINT16
EFI_STRING_ID     = UINT16
EFI_FORM_ID       = UINT16
EFI_VARSTORE_ID   = UINT16
EFI_ANIMATION_ID  = UINT16
EFI_DEFAULT_ID    = UINT16
EFI_HII_FONT_STYLE  = UINT32

class EFI_HII_PACKAGE_LIST_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("PackageListGuid", EFI_GUID),
    ("PackageLength",   UINT32)
  ]

class EFI_HII_PACKAGE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Length",  UINT32, 24),
    ("Type",    UINT32, 8)
    # ("Data",    UINT8 * N)
  ]

EFI_HII_PACKAGE_TYPE_ALL             = 0x00
EFI_HII_PACKAGE_TYPE_GUID            = 0x01
EFI_HII_PACKAGE_FORMS                = 0x02
EFI_HII_PACKAGE_STRINGS              = 0x04
EFI_HII_PACKAGE_FONTS                = 0x05
EFI_HII_PACKAGE_IMAGES               = 0x06
EFI_HII_PACKAGE_SIMPLE_FONTS         = 0x07
EFI_HII_PACKAGE_DEVICE_PATH          = 0x08
EFI_HII_PACKAGE_KEYBOARD_LAYOUT      = 0x09
EFI_HII_PACKAGE_ANIMATIONS           = 0x0A
EFI_HII_PACKAGE_END                  = 0xDF
EFI_HII_PACKAGE_TYPE_SYSTEM_BEGIN    = 0xE0
EFI_HII_PACKAGE_TYPE_SYSTEM_END      = 0xFF

EFI_GLYPH_NON_SPACING                = 0x01
EFI_GLYPH_WIDE                       = 0x02
EFI_GLYPH_HEIGHT                     = 19
EFI_GLYPH_WIDTH                      = 8

class EFI_NARROW_GLYPH (Structure):
  _pack_   = 1
  _fields_ = [
    ("UnicodeWeight", CHAR16),
    ("Attributes",    UINT8),
    ("GlyphCol1",     UINT8 * EFI_GLYPH_HEIGHT)
  ]

class EFI_WIDE_GLYPH (Structure):
  _pack_   = 1
  _fields_ = [
    ("UnicodeWeight", CHAR16),
    ("Attributes",    UINT8),
    ("GlyphCol1",     UINT8 * EFI_GLYPH_HEIGHT),
    ("GlyphCol2",     UINT8 * EFI_GLYPH_HEIGHT),
    ("Pad",           UINT8 * 3)
  ]

class EFI_HII_SIMPLE_FONT_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                EFI_HII_PACKAGE_HEADER),
    ("NumberOfNarrowGlyphs",  UINT16),
    ("NumberOfWideGlyphs",    UINT16)
    # ("NarrowGlyphs",          EFI_NARROW_GLYPH),
    # ("WideGlyphs",            EFI_NARROW_GLYPH)
  ]

EFI_HII_FONT_STYLE_NORMAL            = 0x00000000
EFI_HII_FONT_STYLE_BOLD              = 0x00000001
EFI_HII_FONT_STYLE_ITALIC            = 0x00000002
EFI_HII_FONT_STYLE_EMBOSS            = 0x00010000
EFI_HII_FONT_STYLE_OUTLINE           = 0x00020000
EFI_HII_FONT_STYLE_SHADOW            = 0x00040000
EFI_HII_FONT_STYLE_UNDERLINE         = 0x00080000
EFI_HII_FONT_STYLE_DBL_UNDER         = 0x00100000

class EFI_HII_GLYPH_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",     UINT16),
    ("Height",    UINT16),
    ("OffsetX",   INT16),
    ("OffsetY",   INT16),
    ("AdvanceX",  INT16)
  ]

class EFI_HII_FONT_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("HdrSize",           UINT32),
    ("GlyphBlockOffset",  UINT32),
    ("Cell",              EFI_HII_GLYPH_INFO),
    ("FontStyle",         EFI_HII_FONT_STYLE),
    ("FontFamily",        CHAR16 * 1)
  ]

EFI_HII_GIBT_END                  = 0x00
EFI_HII_GIBT_GLYPH                = 0x10
EFI_HII_GIBT_GLYPHS               = 0x11
EFI_HII_GIBT_GLYPH_DEFAULT        = 0x12
EFI_HII_GIBT_GLYPHS_DEFAULT       = 0x13
EFI_HII_GIBT_DUPLICATE            = 0x20
EFI_HII_GIBT_SKIP2                = 0x21
EFI_HII_GIBT_SKIP1                = 0x22
EFI_HII_GIBT_DEFAULTS             = 0x23
EFI_HII_GIBT_EXT1                 = 0x30
EFI_HII_GIBT_EXT2                 = 0x31
EFI_HII_GIBT_EXT4                 = 0x32

class EFI_HII_GLYPH_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
  ]

class EFI_HII_GIBT_DEFAULTS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_GLYPH_BLOCK),
    ("Cell",    EFI_HII_GLYPH_INFO)
  ]

class EFI_HII_GIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_GLYPH_BLOCK),
    ("TCharValueype", CHAR16)
  ]

class EFI_GLYPH_GIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_GLYPH_BLOCK)
  ]

class EFI_HII_GIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

class EFI_HII_GIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

class EFI_HII_GIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

class EFI_HII_GIBT_GLYPH_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Cell",        EFI_HII_GLYPH_INFO),
    ("BitmapData",  UINT8 * 1)
  ]

class EFI_HII_GIBT_GLYPHS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Cell",        EFI_HII_GLYPH_INFO),
    ("Count",       UINT16),
    ("BitmapData",  UINT8 * 1)
  ]

class EFI_HII_GIBT_GLYPH_DEFAULT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BitmapData",  UINT8 * 1)
  ]

class EFI_HII_GIBT_GLYPHS_DEFAULT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Count",       UINT16),
    ("BitmapData",  UINT8 * 1)
  ]

class EFI_HII_GIBT_VARIABILITY_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_GLYPH_BLOCK),
    ("Cell",              EFI_HII_GLYPH_INFO),
    ("GlyphPackInBits",   UINT8),
    ("BitmapData",        UINT8 * 1),
  ]

class EFI_HII_GIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("SkipCount",   UINT8)
  ]

class EFI_HII_GIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("SkipCount",   UINT16)
  ]

class EFI_HII_DEVICE_PATH_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_PACKAGE_HEADER)
    # ("DevicePath",  EFI_DEVICE_PATH_PROTOCOL * N)
  ]

class EFI_HII_GUID_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_PACKAGE_HEADER),
    ("Guid",    EFI_GUID)
  ]

UEFI_CONFIG_LANG   = b"x-UEFI"
UEFI_CONFIG_LANG_2 = b"x-i-UEFI"

class EFI_HII_STRING_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("HdrSize",           UINT32),
    ("StringInfoOffset",  UINT32),
    ("LanguageWindow",    CHAR16 * 16),
    ("LanguageName",      EFI_STRING_ID),
    ("Language",          CHAR8 * 1)
  ]

class EFI_HII_STRING_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
  ]

EFI_HII_SIBT_END                     = 0x00
EFI_HII_SIBT_STRING_SCSU             = 0x10
EFI_HII_SIBT_STRING_SCSU_FONT        = 0x11
EFI_HII_SIBT_STRINGS_SCSU            = 0x12
EFI_HII_SIBT_STRINGS_SCSU_FONT       = 0x13
EFI_HII_SIBT_STRING_UCS2             = 0x14
EFI_HII_SIBT_STRING_UCS2_FONT        = 0x15
EFI_HII_SIBT_STRINGS_UCS2            = 0x16
EFI_HII_SIBT_STRINGS_UCS2_FONT       = 0x17
EFI_HII_SIBT_DUPLICATE               = 0x20
EFI_HII_SIBT_SKIP2                   = 0x21
EFI_HII_SIBT_SKIP1                   = 0x22
EFI_HII_SIBT_EXT1                    = 0x30
EFI_HII_SIBT_EXT2                    = 0x31
EFI_HII_SIBT_EXT4                    = 0x32
EFI_HII_SIBT_FONT                    = 0x40

class EFI_HII_SIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("StringId",  EFI_STRING_ID)
  ]

class EFI_HII_SIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK)
  ]

class EFI_HII_SIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

class EFI_HII_SIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

class EFI_HII_SIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

class EFI_HII_SIBT_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_SIBT_EXT2_BLOCK),
    ("FontId",    UINT8),
    ("FontSize",  UINT16),
    ("FontStyle", EFI_HII_FONT_STYLE),
    ("FontName",  CHAR16 * 1)
  ]

class EFI_HII_SIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("SkipCount", UINT8)
  ]

class EFI_HII_SIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("SkipCount", UINT16)
  ]

class EFI_HII_SIBT_STRING_SCSU_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringText",  UINT8 * 1)
  ]

class EFI_HII_SIBT_STRING_SCSU_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringText",      UINT8 * 1)
  ]

class EFI_HII_SIBT_STRINGS_SCSU_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringCount", UINT16),
    ("StringText",  UINT8 * 1)
  ]

class EFI_HII_SIBT_STRINGS_SCSU_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringCount",     UINT16),
    ("StringText",      UINT8 * 1)
  ]

class EFI_HII_SIBT_STRING_UCS2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("StringText",      UINT16 * 1)
  ]

class EFI_HII_SIBT_STRING_UCS2_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringText",      CHAR16 * 1)
  ]

class EFI_HII_SIBT_STRINGS_UCS2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringCount", UINT16),
    ("StringText",  CHAR16 * 1)
  ]

class EFI_HII_SIBT_STRINGS_UCS2_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringCount",     UINT16),
    ("StringText",      CHAR16 * 1)
  ]

class EFI_HII_IMAGE_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("ImageInfoOffset",   UINT32),
    ("PaletteInfoOffset", UINT32)
  ]

class EFI_HII_IMAGE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType",  UINT8)
  ]

EFI_HII_IIBT_END               = 0x00
EFI_HII_IIBT_IMAGE_1BIT        = 0x10
EFI_HII_IIBT_IMAGE_1BIT_TRANS  = 0x11
EFI_HII_IIBT_IMAGE_4BIT        = 0x12
EFI_HII_IIBT_IMAGE_4BIT_TRANS  = 0x13
EFI_HII_IIBT_IMAGE_8BIT        = 0x14
EFI_HII_IIBT_IMAGE_8BIT_TRANS  = 0x15
EFI_HII_IIBT_IMAGE_24BIT       = 0x16
EFI_HII_IIBT_IMAGE_24BIT_TRANS = 0x17
EFI_HII_IIBT_IMAGE_JPEG        = 0x18
EFI_HII_IIBT_DUPLICATE         = 0x20
EFI_HII_IIBT_SKIP2             = 0x21
EFI_HII_IIBT_SKIP1             = 0x22
EFI_HII_IIBT_EXT1              = 0x30
EFI_HII_IIBT_EXT2              = 0x31
EFI_HII_IIBT_EXT4              = 0x32

class EFI_HII_IIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK)
  ]

class EFI_HII_IIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

class EFI_HII_IIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

class EFI_HII_IIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

class EFI_HII_IIBT_IMAGE_1BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_HII_IIBT_IMAGE_1BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_1BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_1BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_1BIT_BASE)
  ]

class EFI_HII_RGB_PIXEL (Structure):
  _pack_   = 1
  _fields_ = [
    ("b", UINT8),
    ("g", UINT8),
    ("r", UINT8)
  ]

class EFI_HII_IIBT_IMAGE_24BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Bitmap",  EFI_HII_RGB_PIXEL * 1)
  ]

class EFI_HII_IIBT_IMAGE_24BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Bitmap",  EFI_HII_IIBT_IMAGE_24BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_24BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Bitmap",  EFI_HII_IIBT_IMAGE_24BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_4BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8)
  ]

class EFI_HII_IIBT_IMAGE_4BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_4BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_4BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_4BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_8BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8 * 1)
  ]

class EFI_HII_IIBT_IMAGE_8BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_8BIT_BASE)
  ]

class EFI_HII_IIBT_IMAGE_8BIT_TRAN_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_8BIT_BASE)
  ]

class EFI_HII_IIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("ImageId", EFI_IMAGE_ID)
  ]

class EFI_HII_IIBT_JPEG_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Size",    UINT32),
    ("Data",    UINT8 * 1)
  ]

class EFI_HII_IIBT_PNG_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("Size",      UINT32),
    ("Data",      UINT8 * 1)
  ]

class EFI_HII_IIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("SkipCount", UINT8)
  ]

class EFI_HII_IIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("SkipCount", UINT16)
  ]

class EFI_HII_IMAGE_PALETTE_INFO_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("PaletteCount",  UINT16)
  ]

class EFI_HII_IMAGE_PALETTE_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("PaletteSize",   UINT16),
    ("PaletteValue",  EFI_HII_RGB_PIXEL * 1)
  ]

class EFI_HII_FORM_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_PACKAGE_HEADER)
    # ("OpCodeHeader",  EFI_IFR_OP_HEADER)
  ]

class EFI_HII_TIME (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hour",    UINT8),
    ("Minute",  UINT8),
    ("Second",  UINT8)
  ]

class EFI_HII_DATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Year",  UINT16),
    ("Month", UINT8),
    ("Day",   UINT8)
  ]

class EFI_HII_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormId",      EFI_FORM_ID),
    ("FormSetGuid", EFI_GUID),
    ("DevicePath",  EFI_STRING_ID)
  ]

class EFI_IFR_TYPE_VALUE (Union):
  _pack_   = 1
  _fields_ = [
    ("u8",      UINT8),
    ("u16",     UINT16),
    ("u32",     UINT32),
    ("u64",     UINT64),
    ("b",       BOOLEAN),
    ("time",    EFI_HII_TIME),
    ("date",    EFI_HII_DATE),
    ("string",  EFI_STRING_ID),
    ("ref",     EFI_HII_REF),
    # ("buffer",  UINT8 * N)
  ]

EFI_IFR_FORM_OP                = 0x01
EFI_IFR_SUBTITLE_OP            = 0x02
EFI_IFR_TEXT_OP                = 0x03
EFI_IFR_IMAGE_OP               = 0x04
EFI_IFR_ONE_OF_OP              = 0x05
EFI_IFR_CHECKBOX_OP            = 0x06
EFI_IFR_NUMERIC_OP             = 0x07
EFI_IFR_PASSWORD_OP            = 0x08
EFI_IFR_ONE_OF_OPTION_OP       = 0x09
EFI_IFR_SUPPRESS_IF_OP         = 0x0A
EFI_IFR_LOCKED_OP              = 0x0B
EFI_IFR_ACTION_OP              = 0x0C
EFI_IFR_RESET_BUTTON_OP        = 0x0D
EFI_IFR_FORM_SET_OP            = 0x0E
EFI_IFR_REF_OP                 = 0x0F
EFI_IFR_NO_SUBMIT_IF_OP        = 0x10
EFI_IFR_INCONSISTENT_IF_OP     = 0x11
EFI_IFR_EQ_ID_VAL_OP           = 0x12
EFI_IFR_EQ_ID_ID_OP            = 0x13
EFI_IFR_EQ_ID_VAL_LIST_OP      = 0x14
EFI_IFR_AND_OP                 = 0x15
EFI_IFR_OR_OP                  = 0x16
EFI_IFR_NOT_OP                 = 0x17
EFI_IFR_RULE_OP                = 0x18
EFI_IFR_GRAY_OUT_IF_OP         = 0x19
EFI_IFR_DATE_OP                = 0x1A
EFI_IFR_TIME_OP                = 0x1B
EFI_IFR_STRING_OP              = 0x1C
EFI_IFR_REFRESH_OP             = 0x1D
EFI_IFR_DISABLE_IF_OP          = 0x1E
EFI_IFR_ANIMATION_OP           = 0x1F
EFI_IFR_TO_LOWER_OP            = 0x20
EFI_IFR_TO_UPPER_OP            = 0x21
EFI_IFR_MAP_OP                 = 0x22
EFI_IFR_ORDERED_LIST_OP        = 0x23
EFI_IFR_VARSTORE_OP            = 0x24
EFI_IFR_VARSTORE_NAME_VALUE_OP = 0x25
EFI_IFR_VARSTORE_EFI_OP        = 0x26
EFI_IFR_VARSTORE_DEVICE_OP     = 0x27
EFI_IFR_VERSION_OP             = 0x28
EFI_IFR_END_OP                 = 0x29
EFI_IFR_MATCH_OP               = 0x2A
EFI_IFR_GET_OP                 = 0x2B
EFI_IFR_SET_OP                 = 0x2C
EFI_IFR_READ_OP                = 0x2D
EFI_IFR_WRITE_OP               = 0x2E
EFI_IFR_EQUAL_OP               = 0x2F
EFI_IFR_NOT_EQUAL_OP           = 0x30
EFI_IFR_GREATER_THAN_OP        = 0x31
EFI_IFR_GREATER_EQUAL_OP       = 0x32
EFI_IFR_LESS_THAN_OP           = 0x33
EFI_IFR_LESS_EQUAL_OP          = 0x34
EFI_IFR_BITWISE_AND_OP         = 0x35
EFI_IFR_BITWISE_OR_OP          = 0x36
EFI_IFR_BITWISE_NOT_OP         = 0x37
EFI_IFR_SHIFT_LEFT_OP          = 0x38
EFI_IFR_SHIFT_RIGHT_OP         = 0x39
EFI_IFR_ADD_OP                 = 0x3A
EFI_IFR_SUBTRACT_OP            = 0x3B
EFI_IFR_MULTIPLY_OP            = 0x3C
EFI_IFR_DIVIDE_OP              = 0x3D
EFI_IFR_MODULO_OP              = 0x3E
EFI_IFR_RULE_REF_OP            = 0x3F
EFI_IFR_QUESTION_REF1_OP       = 0x40
EFI_IFR_QUESTION_REF2_OP       = 0x41
EFI_IFR_UINT8_OP               = 0x42
EFI_IFR_UINT16_OP              = 0x43
EFI_IFR_UINT32_OP              = 0x44
EFI_IFR_UINT64_OP              = 0x45
EFI_IFR_TRUE_OP                = 0x46
EFI_IFR_FALSE_OP               = 0x47
EFI_IFR_TO_UINT_OP             = 0x48
EFI_IFR_TO_STRING_OP           = 0x49
EFI_IFR_TO_BOOLEAN_OP          = 0x4A
EFI_IFR_MID_OP                 = 0x4B
EFI_IFR_FIND_OP                = 0x4C
EFI_IFR_TOKEN_OP               = 0x4D
EFI_IFR_STRING_REF1_OP         = 0x4E
EFI_IFR_STRING_REF2_OP         = 0x4F
EFI_IFR_CONDITIONAL_OP         = 0x50
EFI_IFR_QUESTION_REF3_OP       = 0x51
EFI_IFR_ZERO_OP                = 0x52
EFI_IFR_ONE_OP                 = 0x53
EFI_IFR_ONES_OP                = 0x54
EFI_IFR_UNDEFINED_OP           = 0x55
EFI_IFR_LENGTH_OP              = 0x56
EFI_IFR_DUP_OP                 = 0x57
EFI_IFR_THIS_OP                = 0x58
EFI_IFR_SPAN_OP                = 0x59
EFI_IFR_VALUE_OP               = 0x5A
EFI_IFR_DEFAULT_OP             = 0x5B
EFI_IFR_DEFAULTSTORE_OP        = 0x5C
EFI_IFR_FORM_MAP_OP            = 0x5D
EFI_IFR_CATENATE_OP            = 0x5E
EFI_IFR_GUID_OP                = 0x5F
EFI_IFR_SECURITY_OP            = 0x60
EFI_IFR_MODAL_TAG_OP           = 0x61
EFI_IFR_REFRESH_ID_OP          = 0x62
EFI_IFR_WARNING_IF_OP          = 0x63
EFI_IFR_MATCH2_OP              = 0x64

class EFI_IFR_OP_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT8),
    ("Length",  UINT8, 7),
    ("Scope",   UINT8, 1)
  ]

class EFI_IFR_STATEMENT_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Prompt",  EFI_STRING_ID),
    ("Help",    EFI_STRING_ID)
  ]

class EFI_IFR_QUESTION_HEADER_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_QUESTION_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_STATEMENT_HEADER),
    ("QuestionId",    EFI_QUESTION_ID),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_QUESTION_HEADER_VarStoreInfo),
    ("Flags",         UINT8)
  ]

EFI_IFR_FLAG_READ_ONLY          = 0x01
EFI_IFR_FLAG_CALLBACK           = 0x04
EFI_IFR_FLAG_RESET_REQUIRED     = 0x10
EFI_IFR_FLAG_REST_STYLE         = 0x20
EFI_IFR_FLAG_RECONNECT_REQUIRED = 0x40
EFI_IFR_FLAG_OPTIONS_ONLY       = 0x80

class EFI_IFR_DEFAULTSTORE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("DefaultName",   EFI_STRING_ID),
    ("DefaultId",     UINT16)
  ]

EFI_HII_DEFAULT_CLASS_STANDARD       = 0x0000
EFI_HII_DEFAULT_CLASS_MANUFACTURING  = 0x0001
EFI_HII_DEFAULT_CLASS_SAFE           = 0x0002
EFI_HII_DEFAULT_CLASS_PLATFORM_BEGIN = 0x4000
EFI_HII_DEFAULT_CLASS_PLATFORM_END   = 0x7fff
EFI_HII_DEFAULT_CLASS_HARDWARE_BEGIN = 0x8000
EFI_HII_DEFAULT_CLASS_HARDWARE_END   = 0xbfff
EFI_HII_DEFAULT_CLASS_FIRMWARE_BEGIN = 0xc000
EFI_HII_DEFAULT_CLASS_FIRMWARE_END   = 0xffff

class EFI_IFR_VARSTORE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Guid",        EFI_GUID),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Size",        UINT16),
    ("Name",        UINT8 * 1)
  ]

class EFI_IFR_VARSTORE_EFI (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Guid",        EFI_GUID),
    ("Attributes",  UINT32),
    ("Size",        UINT16),
    ("Name",        UINT8 * 1)
  ]

class EFI_IFR_VARSTORE_NAME_VALUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Guid",        EFI_GUID)
  ]

class EFI_IFR_FORM_SET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("Guid",          EFI_GUID),
    ("FormSetTitle",  EFI_STRING_ID),
    ("Help",          EFI_STRING_ID),
    ("Flags",         UINT8)
    # ("ClassGuid",     EFI_GUID)
  ]

class EFI_IFR_END (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_FORM (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("FormId",    UINT16),
    ("FormTitle", EFI_STRING_ID)
  ]

class EFI_IFR_IMAGE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Id",      EFI_IMAGE_ID)
  ]

class EFI_IFR_MODAL_TAG (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_LOCKED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_RULE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("RuleId",  UINT8)
  ]

class EFI_IFR_DEFAULT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("DefaultId", UINT16),
    ("Type",      UINT8),
    ("Value",     EFI_IFR_TYPE_VALUE)
  ]

class EFI_IFR_DEFAULT_2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("DefaultId", UINT16),
    ("Type",      UINT8)
  ]

class EFI_IFR_VALUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_SUBTITLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("Flags",     UINT8)
  ]

EFI_IFR_FLAGS_HORIZONTAL       = 0x01

class EFI_IFR_CHECKBOX (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

EFI_IFR_CHECKBOX_DEFAULT       = 0x01
EFI_IFR_CHECKBOX_DEFAULT_MFG   = 0x02

class EFI_IFR_TEXT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("TextTwo",   EFI_STRING_ID)
  ]

class EFI_IFR_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("FormId",    EFI_FORM_ID)
  ]

class EFI_IFR_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID)
  ]

class EFI_IFR_REF3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormSetId",   EFI_GUID)
  ]

class EFI_IFR_REF4 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormSetId",   EFI_GUID),
    ("DevicePath",  EFI_STRING_ID)
  ]

class EFI_IFR_REF5 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER)
  ]

class EFI_IFR_RESET_BUTTON (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("DefaultId", EFI_DEFAULT_ID)
  ]

class EFI_IFR_ACTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_IFR_OP_HEADER),
    ("Question",        EFI_IFR_QUESTION_HEADER),
    ("QuestionConfig",  EFI_STRING_ID)
  ]

class EFI_IFR_ACTION_1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER)
  ]

class EFI_IFR_DATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

EFI_QF_DATE_YEAR_SUPPRESS      = 0x01
EFI_QF_DATE_MONTH_SUPPRESS     = 0x02
EFI_QF_DATE_DAY_SUPPRESS       = 0x04

EFI_QF_DATE_STORAGE            = 0x30
QF_DATE_STORAGE_NORMAL     = 0x00
QF_DATE_STORAGE_TIME       = 0x10
QF_DATE_STORAGE_WAKEUP     = 0x20
    
class MINMAXSTEP_DATA_u8 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT8),
    ("MaxValue",  UINT8),
    ("Step",      UINT8)
  ]

class MINMAXSTEP_DATA_u16 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT16),
    ("MaxValue",  UINT16),
    ("Step",      UINT16)
  ]

class MINMAXSTEP_DATA_u32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT32),
    ("MaxValue",  UINT32),
    ("Step",      UINT32)
  ]

class MINMAXSTEP_DATA_u64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT64),
    ("MaxValue",  UINT64),
    ("Step",      UINT64)
  ]

class MINMAXSTEP_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("u8",  MINMAXSTEP_DATA_u8),
    ("u16", MINMAXSTEP_DATA_u16),
    ("u32", MINMAXSTEP_DATA_u32),
    ("u64", MINMAXSTEP_DATA_u64)
  ]

class EFI_IFR_NUMERIC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8),
    ("data",      MINMAXSTEP_DATA)
  ]

EFI_IFR_NUMERIC_SIZE           = 0x03
EFI_IFR_NUMERIC_SIZE_1       = 0x00
EFI_IFR_NUMERIC_SIZE_2       = 0x01
EFI_IFR_NUMERIC_SIZE_4       = 0x02
EFI_IFR_NUMERIC_SIZE_8       = 0x03

EFI_IFR_DISPLAY                = 0x30
EFI_IFR_DISPLAY_INT_DEC      = 0x00
EFI_IFR_DISPLAY_UINT_DEC     = 0x10
EFI_IFR_DISPLAY_UINT_HEX     = 0x20

class EFI_IFR_ONE_OF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8),
    ("data",      MINMAXSTEP_DATA)
  ]

class EFI_IFR_STRING (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("MinSize",   UINT8),
    ("MaxSize",   UINT8),
    ("Flags",     UINT8)
  ]

EFI_IFR_STRING_MULTI_LINE      = 0x01

class EFI_IFR_PASSWORD (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("MinSize",   UINT8),
    ("MaxSize",   UINT8)
  ]

class EFI_IFR_ORDERED_LIST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("Question",      EFI_IFR_QUESTION_HEADER),
    ("MaxContainers", UINT8),
    ("Flags",         UINT8)
  ]

EFI_IFR_UNIQUE_SET             = 0x01
EFI_IFR_NO_EMPTY_SET           = 0x02

class EFI_IFR_TIME (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

QF_TIME_HOUR_SUPPRESS          = 0x01
QF_TIME_MINUTE_SUPPRESS        = 0x02
QF_TIME_SECOND_SUPPRESS        = 0x04

QF_TIME_STORAGE                = 0x30
QF_TIME_STORAGE_NORMAL       = 0x00
QF_TIME_STORAGE_TIME         = 0x10
QF_TIME_STORAGE_WAKEUP       = 0x20

class EFI_IFR_DISABLE_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_SUPPRESS_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_GRAY_OUT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_INCONSISTENT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Error",   EFI_STRING_ID)
  ]

class EFI_IFR_NO_SUBMIT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Error",   EFI_STRING_ID)
  ]

class EFI_IFR_WARNING_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Warning", EFI_STRING_ID),
    ("TimeOut", UINT8)
  ]

class EFI_IFR_REFRESH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_IFR_OP_HEADER),
    ("RefreshInterval", UINT8)
  ]

class EFI_IFR_VARSTORE_DEVICE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID)
  ]

class EFI_IFR_ONE_OF_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Option",  EFI_STRING_ID),
    ("Flags",   UINT8),
    ("Type",    UINT8),
    ("Value",   EFI_IFR_TYPE_VALUE)
  ]

EFI_IFR_TYPE_NUM_SIZE_8        = 0x00
EFI_IFR_TYPE_NUM_SIZE_16       = 0x01
EFI_IFR_TYPE_NUM_SIZE_32       = 0x02
EFI_IFR_TYPE_NUM_SIZE_64       = 0x03
EFI_IFR_TYPE_BOOLEAN           = 0x04
EFI_IFR_TYPE_TIME              = 0x05
EFI_IFR_TYPE_DATE              = 0x06
EFI_IFR_TYPE_STRING            = 0x07
EFI_IFR_TYPE_OTHER             = 0x08
EFI_IFR_TYPE_UNDEFINED         = 0x09
EFI_IFR_TYPE_ACTION            = 0x0A
EFI_IFR_TYPE_BUFFER            = 0x0B
EFI_IFR_TYPE_REF               = 0x0C

EFI_IFR_OPTION_DEFAULT         = 0x10
EFI_IFR_OPTION_DEFAULT_MFG     = 0x20

class EFI_IFR_GUID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Guid",    EFI_GUID)
    # Optional Data Follows
  ]

class EFI_IFR_REFRESH_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_IFR_OP_HEADER),
    ("RefreshEventGroupId", EFI_GUID)
  ]

class EFI_IFR_DUP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_EQ_ID_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId1", EFI_QUESTION_ID),
    ("QuestionId2", EFI_QUESTION_ID)
  ]

class EFI_IFR_EQ_ID_VAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID),
    ("Value",       UINT16)
  ]

class EFI_IFR_EQ_ID_VAL_LIST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID),
    ("ListLength",  UINT16),
    ("ValueList",   UINT16 * 1)
  ]

class EFI_IFR_UINT8 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT8)
  ]

class EFI_IFR_UINT16 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT16)
  ]

class EFI_IFR_UINT32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT32)
  ]

class EFI_IFR_UINT64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT64)
  ]

class EFI_IFR_QUESTION_REF1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID)
  ]

class EFI_IFR_QUESTION_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_QUESTION_REF3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_QUESTION_REF3_2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID)
  ]

class EFI_IFR_QUESTION_REF3_3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID),
    ("Guid",        EFI_GUID)
  ]

class EFI_IFR_RULE_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("RuleId",  UINT8)
  ]

class EFI_IFR_STRING_REF1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("StringId",  EFI_STRING_ID)
  ]

class EFI_IFR_STRING_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_THIS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_TRUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_FALSE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_ONE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_ONES (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_ZERO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_UNDEFINED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_VERSION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_LENGTH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_NOT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_BITWISE_NOT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_TO_BOOLEAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

EFI_IFR_STRING_UNSIGNED_DEC      = 0
EFI_IFR_STRING_SIGNED_DEC        = 1
EFI_IFR_STRING_LOWERCASE_HEX     = 2
EFI_IFR_STRING_UPPERCASE_HEX     = 3

EFI_IFR_STRING_ASCII             = 0
EFI_IFR_STRING_UNICODE           = 8

class EFI_IFR_TO_STRING (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Format",    UINT8)
  ]

class EFI_IFR_TO_UINT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_TO_UPPER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_TO_LOWER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_ADD (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_AND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_BITWISE_AND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_BITWISE_OR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_CATENATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_DIVIDE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_GREATER_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_GREATER_THAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_LESS_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_LESS_THAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_MATCH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_MATCH2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("SyntaxType",  EFI_GUID)
  ]

class EFI_IFR_MULTIPLY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_MODULO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_NOT_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_OR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_SHIFT_LEFT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_SHIFT_RIGHT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_SUBTRACT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_CONDITIONAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

EFI_IFR_FF_CASE_SENSITIVE    = 0x00
EFI_IFR_FF_CASE_INSENSITIVE  = 0x01

class EFI_IFR_FIND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Format",    UINT8)
  ]

class EFI_IFR_MID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_TOKEN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

EFI_IFR_FLAGS_FIRST_MATCHING     = 0x00
EFI_IFR_FLAGS_FIRST_NON_MATCHING = 0x01

class EFI_IFR_SPAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Flags",   UINT8)
  ]

class EFI_IFR_SECURITY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Permissions", EFI_GUID)
  ]

class EFI_IFR_FORM_MAP_METHOD (Structure):
  _pack_   = 1
  _fields_ = [
    ("MethodTitle",       EFI_STRING_ID),
    ("MethodIdentifier",  EFI_GUID)
  ]

class EFI_IFR_FORM_MAP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("FormId",  EFI_FORM_ID)
    # ("Methods", EFI_IFR_FORM_MAP_METHOD * N)
  ]

class EFI_IFR_SET_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_SET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_SET_VarStoreInfo),
    ("VarStoreType",  UINT8)
  ]

class EFI_IFR_GET_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_GET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_GET_VarStoreInfo),
    ("VarStoreType",  UINT8)
  ]

class EFI_IFR_READ (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_WRITE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

class EFI_IFR_MAP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

EfiKeyLCtrl       =   0
EfiKeyA0          =   1
EfiKeyLAlt        =   2
EfiKeySpaceBar    =   3
EfiKeyA2          =   4
EfiKeyA3          =   5
EfiKeyA4          =   6
EfiKeyRCtrl       =   7
EfiKeyLeftArrow   =   8
EfiKeyDownArrow   =   9
EfiKeyRightArrow  =  10
EfiKeyZero        =  11
EfiKeyPeriod      =  12
EfiKeyEnter       =  13
EfiKeyLShift      =  14
EfiKeyB0          =  15
EfiKeyB1          =  16
EfiKeyB2          =  17
EfiKeyB3          =  18
EfiKeyB4          =  19
EfiKeyB5          =  20
EfiKeyB6          =  21
EfiKeyB7          =  22
EfiKeyB8          =  23
EfiKeyB9          =  24
EfiKeyB10         =  25
EfiKeyRShift      =  26
EfiKeyUpArrow     =  27
EfiKeyOne         =  28
EfiKeyTwo         =  29
EfiKeyThree       =  30
EfiKeyCapsLock    =  31
EfiKeyC1          =  32
EfiKeyC2          =  33
EfiKeyC3          =  34
EfiKeyC4          =  35
EfiKeyC5          =  36
EfiKeyC6          =  37
EfiKeyC7          =  38
EfiKeyC8          =  39
EfiKeyC9          =  40
EfiKeyC10         =  41
EfiKeyC11         =  42
EfiKeyC12         =  43
EfiKeyFour        =  44
EfiKeyFive        =  45
EfiKeySix         =  46
EfiKeyPlus        =  47
EfiKeyTab         =  48
EfiKeyD1          =  49
EfiKeyD2          =  50
EfiKeyD3          =  51
EfiKeyD4          =  52
EfiKeyD5          =  53
EfiKeyD6          =  54
EfiKeyD7          =  55
EfiKeyD8          =  56
EfiKeyD9          =  57
EfiKeyD10         =  58
EfiKeyD11         =  59
EfiKeyD12         =  60
EfiKeyD13         =  61
EfiKeyDel         =  62
EfiKeyEnd         =  63
EfiKeyPgDn        =  64
EfiKeySeven       =  65
EfiKeyEight       =  66
EfiKeyNine        =  67
EfiKeyE0          =  68
EfiKeyE1          =  69
EfiKeyE2          =  70
EfiKeyE3          =  71
EfiKeyE4          =  72
EfiKeyE5          =  73
EfiKeyE6          =  74
EfiKeyE7          =  75
EfiKeyE8          =  76
EfiKeyE9          =  77
EfiKeyE10         =  78
EfiKeyE11         =  79
EfiKeyE12         =  80
EfiKeyBackSpace   =  81
EfiKeyIns         =  82
EfiKeyHome        =  83
EfiKeyPgUp        =  84
EfiKeyNLck        =  85
EfiKeySlash       =  86
EfiKeyAsterisk    =  87
EfiKeyMinus       =  88
EfiKeyEsc         =  89
EfiKeyF1          =  90
EfiKeyF2          =  91
EfiKeyF3          =  92
EfiKeyF4          =  93
EfiKeyF5          =  94
EfiKeyF6          =  95
EfiKeyF7          =  96
EfiKeyF8          =  97
EfiKeyF9          =  98
EfiKeyF10         =  99
EfiKeyF11         = 100
EfiKeyF12         = 101
EfiKeyPrint       = 102
EfiKeySLck        = 103
EfiKeyPause       = 104
EfiKeyIntl0       = 105
EfiKeyIntl1       = 106
EfiKeyIntl2       = 107
EfiKeyIntl3       = 108
EfiKeyIntl4       = 109
EfiKeyIntl5       = 110
EfiKeyIntl6       = 111
EfiKeyIntl7       = 112
EfiKeyIntl8       = 113
EfiKeyIntl9       = 114
EFI_KEY           = ENUM

class EFI_KEY_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Key",                 EFI_KEY),
    ("Unicode",             CHAR16),
    ("ShiftedUnicode",      CHAR16),
    ("AltGrUnicode",        CHAR16),
    ("ShiftedAltGrUnicode", CHAR16),
    ("Modifier",            UINT16),
    ("AffectedAttribute",   UINT16)
  ]

EFI_AFFECTED_BY_STANDARD_SHIFT       = 0x0001
EFI_AFFECTED_BY_CAPS_LOCK            = 0x0002
EFI_AFFECTED_BY_NUM_LOCK             = 0x0004

class EFI_HII_KEYBOARD_LAYOUT (Structure):
  _pack_   = 1
  _fields_ = [
    ("LayoutLength",                  UINT16),
    ("Guid",                          EFI_GUID),
    ("LayoutDescriptorStringOffset",  UINT32),
    ("DescriptorCount",               UINT8)
    # ("Descriptors",                   EFI_KEY_DESCRIPTOR * N)
  ]

class EFI_HII_KEYBOARD_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_PACKAGE_HEADER),
    ("LayoutCount", UINT16)
    # ("Layout",      EFI_HII_KEYBOARD_LAYOUT)
  ]

EFI_NULL_MODIFIER                = 0x0000
EFI_LEFT_CONTROL_MODIFIER        = 0x0001
EFI_RIGHT_CONTROL_MODIFIER       = 0x0002
EFI_LEFT_ALT_MODIFIER            = 0x0003
EFI_RIGHT_ALT_MODIFIER           = 0x0004
EFI_ALT_GR_MODIFIER              = 0x0005
EFI_INSERT_MODIFIER              = 0x0006
EFI_DELETE_MODIFIER              = 0x0007
EFI_PAGE_DOWN_MODIFIER           = 0x0008
EFI_PAGE_UP_MODIFIER             = 0x0009
EFI_HOME_MODIFIER                = 0x000A
EFI_END_MODIFIER                 = 0x000B
EFI_LEFT_SHIFT_MODIFIER          = 0x000C
EFI_RIGHT_SHIFT_MODIFIER         = 0x000D
EFI_CAPS_LOCK_MODIFIER           = 0x000E
EFI_NUM_LOCK_MODIFIER            = 0x000F
EFI_LEFT_ARROW_MODIFIER          = 0x0010
EFI_RIGHT_ARROW_MODIFIER         = 0x0011
EFI_DOWN_ARROW_MODIFIER          = 0x0012
EFI_UP_ARROW_MODIFIER            = 0x0013
EFI_NS_KEY_MODIFIER              = 0x0014
EFI_NS_KEY_DEPENDENCY_MODIFIER   = 0x0015
EFI_FUNCTION_KEY_ONE_MODIFIER    = 0x0016
EFI_FUNCTION_KEY_TWO_MODIFIER    = 0x0017
EFI_FUNCTION_KEY_THREE_MODIFIER  = 0x0018
EFI_FUNCTION_KEY_FOUR_MODIFIER   = 0x0019
EFI_FUNCTION_KEY_FIVE_MODIFIER   = 0x001A
EFI_FUNCTION_KEY_SIX_MODIFIER    = 0x001B
EFI_FUNCTION_KEY_SEVEN_MODIFIER  = 0x001C
EFI_FUNCTION_KEY_EIGHT_MODIFIER  = 0x001D
EFI_FUNCTION_KEY_NINE_MODIFIER   = 0x001E
EFI_FUNCTION_KEY_TEN_MODIFIER    = 0x001F
EFI_FUNCTION_KEY_ELEVEN_MODIFIER = 0x0020
EFI_FUNCTION_KEY_TWELVE_MODIFIER = 0x0021

EFI_PRINT_MODIFIER               = 0x0022
EFI_SYS_REQUEST_MODIFIER         = 0x0023
EFI_SCROLL_LOCK_MODIFIER         = 0x0024
EFI_PAUSE_MODIFIER               = 0x0025
EFI_BREAK_MODIFIER               = 0x0026

EFI_LEFT_LOGO_MODIFIER           = 0x0027
EFI_RIGHT_LOGO_MODIFIER          = 0x0028
EFI_MENU_MODIFIER                = 0x0029

class EFI_IFR_ANIMATION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Id",      EFI_ANIMATION_ID)
  ]

class EFI_HII_ANIMATION_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_HII_PACKAGE_HEADER),
    ("AnimationInfoOffset", UINT32)
  ]

class EFI_HII_ANIMATION_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
    # ("BlockBody", UINT8 * N)
  ]

EFI_HII_AIBT_END                 = 0x00
EFI_HII_AIBT_OVERLAY_IMAGES      = 0x10
EFI_HII_AIBT_CLEAR_IMAGES        = 0x11
EFI_HII_AIBT_RESTORE_SCRN        = 0x12
EFI_HII_AIBT_OVERLAY_IMAGES_LOOP = 0x18
EFI_HII_AIBT_CLEAR_IMAGES_LOOP   = 0x19
EFI_HII_AIBT_RESTORE_SCRN_LOOP   = 0x1A
EFI_HII_AIBT_DUPLICATE           = 0x20
EFI_HII_AIBT_SKIP2               = 0x21
EFI_HII_AIBT_SKIP1               = 0x22
EFI_HII_AIBT_EXT1                = 0x30
EFI_HII_AIBT_EXT2                = 0x31
EFI_HII_AIBT_EXT4                = 0x32

class EFI_HII_AIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

class EFI_HII_AIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

class EFI_HII_AIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

class EFI_HII_ANIMATION_CELL (Structure):
  _pack_   = 1
  _fields_ = [
    ("OffsetX", UINT16),
    ("OffsetY", UINT16),
    ("ImageId", EFI_IMAGE_ID),
    ("Delay",   UINT16)
  ]

class EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

class EFI_HII_AIBT_CLEAR_IMAGES_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("BackgndColor",  EFI_HII_RGB_PIXEL),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

class EFI_HII_AIBT_RESTORE_SCRN_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

EFI_HII_AIBT_OVERLAY_IMAGES_LOOP_BLOCK  = EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK
EFI_HII_AIBT_CLEAR_IMAGES_LOOP_BLOCK    = EFI_HII_AIBT_CLEAR_IMAGES_BLOCK
EFI_HII_AIBT_RESTORE_SCRN_LOOP_BLOCK    = EFI_HII_AIBT_RESTORE_SCRN_BLOCK
class EFI_HII_AIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("AnimationId", EFI_ANIMATION_ID)
  ]

class EFI_HII_AIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("SkipCount", UINT8)
  ]

class EFI_HII_AIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("SkipCount", UINT16)
  ]

