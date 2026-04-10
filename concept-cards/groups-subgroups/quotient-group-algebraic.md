---
# === CORE IDENTIFICATION ===
concept: Quotient Group (Algebraic)
slug: quotient-group-algebraic

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
pdf_page: 85
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - G/N

# === TYPED RELATIONSHIPS ===
prerequisites:
  - surjective-homomorphism
  - normal-affine-subgroup
extends: []
related:
  - exact-sequence-algebraic-groups
  - kernel-of-homomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A surjective homomorphism G -> Q with kernel N is called the quotient of G by N, denoted Q = G/N. The quotient is uniquely determined up to unique isomorphism by its universal property: any homomorphism from G whose kernel contains N factors through Q.

# Core Definition

A surjective homomorphism G -> Q with kernel N is called the **quotient of G by N**, and Q is denoted G/N (Definition 7.58, p. 87).

**Universal property** (Theorem 7.56, p. 87): Any homomorphism G -> Q' whose kernel contains N factors uniquely through G -> Q.

**Corollary 7.57** (p. 87): If theta: G -> Q and theta': G -> Q' are quotient maps with the same kernel, there is a unique isomorphism alpha: Q -> Q' with alpha composed with theta = theta'.

The quotient G/N always exists when N is a normal affine subgroup of an algebraic group G (proved later, 8.77).

**Dimension formula** (Proposition 7.60, p. 88): dim G = dim N + dim Q for an exact sequence 1 -> N -> G -> Q -> 1.

# Prerequisites

- **Surjective homomorphism** — The quotient map must be surjective in the algebraic sense
- **Normal affine subgroup** — N must be normal for the quotient to be defined

# Key Properties

1. Uniqueness up to unique isomorphism (Corollary 7.57)
2. Universal property: factors any homomorphism whose kernel contains N
3. dim G = dim N + dim G/N (Proposition 7.60)
4. Quotients of smooth groups are smooth (Proposition 7.66)
5. Q represents the sheaf associated with R -> G(R)/N(R) (Proposition 7.73)

# Examples

**Example 1** (p. 85): G_m -> G_m via x -> x^n is surjective with kernel mu_n, so G_m/mu_n = G_m.

**Example 2** (p. 16): GL_n -> PGL_n with kernel G_m (scalar matrices), giving PGL_n = GL_n/G_m.

# Relationships

## Related
- **Exact sequence (algebraic groups)** — A sequence 1 -> N -> G -> Q -> 1 is exact iff G -> Q is a quotient with kernel N
- **Kernel of homomorphism** — N = Ker(G -> Q)

# Source Reference

Chapter I, Section 7g-7h, Definition 7.58 (p. 87), Theorem 7.56, Proposition 7.60.

# Verification Notes

- Definition source: Direct from Definition 7.58 and Theorem 7.56
- Confidence rationale: Explicit definition with universal property
- Uncertainties: None
- Cross-reference status: Verified
