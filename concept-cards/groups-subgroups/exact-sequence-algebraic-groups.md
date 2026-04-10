---
# === CORE IDENTIFICATION ===
concept: Exact Sequence of Algebraic Groups
slug: exact-sequence-algebraic-groups

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
pdf_page: 88
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - surjective-homomorphism
  - kernel-of-homomorphism
extends: []
related:
  - quotient-group-algebraic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A sequence 1 -> N -> G -> Q -> 1 of algebraic groups is exact if G -> Q is a quotient map (surjective homomorphism) with kernel N. This means O(Q) injects into O(G), and the kernel is cut out by the augmentation ideal of Q.

# Core Definition

A sequence 1 -> N -> G -> Q -> 1 is **exact** if G -> Q is a quotient map with kernel N (Definition 7.59, p. 88). This means:
- N -> G is injective (O(G) -> O(N) is surjective)
- G -> Q is surjective (O(Q) -> O(G) is injective)
- N = Ker(G -> Q)

**Dimension formula** (Proposition 7.60): If 1 -> N -> G -> Q -> 1 is exact, then dim G = dim N + dim Q.

# Prerequisites

- **Surjective homomorphism** — G -> Q must be surjective
- **Kernel of homomorphism** — N must be the kernel of G -> Q

# Key Properties

1. dim G = dim N + dim Q
2. N x G is isomorphic to G x_Q G (from the abstract group fact that elements with the same image differ by an element of the kernel)
3. Q represents the sheaf associated with R -> G(R)/N(R) (Proposition 7.73)

# Examples

**Example 1**: 1 -> SL_n -> GL_n -> G_m -> 1 (the determinant sequence).

**Example 2**: 1 -> mu_n -> G_m -> G_m -> 1 (the nth power map sequence).

**Example 3**: 1 -> G_m -> GL_n -> PGL_n -> 1.

# Relationships

## Related
- **Quotient group (algebraic)** — Q = G/N in an exact sequence

# Source Reference

Chapter I, Section 7g, Definition 7.59 (p. 88), Proposition 7.60.

# Verification Notes

- Definition source: Direct from Definition 7.59
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
