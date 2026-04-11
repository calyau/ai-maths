---
concept: Third Isomorphism Theorem
slug: third-isomorphism-theorem
category: group-theory
subcategory: isomorphism-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.3 The Isomorphism Theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - first-isomorphism-theorem
  - quotient-group
extends:
  - first-isomorphism-theorem
related:
  - second-isomorphism-theorem
  - fourth-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What happens when you take a quotient of a quotient?"
---

# Quick Definition
If $H \leq K$ are both normal subgroups of G, then $K/H \trianglelefteq G/H$ and $(G/H)/(K/H) \cong G/K$. Informally: "cancel the H's."

# Core Definition
**Theorem 19 (Third Isomorphism Theorem):** Let H and K be normal subgroups of G with $H \leq K$. Then $K/H \trianglelefteq G/H$ and $(G/H)/(K/H) \cong G/K$. The map $\varphi: G/H \to G/K$ defined by $gH \mapsto gK$ is a well-defined surjective homomorphism with kernel $K/H$ (Dummit & Foote, pp. 98-99).

# Prerequisites
- **First Isomorphism Theorem** — used in the proof
- **Quotient group** — involves quotients of quotients

# Key Properties
1. No new structure from iterated quotients: $(G/H)/(K/H) \cong G/K$
2. Memory aid: "invert and cancel" like fractions

# Context & Application
Shows that quotients of quotients yield nothing new beyond a single quotient. This simplifies computations and shows that iterated quotient constructions are redundant.

# Examples
**Example 1** (p. 99): $(\mathbb{Z}/24\mathbb{Z})/(12\mathbb{Z}/24\mathbb{Z}) \cong \mathbb{Z}/12\mathbb{Z}$.

# Relationships
## Builds Upon
- **first-isomorphism-theorem**, **quotient-group**

## Related
- **second-isomorphism-theorem**, **fourth-isomorphism-theorem**

# Source Reference
Chapter 3, Section 3.3, pages 98-99, Theorem 19.

# Verification Notes
- Definition source: direct from source pp. 98-99
- Confidence rationale: major theorem, explicitly proved
- Uncertainties: none
- Cross-reference status: verified
