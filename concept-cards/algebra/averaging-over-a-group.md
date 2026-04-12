---
concept: Averaging Over a Group
slug: averaging-over-a-group
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.2 Irreducible Representations"
extraction_confidence: high
aliases: ["group averaging", "Reynolds operator"]
prerequisites: [group-representation]
extends: []
related: [g-invariant-vector, g-invariant-hermitian-form, g-invariant-linear-transformation]
contrasts_with: []
answers_questions: ["How does averaging over a group produce invariant objects?"]
---
# Quick Definition
Averaging over a finite group G produces G-invariant objects from arbitrary ones. For vectors: v-tilde = (1/|G|) sum_g gv. For forms: (v,w) = (1/|G|) sum_g {gv, gw}. For maps: T-tilde = (1/|G|) sum_g g^{-1} T g. This technique is the key tool in representation theory.
# Core Definition
The averaging process is a recurring technique: given a representation of a finite group G, summing over all group elements and dividing by |G| produces G-invariant objects (Artin, pp. 305-308, 320-322). It appears in three forms: (1) averaging vectors (10.2.2), (2) averaging Hermitian forms (10.3.7), (3) averaging linear transformations (10.7.7). The proof of G-invariance always uses the reindexing trick: multiplication by h permutes the group elements.
# Prerequisites
- **Group representation** — Averaging requires a group action
# Key Properties
1. Always produces a G-invariant object
2. If the input is already G-invariant, the output equals the input
3. The output may be zero
4. The reindexing trick: as g runs over G, so does hg (left) or gh (right)
5. Trace is preserved by averaging for operators
6. Core tool for: Maschke's theorem, Schur's lemma, orthogonality relations
# Context & Application
Averaging is the single most important technique in representation theory of finite groups. It requires |G| to be finite (to form the sum) and invertible (the factor 1/|G|).
# Examples
**Example 1** (p. 306): For S_3 with h = y: sum_{g in G} g'v = yv + x^2 yv + xyv + v + x^2 v + xv = sum_{g in G} gv.
# Relationships
## Enables
- **G-invariant vector** — Produced by averaging vectors
- **G-invariant Hermitian form** — Produced by averaging forms
- **G-invariant linear transformation** — Produced by averaging maps
# Source Reference
Chapter 10: Group Representations, Sections 10.2, 10.3, 10.7, pages 305-308, 320-322.
# Verification Notes
- Definition source: Synthesized from multiple appearances
- Confidence rationale: Repeatedly used throughout the chapter
- Uncertainties: None
- Cross-reference status: Verified
