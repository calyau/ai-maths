---
concept: Galois Group of a Cyclotomic Extension
slug: galois-group-cyclotomic
category: galois-theory
subcategory: field-automorphisms
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"
extraction_confidence: high
aliases: []
prerequisites:
  - galois-group
  - nth-root-of-unity
  - cyclic-group
extends: []
related:
  - primitive-nth-root-of-unity
contrasts_with: []
answers_questions:
  - "What is the Galois group of a cyclotomic polynomial?"
---

# Quick Definition

The Galois group of the cyclotomic extension $\mathbb{Q}(\omega)/\mathbb{Q}$, where $\omega$ is a primitive $n$th root of unity, is abelian. For prime $p$, $G(\mathbb{Q}(\omega)/\mathbb{Q})$ is abelian of order $p - 1$.

# Core Definition

For a primitive $p$th root of unity $\omega$ (where $p$ is prime), the cyclotomic polynomial $\Phi_p(x) = x^{p-1} + x^{p-2} + \cdots + x + 1$ is irreducible over $\mathbb{Q}$. The Galois group $G(\mathbb{Q}(\omega)/\mathbb{Q})$ is abelian of order $p - 1$ (Judson, Exercise 23.5.20, p. 323).

The automorphisms are $\sigma_i(\omega) = \omega^i$ for $i = 1, \ldots, p - 1$.

# Prerequisites

- **Galois group** — The group of automorphisms
- **Nth root of unity** — The cyclotomic extension
- **Cyclic group** — The Galois group structure

# Key Properties

1. $\Phi_p(x)$ is irreducible over $\mathbb{Q}$ for prime $p$
2. $[\mathbb{Q}(\omega):\mathbb{Q}] = p - 1$
3. Automorphisms send $\omega \mapsto \omega^i$ for $1 \leq i \leq p - 1$
4. The Galois group is abelian (isomorphic to $(\mathbb{Z}/p\mathbb{Z})^*$)

# Examples

**Example 1** (p. 310): For $f(x) = x^4 + x^3 + x^2 + x + 1 = \Phi_5(x)$, the Galois group $G(\mathbb{Q}(\omega)/\mathbb{Q}) \cong \mathbb{Z}_4$ where $\omega = e^{2\pi i/5}$.

# Relationships

## Builds Upon
- **Galois group** — Applied to cyclotomic extensions
- **Nth root of unity** — The cyclotomic extension

# Source Reference

Chapter 23: Galois Theory, Section 23.1, page 310. Example 23.11 and Exercise 20.

# Verification Notes

- Definition source: From Example 23.11 and Exercise 23.5.20
- Confidence: HIGH — explicit example and exercise
- Cross-reference status: Verified
- Uncertainties: None
