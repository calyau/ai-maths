---
concept: Index of a Subgroup
slug: index-of-a-subgroup
category: group-theory
subcategory: quotients
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.2 More on Cosets and Lagrange's Theorem"
extraction_confidence: high
aliases:
  - "$|G:H|$"
prerequisites:
  - coset
  - lagrange-theorem
extends: []
related:
  - normal-subgroup
  - quotient-group
contrasts_with: []
answers_questions:
  - "What is the index of a subgroup?"
  - "How is the index related to cosets?"
---

# Quick Definition
The index of H in G, denoted $|G:H|$, is the number of left cosets of H in G. For finite groups, $|G:H| = |G|/|H|$.

# Core Definition
If G is a group and $H \leq G$, the *index* of H in G, denoted $|G:H|$, is the number of left cosets of H in G. For finite G, $|G:H| = |G|/|H|$. The number of left cosets always equals the number of right cosets. A subgroup of index 2 is always normal (Dummit & Foote, pp. 90-91).

# Prerequisites
- **Coset** — index counts cosets
- **Lagrange's Theorem** — relates index to orders

# Key Properties
1. $|G:H| = |G|/|H|$ for finite G
2. Number of left cosets = number of right cosets
3. $|G:H| = 2$ implies $H \trianglelefteq G$
4. $|G:H| = |G:K| \cdot |K:H|$ for $H \leq K \leq G$ (tower law)
5. $|G/N| = |G:N|$ when $N \trianglelefteq G$

# Context & Application
The index provides a key numerical invariant of how a subgroup sits inside a group. Index 2 subgroups are automatically normal, making them particularly useful.

# Examples
**Example 1** (p. 91): $|\mathbb{Z} : n\mathbb{Z}| = n$.
**Example 2** (p. 87): $|D_{2n} : \langle r \rangle| = 2$, so the rotation subgroup is normal.

# Relationships
## Builds Upon
- **coset**, **lagrange-theorem**

## Related
- **normal-subgroup** — index 2 subgroups are normal
- **quotient-group** — $|G/N| = |G:N|$

# Source Reference
Chapter 3, Section 3.2, pages 90-91.

# Verification Notes
- Definition source: direct from source p. 90
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
