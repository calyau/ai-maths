---
# === CORE IDENTIFICATION ===
concept: Dense Subgroup
slug: dense-subgroup

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 79
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Zariski dense subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - affine-subgroup
extends: []
related:
  - smooth-algebraic-group
  - reduced-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A subgroup Gamma of G(k') is dense in G if the only affine subgroup H of G with H(k') containing Gamma is G itself. Equivalently, no nonzero element of O(G) vanishes on all points of Gamma.

# Core Definition

Let G be an algebraic group over a field k, and let k' be a field containing k. A subgroup Gamma of G(k') is **dense** in G if the only affine subgroup H of G such that H(k') contains Gamma is G itself (Definition 7.26, p. 79).

**Criterion** (7.29, p. 79): G(k) is dense in G iff for all f in O(G), f(P) = 0 for all P in G(k) implies f = 0. Equivalently, the intersection of all kernels of homomorphisms O(G) -> k is zero.

# Prerequisites

- **Affine algebraic group** — Density is defined for subgroups of G(k')
- **Affine subgroup** — The definition quantifies over affine subgroups

# Key Properties

1. If G is smooth, then G(k^{sep}) is dense in G (7.30, p. 79)
2. If G(k) is dense in G, then G is reduced, hence smooth over perfect fields (7.28)
3. G(k) is dense in G for G = G_a, GL_n, SL_n when k is infinite (Proposition 7.32, p. 79)
4. If k is finite and dim G > 0, then G(k) is never dense (7.31)
5. The Zariski closure of Gamma in G is the smallest affine subgroup H with H(k) = closure of Gamma (7.23)

# Examples

**Example 1** (p. 80): Over Q with n odd, mu_n(Q) = {1}, so {1} is not dense in mu_n.

**Example 2** (p. 79): GL_n(k) is dense in GL_n when k is infinite, because no nonzero polynomial vanishes on {a in k^{n^2} | det(a) != 0}.

# Relationships

## Related
- **Smooth algebraic group** — Smooth groups have dense k^{sep}-points
- **Reduced algebraic group** — Having dense k-points implies reduced

# Source Reference

Chapter I, Section 7e, Definition 7.26 (p. 79), Propositions 7.32-7.33.

# Verification Notes

- Definition source: Direct from Definition 7.26
- Confidence rationale: Explicit definition with criterion
- Uncertainties: None
- Cross-reference status: Verified
