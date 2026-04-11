---
concept: Second Isomorphism Theorem
slug: second-isomorphism-theorem
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
  - "Diamond Isomorphism Theorem"
prerequisites:
  - first-isomorphism-theorem
  - normal-subgroup
  - subgroup
extends:
  - first-isomorphism-theorem
related:
  - third-isomorphism-theorem
contrasts_with: []
answers_questions:
  - "What is the Second Isomorphism Theorem?"
  - "How do two subgroups interact in a quotient?"
---

# Quick Definition
If $A \leq N_G(B)$ then AB is a subgroup, $B \trianglelefteq AB$, $A \cap B \trianglelefteq A$, and $AB/B \cong A/(A \cap B)$.

# Core Definition
**Theorem 18 (Second/Diamond Isomorphism Theorem):** Let A and B be subgroups of G with $A \leq N_G(B)$. Then AB is a subgroup of G, $B \trianglelefteq AB$, $A \cap B \trianglelefteq A$, and $AB/B \cong A/(A \cap B)$. The proof defines $\varphi: A \to AB/B$ by $\varphi(a) = aB$, shows it is surjective with kernel $A \cap B$, and applies the First Isomorphism Theorem (Dummit & Foote, pp. 97-98).

# Prerequisites
- **First Isomorphism Theorem** — used in the proof
- **Normal subgroup**, **Subgroup**

# Key Properties
1. AB is a subgroup when A normalizes B
2. $|AB| = |A||B|/|A \cap B|$ (order formula)
3. Called "Diamond" because of the lattice shape: AB at top, $A \cap B$ at bottom

# Context & Application
Used to relate subgroups that interact but neither contains the other. The diamond shape in the lattice makes the theorem visually memorable.

# Examples
**Example 1** (p. 98): The lattice diamond with AB at top, A and B in the middle, $A \cap B$ at bottom, with matching quotients on opposite sides.

# Relationships
## Builds Upon
- **first-isomorphism-theorem**

## Related
- **third-isomorphism-theorem**, **fourth-isomorphism-theorem**

# Source Reference
Chapter 3, Section 3.3, pages 97-98, Theorem 18.

# Verification Notes
- Definition source: direct from source pp. 97-98
- Confidence rationale: major theorem, explicitly proved
- Uncertainties: none
- Cross-reference status: verified
