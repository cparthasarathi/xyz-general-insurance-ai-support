from app.chunking import fixed_chunks, incident_chunks, section_chunks


def test_fixed_chunks_has_overlap_and_ids():
    chunks = fixed_chunks(
        "one two three four five six seven eight",
        document_id="DOC-1", document_type="sop", title="Test",
        chunk_words=4, overlap_words=1,
    )
    assert len(chunks) == 3
    assert chunks[0].text.endswith("four")
    assert chunks[1].text.startswith("four")
    assert chunks[0].chunk_id == "DOC-1#1"


def test_incident_chunk_preserves_incident_boundary():
    chunks = incident_chunks([{
        "incident_id": "DEMO-INC-1",
        "title": "Sample issue",
        "symptoms": "A timeout occurred",
        "resolution": "Verified status before retry",
        "application": "PolicyAdmin",
    }])
    assert len(chunks) == 1
    assert "Verified status before retry" in chunks[0].text
    assert chunks[0].metadata["application"] == "PolicyAdmin"


def test_section_chunks_preserve_heading():
    chunks = section_chunks(
        "# Scope\nRead-only lookup.\n# Restrictions\nDo not modify records.",
        document_id="SOP-1", document_type="sop",
    )
    assert [c.title for c in chunks] == ["Scope", "Restrictions"]
    assert "Restrictions" in chunks[1].text
