---
concept: Tutte Polynomial of a Cycle
slug: tutte-polynomial-of-cycle
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
  - tutte-polynomial-of-thick-edge
contrasts_with:
  - tutte-polynomial-of-thick-edge
answers_questions:
  - "How do I compute the Tutte polynomial using deletion-contraction?"
---

# Quick Definition
The Tutte polynomial of the $n$-cycle is $T_{C_n}(x,y) = y + x + x^2 + \cdots + x^{n-1}$ for $n \geq 1$.

# Core Definition
Exercise 1 (p. 378): "Use the contraction-deletion formula to compute the Tutte polynomial of the $n$-cycle: $T_{C_n}(x,y) = y + x + x^2 + \cdots + x^{n-1}$."

# Prerequisites
- **Tutte polynomial** — The object being computed
- **Deletion-contraction** — The method of computation

# Key Properties
1. $T_{C_n}(1,1) = n$ (number of spanning trees of $C_n$)
2. $T_{C_n}(2,1) = 2^n - 1$ (number of forests)
3. $t_{i0} = 1$ for $1 \leq i \leq n-1$ and $t_{01} = 1$; all other $t_{ij} = 0$
4. $T_{C_1}(x,y) = y$ (single loop); $T_{C_2}(x,y) = y + x$ (two parallel edges)

# Relationships
## Builds Upon
- **tutte-polynomial**, **deletion-contraction**

## Contrasts With
- **tutte-polynomial-of-thick-edge** — $T_{I_k} = x + y + y^2 + \cdots + y^{k-1}$ (roles of $x, y$ swapped)

# Source Reference
Chapter X, Exercise 1, page 378.

# Verification Notes
- Definition source: Direct from Exercise 1
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
