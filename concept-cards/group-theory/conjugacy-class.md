---
# === CORE IDENTIFICATION ===
concept: Conjugacy Class
slug: conjugacy-class

# === CLASSIFICATION ===
category: group-actions
subcategory: orbits-stabilizers
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 57
section: "Orbits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orbit
  - group-action
extends:
  - orbit
related:
  - centralizer
  - class-equation
  - centre-of-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine the conjugacy classes of a group?"
---

# Quick Definition

The conjugacy class of $x \in G$ is the set $\{gxg^{-1} \mid g \in G\}$ of all conjugates of $x$.

# Core Definition

"For a group $G$ acting on itself by conjugation, the orbits are called conjugacy classes: for $x \in G$, the conjugacy class of $x$ is the set $\{gxg^{-1} \mid g \in G\}$ of conjugates of $x$" (Milne, p. 57).

# Prerequisites

- **Orbit** — Conjugacy classes are orbits of the conjugation action
- **Group action** — The conjugation action $G \times G \to G$

# Key Properties

1. Conjugacy classes partition $G$
2. The class of $x_0$ is $\{x_0\}$ iff $x_0 \in Z(G)$
3. Size of the class of $x$ is $(G : C_G(x))$ (orbit-stabilizer theorem)
4. A subgroup $H \trianglelefteq G$ iff $H$ is a union of conjugacy classes
5. In $S_n$, conjugacy classes correspond to cycle types (Proposition 4.30)

# Construction / Recognition

## To find conjugacy classes:
1. Pick $x \in G$
2. Compute $\{gxg^{-1} \mid g \in G\}$
3. The size of this set is $|G|/|C_G(x)|$
4. Repeat for elements not yet classified

# Context & Application

Conjugacy classes are central to understanding group structure. They determine normal subgroups, appear in the class equation, and in representation theory each irreducible representation corresponds to a conjugacy class.

# Examples

**Example 1** (p. 58): In $\operatorname{GL}_n(k)$, conjugacy classes are similarity classes; representatives are rational canonical forms.

**Example 2** (p. 67): In $S_n$, two elements are conjugate iff they have the same cycle type (partition of $n$).

**Example 3** (p. 68): In $S_4$: five conjugacy classes with sizes 1, 6, 8, 3, 6 corresponding to partitions $1{+}1{+}1{+}1$, $1{+}1{+}2$, $1{+}3$, $2{+}2$, $4$.

# Relationships

## Builds Upon
- **orbit** — Conjugacy class = orbit under conjugation

## Enables
- **class-equation** — Sum over conjugacy class sizes
- **normal-subgroup** — $N \trianglelefteq G$ iff $N$ is a union of conjugacy classes

## Related
- **centralizer** — $|$class of $x| = (G : C_G(x))$

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 57.

# Verification Notes

- Definition source: Direct from p. 57
- Confidence: HIGH — explicit definition
- Uncertainties: None
