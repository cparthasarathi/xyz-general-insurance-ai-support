"""Small, dependency-free chunking examples for sanitized reference data.

The word-count approximation is for demos only. For production, use a tokenizer
appropriate to the selected embedding model and the configured Knowledge Base.
"""
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    document_type: str
    title: str
    text: str
    metadata: dict[str, str]


def _words(text: str) -> list[str]:
    return re.findall(r"\S+", text)


def fixed_chunks(
    text: str,
    *,
    document_id: str,
    document_type: str,
    title: str,
    chunk_words: int = 110,
    overlap_words: int = 12,
    metadata: dict[str, str] | None = None,
) -> list[Chunk]:
    """Fixed-size fallback that keeps modest overlap between adjacent chunks."""
    if chunk_words < 1:
        raise ValueError("chunk_words must be >= 1")
    if overlap_words < 0 or overlap_words >= chunk_words:
        raise ValueError("overlap_words must be >= 0 and < chunk_words")
    words = _words(text)
    if not words:
        return []
    stride = chunk_words - overlap_words
    output = []
    for start in range(0, len(words), stride):
        piece = words[start:start + chunk_words]
        if not piece:
            break
        idx = len(output) + 1
        output.append(Chunk(
            chunk_id=f"{document_id}#{idx}",
            document_id=document_id,
            document_type=document_type,
            title=title,
            text=" ".join(piece),
            metadata=dict(metadata or {}),
        ))
        if start + chunk_words >= len(words):
            break
    return output


def incident_chunks(
    incidents: list[dict],
) -> list[Chunk]:
    """Keep each incident record intact; caller should split long histories by stage."""
    output = []
    for incident in incidents:
        required = ("incident_id", "title", "symptoms", "resolution")
        missing = [key for key in required if not incident.get(key)]
        if missing:
            raise ValueError(f"Incident missing required fields: {', '.join(missing)}")
        text = (
            f"Incident: {incident['incident_id']}\n"
            f"Title: {incident['title']}\n"
            f"Symptoms: {incident['symptoms']}\n"
            f"Root cause: {incident.get('root_cause', 'Not documented')}\n"
            f"Resolution: {incident['resolution']}\n"
            f"Verification: {incident.get('verification', 'Not documented')}"
        )
        output.append(Chunk(
            chunk_id=f"{incident['incident_id']}#1",
            document_id=incident["incident_id"],
            document_type="incident",
            title=incident["title"],
            text=text,
            metadata={
                "application": incident.get("application", "unknown"),
                "category": incident.get("category", "unknown"),
                "status": incident.get("status", "resolved"),
            },
        ))
    return output


def section_chunks(
    document: str,
    *,
    document_id: str,
    document_type: str,
    metadata: dict[str, str] | None = None,
) -> list[Chunk]:
    """Split markdown on headings and preserve each heading with its section text."""
    lines = document.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_title = "Introduction"
    current_lines: list[str] = []
    for line in lines:
        if line.lstrip().startswith("#"):
            if current_lines:
                sections.append((current_title, current_lines))
            current_title = line.lstrip("# ").strip() or "Untitled section"
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_title, current_lines))

    output = []
    for i, (title, body) in enumerate(sections, start=1):
        text = "\n".join([title, *body]).strip()
        if text:
            output.append(Chunk(
                chunk_id=f"{document_id}#{i}",
                document_id=document_id,
                document_type=document_type,
                title=title,
                text=text,
                metadata=dict(metadata or {}),
            ))
    return output
