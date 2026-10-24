"""Local lexical retriever over fictional documents.

Replace this adapter with Bedrock Knowledge Bases Retrieve/RetrieveAndGenerate
for an AWS deployment. This module deliberately does not call AWS.
"""
from pathlib import Path
import re
from app.models import Evidence

KNOWLEDGE_DIR = Path(__file__).parent / "data" / "knowledge"


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_-]+", text.lower()))


def retrieve(query: str, top_k: int = 5) -> list[Evidence]:
    q = _tokens(query)
    if not q:
        return []
    results = []
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        title = next((line.lstrip("# ").strip() for line in lines if line.startswith("#")), path.stem)
        doc_tokens = _tokens(text)
        intersection = q & doc_tokens
        if not intersection:
            continue
        score = len(intersection) / max(len(q), 1)
        excerpt = " ".join(line.strip() for line in lines if line.strip() and not line.startswith("#"))
        results.append(Evidence(
            document_id=path.stem,
            title=title,
            excerpt=excerpt[:700],
            source_type="synthetic_knowledge_document",
            relevance_score=round(score, 3),
        ))
    return sorted(results, key=lambda item: item.relevance_score, reverse=True)[:max(1, min(top_k, 10))]
