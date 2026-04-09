---
# === CORE IDENTIFICATION ===
concept: "Verma Module for sl(2,C)"
slug: verma-module-for-sl2

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 59
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "M^lambda"
  - "M_lambda for sl(2)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - highest-weight-vector-for-sl2
  - raising-and-lowering-operators
extends: []
related:
  - verma-module
  - classification-of-sl2-representations
  - quotient-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Verma module for sl(2,C)?"
  - "How are irreducible representations constructed as quotients?"
---

# Quick Definition

The Verma module $M^\lambda$ for $\mathfrak{sl}(2,\mathbb{C})$ is the infinite-dimensional representation with basis $v^0, v^1, v^2, \ldots$ and action given by the formulas from Lemma 5.4. Every irreducible finite-dimensional representation is a quotient of a Verma module.

# Core Definition

**Lemma 5.5** (Kirillov, pp. 59-60): Let $\lambda \in \mathbb{C}$. Define $M^\lambda$ to be the infinite-dimensional vector space with basis $v^0, v^1, \ldots$. The formulas

$$hv^k = (\lambda - 2k)v^k, \quad fv^k = (k+1)v^{k+1}, \quad ev^k = (\lambda - k + 1)v^{k-1} \; (k > 0), \quad ev^0 = 0$$

define on $M^\lambda$ a structure of (infinite-dimensional) representation of $\mathfrak{sl}(2,\mathbb{C})$.

If $V$ is an irreducible finite-dimensional representation with highest weight $\lambda$, then $V = M^\lambda / W$ for some subrepresentation $W$.

# Prerequisites

- **Highest weight vector for sl(2,C)** — $v^0$ is the highest weight vector
- **Raising and lowering operators** — The formulas for $e, f, h$

# Key Properties

1. $M^\lambda$ is infinite-dimensional for any $\lambda \in \mathbb{C}$
2. $v^0$ is the unique highest weight vector (up to scalar)
3. The weights of $M^\lambda$ are $\lambda, \lambda - 2, \lambda - 4, \ldots$ (extending to $-\infty$)
4. Every irreducible finite-dimensional representation is a quotient of $M^\lambda$ for $\lambda = n \in \mathbb{Z}_{\geq 0}$
5. When $\lambda = n$ (non-negative integer), the subspace spanned by $v^{n+1}, v^{n+2}, \ldots$ is a subrepresentation

# Construction / Recognition

## To Construct $M^\lambda$:
1. Take a vector space with basis $v^0, v^1, v^2, \ldots$
2. Define the action of $h, e, f$ by the formulas above
3. Verify this defines a representation (explicit calculation)

## To Get Finite-Dimensional Quotient:
1. Require $\lambda = n \in \mathbb{Z}_{\geq 0}$
2. The subspace $M' = \mathrm{span}(v^{n+1}, v^{n+2}, \ldots)$ is a subrepresentation (because $ev^{n+1} = (n - n)v^n = 0$)
3. The quotient $M^n / M' = V_n$ is the irreducible representation of dimension $n + 1$

# Context & Application

Verma modules are the universal highest-weight representations. They provide a systematic way to construct all irreducible representations as quotients. This construction generalizes to all semisimple Lie algebras (Chapter 9).

# Examples

**Example** (Theorem 5.6, p. 60): For $\lambda = n = 2$: $M^2$ has basis $v^0, v^1, v^2, v^3, \ldots$. The submodule $M'$ spanned by $v^3, v^4, \ldots$ is a subrepresentation because $ev^3 = (2 - 2)v^2 = 0$. The quotient $V_2 = M^2/M'$ has basis $v^0, v^1, v^2$ (the 3-dimensional adjoint representation).

# Relationships

## Builds Upon
- **Highest weight vector for sl(2,C)** — $v^0$ is the highest weight vector of $M^\lambda$

## Enables
- **Classification of sl(2,C) representations** — Irreducibles are quotients of Verma modules

## Related
- **Verma module** — General semisimple version (Chapter 9)
- **Quotient representation** — Irreducibles obtained by quotienting

# Common Confusions

- **Confusion**: Thinking Verma modules are always irreducible.
  **Clarification**: Verma modules are typically reducible. For $\lambda = n \in \mathbb{Z}_{\geq 0}$, $M^n$ has a non-trivial submodule. The irreducible representation is the quotient.

# Source Reference

Chapter 5, Section 5.1, Lemma 5.5, pp. 59-60.

# Verification Notes

- Definition source: Direct from Lemma 5.5
- Confidence rationale: Explicit construction with formulas
- Uncertainties: None
- Cross-reference status: Verified
