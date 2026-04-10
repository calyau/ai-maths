---
# === CORE IDENTIFICATION ===
concept: Surjective Homomorphism
slug: surjective-homomorphism

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
  - quotient map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - injective-homomorphism
  - quotient-group-algebraic
contrasts_with:
  - injective-homomorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A homomorphism G -> Q of affine groups is surjective if for every q in Q(R), there exists a faithfully flat R-algebra R' and a g in G(R') mapping to the image of q in Q(R'). Equivalently, O(Q) -> O(G) is injective.

# Core Definition

A homomorphism G -> Q is said to be **surjective** (and Q is called a **quotient** of G) if for every k-algebra R and q in Q(R), there exists a faithfully flat R-algebra R' and a g in G(R') mapping to the image of q in Q(R') (Definition 7.50, p. 85).

**Theorem 7.51** (p. 85): A homomorphism G -> Q is surjective if and only if O(Q) -> O(G) is injective.

Note: Surjectivity does NOT mean G(R) -> Q(R) is surjective for all R. The naive pointwise condition is too strong (e.g., x -> x^n: G_m -> G_m would not be surjective).

# Prerequisites

- **Affine algebraic group** — Surjectivity is defined for homomorphisms of affine groups

# Key Properties

1. Equivalent to O(Q) -> O(G) being injective (Theorem 7.51)
2. A homomorphism that is both injective and surjective is an isomorphism (Proposition 7.53)
3. Surjectivity is preserved by base change (Proposition 7.52)
4. If G -> Q is surjective, then G(k^{al}) -> Q(k^{al}) is surjective; the converse holds when Q is smooth (Proposition 7.54)

# Examples

**Example 1** (p. 85): x -> x^n: G_m -> G_m is surjective because O(G_m) -> O(G_m) sending Y -> X^n is injective, even though G_m(R) -> G_m(R) via x -> x^n is not surjective for general R.

# Relationships

## Related
- **Quotient group (algebraic)** — A surjective homomorphism with kernel N gives a quotient G/N
- **Injective homomorphism** — Surjective: O(Q) -> O(G) injective; Injective: O(G) -> O(H) surjective

## Contrasts With
- **Injective homomorphism** — Dual conditions on the coordinate ring map

# Common Confusions

- **Confusion**: Thinking surjective means G(R) -> Q(R) is surjective for all R
  **Clarification**: It only requires lifting after a faithfully flat extension. The pointwise condition is too strong.

# Source Reference

Chapter I, Section 7g, Definition 7.50 (p. 85), Theorem 7.51.

# Verification Notes

- Definition source: Direct from Definition 7.50
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
