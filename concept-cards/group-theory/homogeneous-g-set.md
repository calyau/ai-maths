---
# === CORE IDENTIFICATION ===
concept: Homogeneous G-Set
slug: homogeneous-g-set

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 58
section: "Orbits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - homogeneous space

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
  - g-set
extends:
  - g-set
related:
  - orbit-stabilizer-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a homogeneous G-set?"
---

# Quick Definition

A homogeneous $G$-set is a $G$-set on which $G$ acts transitively, i.e., there is a single orbit.

# Core Definition

"The set $X$ is then called a homogeneous $G$-set" (Milne, p. 58), referring to a set $X$ on which $G$ acts transitively.

# Prerequisites

- **Transitive action** — Homogeneous = transitive
- **G-set** — A homogeneous $G$-set is a $G$-set with one orbit

# Key Properties

1. Every homogeneous $G$-set is isomorphic to $G/H$ for some subgroup $H \leq G$ (Proposition 4.7)
2. The isomorphism depends on the choice of basepoint $x_0$: $H = \operatorname{Stab}(x_0)$
3. A homogeneous $G$-set with a preferred point is essentially the same as a subgroup of $G$

# Context & Application

Homogeneous spaces are the building blocks of $G$-sets: every $G$-set decomposes into orbits, each of which is homogeneous.

# Relationships

## Builds Upon
- **transitive-action**, **g-set**

## Related
- **orbit-stabilizer-theorem** — Classifies homogeneous $G$-sets as $G/H$

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit definition
- Uncertainties: None
