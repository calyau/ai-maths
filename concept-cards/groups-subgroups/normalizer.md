---
# === CORE IDENTIFICATION ===
concept: Normalizer
slug: normalizer

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
pdf_page: 82
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "N_G(H)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-subgroup
  - transporter
extends: []
related:
  - centralizer
  - centre-of-algebraic-group
  - normal-affine-subgroup
contrasts_with:
  - centralizer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The normalizer N_G(H) of an affine subgroup H in G is the affine subgroup with N_G(H)(R) = {g in G(R) | gH(R')g^{-1} = H(R') for all R-algebras R'}. It is an affine subgroup represented by a quotient of O(G).

# Core Definition

For a subgroup H of an affine group G, the **normalizer** N_G(H) is the functor R -> {g in G(R) | ^gH = H}, where ^gH is the functor R' -> g * H(R') * g^{-1} for R-algebras R' (p. 82).

**Proposition 7.39** (p. 82): N_G(H) is an affine subgroup of G, represented by a quotient of O(G). The proof uses the transporter: N = T_G(H, H) intersected with T_G(H, H)^{-1}.

H is normal in G if and only if N_G(H) = G (Proposition 7.43a, p. 83).

# Prerequisites

- **Affine subgroup** — H must be an affine subgroup of G
- **Transporter** — The proof uses the transporter construction from Section 6n

# Key Properties

1. N_G(H) is an affine subgroup of G
2. Formation commutes with base change: N_G(H)_{k'} = N_{G_{k'}}(H_{k'})
3. H is normal iff N_G(H) = G
4. If H(k') is dense in H, then N_G(H)(k) = G(k) intersected with N_{G(k')}(H(k')) (Proposition 7.40)

# Relationships

## Related
- **Centralizer** — The centralizer is a subgroup of the normalizer
- **Centre of algebraic group** — Z(G) = C_G(G) is a special case of centralizer
- **Normal affine subgroup** — H is normal iff N_G(H) = G

## Contrasts With
- **Centralizer** — Normalizer: gHg^{-1} = H; Centralizer: ghg^{-1} = h for all h

# Source Reference

Chapter I, Section 7f, Proposition 7.39 (p. 82), Proposition 7.43.

# Verification Notes

- Definition source: Direct from p. 82
- Confidence rationale: Explicit definition with proof of representability
- Uncertainties: None
- Cross-reference status: Verified
