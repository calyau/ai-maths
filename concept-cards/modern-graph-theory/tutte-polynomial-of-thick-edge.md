---
concept: Tutte Polynomial of a Thick Edge
slug: tutte-polynomial-of-thick-edge
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 378
section: "X.7 Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - deletion-contraction
extends: []
related:
  - tutte-polynomial-of-cycle
contrasts_with:
  - tutte-polynomial-of-cycle
answers_questions:
  - "How do I compute the Tutte polynomial using deletion-contraction?"
---

# Quick Definition
The Tutte polynomial of the thick edge $I_k$ (two vertices joined by $k$ parallel edges) is $T_{I_k}(x,y) = x + y + y^2 + \cdots + y^{k-1}$.

# Core Definition
Exercise 2 (p. 378): $T_{I_k} = x + y + y^2 + \cdots + y^{k-1}$. This is the "dual" of the cycle polynomial: if $G^*$ is the dual of $C_n$ in the plane, then $G^* = I_n$, and $T_{G^*}(x,y) = T_G(y,x)$.

# Prerequisites
- **Tutte polynomial**, **deletion-contraction**

# Key Properties
1. Dual to the cycle: $T_{I_k}(x,y) = T_{C_k}(y,x)$
2. $T_{I_k}(1,1) = k$ (spanning trees)
3. For $k = 1$: $T_{I_1} = T_{K_2} = x$ (single edge/bridge)

# Relationships
## Builds Upon
- **tutte-polynomial**, **deletion-contraction**

## Contrasts With
- **tutte-polynomial-of-cycle** — Roles of $x, y$ are swapped

# Source Reference
Chapter X, Exercise 2, page 378.

# Verification Notes
- Definition source: Direct from Exercise 2
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
