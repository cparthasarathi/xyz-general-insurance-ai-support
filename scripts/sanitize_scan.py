#!/usr/bin/env python3
"""Basic public-repository hygiene scanner; not a substitute for DLP/secret scanning."""
from pathlib import Path
import re
import sys

SKIP_PARTS = {".git", ".venv", "__pycache__", "node_modules"}
PATTERNS = {
    "email-like value": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "AWS access key pattern": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key header": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "bearer token": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/-]{16,}", re.I),
    "possible secret assignment": re.compile(r"(?i)\b(api[_-]?key|password|client_secret|access_token)\s*[:=]\s*\S{8,}"),
}
TEXT_EXTS = {".py", ".md", ".json", ".yaml", ".yml", ".toml", ".ini", ".env", ".txt", ".sh"}


def main(root: Path) -> int:
    findings = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_EXTS and path.name not in {".env.example"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                # Do not print matched content; only report file, rule and line.
                line = text.count("\n", 0, match.start()) + 1
                findings.append((path, label, line))
    if findings:
        print("Potential sanitization findings (review manually):")
        for path, label, line in findings:
            print(f"- {path}:{line}: {label}")
        return 1
    print("No matches for the configured basic patterns. This is not proof that the repository is sanitized.")
    return 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    raise SystemExit(main(target))
