---
concept: Unimodality of Chromatic Polynomial Coefficients
slug: chromatic-polynomial-coefficient-unimodality
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 364
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "Read's conjecture"
prerequisites:
  - spanning-tree-expansion
  - chromatic-polynomial-from-tutte
extends: []
related:
  - nonvanishing-coefficients-tutte
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
Theorem 13 proves that for a connected graph with chromatic polynomial $p_G(x) = \sum (-1)^j a_j x^{n-j}$, the coefficients satisfy $a_0 = 1 \leq a_1 \leq \cdots \leq a_{\lfloor n/2 \rfloor}$. Read's full unimodality conjecture remains open.

# Core Definition
Theorem 13 (p. 364): "Let $G$ be a connected graph of order $n$, with chromatic polynomial $p_G(x) = \sum_{j=0}^{n-1}(-1)^j a_j x^{n-j}$. Then $a_0 = 1 \leq a_1 \leq \cdots \leq a_l$ for $l = \lfloor n/2 \rfloor$." Read conjectured (1968) full unimodality; Tutte conjectured unimodality of $t_{ij}$ separately; both remain open (the latter was disproved by Schwärzler in 1993 for matroids).

# Prerequisites
- **Spanning tree expansion** — Proof uses the expression $a_j = \sum_{i=n-j-1}^{n-1} t_{i0} \binom{i}{n-j-1}$
- **Chromatic polynomial from Tutte** — Coefficients related to $T_G$

# Key Properties
1. First half of coefficients is non-decreasing
2. Read's full unimodality conjecture: $a_0 \leq a_1 \leq \cdots \leq a_m \geq \cdots \geq a_{n-1}$ (open)
3. Tutte's unimodality conjecture for $t_{ij}$ disproved by Schwärzler (1993)
4. Proof uses $\binom{i}{n-j-1} \geq \binom{i}{n-j}$ for $n-j-1 \geq (i-1)/2$

# Relationships
## Builds Upon
- **spanning-tree-expansion**, **chromatic-polynomial-from-tutte**

## Related
- **nonvanishing-coefficients-tutte** — Related positivity results

# Source Reference
Chapter X, Section X.5, Theorem 13, pages 364-365.

# Verification Notes
- Definition source: Direct from Theorem 13
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
