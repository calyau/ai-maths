---
# === CORE IDENTIFICATION ===
concept: Orbit
slug: orbit

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
aliases:
  - G-orbit

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - stabilizer
  - orbit-stabilizer-theorem
  - transitive-action
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orbit of a group action?"
  - "How do orbits and stabilizers relate via the orbit-stabilizer theorem?"
---

# Quick Definition

The orbit of $x_0$ under $G$ is $Gx_0 = \{gx_0 \mid g \in G\}$, the set of all images of $x_0$ under the action.

# Core Definition

"Write $x \sim_G y$ if $y = gx$, some $g \in G$. ... It is therefore an equivalence relation. The equivalence classes are called $G$-orbits. ... By definition, the $G$-orbit containing $x_0$ is $Gx_0 = \{gx_0 \mid g \in G\}$" (Milne, p. 57).

# Prerequisites

- **Group action** — Orbits are defined in terms of an action

# Key Properties

1. The $G$-orbits partition $X$
2. $Gx_0$ is the smallest $G$-stable subset containing $x_0$
3. $|Gx_0| = (G : \operatorname{Stab}(x_0))$ (orbit-stabilizer theorem, Corollary 4.8)
4. A subset $S \subset X$ is stable iff it is a union of orbits
5. The action is transitive iff there is exactly one orbit

# Construction / Recognition

## To find orbits:
1. Pick any $x_0 \in X$
2. Compute $\{gx_0 \mid g \in G\}$
3. Repeat for elements not yet in an orbit

# Context & Application

Orbits decompose a $G$-set into homogeneous pieces. The number and sizes of orbits encode structural information about both the group and the action. The class equation arises from orbits of the conjugation action.

# Examples

**Example 1** (p. 57): For $H \leq G$ acting on $G$ by left multiplication, the orbits are the right cosets $Hg$.

**Example 2** (p. 57): For $G$ acting on itself by conjugation, the orbits are the conjugacy classes.

**Example 3** (p. 57): For $\langle \alpha \rangle$ with $\alpha$ of order $n$ acting on $X$, orbits are $\{x_0, \alpha x_0, \ldots, \alpha^{n-1}x_0\}$.

# Relationships

## Builds Upon
- **group-action**

## Enables
- **orbit-stabilizer-theorem** — Relates orbit size to stabilizer index
- **transitive-action** — One orbit = transitive
- **class-equation** — From orbits of conjugation

## Related
- **conjugacy-class** — Orbits of the conjugation action

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 57.

# Verification Notes

- Definition source: Direct from p. 57
- Confidence: HIGH — explicit definition
- Uncertainties: None
