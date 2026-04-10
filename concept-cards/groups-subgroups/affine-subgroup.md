---
# === CORE IDENTIFICATION ===
concept: Affine Subgroup
slug: affine-subgroup

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
pdf_page: 73
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - algebraic subgroup
  - closed subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - hopf-ideal
extends: []
related:
  - normal-affine-subgroup
  - kernel-of-homomorphism
  - injective-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An affine subgroup of an affine group G is a closed subfunctor H of G such that H(R) is a subgroup of G(R) for all k-algebras R. Affine subgroups correspond bijectively to Hopf ideals in O(G).

# Core Definition

An **affine subgroup** (resp. **normal affine subgroup**) of an affine group G is a closed subfunctor H of G such that H(R) is a subgroup (resp. normal subgroup) of G(R) for all R (Definition 7.6, p. 74).

Equivalently, H is an affine subgroup if H(R) is a subgroup of G(R) for all R and H is representable (in which case it is represented by a quotient of O(G), by Proposition 7.3).

**Proposition 7.8** (p. 74): The affine subgroups of G are in natural one-to-one correspondence with the Hopf ideals of O(G). The correspondence sends H to I(H) = Ker(O(G) -> O(H)) and a to G(a) = {g in G(R) | f_R(g) = 0 for all f in a}.

# Prerequisites

- **Affine algebraic group** — Subgroups of algebraic groups
- **Hopf ideal** — The algebraic counterpart of an affine subgroup

# Key Properties

1. O(H) is a quotient of O(G), so H is algebraic when G is (Remark 7.7)
2. Every descending chain of affine subgroups of an algebraic group stabilizes (Corollary 7.9, by the Hilbert basis theorem)
3. |H| is closed in |G| (Proposition 7.10)
4. Arbitrary intersections of affine subgroups are affine subgroups (Proposition 7.11)
5. An injective homomorphism H -> G is equivalent to O(G) -> O(H) being surjective (Proposition 7.3)

# Examples

**Example 1** (p. 75): The intersection of SL_n and G_m (scalar matrices) in GL_n is mu_n.

# Relationships

## Builds Upon
- **Hopf ideal** — Subgroups correspond to Hopf ideals

## Related
- **Normal affine subgroup** — A subgroup H with H(R) normal in G(R) for all R
- **Kernel of homomorphism** — Every kernel is an affine subgroup
- **Injective homomorphism** — An injective homomorphism is the same as an embedding into an affine subgroup

# Source Reference

Chapter I, Section 7c, Definition 7.6 (p. 74), Proposition 7.8.

# Verification Notes

- Definition source: Direct from Definition 7.6
- Confidence rationale: Explicit definition with bijection to Hopf ideals
- Uncertainties: None
- Cross-reference status: Verified
