# Sanitization and Public-Repository Policy

## Naming
- Use `XYZ General Insurance` as a fictional placeholder.
- Use synthetic ticket and incident IDs such as `DEMO-1001` and `DEMO-INC-0042`.
- Use generic application names such as `PolicyAdmin` and fictional error codes such as `DEMO-HTTP-504`.
- Do not publish the original customer name, vendor names tied to a real engagement, internal project identifiers, or customer-specific volumes unless explicitly cleared for public release.

## Data
- All example documents must be newly authored fictional examples.
- Never use a simple find/replace on real ticket exports and assume that they are safe.
- Remove names, email addresses, phone numbers, policy/claim/account identifiers, URLs, IPs, timestamps that can identify incidents, free-text clues, screenshots, and hidden document metadata.
- Prefer generated examples over transformed production data.
- Use broad ranges or explicitly marked synthetic values for any illustrative metrics.

## Architecture and commercial information
- Publish only generalized architecture. Exclude account IDs, resource ARNs, network topology, security-group rules, private hostnames, customer-specific endpoints, exact costs, and proprietary diagrams unless approved.
- Mark candidate services and optional components as such.
- Do not represent target-state components as deployed or tested.

## Pre-publish checklist
- [ ] Search source and history for real customer/vendor names and identifiers.
- [ ] Run `python scripts/sanitize_scan.py .`.
- [ ] Run tests and dependency/security checks.
- [ ] Inspect diagrams, document metadata, screenshots, and sample payloads.
- [ ] Enable GitHub secret scanning / push protection if available.
- [ ] Review commit history before making the repository public.
