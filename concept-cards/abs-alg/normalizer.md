---
concept: Normalizer
slug: normalizer
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
  - "$N_G(A)$"
prerequisites:
  - subgroup
  - centralizer
extends: []
related:
  - centralizer
  - normal-subgroup
  - conjugation
contrasts_with:
  - centralizer
answers_questions:
  - "What is the normalizer of a subset?"
  - "How does the normalizer relate to normality?"
---

# Quick Definition
The normalizer of A in G is $N_G(A) = \{g \in G \mid gAg^{-1} = A\}$, the set of elements that leave A invariant under conjugation. A subgroup N is normal in G iff $N_G(N) = G$.

# Core Definition
For any nonempty subset A of G, define $gAg^{-1} = \{gag^{-1} \mid a \in A\}$. The *normalizer* of A in G is $N_G(A) = \{g \in G \mid gAg^{-1} = A\}$. This is a subgroup of G containing $C_G(A)$. A subgroup N is normal in G precisely when $N_G(N) = G$, so the normalizer measures "how close" N is to being normal (Dummit & Foote, pp. 50-52).

# Prerequisites
- **Subgroup** — normalizers are subgroups
- **Centralizer** — $C_G(A) \leq N_G(A)$

# Key Properties
1. $N_G(A) \leq G$
2. $C_G(A) \leq N_G(A)$
3. $H \leq N_G(H)$ for any subgroup H
4. $N \trianglelefteq G$ iff $N_G(N) = G$
5. $N_G(N)$ is the largest subgroup of G in which N is normal

# Construction / Recognition
## To Construct/Create:
1. For each $g \in G$, check if $gAg^{-1} = A$ (as sets)
2. Collect all such g

# Context & Application
The normalizer is the gateway to normal subgroups. Computing $N_G(H)$ determines the largest subgroup of G in which H is normal, and $|G : N_G(H)|$ counts the number of conjugates of H.

# Examples
**Example 1** (p. 51): $N_{D_8}(\{1,r,r^2,r^3\}) = D_8$ since $sAs^{-1} = A$, so the rotation subgroup is normal.
**Example 2** (p. 52): $N_{S_3}(\{1,(12)\}) = \{1,(12)\}$, so $\langle(12)\rangle$ is NOT normal in $S_3$.

# Relationships
## Builds Upon
- **subgroup**, **centralizer**

## Enables
- **normal-subgroup** — $N \trianglelefteq G$ iff $N_G(N) = G$

## Related
- **conjugation** — normalizer defined via conjugation

## Contrasts With
- **centralizer** — centralizer fixes elements pointwise; normalizer fixes the set

# Common Confusions
- **Confusion**: Thinking $gAg^{-1} = A$ means $gag^{-1} = a$ for all $a$. **Clarification**: It means the SET is invariant; individual elements may be permuted.

# Source Reference
Chapter 2: Subgroups, Section 2.2, pages 50-52.

# Verification Notes
- Definition source: direct from source p. 50
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
