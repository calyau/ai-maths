---
concept: Specializations of the Universal Polynomial
slug: universal-polynomial-specializations
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 347
section: "X.2 The Universal Form of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - universal-polynomial-of-graphs
extends: []
related:
  - tutte-polynomial
  - dichromatic-polynomial
  - chromatic-polynomial-from-tutte
  - flow-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The universal polynomial $U(G; x, y, \alpha, \sigma, \tau)$ specializes to all standard graph polynomials: Tutte ($\alpha = \sigma = \tau = 1$), chromatic ($\alpha = x, \sigma = 1, \tau = -1, y = 0$), flow ($\alpha = 1, \sigma = -1, \tau = 1, x = 0$), and dichromatic ($\alpha = q, \sigma = 1, \tau = v$).

# Core Definition
The specializations follow from Theorem 2: $U(G) = \alpha^{k(G)}\sigma^{n(G)}\tau^{r(G)} T_G(\alpha x/\tau, y/\sigma)$. Setting various parameters recovers all standard polynomials. Special degenerate cases at $\sigma = 0$ or $\tau = 0$ are given by equations (3)-(5) (pp. 347-348).

# Prerequisites
- **Universal polynomial of graphs** — The general polynomial being specialized

# Key Properties
1. $\alpha = \sigma = \tau = 1$: Tutte polynomial $T_G(x,y)$
2. $\alpha = x, \sigma = 1, \tau = -1, y = 0$: chromatic polynomial $p_G(x)$
3. $\alpha = 1, \sigma = -1, \tau = 1, x = 0$: flow polynomial $q_G(y+1)$
4. $\alpha = q, \sigma = 1, \tau = v$: dichromatic polynomial $Z_G(q,v)$
5. At $\sigma = 0$: $U = \alpha^{|G|}\sigma^{n(G)-\ell(G)}x^{r(G)}y^{\ell(G)}$ (equation (3))

# Relationships
## Builds Upon
- **universal-polynomial-of-graphs**

## Related
- **tutte-polynomial**, **dichromatic-polynomial**, **chromatic-polynomial-from-tutte**, **flow-polynomial**

# Source Reference
Chapter X, Section X.2, Theorem 2 and equations (3)-(5), pages 345-348.

# Verification Notes
- Definition source: Synthesized from Theorem 2 and pp. 346-348
- Confidence rationale: Explicit specializations
- Uncertainties: None
- Cross-reference status: Verified
