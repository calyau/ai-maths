---
# === CORE IDENTIFICATION ===
concept: Circle Group
slug: circle-group

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: complex-numbers
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 65
section: "The Circle Group and the Roots of Unity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "T"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complex-number
  - modulus-complex-number
  - subgroup
extends:
  - subgroup
related:
  - roots-of-unity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
  - "What is a subgroup?"
---

# Quick Definition

The circle group $\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\}$ is the group of complex numbers with modulus 1, under multiplication. It is an infinite subgroup of $\mathbb{C}^*$.

# Core Definition

"The multiplicative group of the complex numbers, $\mathbb{C}^*$, possesses some interesting subgroups... We first consider the circle group, $\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\}$" (Judson, p. 65).

**Proposition 4.24**: The circle group is a subgroup of $\mathbb{C}^*$.

# Prerequisites

- **Complex number** — $\mathbb{T} \subset \mathbb{C}$
- **Modulus of a complex number** — Defined by $|z| = 1$
- **Subgroup** — $\mathbb{T}$ is a subgroup of $\mathbb{C}^*$

# Key Properties

1. Consists of all complex numbers on the unit circle
2. In polar form: $\mathbb{T} = \{\operatorname{cis}\theta : 0 \leq \theta < 2\pi\}$
3. Closed under multiplication: if $|z| = |w| = 1$, then $|zw| = 1$
4. Infinite order
5. Contains all finite cyclic subgroups (roots of unity)

# Context & Application

The circle group is an important infinite subgroup of $\mathbb{C}^*$ that contains the $n$th roots of unity as finite cyclic subgroups. It provides a geometric interpretation of cyclic groups and is important in Fourier analysis and physics.

# Examples

**Example 1** (p. 65): $H = \{1, -1, i, -i\}$ is a subgroup of $\mathbb{T}$ consisting of the 4th roots of unity.

# Relationships

## Builds Upon
- **subgroup** — $\mathbb{T}$ is a subgroup of $\mathbb{C}^*$
- **modulus-complex-number** — Defined by modulus condition

## Enables
- **roots-of-unity** — $n$th roots of unity are finite subgroups of $\mathbb{T}$

# Source Reference

Chapter 4: Cyclic Groups, Section 4.2, Proposition 4.24, page 65.

# Verification Notes

- Definition source: Direct from p. 65
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
