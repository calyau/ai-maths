---
concept: Chromatic Polynomial from the Tutte Polynomial
slug: chromatic-polynomial-from-tutte
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 353
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - chromatic-polynomial
  - universal-polynomial-of-graphs
extends: []
related:
  - flow-polynomial
  - deletion-contraction
contrasts_with: []
answers_questions:
  - "How does the chromatic polynomial relate to the Tutte polynomial?"
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The chromatic polynomial is obtained from the Tutte polynomial by setting $y = 0$: $p_G(x) = (-1)^{r(G)} x^{k(G)} T_G(1-x, 0)$.

# Core Definition
Theorem 6 (p. 353): "The chromatic polynomial $p_G(x)$ of a graph $G$ is $p_G(x) = (-1)^{r(G)} x^{k(G)} T_G(1-x, 0)$." The proof uses the universal polynomial (Theorem 2) together with the properties: $p_{E_n} = x^n$, $p_G = \frac{x-1}{x} p_{G-e}$ (bridge), $p_G = 0$ (loop), $p_G = p_{G-e} - p_{G/e}$ (otherwise).

# Prerequisites
- **Tutte polynomial** — The chromatic polynomial is a specialization
- **Chromatic polynomial** — The object being expressed
- **Universal polynomial of graphs** — Used in the proof

# Key Properties
1. $p_G(x) = (-1)^{r(G)} x^{k(G)} T_G(1-x, 0)$
2. Equivalently: $p_G(x) = U(G; (x-1)/x, 0, x, 1, -1)$
3. If $G$ has a loop: $p_G(x) = 0$
4. Multiple edges do not affect $p_G$
5. The chromatic polynomial is the Tutte polynomial at $y = 0$ (suitably normalized)

# Context & Application
This theorem shows that "the chromatic polynomial is simply the Tutte polynomial with $y = 0$, suitably normalized" (p. 353). It demonstrates that the Tutte polynomial carries strictly more information than the chromatic polynomial.

# Examples
**Example**: For $K_n$: $p_{K_n}(x) = x(x-1)\cdots(x-n+1)$, which matches $(-1)^{n-1} x \cdot T_{K_n}(1-x, 0)$.

# Relationships
## Builds Upon
- **tutte-polynomial**, **chromatic-polynomial**, **universal-polynomial-of-graphs**

## Related
- **flow-polynomial** — Analogous relationship at $x = 0$

# Common Confusions
- **Confusion**: Thinking the Tutte polynomial is just a reformulation of the chromatic polynomial.
  **Clarification**: The Tutte polynomial has two variables and carries much more information; the chromatic polynomial is obtained by setting $y = 0$.

# Source Reference
Chapter X, Section X.4, Theorem 6, page 353.

# Verification Notes
- Definition source: Direct from Theorem 6
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
