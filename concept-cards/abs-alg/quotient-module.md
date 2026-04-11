---
concept: Quotient Module
slug: quotient-module
category: module-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 348
section: "10.2 Quotient Modules and Module Homomorphisms"
extraction_confidence: high
aliases:
  - "factor module"
  - "quotient space"
prerequisites:
  - left-module
  - submodule
extends:
  - quotient-group
related:
  - module-homomorphism
  - first-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What is a quotient module?"
---

# Quick Definition
The quotient module M/N is formed from an R-module M and a submodule N by taking the quotient abelian group M/N and defining the R-action by $r(m + N) = rm + N$.

# Core Definition
Let N be a submodule of the R-module M. Since M is an abelian group, N is a normal subgroup, so the quotient group M/N is defined. The action of R on M/N given by $r(m + N) = rm + N$ is well-defined and makes M/N into an R-module called the quotient module (or factor module) of M by N. When R is a field, this is called a quotient space (Dummit & Foote, p. 348).

# Prerequisites
- **left-module** — The ambient module M
- **submodule** — The submodule N by which we quotient

# Key Properties
1. The action $r(m + N) = rm + N$ is well-defined because N is closed under the ring action
2. The natural projection $\pi: M \to M/N$ is an R-module homomorphism
3. There is a lattice correspondence between submodules of M/N and submodules of M containing N

# Construction / Recognition
1. Start with a module M and a submodule N
2. Form the quotient abelian group M/N (cosets $m + N$)
3. Define $r(m + N) = rm + N$
4. Verify this is well-defined: if $m + N = m' + N$ then $m - m' \in N$ so $rm - rm' = r(m-m') \in N$

# Context & Application
Quotient modules are fundamental to the isomorphism theorems and to understanding module structure through short exact sequences.

# Examples
**Example** (p. 349): If $R = \mathbb{Z}$ and $M = \mathbb{Z}$, $N = n\mathbb{Z}$, then $M/N = \mathbb{Z}/n\mathbb{Z}$ is the quotient $\mathbb{Z}$-module (i.e., the cyclic group of order n).

# Relationships
## Builds Upon
- **left-module**, **submodule**, **quotient-group**

## Enables
- **first-isomorphism-theorem** — $M/\ker\varphi \cong \text{image}(\varphi)$

# Source Reference
Chapter 10, Section 10.2, pp. 348-350.

# Verification Notes
- Definition: synthesized from p. 348
- Confidence: HIGH — standard construction
