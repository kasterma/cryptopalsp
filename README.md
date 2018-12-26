# CryptoPals

Working on the challenges of the crypto pals problem set.

## Notes: Set 1

Rule: always operate on raw bytes, never on encoded strings.  Only use hex and base64 for pretty-printing.

This means always use bytes.fromhex() or base64.b64decode(s.encode('utf-8'))

TODO: check that inded utf-8 and ascii overlap in encoding.

`base64.b64decode` by default applies an ascii encoding if a string is passed in.  Hence the fact you _need_ to
decode the output of `base64.b64encode` from bytes to a string while it is not required to encode the input to
`base64.b64encode` is explained.  Can't do the automatic decode since don't know purpose of use.
