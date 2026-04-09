---
# === CORE IDENTIFICATION ===
concept: Quaternion Group
slug: quaternion-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-examples
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 48
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Q_8"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - nonabelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The quaternion group $Q_8 = \{\pm 1, \pm I, \pm J, \pm K\}$ is a nonabelian group of order 8 with relations $I^2 = J^2 = K^2 = -1$, $IJ = K$, $JK = I$, $KI = J$.

# Core Definition

The quaternion group is defined by matrices: $1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $I = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, $J = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$, $K = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$ where $i^2 = -1$. The relations $I^2 = J^2 = K^2 = -1$, $IJ = K$, $JK = I$, $KI = J$, $JI = -K$, $KJ = -I$, $IK = -J$ hold. "The set $Q_8 = \{\pm 1, \pm I, \pm J, \pm K\}$ is a group called the quaternion group" (Judson, p. 48).

# Prerequisites

- **Group** — $Q_8$ satisfies the group axioms

# Key Properties

1. Order 8
2. Nonabelian: $IJ = K$ but $JI = -K$
3. Every subgroup of $Q_8$ is normal (though not needed for Ch. 1-4)
4. Not isomorphic to $\mathbb{Z}_8$, $\mathbb{Z}_4 \times \mathbb{Z}_2$, $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$, or $D_4$

# Context & Application

$Q_8$ is an important example of a nonabelian group of order 8. It demonstrates that nonabelian groups can have properties quite different from dihedral groups. Quaternions have applications in 3D rotations, computer graphics, and physics.

# Examples

**Example 1** (p. 48): $IJ = K$, $JK = I$, $KI = J$ (cyclic pattern), but reversing the order gives negatives: $JI = -K$.

# Relationships

## Builds Upon
- **group** — $Q_8$ is a group

## Related
- **nonabelian-group** — $Q_8$ is nonabelian

# Common Confusions

- **Confusion**: Thinking all groups of order 8 are the same
  **Clarification**: There are five distinct groups of order 8 (up to isomorphism)

# Source Reference

Chapter 3: Groups, Section 3.2, Example 3.15, pages 48-49.

# Verification Notes

- Definition source: Direct from Example 3.15, p. 48
- Confidence: HIGH — explicit definition with multiplication rules
- Cross-reference status: Verified
- Uncertainties: None
