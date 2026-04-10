---
# === CORE IDENTIFICATION ===
concept: Homogeneity of Algebraic Groups
slug: homogeneity

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 60
section: "Affine groups and affine group schemes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - left translation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - smooth-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

For each a in G(k), left translation L_a: g -> ag is an isomorphism of the functor G. This implies all local rings O(G)_{m_a} are isomorphic, so algebraic groups are "geometrically homogeneous."

# Core Definition

For each a in G(k), the natural map L_a: G(R) -> G(R) sending g to a_R * g is an isomorphism of set-valued functors. Moreover, L_e = id_G and L_a composed with L_b = L_{ab} (Proposition 6.12, p. 60).

**Proposition 6.13** (p. 60): For each a in G(k), O(G)_{m_a} is isomorphic to O(G)_{m_e}, where m_a = Ker(a: O(G) -> k).

**Corollary 6.14** (p. 61): When k is algebraically closed, the local rings O(G)_m at all maximal ideals m are isomorphic.

This homogeneity property means that smoothness at the identity implies smoothness everywhere (Proposition 6.25), which is crucial for Cartier's theorem.

# Prerequisites

- **Affine algebraic group** — Homogeneity is a property of algebraic groups

# Key Properties

1. L_a is an automorphism of the functor G for each a in G(k)
2. All local rings are isomorphic (over algebraically closed fields)
3. Smoothness at the identity implies global smoothness
4. The map on coordinate rings is given by Delta followed by (a tensor id): O(G) -> O(G) (equation (45), p. 60)

# Relationships

## Related
- **Smooth algebraic group** — Homogeneity reduces smoothness to checking at one point

# Source Reference

Chapter I, Section 6h (p. 60), Propositions 6.12-6.13, Corollary 6.14.

# Verification Notes

- Definition source: Direct from Propositions 6.12-6.13
- Confidence rationale: Explicit statements with proofs
- Uncertainties: None
- Cross-reference status: Verified
