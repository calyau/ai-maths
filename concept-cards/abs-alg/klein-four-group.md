---
concept: Klein Four-Group
slug: klein-four-group
category: group-theory
subcategory: important-groups
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Subgroups"
chapter_number: 2
pdf_page: 46
section: "2.5 The Lattice of Subgroups of a Group"
extraction_confidence: high
aliases:
  - "$V_4$"
  - "Viergruppe"
prerequisites:
  - group
  - abelian-group
extends:
  - abelian-group
related:
  - cyclic-group
  - dihedral-group
contrasts_with:
  - cyclic-group
answers_questions:
  - "What is the Klein four-group?"
  - "How does $V_4$ differ from $Z_4$?"
---

# Quick Definition
The Klein four-group $V_4 = \{1, a, b, c\}$ is the unique non-cyclic group of order 4. Every nonidentity element has order 2, and $V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.

# Core Definition
The *Klein four-group* (Viergruppe) $V_4$ is the abelian group of order 4 with multiplication table where $a^2 = b^2 = c^2 = 1$ and $ab = c$, $bc = a$, $ac = b$. It is isomorphic to $\mathbb{Z}_2 \times \mathbb{Z}_2$ and is NOT cyclic (no element of order 4). Up to isomorphism, $Z_4$ and $V_4$ are the only groups of order 4 (Dummit & Foote, pp. 67-68).

# Prerequisites
- **Group**, **Abelian group**

# Key Properties
1. $|V_4| = 4$, abelian, non-cyclic
2. Every nonidentity element has order 2
3. Three subgroups of order 2: $\langle a \rangle, \langle b \rangle, \langle c \rangle$
4. $V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$
5. Appears as a subgroup of $D_8$, $S_4$, and $A_4$

# Context & Application
$V_4$ is the simplest non-cyclic group. It appears as $D_8/Z(D_8)$, $Q_8/Z(Q_8)$, and the unique normal subgroup of $A_4$ of order 4.

# Examples
**Example 1** (p. 67): The multiplication table has $ab = c$, $ba = c$, $ac = b$, etc.
**Example 2** (p. 68): In $D_8$, $\{1, s, r^2, sr^2\} \cong V_4$.

# Relationships
## Builds Upon
- **abelian-group**

## Related
- **dihedral-group** — $V_4$ appears as a subgroup and quotient of $D_8$

## Contrasts With
- **cyclic-group** — $V_4$ is not cyclic (no element of order 4); $Z_4$ is cyclic

# Source Reference
Chapter 2, Section 2.5, pages 67-68; Exercise 10 classifies groups of order 4.

# Verification Notes
- Definition source: direct from source pp. 67-68
- Confidence rationale: explicitly defined with multiplication table
- Uncertainties: none
- Cross-reference status: verified
