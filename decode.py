#!/usr/bin/env python3
"""
Decode marshal+zlib+base85 obfuscated Python scripts (Python 3.12+).
Usage: python decode.py <input.py> <output.py>
"""

import marshal
import zlib
import base64
import random
import struct
import hashlib
import dis
import sys
import re
from typing import Any


def _strip_debug_guards(raw: str) -> str:
    """Remove anti-debug checks (_0q, _0p) from the obfuscated code."""
    idx = raw.find("#!/usr/bin/env python3")
    if idx == -1:
        for marker in ("_s0=__import__", "_m1=_s0('marshal')"):
            idx = raw.find(marker)
            if idx != -1:
                break
    if idx == -1:
        raise ValueError("Cannot find obfuscated code block")
    code = raw[idx:]
    code = re.sub(r"^\s*_0q\(\)\s*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"def _0p\(.+?except:return True\s*\n", "", code, flags=re.DOTALL)
    return code


def _load_vars(code: str) -> dict[str, Any]:
    """Execute variable definitions (_1c, _1d, _1e, _1f, _1g) in isolation."""
    data_start = code.find("\n_1c=")
    data_end = code.rfind("\n_1h=_1g()")
    if data_start == -1 or data_end == -1:
        raise ValueError("Cannot locate _1c/_1h markers")
    block = code[data_start + 1 : data_end]
    block = block.replace("_0p(", "(lambda *a: True)(")
    ns: dict[str, Any] = {}
    exec(block, ns)
    return ns


def _decode_payload(data: dict[str, Any]) -> bytes:
    """Mirrors _1g() to extract the raw marshal payload."""
    c, d, e, f = data["_1c"], data["_1d"], data["_1e"], data["_1f"]

    # reorder
    s = "".join(c)
    pb = base64.b85decode(d.encode())
    pi = [struct.unpack(">H", pb[i : i + 2])[0] for i in range(0, len(pb), 2)]
    o = [""] * len(c)
    for x, y in enumerate(pi):
        if y < len(c):
            o[y] = c[x]
    s = "".join(o)
    del o, pb, pi

    r = base64.b85decode(s.encode())  # decode base85
    del s

    g = random.Random(e)
    p = list(range(len(r)))
    g.shuffle(p)
    u = bytearray(len(r))
    for i, t in enumerate(p):
        u[i] = r[t]
    r = bytes(u)
    del u, p, g

    k = base64.b85decode(f.encode())
    chunks = [k[i : i + 32] for i in range(0, len(k), 32)]
    for chunk in chunks[::-1]:
        n = len(chunk)
        r = bytes(r[i] ^ chunk[i % n] for i in range(len(r)))
    del chunks, k

    return zlib.decompress(r)


def _format_const(c: Any, depth: int = 0) -> str:
    """Format a constant for display."""
    if isinstance(c, str):
        if "\n" in c and len(c) > 40:
            return f'"""{c}"""'
        return repr(c)
    if isinstance(c, bytes):
        return f"b{repr(c)}"
    if isinstance(c, (int, float)):
        return repr(c)
    if c is None:
        return "None"
    if hasattr(c, "co_code"):
        return f"<code object {c.co_name}>"
    return repr(c)[:200]


def _dump_code(co, indent: int = 0) -> str:
    """Dump a readable representation of a code object."""
    pad = "  " * indent
    lines = [f"{pad}=== Code: {co.co_name} ==="]
    lines.append(f'{pad}  file: {co.co_filename}')
    lines.append(f'{pad}  names: {co.co_names}')
    lines.append(f'{pad}  varnames: {co.co_varnames}')

    # Constants
    lines.append(f'{pad}  constants ({len(co.co_consts)}):')
    for i, c in enumerate(co.co_consts):
        if isinstance(c, str) and len(c) > 2:
            lines.append(f'{pad}    [{i}] {repr(c[:120])}')
        elif hasattr(c, 'co_code'):
            lines.append(f'{pad}    [{i}] <code {c.co_name}>')
        elif c is not None:
            lines.append(f'{pad}    [{i}] {_format_const(c)[:120]}')

    # Nested codes
    for c in co.co_consts:
        if hasattr(c, 'co_code'):
            lines.append("")
            lines.append(_dump_code(c, indent + 1))

    return "\n".join(lines)


def main(input_path: str, output_path: str):
    print(f"[decode] {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    code = _strip_debug_guards(raw)
    data = _load_vars(code)
    payload = _decode_payload(data)
    co = marshal.loads(payload)

    print(f"[decode] Code object: {co.co_name}")
    print(f"[decode] Names: {co.co_names}")

    header = [
        "# Decoded from obfuscated Python (marshal+zlib+base85)",
        f"# Code object name: {co.co_name}",
        f"# Top-level names: {co.co_names}",
        f"# Varnames: {co.co_varnames}",
        "",
        "import os, sys, time, random, hashlib, platform, requests",
        "from concurrent.futures import ThreadPoolExecutor, as_completed",
        "from sys import stdout, reconfigure",
        "",
        "# ===== Constants =====",
    ]

    for c in co.co_consts:
        if isinstance(c, str) and not c.startswith("\n") and len(c) > 3:
            if c.startswith("https://"):
                header.append(f'BASE_URL = "{c}"')
                header.append("APP_ID = 20")
            elif c.startswith("Mozilla"):
                header.append(f'UA = """{c}"""')
            else:
                header.append(f"# {c[:100]}")

    header.append("")
    header.append("# ===== Bytecode Structure =====")
    header.append(_dump_code(co))
    header.append("")
    header.append("# Use the original decode logic to reconstruct manually")
    header.append("# or run this module with Python 3.12+ to execute directly.")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(header))

    print(f"[decode] -> {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.py> <output.py>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])