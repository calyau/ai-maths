---
concept: "Cauchy's Theorem"
slug: cauchy-theorem
category: group-theory
subcategory: structure-theory
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.2 More on Cosets and Lagrange's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - lagrange-theorem
extends: []
related:
  - sylow-theorem
  - order-of-an-element
contrasts_with: []
answers_questions:
  - "Does a finite group always have an element of prime order p when p divides the group order?"
---

# Quick Definition
If G is a finite group and p is a prime dividing $|G|$, then G has an element of order p. This is a partial converse to Lagrange's Theorem.

# Core Definition
**Theorem 11 (Cauchy's Theorem):** If G is a finite group and p is a prime dividing $|G|$, then G has an element of order p. A proof due to James McKay is outlined in Exercise 9: consider the set of p-tuples $(x_1, \ldots, x_p)$ with $x_1 \cdots x_p = 1$, and use a counting argument modulo p (Dummit & Foote, p. 91).

# Prerequisites
- **Lagrange's Theorem** — Cauchy is a partial converse

# Key Properties
1. Guarantees existence of elements of prime order
2. Partial converse to Lagrange's Theorem
3. Combined with Sylow's Theorem, gives existence of subgroups of prime power order
4. For abelian groups, proved by induction using quotient groups (Proposition 21)

# Context & Application
Cauchy's Theorem is essential for proving the existence of subgroups and for structural results about finite groups. It is a stepping stone to the Sylow theorems.

# Examples
**Example 1** (p. 91): Since $3 \mid |S_3| = 6$, $S_3$ contains an element of order 3, namely $(123)$.

# Relationships
## Builds Upon
- **lagrange-theorem**

## Related
- **sylow-theorem** — stronger partial converse
- **order-of-an-element** — Cauchy gives elements of specific order

# Source Reference
Chapter 3, Section 3.2, page 91, Theorem 11; Section 3.4, Proposition 21 (abelian case).

# Verification Notes
- Definition source: direct from source p. 91
- Confidence rationale: theorem stated, proof deferred/outlined
- Uncertainties: none
- Cross-reference status: verified
