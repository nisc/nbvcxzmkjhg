#!/usr/bin/env python3
# type: ignore
# flake8: noqa: E741, E501

import argparse
import base64
import os
import requests

U = base64.b64decode(
    "aHR0cHM6Ly9hcGkubXVsbHZhZC5uZXQvcHVibGljL3JlbGF5cy93aXJlZ3VhcmQvdjI="
).decode()
S = [
    base64.b64decode("Tlk=").decode(),
    base64.b64decode("Tko=").decode(),
    base64.b64decode("REM=").decode(),
    base64.b64decode("VkE=").decode(),
    base64.b64decode("R0E=").decode(),
    base64.b64decode("TUE=").decode(),
    base64.b64decode("SUw=").decode(),
    base64.b64decode("VFg=").decode(),
    base64.b64decode("Q08=").decode(),
    base64.b64decode("TUk=").decode(),
    base64.b64decode("TU8=").decode(),
    base64.b64decode("Q0E=").decode(),
    base64.b64decode("Rkw=").decode(),
    base64.b64decode("QVo=").decode(),
]
O = base64.b64decode("Y29uZmlnLnR4dA==").decode()
M = 10
SEP = base64.b64decode("PTUw").decode()


def e(c):
    if base64.b64decode("LCA=").decode() in c:
        return c.split(base64.b64decode("LCA=").decode())[-1]
    elif base64.b64decode("IA==").decode() in c:
        p = c.split(base64.b64decode("IA==").decode())
        if len(p[-1]) == 2:
            return p[-1]
    return c


def g(t):
    try:
        r = requests.get(U, timeout=10)
        r.raise_for_status()
        d = r.json()

        w = d[base64.b64decode("d2lyZWd1YXJk").decode()][
            base64.b64decode("cmVsYXlz").decode()
        ]
        l = d[base64.b64decode("bG9jYXRpb25z").decode()]

        tl = set()
        for k, v in l.items():
            if (
                k.startswith(base64.b64decode("dXMt").decode())
                and v[base64.b64decode("Y291bnRyeQ==").decode()]
                == base64.b64decode("VVNB").decode()
            ):
                c = v[base64.b64decode("Y2l0eQ==").decode()]
                if any(c.endswith(s) for s in t):
                    tl.add(k)

        ti = []
        rb = {}

        for relay in w:
            if (
                relay[base64.b64decode("YWN0aXZl").decode()]
                and relay[base64.b64decode("bG9jYXRpb24=").decode()] in tl
            ):
                ti.append(relay[base64.b64decode("aXB2NF9hZGRyX2lu").decode()])

                c = l[relay[base64.b64decode("bG9jYXRpb24=").decode()]][
                    base64.b64decode("Y2l0eQ==").decode()
                ]
                s = e(c)
                if s not in rb:
                    rb[s] = []
                rb[s].append(relay[base64.b64decode("aG9zdG5hbWU=").decode()])

        return ti

    except Exception:
        return []


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        base64.b64decode("c3RhdGVz").decode(),
        nargs="*",
    )
    a = p.parse_args()

    t = a.states if a.states else S

    cwd = os.environ.get(base64.b64decode("T1JJR0lOQUxfQ1dE").decode(), os.getcwd())
    os.chdir(cwd)

    i = g(t)

    if not i:
        return

    with open(O, base64.b64decode("dw==").decode()) as f:
        for ip in i:
            f.write(f"{ip}\n")


if __name__ == base64.b64decode("X19tYWluX18=").decode():
    main()
