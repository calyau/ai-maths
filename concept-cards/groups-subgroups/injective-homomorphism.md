---
# === CORE IDENTIFICATION ===
concept: Injective Homomorphism
slug: injective-homomorphism

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
  - embedding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - affine-subgroup
  - surjective-homomorphism
contrasts_with:
  - surjective-homomorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A homomorphism alpha: H -> G of affine groups is injective if alpha(R): H(R) -> G(R) is injective for all k-algebras R. Equivalently, alpha*: O(G) -> O(H) is surjective, i.e., |H| -> |G| is a closed immersion.

# Core Definition

A homomorphism H -> G of affine groups is **injective** if the map H(R) -> G(R) is injective for all k-algebras R. An injective homomorphism is also called an **embedding** (Definition 7.2, p. 73).

**Proposition 7.3** (p. 73): alpha is injective if and only if alpha*: O(G) -> O(H) is surjective.

This means |alpha|: |H| -> |G| is a closed immersion of affine schemes.

# Prerequisites

- **Affine algebraic group** — Injectivity is defined for homomorphisms of affine groups

# Key Properties

1. Equivalent to O(G) -> O(H) being surjective (Proposition 7.3)
2. Preserved by base change (Proposition 7.4)
3. In characteristic zero: alpha is injective iff G(k^{al}) -> H(k^{al}) is injective (Proposition 7.18)
4. In characteristic p: the above fails -- x -> x^p: G_a -> G_a has trivial kernel on fields but is not injective (7.19)
5. A monomorphism in the category of affine groups iff injective (Remark 7.20)

# Examples

**Example 1**: SL_n -> GL_n is an injective homomorphism (embedding). O(GL_n) -> O(SL_n) is surjective.

**Example 2** (p. 77): In characteristic p, x -> x^p: G_a -> G_a is not injective because its kernel alpha_p is nontrivial, even though G_a(K) -> G_a(K) is injective for all fields K.

# Relationships

## Related
- **Affine subgroup** — An injective homomorphism identifies H with an affine subgroup of G

## Contrasts With
- **Surjective homomorphism** — Injective: O(G) -> O(H) surjective; Surjective: O(Q) -> O(G) injective

# Source Reference

Chapter I, Section 7b, Definition 7.2, Proposition 7.3 (p. 73).

# Verification Notes

- Definition source: Direct from Definition 7.2
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
