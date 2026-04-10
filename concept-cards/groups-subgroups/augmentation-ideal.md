---
# === CORE IDENTIFICATION ===
concept: Augmentation Ideal
slug: augmentation-ideal

# === CLASSIFICATION ===
category: hopf-algebras
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
  - "I_G"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - counit
  - hopf-algebra
extends: []
related:
  - kernel-of-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I construct the Hopf algebra of an affine algebraic group?"
---

# Quick Definition

The augmentation ideal I_G of an affine group G is the kernel of the counit epsilon: O(G) -> k. It encodes the identity element: A = k direct-sum I_G.

# Core Definition

The **augmentation ideal** I_G is the kernel of epsilon: O(G) -> k, where epsilon is the counit (p. 76). The augmentation ideal plays a fundamental role in constructing kernels: for a homomorphism alpha: H -> G, Ker(alpha) has coordinate ring O(H)/I_G * O(H).

By Lemma 6.30 (p. 64), A = k direct-sum I (as k-vector spaces), and for any a in I, Delta(a) = a tensor 1 + 1 tensor a (mod I tensor I).

# Prerequisites

- **Counit** — I_G = Ker(epsilon)
- **Hopf algebra** — The augmentation ideal is part of the Hopf algebra structure

# Key Properties

1. I_G = Ker(epsilon: O(G) -> k)
2. O(G) = k direct-sum I_G (Lemma 6.30a)
3. For a in I_G: Delta(a) = a tensor 1 + 1 tensor a (mod I_G tensor I_G) (Lemma 6.30b)
4. I_G * O(H) generates the ideal whose quotient gives the kernel of any H -> G

# Examples

**Example 1** (p. 76): For G_m, epsilon sends f(X, X^{-1}) to f(1, 1), so I_{G_m} = (X - 1) in k[X, X^{-1}].

# Relationships

## Related
- **Kernel of homomorphism** — The kernel construction uses the augmentation ideal

# Source Reference

Chapter I, Section 7d (p. 76), Lemma 6.30 (p. 64).

# Verification Notes

- Definition source: Direct from p. 76 and Lemma 6.30
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
