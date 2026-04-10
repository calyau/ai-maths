---
concept: One-Variable Kauffman Polynomial
slug: one-variable-kauffman-polynomial
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 370
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "f[L]"
prerequisites:
  - kauffman-bracket
  - self-writhe
extends:
  - kauffman-bracket
related:
  - jones-polynomial
  - ambient-isotopy
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The one-variable Kauffman polynomial $f[L] = (-A)^{-3s(L)} \langle L \rangle \in \mathbb{Z}[A, A^{-1}]$ is an ambient isotopy invariant for unoriented links, obtained by normalizing the Kauffman bracket by the self-writhe.

# Core Definition
Theorem 18 (p. 370): "The Laurent polynomial $f[L] = (-A)^{-3s(L)} \langle L \rangle \in \mathbb{Z}[A, A^{-1}]$ is an invariant of ambient isotopy for unoriented links." Here $s(L)$ is the self-writhe and $\langle L \rangle$ is the Kauffman bracket.

# Prerequisites
- **Kauffman bracket** — The regular isotopy invariant being normalized
- **Self-writhe** — The correction factor for Type I invariance

# Key Properties
1. Ambient isotopy invariant (for unoriented links)
2. $f[L] = (-A)^{-3s(L)} \langle L \rangle$
3. The Jones polynomial is $V_L(t) = f[L](t^{-1/4})$ (for oriented links, using writhe $w$ instead of self-writhe $s$)
4. Mirror image: $f_{L^*}[A] = f_L[A^{-1}]$ (Theorem 20)

# Context & Application
This polynomial "is perhaps the nicest of many closely related link polynomials" (p. 371). It can prove knots are knotted and detect chirality.

# Examples
**Example** (p. 371): For the right-handed trefoil: $f[L] = -A^{-16} + A^{-12} + A^{-4}$. Since $f[L](A) \neq f[L](A^{-1})$, the trefoil is not amphicheiral.

# Relationships
## Builds Upon
- **kauffman-bracket**, **self-writhe**

## Enables
- **jones-polynomial** — $V_L(t) = f[L](t^{-1/4})$

## Related
- **ambient-isotopy** — $f[L]$ is invariant under it

# Source Reference
Chapter X, Section X.6, Theorem 18, page 370.

# Verification Notes
- Definition source: Direct from Theorem 18
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
