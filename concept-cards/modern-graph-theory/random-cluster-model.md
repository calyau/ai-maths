---
concept: Random Cluster Model
slug: random-cluster-model
category: statistical-mechanics
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 351
section: "X.3 The Tutte Polynomial in Statistical Mechanics"
extraction_confidence: high
aliases:
  - "Fortuin-Kasteleyn model"
  - "FK model"
prerequisites:
  - dichromatic-polynomial
extends:
  - potts-model
related:
  - partition-function-potts-model
  - tutte-polynomial
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to statistical mechanics?"
---

# Quick Definition
The random cluster model on $G$ with parameters $q > 0$ and $0 < p < 1$ is a probability space on spanning subgraphs where the measure of $F \subset E$ is $\nu_G^{q,p}(F) = p^{|F|}(1-p)^{|E|-|F|} q^{k(F)}$, with partition function $R_G(q,p) = (1-p)^{|E|} Z_G(q, p/(1-p))$.

# Core Definition
The random cluster model, constructed by Fortuin and Kasteleyn, has measure $\nu_G^{q,p}(F) = p^{|F|}(1-p)^{|E|-|F|} q^{k(F)}$ and partition function $R_G(q,p) = \sum_{F \subset E} p^{|F|}(1-p)^{|E|-|F|} q^{k(F)}$ (Bollobás, p. 351). Theorem 4: $R_G(q,p) = (1-p)^{|E|} Z_G(q, v)$ where $v = p/(1-p)$.

# Prerequisites
- **Dichromatic polynomial** — Partition function is $(1-p)^{|E|} Z_G(q, v)$

# Key Properties
1. $q > 0$ need not be an integer (unlike Potts model)
2. For $q = 1$: reduces to the standard random graph model $\mathcal{G}(G, p)$
3. For large $q$: favours graphs with many components
4. Partition function: $R_G(q,p) = (1-p)^{|E|} Z_G(q, p/(1-p))$
5. "Not too far from the standard random graph model $\mathcal{G}(G,p)$" (p. 351)

# Context & Application
The random cluster model is "an extension of the Potts model itself" (p. 351) by Fortuin and Kasteleyn. It allows non-integer $q$ and connects the Tutte polynomial to percolation theory. Methods from random graph theory can sometimes be applied.

# Examples
**Example** (p. 351): For $q = 1$, the model is exactly $\mathcal{G}(G, p)$, the standard random subgraph model.

# Relationships
## Builds Upon
- **dichromatic-polynomial**

## Extends
- **potts-model** — Generalizes to non-integer $q$

## Related
- **tutte-polynomial** — Partition function is a transform of $T_G$

# Source Reference
Chapter X, Section X.3, Theorem 4, pages 351-352.

# Verification Notes
- Definition source: Direct from p. 351
- Confidence rationale: Explicit definition and theorem
- Uncertainties: None
- Cross-reference status: Verified
