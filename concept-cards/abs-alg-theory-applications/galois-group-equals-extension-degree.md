---
# === CORE IDENTIFICATION ===
concept: Galois Group Order Equals Extension Degree
slug: galois-group-equals-extension-degree

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - galois-group
  - degree-of-field-extension
  - splitting-field
extends: []
related:
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does the order of the Galois group equal the degree of the extension?"
---

# Quick Definition

If $E$ is the splitting field of a separable polynomial $f(x)$ over $F$, then $|G(E/F)| = [E:F]$. This equality is the key numerical relationship in Galois theory.

# Core Definition

**Theorem 23.7.** Let $f(x)$ be a polynomial in $F[x]$ and suppose that $E$ is the splitting field for $f(x)$ over $F$. If $f(x)$ has no repeated roots, then

$$|G(E/F)| = [E:F]$$

(Judson, p. 309).

# Prerequisites

- **Galois group** — The group whose order is being computed
- **Degree of field extension** — The dimension of the extension
- **Splitting field** — The extension must be a splitting field

# Key Properties

1. Requires $f(x)$ to have no repeated roots (separability)
2. Proved by induction on $[E:F]$
3. Each irreducible factor of degree $d$ contributes exactly $d$ automorphisms
4. For finite fields: $G(GF(p^{nk})/GF(p^n))$ is cyclic of order $k$ (Corollary 23.9)

# Context & Application

This theorem is the quantitative foundation of Galois theory. It ensures that the Galois group has "enough" automorphisms to distinguish all intermediate fields.

# Examples

**Example 1** (p. 309): For $\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q}$: $|G| = [\mathbb{Q}(\sqrt{3}, \sqrt{5}):\mathbb{Q}] = 4$.

**Example 2** (p. 310): For the splitting field of $x^4 + x^3 + x^2 + x + 1$ over $\mathbb{Q}$: $|G| = [\mathbb{Q}(\omega):\mathbb{Q}] = 4$.

# Relationships

## Builds Upon
- **Galois group** — Computes its order
- **Degree of field extension** — Equals the group order

## Enables
- **Fundamental Theorem of Galois Theory** — This equality is essential

# Source Reference

Chapter 23: Galois Theory, Section 23.1, pages 309–310. Theorem 23.7.

# Verification Notes

- Definition source: Direct from Theorem 23.7, p. 309
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
