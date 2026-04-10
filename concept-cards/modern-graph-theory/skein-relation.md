---
concept: Skein Relation
slug: skein-relation
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 371
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "Jones skein relation"
prerequisites:
  - jones-polynomial
  - link-diagram
extends: []
related:
  - kauffman-bracket
  - deletion-contraction
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The skein relation for the Jones polynomial is $t^{-1}V_{\nearrow} - tV_{\searrow} = (\sqrt{t} - 1/\sqrt{t})V_{\asymp}$, relating the polynomials of three link diagrams that differ only at one crossing.

# Core Definition
Equation (9) (p. 371): "$t^{-1}V_{\nearrow} - tV_{\searrow} = (\sqrt{t} - 1/\sqrt{t})V_{\asymp}$." Together with $V_{\bigcirc} = 1$, this uniquely determines the Jones polynomial. It is the knot-theoretic analogue of the deletion-contraction relation.

# Prerequisites
- **Jones polynomial** — The polynomial satisfying the relation
- **Link diagram** — The three diagrams related by the skein relation

# Key Properties
1. Relates three diagrams differing at one crossing
2. Together with $V_{\bigcirc} = 1$, uniquely determines $V_L$
3. Analogous to $T_G = T_{G-e} + T_{G/e}$ for graphs
4. "It is easily seen that there is at most one Laurent polynomial satisfying the relations above" (p. 371)

# Context & Application
The skein relation demonstrates the deep parallel between the Tutte polynomial (deletion-contraction) and the Jones polynomial (skein relation). Both are defined by resolving local structure (edges vs crossings) in two ways.

# Relationships
## Builds Upon
- **jones-polynomial**, **link-diagram**

## Related
- **kauffman-bracket** — Satisfies $\langle L \rangle = A\langle L_v^A \rangle + A^{-1}\langle L_v^B \rangle$
- **deletion-contraction** — Graph-theoretic analogue

# Source Reference
Chapter X, Section X.6, equation (9), page 371.

# Verification Notes
- Definition source: Direct from equation (9)
- Confidence rationale: Explicit equation
- Uncertainties: None
- Cross-reference status: Verified
