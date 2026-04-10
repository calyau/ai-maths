---
concept: Self-Writhe
slug: self-writhe
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 370
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "s(L)"
prerequisites:
  - writhe
extends:
  - writhe
related:
  - one-variable-kauffman-polynomial
contrasts_with:
  - writhe
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The self-writhe $s(L)$ of a link diagram is the sum of writhes of individual components: $s(L) = w(L_1) + \cdots + w(L_k)$, counting only self-crossings. It is independent of orientation.

# Core Definition
"Given an oriented link diagram $L$ with components $L_1, \ldots, L_k$, the self-writhe of $L$ is $s(L) = w(L_1) + \cdots + w(L_k)$" (Bollobás, p. 370). Since changing orientations of both arcs at a crossing does not change its sign, $s(L)$ is independent of orientation.

# Prerequisites
- **Writhe** — Self-writhe sums component writhes

# Key Properties
1. Independent of orientation (can be defined for unoriented links)
2. Counts only self-crossings of each component
3. Used to define ambient isotopy invariant: $f[L] = (-A)^{-3s(L)} \langle L \rangle$

# Relationships
## Builds Upon
- **writhe**

## Enables
- **one-variable-kauffman-polynomial** — $f[L] = (-A)^{-3s(L)} \langle L \rangle$ for unoriented links

## Contrasts With
- **writhe** — Writhe includes inter-component crossings

# Source Reference
Chapter X, Section X.6, page 370.

# Verification Notes
- Definition source: Direct from p. 370
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
