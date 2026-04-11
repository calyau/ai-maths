---
concept: Center of a Group
slug: center-of-a-group
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
  - "center"
  - "$Z(G)$"
prerequisites:
  - centralizer
extends:
  - centralizer
related:
  - abelian-group
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "What is the center of a group?"
  - "When is the center trivial?"
---

# Quick Definition
The center of G is $Z(G) = \{g \in G \mid gx = xg \text{ for all } x \in G\}$, the set of elements commuting with everything. It is always a normal subgroup.

# Core Definition
The *center* of G is $Z(G) = \{g \in G \mid gx = xg \text{ for all } x \in G\}$. Since $Z(G) = C_G(G)$, it is a subgroup of G. Moreover, $Z(G) \trianglelefteq G$ since $gng^{-1} = n$ for all $n \in Z(G)$ and all $g \in G$ (Dummit & Foote, p. 50).

# Prerequisites
- **Centralizer** — $Z(G) = C_G(G)$

# Key Properties
1. $Z(G) \leq G$ and $Z(G) \trianglelefteq G$
2. G is abelian iff $Z(G) = G$
3. $Z(G) \leq C_G(A)$ for every subset A
4. If $G/Z(G)$ is cyclic, then G is abelian
5. $Z(D_{2n}) = 1$ if n is odd; $Z(D_{2n}) = \{1, r^{n/2}\}$ if n is even
6. $Z(S_n) = 1$ for $n \geq 3$

# Context & Application
The center measures how far G is from being abelian. The quotient $G/Z(G)$ measures the "non-abelian part" of G and plays a role in classification results.

# Examples
**Example 1** (p. 52): $Z(D_8) = \{1, r^2\}$.
**Example 2** (p. 52): $Z(S_3) = 1$ since $(12)$ does not commute with $(123)$.
**Example 3** (p. 52): $Z(Q_8) = \{\pm 1\}$.

# Relationships
## Builds Upon
- **centralizer**

## Enables
- **normal-subgroup** — the center is always normal
- **quotient-group** — $G/Z(G)$ is always well defined

## Related
- **abelian-group** — G is abelian iff $Z(G) = G$

# Common Confusions
- **Confusion**: Assuming every group has a large center. **Clarification**: Many important groups have trivial center (e.g., $S_n$ for $n \geq 3$).

# Source Reference
Chapter 2: Subgroups, Section 2.2, pages 50-52.

# Verification Notes
- Definition source: direct from source p. 50
- Confidence rationale: explicitly defined with examples
- Uncertainties: none
- Cross-reference status: verified
