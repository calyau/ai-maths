---
# === CORE IDENTIFICATION ===
concept: Galois Group Permutes Roots
slug: galois-group-permutes-roots

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
  - field-automorphism
extends: []
related:
  - galois-group-of-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Galois group act on the roots of a polynomial?"
---

# Quick Definition

Any automorphism in the Galois group $G(E/F)$ permutes the roots of any polynomial $f(x) \in F[x]$ that lie in $E$. This means the Galois group is a subgroup of the symmetric group on the roots.

# Core Definition

**Proposition 23.5.** Let $E$ be a field extension of $F$ and $f(x)$ be a polynomial in $F[x]$. Then any automorphism in $G(E/F)$ defines a permutation of the roots of $f(x)$ that lie in $E$ (Judson, p. 308).

The proof is direct: if $f(\alpha) = 0$ and $\sigma \in G(E/F)$, then $f(\sigma(\alpha)) = \sigma(f(\alpha)) = \sigma(0) = 0$ since $\sigma$ fixes the coefficients of $f$.

# Prerequisites

- **Galois group** — The automorphisms that permute roots
- **Field automorphism** — Preserves all field operations

# Key Properties

1. Automorphisms fixing $F$ must send roots to roots of the same polynomial
2. The Galois group embeds into $S_n$ where $n = \deg f(x)$
3. Each automorphism is uniquely determined by its action on the roots
4. The number of automorphisms divides $n!$

# Context & Application

This proposition is the link between field automorphisms and permutation groups. It allows us to view the Galois group as a subgroup of a symmetric group, making it accessible to the group-theoretic tools developed earlier in the text.

# Examples

**Example 1** (p. 308): Complex conjugation $\sigma(a + bi) = a - bi$ permutes the roots of any polynomial with real coefficients: it swaps each complex root with its conjugate.

**Example 2** (p. 308): In $G(\mathbb{Q}(\sqrt{3}, \sqrt{5})/\mathbb{Q})$, the automorphism $\sigma(\sqrt{3}) = -\sqrt{3}$ permutes the roots of $x^2 - 3$.

# Relationships

## Builds Upon
- **Galois group** — The group whose elements permute roots
- **Field automorphism** — Each element is an automorphism

## Related
- **Galois group of polynomial** — Viewed as a subgroup of the symmetric group on roots

# Source Reference

Chapter 23: Galois Theory, Section 23.1, page 308. Proposition 23.5.

# Verification Notes

- Definition source: Direct from Proposition 23.5, p. 308
- Confidence: HIGH — explicit proposition with proof
- Cross-reference status: Verified
- Uncertainties: None
