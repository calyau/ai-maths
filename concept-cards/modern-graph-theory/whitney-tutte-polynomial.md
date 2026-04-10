---
concept: Whitney-Tutte Polynomial
slug: whitney-tutte-polynomial
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 348
section: "X.2 The Universal Form of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "Q_G(t, z)"
prerequisites:
  - rank-generating-polynomial
  - tutte-polynomial
extends:
  - rank-generating-polynomial
related:
  - dichromatic-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The Whitney-Tutte polynomial $Q_G(t, z) = \sum_{F \subset E(G)} t^{k(F)} z^{n(F)} = t^{k(G)} S(G; t, z)$ is another member of the Tutte polynomial family, related by $T_G(x,y) = (x-1)^{-k(G)} Q_G(x-1, y-1)$.

# Core Definition
$Q_G(t,z) = \sum_{F \subset E(G)} t^{k(F)} z^{n(F)}$ (Bollobás, p. 348), so $Q_G(t,z) = t^{k(G)} S(G; t, z)$ and $T_G(x,y) = (x-1)^{-k(G)} Q_G(x-1, y-1)$.

# Prerequisites
- **Rank-generating polynomial** — $Q_G = t^{k(G)} S(G; t, z)$
- **Tutte polynomial** — Related by a simple transformation

# Key Properties
1. $Q_G(t,z) = \sum_{F \subset E} t^{k(F)} z^{n(F)}$
2. $Q_G = t^{k(G)} S(G; t, z)$

# Source Reference
Chapter X, Section X.2, page 348.

# Verification Notes
- Definition source: Direct from p. 348
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
