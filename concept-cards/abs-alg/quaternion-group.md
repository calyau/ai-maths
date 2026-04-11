---
concept: Quaternion Group
slug: quaternion-group
category: group-theory
subcategory: important-groups
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Groups"
chapter_number: 1
pdf_page: 26
section: "1.5 The Quaternion Group"
extraction_confidence: high
aliases:
  - "$Q_8$"
prerequisites:
  - group
extends:
  - group
related:
  - dihedral-group
  - center-of-a-group
contrasts_with:
  - dihedral-group
answers_questions:
  - "What is the quaternion group?"
  - "How does $Q_8$ differ from $D_8$?"
---

# Quick Definition
The quaternion group $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$ is a non-abelian group of order 8 with $i^2 = j^2 = k^2 = -1$, $ij = k$, $ji = -k$, etc.

# Core Definition
The *quaternion group* $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$ with multiplication: $(-1)^2 = 1$, $i^2 = j^2 = k^2 = -1$, $ij = k$, $ji = -k$, $jk = i$, $kj = -i$, $ki = j$, $ik = -j$. It is non-abelian of order 8 (Dummit & Foote, pp. 36-37).

# Prerequisites
- **Group** — $Q_8$ is a group

# Key Properties
1. $|Q_8| = 8$, non-abelian
2. $Z(Q_8) = \{\pm 1\}$
3. Every subgroup of $Q_8$ is normal
4. $Q_8/\langle -1 \rangle \cong V_4$
5. $Q_8$ is not isomorphic to $D_8$ (all subgroups of $Q_8$ are normal; $D_8$ has non-normal subgroups)
6. $Q_8$ has a unique element of order 2 (namely $-1$)

# Context & Application
$Q_8$ is the smallest non-abelian group in which every subgroup is normal. It serves as a key example distinguishing from $D_8$ and illustrating that groups with the same order and quotient structure need not be isomorphic.

# Examples
**Example 1** (p. 37): $ij = k$ but $ji = -k$, showing non-commutativity.
**Example 2** (p. 83): $Q_8/\{\pm 1\} \cong V_4$ via the "absolute value" map.

# Relationships
## Builds Upon
- **group**

## Related
- **center-of-a-group** — $Z(Q_8) = \{\pm 1\}$

## Contrasts With
- **dihedral-group** — $D_8$ and $Q_8$ have order 8 but are not isomorphic

# Source Reference
Chapter 1, Section 1.5, pages 36-37.

# Verification Notes
- Definition source: direct from source pp. 36-37
- Confidence rationale: explicitly defined
- Uncertainties: none
- Cross-reference status: verified
