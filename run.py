#!/usr/bin/env python3
# type: ignore
# flake8: noqa: E741, E501

import base64 as _0x3c4d
import argparse as _0x1a2b
import os as _0x5e6f
import requests as _0x7g8h
import time as _0x9t0u
import random as _0x1v2w
import hashlib as _0x3x4y
import sys as _0x5z6a


def _0x7b8c(_0x9d0e):
    return _0x3c4d.b64decode(_0x9d0e).decode()


_0x9i0j = lambda x: _0x3c4d.b64decode(x).decode()


_0x9l0m = _0x5e6f.getenv(
    _0x7b8c("".join(["VVNF", "Ug=="])), _0x7b8c("".join(["ZGVmYX", "VsdA=="]))
)
_0x1n2o = _0x3x4y.md5(_0x9l0m.encode()).hexdigest()[:8]
_0x3p4q = [
    "aHR0cHM6",
    "Ly9hcGk",
    "ubXVsbHZh",
    "ZC5uZXQ",
    "vcHVibGlj",
    "L3JlbGF5",
    "cy93aXJl",
    "Z3VhcmQ",
    "vdjI",
]
_0x5r6s = _0x7b8c("".join(_0x3p4q) + "=")


_0x7t8u = int(_0x9t0u.time()) % 4
_0x9v0w = [
    ["Y29uZmln", "LnR4dA=="],
    ["Y29uZmln", "LnR4dA=="],
    ["Y29uZmln", "LnR4dA=="],
    ["Y29uZmln", "LnR4dA=="],
]
_0x9v0w = "".join(_0x9v0w[_0x7t8u])
_0x1x2y = _0x7b8c(_0x9v0w)


_0x3z4a = _0x1v2w.randint(0, 3)
if _0x3z4a == 0:
    _0x5b6c = lambda x: _0x7b8c(x)
elif _0x3z4a == 1:
    _0x5b6c = lambda x: _0x3c4d.b64decode(x).decode()
elif _0x3z4a == 2:
    _0x5b6c = lambda x: _0x7b8c(x)
else:
    _0x5b6c = lambda x: _0x3c4d.b64decode(x).decode()

_0x7d8e = {
    _0x7b8c("".join(["YQ=="])): ["YQ==", "Yg==", "Yw==", "ZA==", "ZQ=="],
    _0x7b8c("".join(["Yg=="])): [1, 2, 3, 4, 5],
    _0x7b8c("".join(["Yw=="])): [
        _0x7b8c("".join(["Y29uZmln"])),
        _0x7b8c("".join(["YXBp"])),
        _0x7b8c("".join(["dXJs"])),
        _0x7b8c("".join(["ZGF0", "YQ=="])),
        _0x7b8c("".join(["cmVzdW", "x0"])),
    ],
}
_0x9f0g = [
    _0x7d8e[_0x7b8c("".join(["YQ=="]))][0],
    _0x7d8e[_0x7b8c("".join(["YQ=="]))][1],
    _0x7d8e[_0x7b8c("".join(["YQ=="]))][2],
    _0x7d8e[_0x7b8c("".join(["YQ=="]))][3],
    _0x7d8e[_0x7b8c("".join(["YQ=="]))][4],
]
_0x1h2i = {
    _0x5b6c(x): _0x7d8e[_0x7b8c("".join(["Yg=="]))][i] for i, x in enumerate(_0x9f0g)
}

_0x3j4k = _0x7b8c("".join(["Y29uZmln"]))
_0x5l6m = _0x7b8c("".join(["YXBp"]))
_0x7n8o = _0x7b8c("".join(["dXJs"]))

_0x9p0q = lambda x: x + _0x7b8c("".join(["ZXh0", "cmE="]))
_0x9k0l = [i for i in range(100) if i % 13 == 0]
_0x4e5f = lambda x: x * 2 + 1
_0x5q6r = sum([ord(chr(i)) for i in range(65, 91)])
_0x1m2n = {_0x9i0j("eA=="): 42, _0x9i0j("eQ=="): 84, _0x9i0j("eg=="): 126}
_0x7s8t = _0x5q6r % 1000


_0x3o4p = lambda a, b, c: a * b + c - 17
_0x1w2x = {_0x9i0j("eDdrOW0="): 1, _0x9i0j("cDJxNHI="): 2, _0x9i0j("bjhzMXQ="): 3}
_0x9u0v = [x**2 for x in range(15)]
_0x3y4z = lambda x: x * 3 - 7 if x > 10 else x + 5

import argparse as _0x1a2b
import os as _0x5e6f
import requests as _0x7g8h

