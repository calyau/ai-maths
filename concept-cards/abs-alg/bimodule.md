---
concept: Bimodule
slug: bimodule
category: module-theory
subcategory: tensor-products
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 378
section: "10.4 Tensor Products of Modules"
extraction_confidence: high
aliases:
  - "(S,R)-bimodule"
prerequisites:
  - left-module
  - right-module
extends: []
related:
  - tensor-product
  - extension-of-scalars
contrasts_with: []
answers_questions:
  - "What is a bimodule?"
---

# Quick Definition
An (S, R)-bimodule is an abelian group M that is simultaneously a left S-module and a right R-module, with the compatibility condition $s(mr) = (sm)r$ for all $s \in S$, $r \in R$, $m \in M$.

# Core Definition
Let R and S be rings with 1. An abelian group M is called an (S, R)-bimodule if M is a left S-module, a right R-module, and $s(mr) = (sm)r$ for all $s \in S$, $r \in R$ and $m \in M$ (Dummit & Foote, p. 378).

# Prerequisites
- **left-module** — One of the two module structures
- **right-module** — The other module structure

# Key Properties
1. Any ring S is an (S, R)-bimodule for any subring R with $1_R = 1_S$
2. If R is commutative, every left R-module has a natural (R, R)-bimodule structure with $mr = rm$
3. The (S, R)-bimodule structure on M makes $M \otimes_R N$ into a left S-module

# Examples
**Example** (p. 378): $R/I$ is an (R/I, R)-bimodule for any two-sided ideal I of R.

# Relationships
## Builds Upon
- **left-module**, **right-module**

## Enables
- **tensor-product** — Bimodule structure gives tensor products module structure

# Source Reference
Chapter 10, Section 10.4, pp. 378-380.

# Verification Notes
- Confidence: HIGH — explicit definition
