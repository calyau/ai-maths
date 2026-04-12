---
# === CORE IDENTIFICATION ===
concept: Diophantine Equation for Finite Rotation Groups
slug: diophantine-equation-for-rotation-groups

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finite Rotation Groups"
chapter_number: 19
pdf_page: 111
section: "Theorem 19.2 proof"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rotation group Diophantine constraint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - counting-theorem
  - orbit-stabilizer-theorem
  - poles-of-rotation
extends: []
related:
  - finite-subgroups-of-so3
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What Diophantine equation constrains finite rotation groups?"
  - "How does the Counting Theorem lead to the classification of finite subgroups of SO(3)?"
---

# Quick Definition

Applying the Counting Theorem to the action of a finite subgroup $G \le SO_3$ on its poles yields the equation $2(1 - 1/|G|) = \sum_{i=1}^{N}(1 - 1/|G_{x_i}|)$. Since the left side is between 1 and 2, and each summand is at least $1/2$, there are only finitely many solutions.

# Core Definition

In the proof of Theorem 19.2, Armstrong derives the constraint (Armstrong, p. 113):

$$2\left(1 - \frac{1}{|G|}\right) = \sum_{i=1}^{N}\left(1 - \frac{1}{|G_{x_i}|}\right)$$

where $N$ is the number of orbits of poles and $G_{x_i}$ is the stabilizer of a chosen pole from orbit $i$. Since each non-identity rotation fixes exactly 2 poles and the identity fixes them all, the Counting Theorem gives $N = \frac{1}{|G|}\{2(|G|-1) + |X|\}$, which rearranges to the equation above.

# Prerequisites

- **Counting theorem** -- produces the initial equation
- **Orbit-Stabilizer theorem** -- used to rewrite in terms of stabilizer orders
- **Poles of rotation** -- the set being acted upon

# Key Properties

1. The left side satisfies $1 \le 2(1 - 1/|G|) < 2$ for non-trivial $G$
2. Each summand satisfies $1/2 \le 1 - 1/|G_{x_i}| < 1$
3. Therefore $N \in \{2, 3\}$
4. $N = 2$: gives cyclic groups
5. $N = 3$: gives four solutions $(|G_{x_1}|, |G_{x_2}|, |G_{x_3}|)$: $(2,2,n)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$

# Context & Application

This Diophantine analysis is the heart of the classification of finite rotation groups. The interplay between number theory (which solutions exist) and geometry (what each solution means) is one of the most elegant arguments in group theory.

# Relationships

## Builds Upon
- **Counting theorem** -- the starting point
- **Poles of rotation** -- the geometric input

## Enables
- **Finite subgroups of SO(3)** -- the solutions enumerate all possibilities

# Source Reference

Chapter 19: Finite Rotation Groups, Theorem 19.2 proof, pages 112--113. Equation (*) on p. 113.

# Verification Notes

- Derivation: Direct from pp. 112--113
- Confidence: HIGH -- central calculation with complete derivation
