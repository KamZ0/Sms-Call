import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))