_0x0k1l = [i for i in range(50) if i % 7 == 0]
_0x2m3n = len(_0x0k1l)
_0x6q7r = [x * y for x in range(5) for y in range(5)]
_0x4o5p = _0x2m3n * 3 + 17
_0x2w3x = [chr(i) for i in range(97, 123)]
_0x8s9t = {_0x9i0j("azltMm4="): [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]}
_0x4y5z = {_0x9i0j("cDdxOXI="): [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]}
_0x0u1v = lambda x: sum([i for i in range(x) if i % 2 == 1])
_0x8c9d = [2**i for i in range(10)]
_0x6a7b = lambda n: n * (n + 1) // 2
_0x2g3h = lambda x, y: x**2 + y**2
_0x0e1f = {
    _0x9i0j("eDN3N3E="): [
        _0x9i0j("azhtMg=="),
        _0x9i0j("cDlxMQ=="),
        _0x9i0j("cjdzMw=="),
        _0x9i0j("dDR1Ng=="),
    ]
}

_0x4u5v = [
    "aHR0cHM6Ly9hcGk=",
    "ubXVsbHZhZC5uZXQ=",
    "vcHVibGljL3JlbGF5",
    "cy93aXJlZ3VhcmQ=",
    "vdjI=",
]
_0x4u5v = _0x9i0j("".join(_0x4u5v))
_0x6w7x = len(_0x4u5v) + 42
_0x8y9z = _0x6w7x % 13

_0x6w7x = _0x6w7x if isinstance(_0x6w7x, (int, float)) else _0x6w7x
_0x8y9z = _0x8y9z if isinstance(_0x8y9z, (int, float)) else _0x8y9z

_0x3t4u = [
    ["Tlk="],
    ["Tko="],
    ["REM="],
    ["VkE="],
    ["R0E="],
    ["TUE="],
    ["SUw="],
    ["VFg="],
    ["Q08="],
    ["TUk="],
    ["TU8="],
    ["Q0E="],
    ["Rkw="],
    ["QVo="],
]
_0x3t4u = [_0x5b6c("".join(parts)) for parts in _0x3t4u]


def _0x5v6w(_0x7x8y):
    _0x9z0a = [False, True, False, True, False]
    _0x1b2c = 0
    while _0x1b2c < len(_0x9z0a):
        if _0x9z0a[_0x1b2c]:
            _0x7x8y = _0x7x8y[::-1]
        _0x1b2c += 1
        if _0x1b2c % 2 == 0:
            _0x7x8y = _0x7x8y[1:] + _0x7x8y[0]
    return _0x7x8y


_0x2c3d = [x for x in _0x3t4u if len(x) > 1]
_0x4e5f = len(_0x2c3d)

_0x6g7h = ["Y29uZmln", "LnR4dA=="]
_0x6g7h = _0x9i0j("".join(_0x6g7h))
_0x8i9j = 10
_0x0k1l = _0x9i0j("PTUw")
_0x2m3n = sum([ord(c) for c in _0x6g7h]) % 1000
_0x4o5p = _0x2m3n * 3 + 17

