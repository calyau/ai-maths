---
concept: Fourth Isomorphism Theorem
slug: fourth-isomorphism-theorem
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
aliases:
  - "Lattice Isomorphism Theorem"
  - "Correspondence Theorem"
prerequisites:
  - quotient-group
  - normal-subgroup
extends: []
related:
  - first-isomorphism-theorem
  - lattice-of-subgroups
contrasts_with: []
answers_questions:
  - "How do subgroups of G/N correspond to subgroups of G?"
---

# Quick Definition
There is a bijection between subgroups of G containing N and subgroups of G/N, given by $A \mapsto A/N$. This bijection preserves containment, index, normality, joins, and intersections.

# Core Definition
**Theorem 20 (Fourth/Lattice Isomorphism Theorem):** Let $N \trianglelefteq G$. There is a bijection from subgroups of G containing N to subgroups of $G/N$, given by $A \mapsto A/N = \overline{A}$. Properties preserved: (1) $A \leq B$ iff $\overline{A} \leq \overline{B}$; (2) $|B:A| = |\overline{B}:\overline{A}|$; (3) $\overline{\langle A,B \rangle} = \langle \overline{A}, \overline{B} \rangle$; (4) $\overline{A \cap B} = \overline{A} \cap \overline{B}$; (5) $A \trianglelefteq G$ iff $\overline{A} \trianglelefteq \overline{G}$ (Dummit & Foote, pp. 99-100).

# Prerequisites
- **Quotient group**, **Normal subgroup**

# Key Properties
1. Bijection between $\{A \leq G \mid N \leq A\}$ and $\{$subgroups of $G/N\}$
2. Every subgroup of $G/N$ has the form $A/N$ for some $A \leq G$ with $N \leq A$
3. Preserves containment, index, normality, joins, intersections
4. The lattice of $G/N$ appears as the "top part" of the lattice of G (above N)

# Context & Application
This theorem allows reading the subgroup structure of G/N directly from the lattice of G. Subgroups of G not containing N do not appear in the quotient lattice.

# Examples
**Example 1** (p. 100): The lattice of $Q_8/\langle -1 \rangle \cong V_4$ appears as the double lines in the lattice of $Q_8$.
**Example 2** (p. 100): The lattice of $D_8/\langle r^2 \rangle$ appears similarly in the lattice of $D_8$.

# Relationships
## Builds Upon
- **quotient-group**, **normal-subgroup**

## Related
- **lattice-of-subgroups** — the correspondence is between lattices

# Source Reference
Chapter 3, Section 3.3, pages 99-101, Theorem 20.

# Verification Notes
- Definition source: direct from source pp. 99-100
- Confidence rationale: major theorem, explicitly stated
- Uncertainties: none
- Cross-reference status: verified
