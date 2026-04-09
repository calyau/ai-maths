---
# === CORE IDENTIFICATION ===
concept: Separable Polynomial
slug: separable-polynomial

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - splitting-field
  - derivative-of-polynomial
extends: []
related:
  - separable-extension
  - normal-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a separable polynomial?"
  - "How can I test if a polynomial is separable?"
---

# Quick Definition

A polynomial $f(x) \in F[x]$ of degree $n$ is separable if it has $n$ distinct roots in its splitting field. Equivalently, $f(x)$ is separable if and only if $\gcd(f(x), f'(x)) = 1$.

# Core Definition

Let $f(x) \in F[x]$ be a polynomial of degree $n$. The polynomial $f(x)$ is **separable** if it has $n$ distinct roots in the splitting field of $f(x)$; that is, $f(x)$ is separable when it factors into distinct linear factors over the splitting field (Judson, p. 293).

# Prerequisites

- **Splitting field** — Separability is defined in terms of roots in the splitting field
- **Derivative of polynomial** — The separability test uses the formal derivative

# Key Properties

1. $f(x)$ is separable if and only if $\gcd(f(x), f'(x)) = 1$ (Lemma 22.5)
2. In characteristic 0, every irreducible polynomial is separable (Proposition 23.12)
3. In characteristic $p$, an irreducible $f(x)$ is separable unless $f(x) = g(x^p)$ (Proposition 23.12)
4. The polynomial $x^{p^n} - x$ over $\mathbb{Z}_p$ is always separable (its derivative is $-1$)

# Construction / Recognition

## To Test:
1. Compute the formal derivative $f'(x)$
2. Compute $\gcd(f(x), f'(x))$
3. If the gcd is 1, $f(x)$ is separable
4. If the gcd is nontrivial, $f(x)$ has repeated roots

# Context & Application

Separability is essential for Galois theory. The Fundamental Theorem of Galois Theory requires the extension to be both normal and separable. In characteristic 0, separability is automatic, but in positive characteristic, inseparable polynomials exist and cause complications.

# Examples

**Example 1** (p. 293): $x^2 - 2$ is separable over $\mathbb{Q}$ since it factors as $(x - \sqrt{2})(x + \sqrt{2})$ with distinct roots.

**Example 2**: $x^2 + 1 \in \mathbb{Z}_2[x]$ is inseparable since $(x+1)^2 = x^2 + 1$ in characteristic 2.

# Relationships

## Builds Upon
- **Splitting field** — Separability concerns roots in the splitting field
- **Derivative of polynomial** — Used in the separability test

## Enables
- **Separable extension** — Extensions where every element satisfies a separable polynomial
- **Galois theory** — Requires separability

# Common Confusions

- **Confusion**: Thinking a polynomial with no roots in $F$ is inseparable
  **Clarification**: Separability concerns roots in the splitting field, not in $F$ itself

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 293. See Lemma 22.5 and Proposition 23.12.

# Verification Notes

- Definition source: Direct from p. 293
- Confidence: HIGH — explicit definition with test
- Cross-reference status: Verified
- Uncertainties: None
