---
# === CORE IDENTIFICATION ===
concept: Fixed Point
slug: fixed-point

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
pdf_page: 61
section: "The class equation"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "X^G"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - stabilizer
extends: []
related:
  - class-equation
  - centre-of-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fixed point of a group action?"
---

# Quick Definition

A fixed point of a group action is an element $x \in X$ with $gx = x$ for all $g \in G$, i.e., $\operatorname{Stab}(x) = G$.

# Core Definition

An element $x \in X$ is a fixed point if it forms a singleton orbit $\{x\}$. In the conjugation action, the fixed points are exactly the elements of the centre $Z(G)$.

# Prerequisites

- **Group action** — Fixed points are defined in terms of actions
- **Stabilizer** — A fixed point has $\operatorname{Stab}(x) = G$

# Key Properties

1. $x$ is a fixed point iff $Gx = \{x\}$ (orbit is a singleton)
2. For conjugation on $G$: fixed points = $Z(G)$
3. The class equation separates fixed points from non-fixed orbits

# Context & Application

Fixed points appear in the class equation, Burnside's lemma, and in proving that $p$-groups have non-trivial centres.

# Relationships

## Related
- **class-equation** — Fixed points contribute $|Z(G)|$ to the class equation
- **centre-of-group** — Fixed points of conjugation

# Source Reference

Chapter 4: Groups Acting on Sets, "The class equation", page 61.

# Verification Notes

- Confidence: MEDIUM — concept implicit in class equation discussion
- Uncertainties: None
