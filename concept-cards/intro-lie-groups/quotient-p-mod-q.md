---
# === CORE IDENTIFICATION ===
concept: Quotient P/Q
slug: quotient-p-mod-q

# === CLASSIFICATION ===
category: root-systems
subcategory: lattices
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 98
section: "8.5. Weight and root lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "weight lattice modulo root lattice"
  - "$P/Q$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-lattice
  - root-lattice
extends: []
related:
  - cartan-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the quotient $P/Q$?"
  - "How is $|P/Q|$ computed?"
---

# Quick Definition
The quotient $P/Q$ of the weight lattice by the root lattice is a finite abelian group whose order equals $|\det A|$, where $A$ is the Cartan matrix. It measures how much larger the weight lattice is than the root lattice.

# Core Definition
Since both $P$ and $Q$ are free abelian groups of rank $r$ with $Q \subset P$, the quotient $P/Q$ is a finite abelian group (p. 98). Its order is $|P/Q| = |\det A|$ where $a_{ij} = \langle\alpha_i^\vee, \alpha_j\rangle$ is the Cartan matrix (Exercise 8.4).

# Prerequisites
- **weight-lattice** -- the larger lattice
- **root-lattice** -- the sublattice

# Key Properties
1. $P/Q$ is a finite abelian group
2. $|P/Q| = |\det A|$ (Exercise 8.4)
3. $P/Q = 0$ iff $P = Q$ iff $\det A = \pm 1$

# Construction / Recognition
1. Compute the Cartan matrix $A$
2. $|P/Q| = |\det A|$
3. The full group structure can be determined from the Smith normal form of $A$

# Context & Application
The quotient $P/Q$ is isomorphic to the center of the simply-connected compact Lie group and to the fundamental group of the adjoint group. It is a key invariant distinguishing the global structure of Lie groups with the same Lie algebra.

# Examples
**Example 8.20** (p. 97): For $A_1$, $P = \mathbb{Z}(\alpha/2)$, $Q = \mathbb{Z}\alpha$, so $P/Q \cong \mathbb{Z}_2$.

**Example 8.21** (p. 97): For $A_2$, $P/Q \cong \mathbb{Z}_3$.

# Relationships
## Builds Upon
- **weight-lattice** and **root-lattice**

## Enables
- Classification of Lie groups with a given Lie algebra

## Related
- **cartan-matrix** -- $|P/Q| = |\det A|$

## Contrasts With
(none)

# Common Errors
- **Error**: Assuming $P/Q$ is always cyclic
  **Correction**: $P/Q$ can be non-cyclic, e.g., for $D_n$ with $n$ even, $P/Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$

# Common Confusions
(none)

# Source Reference
Chapter 8: Root Systems, Section 8.5, page 98. Exercise 8.4.

# Verification Notes
- Definition source: Direct from discussion on p. 98
- Confidence rationale: HIGH -- explicit statement, concrete examples
- Uncertainties: Full group structure not computed in source (only order)
- Cross-reference status: Verified
