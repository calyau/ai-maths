---
concept: Ramsey Numbers for Multiple Copies
slug: ramsey-for-multiple-copies
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 201
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "r(sK_p, tK_q)"
  - "Theorem VI.15"
  - "Theorem VI.16"
prerequisites:
  - graphical-ramsey-number
extends: []
related:
  - ramsey-number-lower-bound
contrasts_with: []
answers_questions:
  - "What is r(sK₂, tK₂) or r(sK₃, tK₃)?"
---

# Quick Definition
Exact formulas: r(sK₂, tK₂) = 2s + t − 1 for s ≥ t ≥ 1; r(sK₃, tK₃) = 3s + 2t for s ≥ t ≥ 1, s ≥ 2. For general p, q: r(sKₚ, tKq) = ps + (q−1)t + O(1).

# Core Definition
**Theorem 15** (p. 201): r(sK₂, tK₂) = 2s + t − 1 for s ≥ t ≥ 1.
**Theorem 16** (p. 202): r(sK₃, tK₃) = 3s + 2t for s ≥ t ≥ 1, s ≥ 2.
**Theorem 17** (p. 203): For fixed p, q ≥ 2, ps + (q−1)t − 1 ≤ r(sKₚ, tKq) ≤ ps + (q−1)t + C, where C depends only on p and q.

The proofs use Lemma 14: r(G, H₁ ∪ H₂) ≤ max{r(G, H₁) + |H₂|, r(G, H₂)}, enabling induction on s + t.

# Prerequisites
- **Graphical Ramsey number** — the quantity being determined

# Key Properties
1. r(sK₂, tK₂) = 2s + t − 1 (exact)
2. r(sK₃, tK₃) = 3s + 2t (exact for s ≥ t ≥ 1, s ≥ 2)
3. General formula: r(sKₚ, tKq) = ps + (q−1)t + O(1)
4. Lemma 14 provides the key reduction tool

# Relationships
## Related
- Lower bounds from Theorem 11

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorems 15–17, pages 201–203.

# Verification Notes
- Definition source: Direct theorem statements
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
