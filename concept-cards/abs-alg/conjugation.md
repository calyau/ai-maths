---
concept: Conjugation
slug: conjugation
category: group-theory
subcategory: actions
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
  - "conjugate"
prerequisites:
  - group
  - group-action
extends: []
related:
  - normal-subgroup
  - normalizer
  - centralizer
  - center-of-a-group
contrasts_with: []
answers_questions:
  - "What is a conjugate of an element?"
  - "What does it mean for a subgroup to be invariant under conjugation?"
---

# Quick Definition
The conjugate of $n$ by $g$ is $gng^{-1}$. For a subset N, $gNg^{-1} = \{gng^{-1} \mid n \in N\}$. An element g normalizes N if $gNg^{-1} = N$. A subgroup is normal iff it is invariant under all conjugations.

# Core Definition
The element $gng^{-1}$ is the *conjugate* of $n$ by $g$. The set $gNg^{-1} = \{gng^{-1} \mid n \in N\}$ is the *conjugate* of N by g. The element g *normalizes* N if $gNg^{-1} = N$. Conjugation defines a group action of G on itself: $g \cdot a = gag^{-1}$ satisfies the axioms of a left group action. For fixed g, conjugation by g is an automorphism of G (Dummit & Foote, pp. 82-83, Section 1.7 Exercise 16-17).

# Prerequisites
- **Group**, **Group action**

# Key Properties
1. Conjugation preserves element order: $|gxg^{-1}| = |x|$
2. Conjugation is an automorphism of G (for each fixed g)
3. $N \trianglelefteq G$ iff $gNg^{-1} = N$ for all $g \in G$
4. The centralizer of A is the kernel of G acting on A by conjugation
5. The normalizer of A is the stabilizer of A under conjugation on $\mathcal{P}(G)$

# Context & Application
Conjugation is arguably the most important group action in group theory. It connects normal subgroups, centralizers, normalizers, and the center. Many structural results about groups are proved using conjugation.

# Examples
**Example 1** (p. 87): In $S_3$, $(12)(123)(12)^{-1} = (132)$.
**Example 2** (p. 88): $rsr^{-1} = sr^{-2}$ in $D_8$, showing $\langle s \rangle$ is not normal.

# Relationships
## Builds Upon
- **group**, **group-action**

## Enables
- **normal-subgroup** — defined via conjugation invariance
- **normalizer** — stabilizer under conjugation
- **centralizer** — kernel of conjugation action on a subset

# Source Reference
Chapter 3, Section 3.1, pages 82-83; Chapter 1, Section 1.7, Exercises 16-17.

# Verification Notes
- Definition source: direct from source p. 82
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
