---
# === CORE IDENTIFICATION ===
concept: Normal Affine Subgroup
slug: normal-affine-subgroup

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
pdf_page: 74
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - normal subgroup (algebraic)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-subgroup
  - normalizer
extends:
  - affine-subgroup
related:
  - quotient-group-algebraic
  - kernel-of-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A normal affine subgroup of an affine group G is a closed subfunctor H such that H(R) is a normal subgroup of G(R) for all k-algebras R. Equivalently, N_G(H) = G.

# Core Definition

An affine subgroup H of G is **normal** if H(R) is a normal subgroup of G(R) for all k-algebras R (Definition 7.6, p. 74). Equivalently, H is normal iff N_G(H) = G (Proposition 7.43a, p. 83).

Every kernel of a homomorphism is a normal affine subgroup. Conversely, when a normal subgroup N of an algebraic group G admits a quotient G/N, the kernel of G -> G/N is exactly N.

For smooth groups over perfect fields: if H(k^{sep}) is normal in G(k^{sep}), then H is normal in G (Corollary 7.41, p. 83). This fails without the smoothness assumption (7.42).

# Prerequisites

- **Affine subgroup** — Normal subgroups are a special case
- **Normalizer** — N_G(H) = G characterizes normality

# Key Properties

1. H is normal iff N_G(H) = G
2. Every kernel is a normal subgroup
3. For smooth H and G: normality can be checked on k^{sep}-points (Corollary 7.41)
4. Normal subgroups determine quotients: Q = G/N with universal property

# Examples

**Example 1**: SL_n is normal in GL_n (kernel of the determinant).

**Example 2** (p. 83): In characteristic p, alpha_p is a subgroup of SL_2 with alpha_p(k^{al}) = 1, but alpha_p is not normal (showing the smoothness assumption in 7.41 is needed).

# Relationships

## Extends
- **Affine subgroup** — A normal affine subgroup has the additional normality condition

## Related
- **Quotient group (algebraic)** — Normal subgroups determine quotients
- **Kernel of homomorphism** — Every kernel is normal

# Source Reference

Chapter I, Definition 7.6 (p. 74), Proposition 7.43 (p. 83), Corollary 7.41 (p. 83).

# Verification Notes

- Definition source: Direct from Definition 7.6
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
