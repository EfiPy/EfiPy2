# Http11.py
#
# EfiPy2.MdePkg.IndustryStandard.Http11
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2025 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
HTTP_VERSION  = b"HTTP/1.1"

HTTP_METHOD_OPTIONS  = b"OPTIONS"
HTTP_METHOD_GET      = b"GET"
HTTP_METHOD_HEAD     = b"HEAD"
HTTP_METHOD_POST     = b"POST"
HTTP_METHOD_PUT      = b"PUT"
HTTP_METHOD_DELETE   = b"DELETE"
HTTP_METHOD_TRACE    = b"TRACE"
HTTP_METHOD_CONNECT  = b"CONNECT"
HTTP_METHOD_PATCH    = b"PATCH"

HTTP_METHOD_MAXIMUM_LEN  = len (HTTP_METHOD_CONNECT)

HTTP_HEADER_ACCEPT  = b"Accept"

HTTP_HEADER_ACCEPT_CHARSET  = b"Accept-Charset"

HTTP_HEADER_ACCEPT_LANGUAGE  = b"Accept-Language"

HTTP_HEADER_ACCEPT_RANGES  = b"Accept-Ranges"

HTTP_HEADER_ACCEPT_ENCODING  = b"Accept-Encoding"
HTTP_HEADER_CONTENT_ENCODING  = b"Content-Encoding"

HTTP_CONTENT_ENCODING_IDENTITY  = b"identity" # No transformation is used. This is the default value for content coding.
HTTP_CONTENT_ENCODING_GZIP      = b"gzip"     # Content-Encoding: GNU zip format (described in RFC 1952).
HTTP_CONTENT_ENCODING_COMPRESS  = b"compress" # encoding format produced by the common UNIX file compression program "compress".
HTTP_CONTENT_ENCODING_DEFLATE   = b"deflate"  # The "zlib" format defined in RFC 1950 in combination with the "deflate"

HTTP_HEADER_CONTENT_TYPE  = b"Content-Type"

HTTP_CONTENT_TYPE_APP_JSON          = b"application/json"
HTTP_CONTENT_TYPE_APP_OCTET_STREAM  = b"application/octet-stream"

HTTP_CONTENT_TYPE_TEXT_HTML   = b"text/html"
HTTP_CONTENT_TYPE_TEXT_PLAIN  = b"text/plain"
HTTP_CONTENT_TYPE_TEXT_CSS    = b"text/css"
HTTP_CONTENT_TYPE_TEXT_XML    = b"text/xml"

HTTP_CONTENT_TYPE_IMAGE_GIF      = b"image/gif"
HTTP_CONTENT_TYPE_IMAGE_JPEG     = b"image/jpeg"
HTTP_CONTENT_TYPE_IMAGE_PNG      = b"image/png"
HTTP_CONTENT_TYPE_IMAGE_SVG_XML  = b"image/svg+xml"

HTTP_HEADER_CONTENT_LENGTH  = b"Content-Length"

HTTP_HEADER_TRANSFER_ENCODING                = b"Transfer-Encoding"
HTTP_HEADER_TRANSFER_ENCODING_CHUNKED        = b"chunked"
CHUNKED_TRANSFER_CODING_CR                   = b'\r'
CHUNKED_TRANSFER_CODING_LF                   = b'\n'
CHUNKED_TRANSFER_CODING_LAST_CHUNK           = b'0'
CHUNKED_TRANSFER_CODING_EXTENSION_SEPARATOR  = b';'

HTTP_HEADER_USER_AGENT  = b"User-Agent"

HTTP_HEADER_HOST  = b"Host"

HTTP_HEADER_LOCATION  = b"Location"

HTTP_HEADER_IF_MATCH  = b"If-Match"

HTTP_HEADER_IF_NONE_MATCH  = b"If-None-Match"

HTTP_HEADER_WWW_AUTHENTICATE  = b"WWW-Authenticate"
HTTP_HEADER_AUTHORIZATION  = b"Authorization"

HTTP_HEADER_ETAG  = b"ETag"

HTTP_HEADER_X_AUTH_TOKEN  = b"X-Auth-Token"
HTTP_HEADER_EXPECT  = b"Expect"
HTTP_EXPECT_100_CONTINUE  = b"100-continue"
HTTP_HEADER_CONTENT_RANGE  = b"Content-Range"
HTTP_HEADER_LAST_MODIFIED  = b"Last-Modified"
HTTP_HEADER_IF_UNMODIFIED_SINCE  = b"If-Unmodified-Since"