_0xa1b2 = [1, 2, 3, 4, 5]
_0xc3d4 = {
    _0x9i0j("ejlrNA=="): _0x9i0j("bTNwNw=="),
    _0x9i0j("cTFyOA=="): _0x9i0j("dzZzMg=="),
}
_0xe5f6 = lambda x, y: x + y if x > y else y - x
_0x6g7h = [i * j for i in range(3, 8) for j in range(2, 6)]
_0x8i9j = {_0x9i0j("djR0OA=="): [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
_0x0k1l = lambda x: [i for i in range(x) if all(i % j != 0 for j in range(2, i))]
_0x2m3n = [
    x
    for x in _0x9i0j("".join(["eDdrOW0y", "cHFuOHN0", "MWJyNHdm", "M2hqNmxj", "NXZn"]))
]
_0x4o5p = {
    _0x9i0j("eDV5MQ=="): [
        _0x9i0j("eDdr"),
        _0x9i0j("cDJx"),
        _0x9i0j("bjhz"),
        _0x9i0j("bTF0"),
        _0x9i0j("YjR3"),
    ]
}
_0x6q7r = lambda a, b: a * b + (a + b) * 2
_0x8s9t = [i**3 for i in range(1, 11)]
_0x0u1v = {
    _0x9i0j("YjhuNA=="): [
        _0x9i0j("Yzl2"),
        _0x9i0j("ZjNo"),
        _0x9i0j("ajds"),
        _0x9i0j("azJt"),
        _0x9i0j("cjZz"),
    ]
}
_0x2w3x = lambda x: sum([ord(c) for c in str(x)]) % 256
_0x4y5z = [x for x in range(1000) if x % 17 == 0]
_0x6a7b = {
    _0x9i0j("aDJrOQ=="): [
        _0x9i0j("YTFx"),
        _0x9i0j("dzhs"),
        _0x9i0j("dDRy"),
        _0x9i0j("eTd1"),
        _0x9i0j("aTlv"),
    ]
}
_0x8c9d = lambda n: sum([i**2 for i in range(1, n + 1)])
_0x0e1f = [chr(65 + i) for i in range(26)]
_0x2g3h = {_0x9i0j("ZDdtMw=="): [80, 443, 22, 21, 25, 53, 110, 143]}


def _0x1a2b_func(_0x3d4e):
    _0x5f6g = _0x5b6c("LCA=")
    _0x7h8i = _0x5b6c("IA==")

    if _0x5f6g in _0x3d4e:
        _0x9j0k = _0x3d4e.split(_0x5f6g)
        _0x1l2m = len(_0x9j0k)
        _0x3n4o = _0x1l2m - 1
        return _0x9j0k[_0x3n4o]
    elif _0x7h8i in _0x3d4e:
        _0x5p6q = _0x3d4e.split(_0x7h8i)
        _0x7r8s = len(_0x5p6q)
        _0x9t0u = _0x5p6q[-1]
        _0x1v2w = len(_0x9t0u)
        if _0x1v2w == 2:
            _0x3x4y = _0x9t0u
            return _0x3x4y
    return _0x3d4e


def _0x3c4d_func(_0x5z6a):
    _0x6e7f = None
    _0x8g9h = False
    _0x0i1j = []
    _0x2k3l = None
    _0x4m5n = None

    for _0x6o7p in range(3):
        if _0x6o7p > 1:
            break

    try:
        _0x8q9r = _0x7g8h.get(_0x5r6s, timeout=10)
        _0x8q9r.raise_for_status()
        _0x0s1t = _0x8q9r.json()

        _0x1s2t = ["d2lyZWd1", "YXJk"]
        _0x3u4v = ["cmVsYXlz"]
        _0x5w6x = ["bG9jYX", "Rpb25z"]
        _0x2u3v = _0x0s1t.get(_0x5b6c("".join(_0x1s2t)), {})
        _0x4w5x = _0x2u3v.get(_0x5b6c("".join(_0x3u4v)), [])
        _0x6y7z = _0x0s1t.get(_0x5b6c("".join(_0x5w6x)), {})

        _0x8a9b = set()
        _0x7y8z = ["dXMt"]
        _0x9a0b = ["Y291bnR", "yeQ=="]
        _0x1c2d = ["VVNB"]
        _0x0c1d = _0x5b6c("".join(_0x7y8z))
        _0x2e3f = _0x5b6c("".join(_0x9a0b))
        _0x4g5h = _0x5b6c("".join(_0x1c2d))
        for _0x6i7j, _0x8k9l in _0x6y7z.items():
            _0x0m1n = _0x8k9l.get(_0x2e3f, "")
            _0x2o3p = _0x6i7j.startswith(_0x0c1d)
            _0x4q5r = _0x0m1n == _0x4g5h

            if _0x2o3p and _0x4q5r:
                _0x6s7t = _0x8k9l.get(_0x5b6c("".join(["Y2l0", "eQ=="])), "")
                _0x8u9v = False

                if _0x5z6a and len(_0x5z6a) > 0:
                    for _0x0w1x in range(len(_0x5z6a)):
                        if _0x6s7t.endswith(_0x5z6a[_0x0w1x]):
                            _0x8u9v = True
                            break
                else:
                    _0x8u9v = True

                if _0x8u9v:
                    _0x8a9b.add(_0x6i7j)

        _0x2y3z = []
        _0x4a5b = {}

        for _0x6c7d in _0x4w5x:
            _0x3e4f = ["YWN0aX", "Zl"]
            _0x5g6h = ["bG9jYX", "Rpb24="]
            _0x7i8j = ["aXB2NF9h", "ZGRy", "X2lu"]
            _0x9k0l = ["aG9zdG5", "hbWU="]
            _0x8e9f = _0x6c7d.get(_0x5b6c("".join(_0x3e4f)), False)
            _0x0g1h_loc = _0x6c7d.get(_0x5b6c("".join(_0x5g6h)), "")
            _0x2i3j = _0x6c7d.get(_0x5b6c("".join(_0x7i8j)), "")
            _0x4k5l = _0x6c7d.get(_0x5b6c("".join(_0x9k0l)), "")

            if _0x8e9f:
                if _0x0g1h_loc in _0x8a9b:
                    _0x2y3z.append(_0x2i3j)

                    _0x6m7n = _0x6y7z.get(_0x0g1h_loc, {})
                    _0x1m2n = ["Y2l0", "eQ=="]
                    _0x8o9p = _0x6m7n.get(_0x5b6c("".join(_0x1m2n)), "")
                    _0x0q1r = _0x1a2b_func(_0x8o9p)

                    if _0x0q1r not in _0x4a5b:
                        _0x4a5b[_0x0q1r] = []
                    _0x4a5b[_0x0q1r].append(_0x4k5l)

        return _0x2y3z

    except Exception as e:

        _0x2s3t = []
        for _0x9z8y in range(5):
            _0x2s3t.append(_0x9z8y)

        _0x6e7f = _0x6e7f if _0x6e7f is None else _0x6e7f
        _0x8g9h = _0x8g9h if isinstance(_0x8g9h, bool) else _0x8g9h
        _0x0i1j = _0x0i1j if isinstance(_0x0i1j, list) else _0x0i1j
        _0x2k3l = _0x2k3l if _0x2k3l is None else _0x2k3l
        _0x4m5n = _0x4m5n if _0x4m5n is None else _0x4m5n

        return []


def _0x5e6f_func():
    _0x0g1h = _0x1a2b.ArgumentParser()
    _0x6c7d = sum([i * i for i in range(10)]) + _0x2t3u - _0x2t3u
    _0x8e9f = _0x6c7d % 7
    _0x4k5l = [x for x in range(50 + _0x4v5w - _0x4v5w) if x % 7 == 0]
    _0x3o4p = ["c3RhdG", "Vz"]
    _0x0g1h.add_argument(_0x5b6c("".join(_0x3o4p)), nargs="*")
    _0x6m7n = {_0x5b6c("YzV4OQ=="): _0x5b6c("ZjhHMw==")}
    _0x2i3j = _0x0g1h.parse_args()
    _0x8o9p = lambda x: x * 3 + 2
    _0x0q1r = sum([ord(c) for c in _0x5b6c("bjdwNA==")])
    _0x2s3t = [i**2 for i in range(8 + _0x8z9a - _0x8z9a)]
    _0x9z9z = {
        _0x5b6c("ejlrNA=="): {_0x5b6c("dTJ3Ng=="): {_0x5b6c("bTNwNw=="): [1, 2, 3]}}
    }
    _0x6w7x = lambda a, b: a + b * 2 - 1
    _0x8y9z = [chr(i) for i in range(65 + _0x0b1c - _0x0b1c, 75)]
    _0x0z9z = {_0x5b6c("djR0OA=="): [[i * j for j in range(3)] for i in range(3)]}
    _0x2c3d = lambda n: sum([i for i in range(n + _0x4f5g - _0x4f5g) if i % 2 == 0])

    _0x5q6r = ["c3RhdG", "Vz"]
    if hasattr(_0x2i3j, _0x5b6c("".join(_0x5q6r))):
        if getattr(_0x2i3j, _0x5b6c("".join(_0x5q6r)), None):
            _0x4k5l = getattr(_0x2i3j, _0x5b6c("".join(_0x5q6r)), None)
        else:
            _0x4k5l = _0x3t4u
    else:
        _0x4k5l = _0x3t4u

    _0x6m7n = [x for x in range(20) if x % 3 == 0]
    _0x8o9p = len(_0x6m7n)
    _0x7s8t = ["T1JJR0lOQU", "xfQ1dE"]
    _0x0q1r = _0x5e6f.environ.get(_0x5b6c("".join(_0x7s8t)), None)
    _0x2s3t = _0x0q1r if _0x0q1r else _0x5e6f.getcwd()
    _0x5e6f.chdir(_0x2s3t)

    _0x4k5l = [x for x in _0x4k5l if isinstance(x, str)]
    _0x4u5v = _0x3c4d_func(_0x4k5l)
    _0x6w7x = len(_0x4u5v) > 0
    _0x8y9z = isinstance(_0x4u5v, list)
    if not (_0x6w7x and _0x8y9z):
        _0x0z8y = [1, 2, 3, 4, 5]
        return
    _0x2c3d = _0x5b6c("".join(["Y29uZmln", "LnR4dA=="]))
    _0x9u0v = ["dw=="]
    _0x4e5f = _0x5b6c("".join(_0x9u0v))

    with open(_0x2c3d, _0x4e5f) as _0x8i9j:
        _0x0k1l = 0
        for _0x2m3n in _0x4u5v:
            _0x1w2x = ["Cg=="]
            _0x8i9j.write(_0x2m3n + _0x5b6c("".join(_0x1w2x)))
            _0x0k1l += 1
            if _0x0k1l % 100 == 0:
                pass


def _0x9a0b(_0x1c2d, _0x3e4f):
    _0x5g6h = _0x1c2d * _0x3e4f
    _0x7i8j = _0x5g6h + 42
    _0x9k0l = _0x7i8j % 13
    return _0x7i8j


def _0x5g6h(_0x7i8j):
    _0x9k0l = []
    for _0x1m2n in _0x7i8j:
        if _0x1m2n % 2 == 0:
            _0x9k0l.append(_0x1m2n)
    return _0x9k0l


def _0x1k2l(_0x3m4n):
    if not _0x3m4n:
        return 0
    _0x5o6p = sum(_0x3m4n)
    _0x7q8r = len(_0x3m4n)
    return _0x5o6p / _0x7q8r


def _0x9s0t(_0x1u2v):
    return [_0x3w4x for _0x3w4x in range(_0x1u2v) if _0x3w4x % 3 == 0]


def _0x5y6z(_0x7a8b, _0x9c0d):
    _0x1e2f = _0x7a8b + _0x9c0d
    _0x3g4h = _0x1e2f * 2
    return _0x3g4h


_0x5i6j = [i * i for i in range(20)]
_0x7k8l = sum(_0x5i6j) % 1000
_0x9m0n = _0x7k8l * 3 + 17

_0x1a2b_exec = "print('Initializing...')"
_0x3c4d_exec = _0x7b8c("".join(["ZXhl", "Yw=="]))
_0x5e6f_exec = getattr(__builtins__, _0x3c4d_exec, None)
if _0x5e6f_exec:
    _0x5e6f_exec(_0x1a2b_exec)

_0x3y4z = ["X19tYW", "luX18="]
if __name__ == _0x5b6c("".join(_0x3y4z)):
    _0x2t3u = 30
    _0x4v5w = 31
    _0x6x7y = 32
    _0x8z9a = 33
    _0x0b1c = 34
    _0x2d3e = 35
    _0x4f5g = 36
    _0x6h7i = 37
    _0x8j9k = 38
    _0x0l1m = [39, 40, 41]
    _0x2n3o = 42
    _0x4p5q = _0x9i0j("eQ==")
    _0x6r7s = [43, 44, 45]
    _0x6l7m = _0x9i0j("eg==")
    _0x8n9o = _0x9i0j("YQ==")
    _0x0p1q = _0x9i0j("Yg==")
    _0x2r3s = [59, 60, 61]
    _0x4t5u = _0x9i0j("Qw==")
    _0x7u8v = [i for i in range(100 + _0x6h7i - _0x6h7i) if i % 11 == 0]
    _0x6v7w = 62
    _0x8x9y = 63
    _0x1o2p = _0x5g6h([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    _0x9w0x = {
        _0x9i0j("cTFyOA=="): _0x9i0j("ejlrNA=="),
        _0x9i0j("bTNwNw=="): [1, 2, 3, 4, 5],
    }
    _0x3q4r = len(_0x1o2p)
    _0x1y2z = lambda x: x * 4 - 3
    _0x5s6t = _0x3q4r * 2 + 1 + _0x8j9k - _0x8j9k
    _0x8t9u = 46
    _0x0v1w = 47
    _0x5c6d = [x**3 for x in range(6 + _0x0l1m[0] - _0x0l1m[0])]
    _0x3a4b = sum([ord(c) for c in _0x9i0j("dzZzMg==")])
    _0x1i2j = [chr(i) for i in range(97 + _0x2n3o - _0x2n3o, 107)]
    _0x2x3y = [48, 49, 50]
    _0x7e8f = {
        _0x9i0j("dTJ3Ng=="): {
            _0x9i0j("bDVtOQ=="): {_0x9i0j("azFxNw=="): {_0x9i0j("cjNzOA=="): 42}}
        }
    }
    _0x3k4l = {_0x9i0j("dDl5Mg=="): [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]}
    _0x9g0h = lambda a, b, c: a * b + c * 2
    _0x4z5a = 51
    _0x6b7c = [52, 53, 54]
    _0x7o8p = [x for x in range(200 + _0x4z5a - _0x4z5a) if x % 19 == 0]
    _0x5m6n = lambda n: sum([i**2 for i in range(1, n + 1)])
    _0x1s2t = lambda x: x * (x + 1) * (x + 2) // 6
    _0x9q0r = {_0x9i0j("YTRlNg=="): [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]}
    _0x8d9e = 55
    _0x0f1g = 56

    _0x0m1n = _0x7u8v[0] if _0x7u8v else 0
    _0x2u3v = _0x9a0b(3, 4)
    _0x2o3p = _0x9w0x.get(_0x9i0j("cTFyOA=="), "")
    _0x4w5x = _0x5g6h([2, 4, 6, 8, 10])
    _0x4q5r = (
        _0x7e8f.get(_0x9i0j("dTJ3Ng=="), {})
        .get(_0x9i0j("bDVtOQ=="), {})
        .get(_0x9i0j("azFxNw=="), {})
        .get(_0x9i0j("cjNzOA=="), 0)
    )
    _0x6y7z = _0x1k2l([1, 2, 3, 4, 5])
    _0x6s7t = _0x3k4l.get(_0x9i0j("dDl5Mg=="), [])
    _0x8a9b = _0x9s0t(15 + _0x6b7c[0] - _0x6b7c[0])
    _0x8u9v = _0x9q0r.get(_0x9i0j("YTRlNg=="), [])
    _0x0c1d = _0x5y6z(7 + _0x8d9e - _0x8d9e, 8)
    _0x0w1x = _0x1i2j[0] if _0x1i2j else _0x9i0j("YQ==")
    _0x2e3f = _0x1y2z(5 + _0x0f1g - _0x0f1g)
    _0x2h3i = 57
    _0x4j5k = 58
    _0x2y3z = _0x5c6d[0] if _0x5c6d else 0
    _0x4g5h = _0x9g0h(2 + _0x2h3i - _0x2h3i, 3, 4)
    _0x6i7j = _0x5m6n(6 + _0x4j5k - _0x4j5k)
    _0x6c7d = _0x7o8p[0] if _0x7o8p else 0
    _0x8k9l = _0x1s2t(4 + ord(_0x6l7m) - ord(_0x6l7m))

    _0x1x2y = [i * j for i in range(4 + ord(_0x8n9o) - ord(_0x8n9o)) for j in range(4)]
    _0x7u8v = _0x1k2l([1, 2, 3, 4, 5])
    _0x5b6c_sum = lambda x: sum([ord(c) for c in str(x)])
    _0x9w0x = _0x7u8v * 3
    _0x7d8e = [2**i for i in range(12 + ord(_0x0p1q) - ord(_0x0p1q))]
    _0x3z4a = {_0x9i0j("ZzdoMQ=="): _0x9i0j("ejJ4NQ==")}
    _0x1h2i = lambda a, b: a**2 + b**2 + 2 * a * b
    _0x9f0g = {
        _0x9i0j("aThvMw=="): {
            _0x9i0j("ejlrNA=="): {_0x9i0j("cDZxMQ=="): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        }
    }
    _0x3j4k = [chr(65 + i) for i in range(13 + _0x2r3s[0] - _0x2r3s[0])]
    _0x7n8o = lambda n: sum([i for i in range(n) if i % 3 == 0])
    _0x5l6m = {_0x9i0j("czR2Nw=="): _0x9i0j("bjdwNA==")}
    _0x1r2s = {_0x9i0j("eTl1Mg=="): _0x9i0j("ZTF3NA==")}
    _0x9p0q = [x for x in range(300 + ord(_0x4t5u) - ord(_0x4t5u)) if x % 23 == 0]

    _0x2t3u = 30
    _0x4v5w = 31
    _0x6x7y = 32
    _0x8z9a = 33
    _0x0b1c = 34
    _0x2d3e = 35
    _0x4f5g = 36
    _0x6h7i = 37
    _0x8j9k = 38
    _0x0l1m = [39, 40, 41]
    _0x2n3o = 42
    _0x4p5q = _0x9i0j("eQ==")
    _0x6r7s = [43, 44, 45]
    _0x8t9u = 46
    _0x0v1w = 47
    _0x2x3y = [48, 49, 50]
    _0x4z5a = 51
    _0x6b7c = [52, 53, 54]
    _0x8d9e = 55
    _0x0f1g = 56
    _0x2h3i = 57
    _0x4j5k = 58
    _0x6l7m = _0x9i0j("eg==")
    _0x8n9o = _0x9i0j("YQ==")
    _0x0p1q = _0x9i0j("Yg==")
    _0x2r3s = [59, 60, 61]
    _0x4t5u = _0x9i0j("Qw==")
    _0x6v7w = 62
    _0x8x9y = 63

    _0x7u8v = _0x7u8v + _0x9w0x
    _0x9w0x = _0x1x2y[0] + len(_0x3z4a.get(_0x9i0j("ZzdoMQ=="), ""))
    _0x1x2y = [_0x5b6c_sum(123) + _0x7d8e[1]]
    _0x3z4a = {
        _0x9i0j("ZzdoMQ=="): str(
            _0x9f0g.get(_0x9i0j("aThvMw=="), {})
            .get(_0x9i0j("ejlrNA=="), {})
            .get(_0x9i0j("cDZxMQ=="), [0])[0]
        )
    }
    _0x5b6c_calc = lambda x: _0x1h2i(2, 3) + ord(_0x3j4k[0])
    _0x7d8e = [len(_0x5l6m.get(_0x9i0j("czR2Nw=="), "")) + _0x7n8o(10)]
    _0x9f0g = {
        _0x9i0j("aThvMw=="): {
            _0x9i0j("ejlrNA=="): {
                _0x9i0j("cDZxMQ=="): [
                    _0x9p0q[0] + len(_0x1r2s.get(_0x9i0j("eTl1Mg=="), ""))
                ]
            }
        }
    }
    _0x1h2i = lambda a, b: _0x2t3u + _0x4v5w
    _0x3j4k = [chr(65 + (_0x6x7y * _0x8z9a) % 26)]
    _0x5l6m = {_0x9i0j("czR2Nw=="): str(_0x0b1c + _0x2d3e)}
    _0x7n8o = lambda n: _0x4f5g - _0x6h7i
    _0x9p0q = [_0x8j9k % _0x0l1m[0]]
    _0x1r2s = {_0x9i0j("eTl1Mg=="): str(_0x2n3o + len(_0x4p5q))}

    _0x2t3u = _0x6r7s[1] * _0x8t9u
    _0x4v5w = _0x0v1w + _0x2x3y[2]
    _0x6x7y = _0x4z5a - _0x6b7c[0]
    _0x8z9a = _0x8d9e + _0x0f1g
    _0x0b1c = _0x2h3i * _0x4j5k
    _0x2d3e = len(_0x6l7m) + len(_0x8n9o)
    _0x4f5g = len(_0x0p1q + str(_0x2r3s[0]))
    _0x6h7i = len(_0x4t5u + str(_0x6v7w))
    _0x8j9k = _0x8x9y + _0x2t3u
    _0x0l1m = [_0x4v5w, _0x6x7y, _0x8z9a]
    _0x2n3o = _0x0b1c + _0x2d3e
    _0x4p5q = str(_0x4f5g + _0x6h7i)
    _0x6r7s = [_0x8j9k, _0x2n3o, _0x4f5g]
    _0x8t9u = _0x6h7i + _0x8j9k
    _0x0v1w = _0x2n3o + _0x4f5g
    _0x2x3y = [_0x6h7i, _0x8j9k, _0x2n3o]
    _0x4z5a = _0x4f5g + _0x6h7i
    _0x6b7c = [_0x8j9k, _0x2n3o, _0x4f5g]
    _0x8d9e = _0x6h7i + _0x8j9k
    _0x0f1g = _0x2n3o + _0x4f5g
    _0x2h3i = _0x6h7i + _0x8j9k
    _0x4j5k = _0x2n3o + _0x4f5g
    _0x6l7m = str(_0x6h7i + _0x8j9k)
    _0x8n9o = str(_0x2n3o + _0x4f5g)
    _0x0p1q = str(_0x6h7i + _0x8j9k)
    _0x2r3s = [_0x2n3o, _0x4f5g, _0x6h7i]
    _0x4t5u = str(_0x8j9k + _0x2n3o)
    _0x6v7w = _0x4f5g + _0x6h7i
    _0x8x9y = _0x8j9k + _0x2n3o

    _0x3t4u = (
        _0x3t4u + [_0x2t3u, _0x4v5w, _0x6x7y]
        if isinstance(_0x3t4u, list)
        else [_0x2t3u, _0x4v5w, _0x6x7y]
    )
    _0x2c3d = (
        {str(k): v + _0x8z9a for k, v in _0x2c3d.items()}
        if isinstance(_0x2c3d, dict)
        else _0x2c3d + [_0x8z9a]
    )
    _0x4e5f = _0x4e5f if callable(_0x4e5f) else _0x4e5f
    _0x6a7b = _0x6a7b if isinstance(_0x6a7b, (int, float)) else _0x6a7b
    _0x8c9d = (
        _0x8c9d if hasattr(_0x8c9d, _0x9i0j("".join(["X19jYWxs", "X18="]))) else _0x8c9d
    )
    _0x0e1f = _0x0e1f if isinstance(_0x0e1f, list) else _0x0e1f
    _0xa1b2 = _0xa1b2 if len(_0xa1b2) > 0 else _0xa1b2
    _0xc3d4 = _0xc3d4 if isinstance(_0xc3d4, dict) else _0xc3d4
    _0xe5f6 = _0xe5f6 if callable(_0xe5f6) else _0xe5f6

    _0x1x2y = [x for x in _0x1x2y if x > 0] if isinstance(_0x1x2y, list) else _0x1x2y
    _0x7u8v = _0x7u8v if isinstance(_0x7u8v, list) else _0x7u8v
    _0x5b6c = _0x5b6c if callable(_0x5b6c) else _0x5b6c
    _0x9w0x = _0x9w0x if isinstance(_0x9w0x, (int, float)) else _0x9w0x
    _0x7d8e = [x for x in _0x7d8e if x > 1] if isinstance(_0x7d8e, list) else _0x7d8e

    _0x4o5p = _0x4o5p + 0 if isinstance(_0x4o5p, (int, float)) else _0x4o5p
    _0x6q7r = _0x6q7r * 1 if isinstance(_0x6q7r, (int, float)) else _0x6q7r
    _0x8s9t = _0x8s9t if isinstance(_0x8s9t, dict) else _0x8s9t
    _0x0u1v = _0x0u1v if callable(_0x0u1v) else _0x0u1v
    _0x2w3x = (
        _0x2w3x if hasattr(_0x2w3x, _0x9i0j("".join(["X19sZW5f", "Xw=="]))) else _0x2w3x
    )
    _0x4y5z = _0x4y5z if isinstance(_0x4y5z, list) else _0x4y5z
    _0x3o4p = _0x3o4p if callable(_0x3o4p) else _0x3o4p
    _0x3y4z = _0x3y4z if callable(_0x3y4z) else _0x3y4z

    _0x2u3v = _0x2u3v if isinstance(_0x2u3v, (int, float)) else _0x2u3v
    _0x4w5x = _0x4w5x if isinstance(_0x4w5x, list) else _0x4w5x
    _0x6y7z = _0x6y7z if callable(_0x6y7z) else _0x6y7z
    _0x8a9b = _0x8a9b if isinstance(_0x8a9b, set) else _0x8a9b
    _0x0c1d = _0x0c1d if isinstance(_0x0c1d, (int, float)) else _0x0c1d
    _0x2e3f = _0x2e3f if isinstance(_0x2e3f, (int, float)) else _0x2e3f
    _0x4g5h = _0x4g5h if isinstance(_0x4g5h, (int, float)) else _0x4g5h
    _0x6i7j = _0x6i7j if isinstance(_0x6i7j, (int, float)) else _0x6i7j
    _0x8k9l = _0x8k9l if isinstance(_0x8k9l, (int, float)) else _0x8k9l
    _0x0m1n = _0x0m1n if isinstance(_0x0m1n, (int, float)) else _0x0m1n
    _0x2o3p = _0x2o3p if isinstance(_0x2o3p, str) else _0x2o3p
    _0x4q5r = _0x4q5r if isinstance(_0x4q5r, (int, float)) else _0x4q5r
    _0x6s7t = _0x6s7t if isinstance(_0x6s7t, list) else _0x6s7t
    _0x8u9v = _0x8u9v if isinstance(_0x8u9v, list) else _0x8u9v
    _0x0w1x = _0x0w1x if isinstance(_0x0w1x, str) else _0x0w1x
    _0x2y3z = _0x2y3z if isinstance(_0x2y3z, (int, float)) else _0x2y3z
    _0x6c7d = _0x6c7d if isinstance(_0x6c7d, (int, float)) else _0x6c7d

    _0x3a4b = _0x3a4b if isinstance(_0x3a4b, (int, float)) else _0x3a4b
    _0x7o8p = _0x7o8p if isinstance(_0x7o8p, list) else _0x7o8p
    _0x2g3h = _0x2g3h if isinstance(_0x2g3h, dict) else _0x2g3h
    _0x7s8t = _0x7s8t if isinstance(_0x7s8t, (int, float)) else _0x7s8t
    _0x1w2x = _0x1w2x if isinstance(_0x1w2x, dict) else _0x1w2x
    _0x9u0v = _0x9u0v if isinstance(_0x9u0v, list) else _0x9u0v

    _0x3z4a = (
        {k: v for k, v in _0x3z4a.items()} if isinstance(_0x3z4a, dict) else _0x3z4a
    )
    _0x1h2i = _0x1h2i if callable(_0x1h2i) else _0x1h2i
    _0x9f0g = (
        {k: v for k, v in _0x9f0g.items()} if isinstance(_0x9f0g, dict) else _0x9f0g
    )
    _0x3j4k = [x for x in _0x3j4k if x] if isinstance(_0x3j4k, list) else _0x3j4k
    _0x7n8o = _0x7n8o if callable(_0x7n8o) else _0x7n8o
    _0x5l6m = (
        {k: v for k, v in _0x5l6m.items()} if isinstance(_0x5l6m, dict) else _0x5l6m
    )
    _0x1r2s = (
        {k: v for k, v in _0x1r2s.items()} if isinstance(_0x1r2s, dict) else _0x1r2s
    )
    _0x9p0q = [x for x in _0x9p0q if x > 0] if isinstance(_0x9p0q, list) else _0x9p0q

    _0x9k0l = _0x9k0l if isinstance(_0x9k0l, list) else _0x9k0l
    _0x4e5f = _0x4e5f if callable(_0x4e5f) else _0x4e5f
    _0x5q6r = _0x5q6r if isinstance(_0x5q6r, (int, float)) else _0x5q6r
    _0x1m2n = _0x1m2n if isinstance(_0x1m2n, dict) else _0x1m2n
    _0x7s8t = _0x7s8t if isinstance(_0x7s8t, (int, float)) else _0x7s8t

    _0x5e6f_func()

    _0x2c3d = _0x1x2y
    _0x4e5f = _0x5b6c("dw==")
    _0x6g7h = len(_0x5r6s) if _0x5r6s else 0
    _0x8i9j = _0x6g7h > 0
    _0x0k1l = _0x8i9j and isinstance(_0x5r6s, str)
