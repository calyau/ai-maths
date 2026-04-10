---
# === CORE IDENTIFICATION ===
concept: Group of nth Roots of Unity
slug: group-of-nth-roots-of-unity

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 29
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - mu_n
  - "\\mu_n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - multiplicative-group
extends: []
related:
  - constant-finite-algebraic-group
  - kernel-of-homomorphism
contrasts_with:
  - alpha-p

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The group mu_n of nth roots of unity is the algebraic group with mu_n(R) = {r in R | r^n = 1}. Its coordinate ring is k[X]/(X^n - 1).

# Core Definition

For an integer n >= 1, the **group of nth roots of unity** mu_n is the functor R -> mu_n(R) = {r in R | r^n = 1}, which is a multiplicative group. It is an affine algebraic group with O(mu_n) = k[X]/(X^n - 1) (3.4, p. 29).

Equivalently, mu_n is the kernel of the nth power map G_m -> G_m (Example 7.16, p. 76).

# Prerequisites

- **Affine algebraic group** — mu_n is an example
- **Multiplicative group** — mu_n is a subgroup of G_m

# Key Properties

1. O(mu_n) = k[X]/(X^n - 1)
2. mu_n is a finite algebraic group
3. When char(k) does not divide n, mu_n is a smooth (etale) group scheme
4. When char(k) = p divides n, mu_n is not smooth (has nilpotent elements in its coordinate ring)
5. mu_n is the intersection of SL_n and G_m (scalar matrices) in GL_n (Example 7.12, p. 75)

# Examples

**Example 1** (p. 29): mu_n(R) = Hom_{k-alg}(k[X]/(X^n - 1), R) = {r in R | r^n = 1}.

**Example 2** (p. 76): mu_n arises as Ker(x -> x^n: G_m -> G_m). The augmentation ideal for G_m is (Y-1), so O(Ker) = k[X, X^{-1}]/(X^n - 1) = k[X]/(X^n - 1).

**Example 3** (p. 61): Over Q, mu_3 has O(mu_3) = Q x Q[sqrt(-3)], showing different local rings.

# Relationships

## Builds Upon
- **Multiplicative group** — mu_n is a closed subgroup of G_m

## Related
- **Kernel of homomorphism** — mu_n = Ker of the nth power map on G_m

## Contrasts With
- **alpha_p** — alpha_p is the additive analogue in characteristic p; mu_p is multiplicative

# Source Reference

Chapter I, 3.4 (p. 29), Example 7.16 (p. 76), Example 7.12 (p. 75).

# Verification Notes

- Definition source: Direct from 3.4
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
