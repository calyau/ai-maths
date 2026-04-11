---
concept: Coset
slug: coset
category: group-theory
subcategory: quotients
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.1 Definitions and Examples"
extraction_confidence: high
aliases:
  - "left coset"
  - "right coset"
prerequisites:
  - subgroup
extends: []
related:
  - normal-subgroup
  - quotient-group
  - lagrange-theorem
  - index-of-a-subgroup
contrasts_with: []
answers_questions:
  - "What is a coset?"
  - "How do cosets partition a group?"
  - "How do I construct a quotient group?"
---

# Quick Definition
For a subgroup N of G and $g \in G$, the left coset is $gN = \{gn \mid n \in N\}$ and the right coset is $Ng = \{ng \mid n \in N\}$. Cosets partition G into subsets of equal size.

# Core Definition
For any $N \leq G$ and $g \in G$, the *left coset* of N with representative g is $gN = \{gn \mid n \in N\}$ and the *right coset* is $Ng = \{ng \mid n \in N\}$. Any element of a coset is a *representative*. The left cosets partition G: $uN = vN$ iff $v^{-1}u \in N$ (Proposition 4). Each coset has $|N|$ elements, and all cosets have the same size (Dummit & Foote, pp. 77-80).

# Prerequisites
- **Subgroup** — cosets are defined for subgroups

# Key Properties
1. Left cosets of N partition G (Proposition 4)
2. $uN = vN$ iff $v^{-1}u \in N$
3. All cosets have the same cardinality $|N|$
4. For normal N: $gN = Ng$ for all g (left = right cosets)
5. $|G| = |N| \cdot [\text{number of cosets}]$ for finite G
6. Coset multiplication $uN \cdot vN = (uv)N$ is well defined iff $N \trianglelefteq G$

# Construction / Recognition
## To Construct/Create:
1. Pick a representative $g \in G$
2. Multiply g by every element of N: $gN = \{gn \mid n \in N\}$

## To Identify/Recognize:
1. A coset is a translate of the subgroup N
2. Two elements are in the same left coset iff their ratio $v^{-1}u$ is in N

# Context & Application
Cosets are the building blocks of quotient groups. They generalize the residue classes of $\mathbb{Z}/n\mathbb{Z}$. Lagrange's Theorem follows directly from the fact that cosets partition G into equal-sized pieces.

# Examples
**Example 1** (p. 80): In $\mathbb{Z}$, the cosets of $n\mathbb{Z}$ are the residue classes $a + n\mathbb{Z}$.
**Example 2** (p. 84): In $D_8$ with $Z = \{1, r^2\}$: the cosets are $\{1, r^2\}, \{r, r^3\}, \{s, sr^2\}, \{sr, sr^3\}$.

# Relationships
## Builds Upon
- **subgroup**

## Enables
- **quotient-group** — elements of G/N are cosets
- **lagrange-theorem** — cosets have equal size
- **index-of-a-subgroup** — number of cosets

## Related
- **normal-subgroup** — left and right cosets agree iff N is normal

# Common Errors
- **Error**: Multiplying cosets when the subgroup is not normal. **Correction**: The product $uN \cdot vN = (uv)N$ is only well defined when $N \trianglelefteq G$.

# Common Confusions
- **Confusion**: Thinking $gN = Ng$ always. **Clarification**: Left and right cosets coincide only when N is normal. In general, $gN \neq Ng$.

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.1-3.2, pages 77-86.

# Verification Notes
- Definition source: direct from source pp. 77-78
- Confidence rationale: explicitly defined with propositions
- Uncertainties: none
- Cross-reference status: verified
