---
# === CORE IDENTIFICATION ===
concept: Centralizer
slug: centralizer

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
pdf_page: 83
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C_G(H)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalizer
  - transporter
extends: []
related:
  - normalizer
  - centre-of-algebraic-group
contrasts_with:
  - normalizer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The centralizer C_G(H) of an affine subgroup H in G is the affine subgroup with C_G(H)(R) = {n in N_G(H)(R) | the inner automorphism i_n acts as the identity on H}. The centre Z(G) = C_G(G) is the special case H = G.

# Core Definition

The **centralizer** C_G(H) of H in G is the functor R -> {n in N(R) | i_n = id_H}, where N = N_G(H) and i_n is the inner automorphism h -> nhn^{-1} (p. 83).

Equivalently, C(R) = G(R) intersected with the intersection over all R'-algebras of C_{G(R')}(H(R')).

**Proposition 7.44** (p. 83): C_G(H) is an affine subgroup of G, proved using the transporter: C = T_{G x G}(H, H) where G acts on G x G by g(g_1, g_2) = (g_1, gg_2g^{-1}) and H embeds diagonally.

# Prerequisites

- **Normalizer** — The centralizer is defined as a subgroup of the normalizer
- **Transporter** — The proof uses the transporter construction

# Key Properties

1. C_G(H) is an affine subgroup of G
2. Formation commutes with base change: C_G(H)_{k'} = C_{G_{k'}}(H_{k'})
3. Even when G and H are smooth, C_G(H) need not be smooth (7.47, p. 84)
4. Z(GL_n) = G_m (scalar matrices) (Example 7.48, p. 84)
5. Z(SL_p) = mu_p in characteristic p (7.47)

# Examples

**Example 1** (p. 84): Z(GL_n) = G_m (diagonal scalar matrices).

**Example 2** (p. 84): For G = GL_n, with H_N = (mu_N)^n (diagonal matrices with N-th roots of unity), C_G(H_N) = D_n (diagonal matrices) for sufficiently large N.

# Relationships

## Builds Upon
- **Normalizer** — C_G(H) is a subgroup of N_G(H)

## Related
- **Centre of algebraic group** — Z(G) = C_G(G)

## Contrasts With
- **Normalizer** — Centralizer requires pointwise commutation, not just set-wise invariance

# Source Reference

Chapter I, Section 7f, Proposition 7.44 (p. 83), Examples 7.48-7.49.

# Verification Notes

- Definition source: Direct from p. 83
- Confidence rationale: Explicit definition with proof
- Uncertainties: None
- Cross-reference status: Verified
