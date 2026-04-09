---
# === CORE IDENTIFICATION ===
concept: Raising and Lowering Operators
slug: raising-and-lowering-operators

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 58
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ladder operators"
  - "e and f operators"
  - "creation and annihilation operators"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-for-sl2
  - weight-space-for-sl2
extends: []
related:
  - highest-weight-vector-for-sl2
  - classification-of-sl2-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the generators e and f of sl(2,C) act on weight spaces?"
---

# Quick Definition

In a representation of $\mathfrak{sl}(2,\mathbb{C})$, the operator $e$ raises weights by 2 and $f$ lowers weights by 2. These operators move between weight spaces and are the mechanism for constructing all weight vectors from a highest weight vector.

# Core Definition

**Lemma 5.2** (Kirillov, p. 58):

$$eV[\lambda] \subset V[\lambda + 2], \qquad fV[\lambda] \subset V[\lambda - 2].$$

Proof: If $v \in V[\lambda]$, then $hev = [h,e]v + ehv = 2ev + \lambda ev = (\lambda+2)ev$, so $ev \in V[\lambda+2]$.

# Prerequisites

- **Weight for sl(2,C)** — Weights define the eigenspaces that $e$ and $f$ shift between
- **Weight space for sl(2,C)** — The spaces being mapped by $e$ and $f$

# Key Properties

1. $e$ raises weight by 2 (uses $[h,e] = 2e$)
2. $f$ lowers weight by 2 (uses $[h,f] = -2f$)
3. Together with $h$, they form the standard basis of $\mathfrak{sl}(2,\mathbb{C})$
4. On a highest weight vector $v$: $ev = 0$ and $v^k = \frac{f^k}{k!}v$ generates all lower weight vectors (Lemma 5.4)
5. The formulas for their action on the basis $v^k$: $hv^k = (\lambda - 2k)v^k$, $fv^k = (k+1)v^{k+1}$, $ev^k = (\lambda - k + 1)v^{k-1}$

# Context & Application

The raising/lowering operators are the prototype for root vectors in semisimple Lie algebras. The strategy of starting with a highest weight vector and applying lowering operators generalizes to all semisimple Lie algebras. In physics, these correspond to angular momentum raising/lowering operators $J_\pm$.

# Examples

**Lemma 5.4** (p. 59): For a highest weight vector $v \in V[\lambda]$, define $v^k = \frac{f^k}{k!}v$. Then:
- $hv^k = (\lambda - 2k)v^k$
- $fv^k = (k+1)v^{k+1}$
- $ev^k = (\lambda - k + 1)v^{k-1}$ for $k > 0$

# Relationships

## Builds Upon
- **Weight spaces** — $e$ and $f$ map between weight spaces

## Enables
- **Highest weight vector** — Defined as annihilated by $e$
- **Classification of sl(2,C) representations** — Built by applying $f$ repeatedly

# Source Reference

Chapter 5, Section 5.1, Lemma 5.2, Lemma 5.4, pp. 58-59.

# Verification Notes

- Definition source: Direct from Lemma 5.2
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
