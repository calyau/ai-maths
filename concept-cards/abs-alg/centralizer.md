---
concept: Centralizer
slug: centralizer
category: group-theory
subcategory: subgroups
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Subgroups"
chapter_number: 2
pdf_page: 46
section: "2.2 Centralizers and Normalizers, Stabilizers and Kernels"
extraction_confidence: high
aliases:
  - "$C_G(A)$"
prerequisites:
  - subgroup
extends: []
related:
  - normalizer
  - center-of-a-group
  - stabilizer
contrasts_with:
  - normalizer
answers_questions:
  - "What is the centralizer of a subset?"
  - "How does the centralizer differ from the normalizer?"
---

# Quick Definition
The centralizer of a subset A in G is $C_G(A) = \{g \in G \mid gag^{-1} = a \text{ for all } a \in A\}$, the set of elements commuting with every element of A. It is always a subgroup of G.

# Core Definition
For any nonempty subset A of G, the *centralizer* of A in G is $C_G(A) = \{g \in G \mid gag^{-1} = a \text{ for all } a \in A\}$. Since $gag^{-1} = a$ iff $ga = ag$, the centralizer is the set of elements commuting with every element of A. It is a subgroup of G: $1 \in C_G(A)$, it is closed under inverses and products (Dummit & Foote, pp. 49-50).

# Prerequisites
- **Subgroup** — centralizers are subgroups

# Key Properties
1. $C_G(A) \leq G$ for any nonempty $A \subseteq G$
2. $C_G(A) \leq N_G(A)$ (centralizer is contained in normalizer)
3. If G is abelian, $C_G(A) = G$ for all A
4. $C_G(\langle x \rangle) = C_G(x)$ for any $x \in G$
5. If $A \subseteq B$ then $C_G(B) \leq C_G(A)$

# Construction / Recognition
## To Construct/Create:
1. For each $g \in G$, check if $gag^{-1} = a$ for all $a \in A$
2. Collect all such g

# Context & Application
Centralizers measure commutativity in non-abelian groups. Computing centralizers helps determine the center and understand conjugacy.

# Examples
**Example 1** (p. 50): $C_{Q_8}(i) = \{\pm 1, \pm i\}$.
**Example 2** (p. 51): In $D_8$, $C_{D_8}(\{1,r,r^2,r^3\}) = \{1,r,r^2,r^3\}$ since $s$ does not commute with $r$.

# Relationships
## Builds Upon
- **subgroup**

## Enables
- **center-of-a-group** — $Z(G) = C_G(G)$

## Related
- **normalizer** — $C_G(A) \leq N_G(A)$

## Contrasts With
- **normalizer** — centralizer fixes elements pointwise; normalizer fixes the set

# Common Errors
- **Error**: Assuming $x \in C_G(A)$ and $y \in C_G(A)$ implies $xy = yx$. **Correction**: Both commute with A, but they need not commute with each other.

# Common Confusions
- **Confusion**: Confusing centralizer with normalizer. **Clarification**: $g \in C_G(A)$ means $gag^{-1} = a$ for ALL $a \in A$; $g \in N_G(A)$ means $gAg^{-1} = A$ as a SET.

# Source Reference
Chapter 2: Subgroups, Section 2.2, pages 49-52.

# Verification Notes
- Definition source: direct from source pp. 49-50
- Confidence rationale: explicitly defined with proof it is a subgroup
- Uncertainties: none
- Cross-reference status: verified
