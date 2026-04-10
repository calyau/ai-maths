---
# === CORE IDENTIFICATION ===
concept: Kernel of Homomorphism
slug: kernel-of-homomorphism

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
pdf_page: 76
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Ker(\\alpha)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-subgroup
  - augmentation-ideal
extends: []
related:
  - fibred-product
  - injective-homomorphism
  - exact-sequence-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The kernel of a homomorphism alpha: H -> G of affine groups is the affine subgroup N of H with N(R) = Ker(alpha(R): H(R) -> G(R)) for all R. Its coordinate ring is O(H)/I_G * O(H), where I_G is the augmentation ideal of G.

# Core Definition

The **kernel** of a homomorphism alpha: H -> G of affine groups is the functor R -> Ker(alpha(R): H(R) -> G(R)). It is an affine subgroup of H with coordinate ring O(H)/I_G * O(H), where I_G = Ker(epsilon: O(G) -> k) is the augmentation ideal (Proposition 7.15, p. 76).

Alternatively, the kernel is the fibred product H x_G *, and so O(Ker) = O(H) tensor_{O(G)} (O(G)/I_G) = O(H)/I_G * O(H) (see Section 4b).

# Prerequisites

- **Affine subgroup** — The kernel is an affine subgroup
- **Augmentation ideal** — The kernel construction uses I_G = Ker(epsilon)

# Key Properties

1. N(R) = Ker(H(R) -> G(R)) for all k-algebras R
2. O(N) = O(H)/I_G * O(H)
3. In characteristic zero, alpha is injective iff G(k^{al}) -> H(k^{al}) is injective (Proposition 7.18)
4. The kernel is always a normal affine subgroup of H

# Examples

**Example 1** (p. 76): Ker(x -> x^n: G_m -> G_m) = mu_n. The augmentation ideal is (Y-1), so O(Ker) = k[X, X^{-1}]/(X^n - 1) = k[X]/(X^n - 1).

**Example 2** (p. 77): Ker(det: GL_n -> G_m) = SL_n, with O(SL_n) = k[X_ij]/(det(X_ij) - 1).

# Relationships

## Related
- **Augmentation ideal** — The kernel construction uses the augmentation ideal of the target
- **Fibred product** — Ker(alpha) = H x_G *
- **Injective homomorphism** — alpha is injective iff Ker(alpha) is trivial

# Source Reference

Chapter I, Section 7d, Proposition 7.15 (p. 76), Examples 7.16-7.17.

# Verification Notes

- Definition source: Direct from Proposition 7.15
- Confidence rationale: Explicit definition with worked examples
- Uncertainties: None
- Cross-reference status: Verified
