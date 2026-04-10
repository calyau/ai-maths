---
concept: Dichromatic Polynomial
slug: dichromatic-polynomial
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
  - "Z_G(q, v)"
prerequisites:
  - tutte-polynomial
  - universal-polynomial-of-graphs
extends:
  - tutte-polynomial
related:
  - partition-function-potts-model
  - random-cluster-model
  - whitney-tutte-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The dichromatic polynomial $Z_G(q, v) \in \mathbb{Z}[q, v]$ satisfies $Z_{E_n} = q^n$ and $Z_G = Z_{G-e} + v Z_{G/e}$ for every edge $e$, and equals $q^{k(G)} v^{r(G)} T_G((q+v)/v, 1+v)$.

# Core Definition
$Z_G(q, v)$ is the unique polynomial such that $Z_{E_n} = q^n$ and $Z_G = Z_{G-e} + v Z_{G/e}$ for every edge $e$, whether bridge, loop, or neither (Bollobás, p. 348, equation (6)). It equals $U$ evaluated at $\alpha = q$, $\sigma = 1$, $\tau = v$, giving $Z_G(q,v) = q^{k(G)} v^{r(G)} T_G((q+v)/v, 1+v)$.

# Prerequisites
- **Tutte polynomial** — $Z_G$ is a variant
- **Universal polynomial of graphs** — $Z_G$ is a specialization

# Key Properties
1. Satisfies $Z_G = Z_{G-e} + v Z_{G/e}$ for all edges (no case distinction needed)
2. $Z_G(q,v) = \sum_{F \subset E} v^{|F|} q^{k(F)}$ (from the proof of Theorem 4)
3. "It is precisely the incarnation $Z_G$ of the Tutte polynomial that appears in statistical physics" (p. 348)

# Context & Application
The dichromatic polynomial is the form of the Tutte polynomial that appears naturally in statistical mechanics. The Potts model partition function is $P_G(q,\beta) = e^{-\beta|E|} Z_G(q, e^\beta - 1)$ and the random cluster model partition function is $R_G(q,p) = (1-p)^{|E|} Z_G(q, p/(1-p))$.

# Examples
**Example**: $Z_{K_2}(q,v) = q^2 + qv = q(q+v)$.

# Relationships
## Builds Upon
- **tutte-polynomial**, **universal-polynomial-of-graphs**

## Enables
- **partition-function-potts-model** — $P_G = e^{-\beta|E|} Z_G(q, e^\beta - 1)$
- **random-cluster-model** — $R_G = (1-p)^{|E|} Z_G(q, p/(1-p))$

# Source Reference
Chapter X, Section X.2, equation (6), pages 348-349.

# Verification Notes
- Definition source: Direct from equation (6), p. 348
- Confidence rationale: Explicit definition and formula
- Uncertainties: None
- Cross-reference status: Verified
