#! /usr/bin/env python3

from sys import stdin
import urllib.parse
from base64 import b32decode
from datetime import datetime, timedelta, timezone
import hmac

for line in stdin:
    line = line.strip()
    if ':' in line:
        line = urllib.parse.urlsplit(line)
        assert line.scheme == 'otpauth' and line.netloc == 'totp'
        assert line.path.startswith('/')
        params = urllib.parse.parse_qs(line.query,
            strict_parsing=True, keep_blank_values=True)
        [secret] = params['secret']
        for [optional, expected] in (
            ('algorithm', ['SHA1']),
            ('digits', ['6']),
            ('counter', []),
            ('period', ['30']),
        ):
            found = params.get(optional)
            assert not found or found == expected
        account = urllib.parse.unquote(line.path[1:])
        [issuer, sep, account] = account.rpartition(':')
        if not sep:
            issuer = None
        account = account.lstrip(' ')
        iparam = params.get('issuer')
        if iparam:
            [iparam] = iparam
            if issuer is None:
                issuer = iparam
            if iparam == issuer:
                iparam = None
    else:
        secret = line.replace(' ', '')
        account = None
    
    x = timedelta(seconds=30)
    secret = b32decode(secret.upper())
    t0 = datetime(1970, 1, 1, tzinfo=timezone.utc)
    c = (datetime.now(timezone.utc) - t0) // x
    secret = hmac.digest(secret, c.to_bytes(8, 'big'), 'sha1')
    o = secret[19] & ~(~0 << 4)
    secret = int.from_bytes(secret[o : o + 4], 'big') & ~(~0 << 31)
    print(end=format(secret % 10**6, '06'))
    print('  ', end=(t0 + c*x).astimezone().time().isoformat('seconds'))
    if account is not None:
        print(end='  ')
        if issuer is not None:
            print(end=f'{issuer}: ')
        print(end=account)
        if iparam is not None:
            print(end=f' ({iparam})')
    print()
