---
# === CORE IDENTIFICATION ===
concept: Semidirect Product (Algebraic Groups)
slug: semidirect-product-algebraic

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
pdf_page: 89
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "N \\rtimes Q"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-subgroup
  - normal-affine-subgroup
  - quotient-group-algebraic
extends: []
related:
  - exact-sequence-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An affine group G is a semidirect product of its affine subgroups N and Q, written G = N rtimes Q, if N is normal in G and (n, q) -> nq: N(R) x Q(R) -> G(R) is a bijection for all R.

# Core Definition

An affine group G is said to be a **semidirect product** of its affine subgroups N and Q, denoted G = N rtimes Q, if N is normal in G and the map (n, q) -> nq: N(R) x Q(R) -> G(R) is a bijection of sets for all k-algebras R (Definition 7.64, p. 89).

Equivalently (Proposition 7.65): G = N rtimes Q iff there exists a homomorphism G -> Q whose restriction to Q is the identity and whose kernel is N.

Given an action theta of Q on N by group automorphisms, the semidirect product N rtimes_theta Q is the functor R -> N(R) rtimes_{theta_R} Q(R), which is an affine group with coordinate ring O(N) tensor O(Q) (p. 90).

# Prerequisites

- **Affine subgroup** — N and Q are subgroups
- **Normal affine subgroup** — N must be normal
- **Quotient group (algebraic)** — The quotient map G -> Q splits

# Key Properties

1. G(R) = N(R) rtimes Q(R) for all k-algebras R (pointwise semidirect product)
2. O(G) = O(N) tensor O(Q) as a functor to sets
3. Equivalent to having a splitting homomorphism G -> Q with kernel N

# Examples

**Example 1** (p. 89): T_n (upper triangular matrices) is the semidirect product of U_n (upper unitriangular) and D_n (diagonal matrices): T_n = U_n rtimes D_n.

**Example 2** (p. 16-17): The group of monomial matrices is D_n rtimes S_n, where S_n acts on D_n by permuting diagonal entries.

# Relationships

## Related
- **Exact sequence (algebraic groups)** — A semidirect product gives a split exact sequence 1 -> N -> G -> Q -> 1

# Source Reference

Chapter I, Section 7i, Definition 7.64 (p. 89), Proposition 7.65.

# Verification Notes

- Definition source: Direct from Definition 7.64
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
