---
concept: Universal Polynomial of Graphs
slug: universal-polynomial-of-graphs
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 345
section: "X.2 The Universal Form of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "U(G; x, y, alpha, sigma, tau)"
  - "Oxley-Welsh polynomial"
prerequisites:
  - tutte-polynomial
extends:
  - tutte-polynomial
related:
  - dichromatic-polynomial
  - whitney-tutte-polynomial
  - chromatic-polynomial-from-tutte
  - flow-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The universal polynomial $U(G; x, y, \alpha, \sigma, \tau) \in \mathbb{Z}[x, y, \alpha, \sigma, \tau]$ is a 5-variable polynomial that reduces to the Tutte polynomial at $\alpha = \sigma = \tau = 1$ and captures all graph polynomials definable by deletion-contraction with multiplicativity.

# Core Definition
Theorem 2 (p. 345): There is a unique map $U: \mathcal{G} \to \mathbb{Z}[x, y, \alpha, \sigma, \tau]$ such that $U(E_n) = \alpha^n$ and for every $e \in E(G)$: $U(G) = xU(G-e)$ (bridge), $U(G) = yU(G-e)$ (loop), $U(G) = \sigma U(G-e) + \tau U(G/e)$ (otherwise). Furthermore: $U(G) = \alpha^{k(G)} \sigma^{n(G)} \tau^{r(G)} T_G(\alpha x/\tau, y/\sigma)$.

# Prerequisites
- **Tutte polynomial** — The universal polynomial generalizes it

# Key Properties
1. $U(E_n) = \alpha^n$
2. At $\alpha = \sigma = \tau = 1$: $U = T_G$
3. $U(G) = \alpha^{k(G)} \sigma^{n(G)} \tau^{r(G)} T_G(\alpha x/\tau, y/\sigma)$ (equation (2))
4. Multiplicativity: $U(G_1 \cup G_2) = U(G_1) U(G_2)$ (disjoint) or $U(G_1) U(G_2)/\alpha$ (shared vertex)
5. Chromatic polynomial: $p_G(x) = U(G; (x-1)/x, 0, x, 1, -1)$
6. Flow polynomial: $q_G(k) = U(G; 0, k-1, 1, -1, 1)$

# Construction / Recognition
For any commutative ring $R$ and $x, y, \alpha, \sigma, \tau \in R$, evaluate the polynomial $U$ at those values. This is the unique map satisfying the recursion.

# Context & Application
The universal polynomial shows that the Tutte polynomial, chromatic polynomial, flow polynomial, and all deletion-contraction-definable graph polynomials are "easily obtained" (p. 346) by specializing parameters. "Theorem 2 implies that if $R$ is a commutative ring and $x, y, \alpha, \sigma, \tau \in R$ then there is a unique map $G \to R$ satisfying the conditions."

# Examples
**Example**: Chromatic polynomial: $\alpha = x$, $\sigma = 1$, $\tau = -1$, $x \leftarrow (x-1)/x$, $y = 0$.

**Example**: Flow polynomial: $\alpha = 1$, $\sigma = -1$, $\tau = 1$, $x = 0$, $y = k-1$.

# Relationships
## Builds Upon
- **tutte-polynomial**

## Enables
- **chromatic-polynomial-from-tutte** — As a specialization
- **flow-polynomial** — As a specialization
- **dichromatic-polynomial** — As a specialization

# Source Reference
Chapter X, Section X.2, Theorem 2, pages 345-347.

# Verification Notes
- Definition source: Direct from Theorem 2, p. 345
- Confidence rationale: Named theorem with explicit formula
- Uncertainties: None
- Cross-reference status: Verified
