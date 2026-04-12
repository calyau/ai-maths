---
# === CORE IDENTIFICATION ===
concept: Centralizer
slug: centralizer

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Exercise 17.10"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "centraliser"
  - "C(x)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugation-action
  - stabilizer
extends:
  - stabilizer
related:
  - orbit-stabilizer-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centralizer of an element in a group?"
  - "How does the centralizer relate to the conjugation action?"
---

# Quick Definition

The centralizer of an element $x$ in a group $G$ is the subgroup $C(x) = \{g \in G \mid gx = xg\}$ of all elements that commute with $x$. It is the stabilizer of $x$ under the conjugation action.

# Core Definition

Let $x$ be an element of a group $G$. The elements of $G$ which commute with $x$ form a subgroup of $G$ called the **centraliser** of $x$ and written $C(x)$. The size of the conjugacy class of $x$ is equal to the index of $C(x)$ in $G$ (Armstrong, Exercise 17.10, p. 102).

# Prerequisites

- **Conjugation action** -- the centralizer is the stabilizer under conjugation
- **Stabilizer** -- $C(x) = G_x$ in the conjugation action

# Key Properties

1. $C(x)$ is a subgroup of $G$
2. $C(x) = G_x$ where the action is conjugation
3. The conjugacy class of $x$ has $|G|/|C(x)|$ elements (by Orbit-Stabilizer)
4. $x \in Z(G)$ iff $C(x) = G$ (centre elements have full centralizer)
5. $C(x)$ always contains $\langle x \rangle$ and $Z(G)$

# Context & Application

The centralizer connects the conjugation action to commutative structure. Armstrong uses it to show that if a conjugacy class has exactly two elements, then $G$ cannot be simple (Exercise 17.10, p. 102).

# Relationships

## Builds Upon
- **Stabilizer** -- the centralizer is a special case
- **Conjugation action** -- the centralizer arises as the stabilizer

## Related
- **Orbit-Stabilizer theorem** -- gives $|\text{conjugacy class}| = [G : C(x)]$

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Exercise 17.10, page 102.

# Verification Notes

- Definition: From Exercise 17.10, p. 102
- Confidence: HIGH -- standard definition, clearly stated in exercise
