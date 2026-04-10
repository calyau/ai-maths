---
concept: Kauffman Square Bracket
slug: kauffman-square-bracket
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 368
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "[L]"
  - "square bracket polynomial"
prerequisites:
  - state-of-link-diagram
  - link-diagram
extends: []
related:
  - kauffman-bracket
  - tutte-polynomial
contrasts_with:
  - kauffman-bracket
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The Kauffman square bracket $[L] \in \mathbb{Z}[A, B, d]$ of a link diagram $L$ is $[L] = \sum_S A^{a_L(S)} B^{b_L(S)} d^{c_L(S)-1}$, summing over all states of the diagram.

# Core Definition
$[L] = \sum_S A^{a_L(S)} B^{b_L(S)} d^{c_L(S)-1}$ (Bollobás, p. 368). Theorem 16 establishes this is the unique map $\varphi: \mathcal{L} \to \mathbb{Z}[A, B, d]$ satisfying: (i) invariance under planar isotopy, (ii) $\varphi(\bigcirc) = 1$, (iii) $\varphi(L \cup \bigcirc) = d\varphi(L)$, (iv) $\varphi(L) = A\varphi(L_v^A) + B\varphi(L_v^B)$.

# Prerequisites
- **State of a link diagram** — The sum is over all states
- **Link diagram** — Input to the bracket

# Key Properties
1. Three-variable polynomial in $A, B, d$
2. Recursion mirrors the Tutte polynomial: $[L] = A[L_v^A] + B[L_v^B]$
3. Multiplicative: $[L_1 \cup L_2] = d \cdot [L_1] \cdot [L_2]$ (for disjoint components)
4. Setting $B = A^{-1}$, $d = -A^2 - A^{-2}$ gives the Kauffman bracket $\langle L \rangle$

# Context & Application
"Imitating the Tutte polynomial and its variants, we shall define a polynomial, the Kauffman bracket, whose value on a link diagram $L$ is a fixed linear combination of its values on $L_v^A$ and $L_v^B$" (p. 368). The resemblance to the Tutte polynomial "is not only skin deep" (p. 340).

# Relationships
## Builds Upon
- **state-of-link-diagram**, **link-diagram**

## Enables
- **kauffman-bracket** — Evaluation at $B = A^{-1}$, $d = -A^2 - A^{-2}$

## Related
- **tutte-polynomial** — Analogous structure; related for alternating links

## Contrasts With
- **kauffman-bracket** — Two fewer variables

# Source Reference
Chapter X, Section X.6, Theorem 16, pages 368-369.

# Verification Notes
- Definition source: Direct from p. 368
- Confidence rationale: Explicit definition and uniqueness theorem
- Uncertainties: None
- Cross-reference status: Verified
