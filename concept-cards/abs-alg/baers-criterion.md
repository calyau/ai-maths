---
concept: "Baer's Criterion"
slug: baers-criterion
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 409
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases: []
prerequisites:
  - injective-module
  - left-ideal
extends: []
related:
  - divisible-module
contrasts_with: []
answers_questions:
  - "How do I check if a module is injective?"
---

# Quick Definition
Baer's Criterion states that an R-module Q is injective if and only if every R-module homomorphism from a left ideal I of R into Q can be extended to a homomorphism from R into Q.

# Core Definition
(Proposition 36) The module Q is injective if and only if for every left ideal I of R, any R-module homomorphism $g: I \to Q$ can be extended to an R-module homomorphism $G: R \to Q$. Over a PID, Q is injective if and only if $rQ = Q$ for every nonzero $r \in R$. In particular, a $\mathbb{Z}$-module is injective if and only if it is divisible (Dummit & Foote, Proposition 36, pp. 409-410).

# Prerequisites
- **injective-module** — Baer's criterion characterizes injective modules
- **left-ideal** — Extension from ideals to the whole ring

# Key Properties
1. Reduces checking injectivity to extending maps from ideals (not arbitrary submodules)
2. Over a PID with ideal $(r)$, extending amounts to showing $rQ = Q$
3. Quotients of injective modules over PIDs are injective

# Context & Application
Baer's Criterion (introduced around 1940) provides a practical test for injectivity, reducing the universal extension property to a check on ideals only.

# Examples
**Example** (p. 410): $\mathbb{Q}$ is injective over $\mathbb{Z}$ since $n\mathbb{Q} = \mathbb{Q}$ for all nonzero integers n.

# Relationships
## Builds Upon
- **injective-module**

## Related
- **divisible-module** — Over a PID, injective = divisible

# Source Reference
Chapter 10, Section 10.5, Proposition 36, pp. 409-410.

# Verification Notes
- Confidence: HIGH — explicit proposition with proof
