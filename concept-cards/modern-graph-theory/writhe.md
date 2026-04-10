---
concept: Writhe
slug: writhe
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 370
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "twist number"
  - "w(L)"
prerequisites:
  - link-diagram
extends: []
related:
  - self-writhe
  - jones-polynomial
  - one-variable-kauffman-polynomial
contrasts_with:
  - self-writhe
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The writhe $w(L)$ of an oriented link diagram $L$ is the sum of the signs ($\pm 1$) of all crossings. It is a regular isotopy invariant but not an ambient isotopy invariant.

# Core Definition
"The sum of the signs of all the crossings in an oriented link diagram $L$ is the twist number or writhe $w(L)$ of $L$" (Bollobás, p. 370). Crossings are assigned signs $+1$ or $-1$ according to the convention in Fig. X.11.

# Prerequisites
- **Link diagram** — Writhe is defined on oriented link diagrams

# Key Properties
1. $w(L) = \sum_v \varepsilon(v)$ where $\varepsilon(v) \in \{+1, -1\}$
2. Regular isotopy invariant (unchanged by Types II and III)
3. NOT ambient isotopy invariant (changes under Type I)
4. Under Type I: $w$ changes by $\pm 1$

# Examples
**Example** (Fig. X.11, p. 370): Diagram of knot $6_1$ with writhe computed.

# Relationships
## Builds Upon
- **link-diagram**

## Enables
- **jones-polynomial** — Uses $(-A)^{-3w(L)}$ normalization
- **one-variable-kauffman-polynomial** — $f[L] = (-A)^{-3w(L)} \langle L \rangle$

## Contrasts With
- **self-writhe** — Sum only over self-crossings of each component

# Source Reference
Chapter X, Section X.6, page 370. Figure X.11.

# Verification Notes
- Definition source: Direct from p. 370
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
