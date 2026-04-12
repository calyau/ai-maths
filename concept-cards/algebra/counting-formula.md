---
concept: Counting Formula
slug: counting-formula
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.9 The Counting Formula"
extraction_confidence: high
aliases:
  - "orbit-stabilizer theorem"
  - "orbit-stabilizer formula"
prerequisites:
  - group-action
  - orbit
  - stabilizer
  - operation-on-cosets
extends: []
related:
  - class-equation
contrasts_with: []
answers_questions:
  - "How do orbits and stabilizers relate via the counting formula?"
  - "What is the orbit-stabilizer theorem?"
---

# Quick Definition

The Counting Formula states that for a finite group G acting on a set S, |G| = |G_s| * |O_s| (order of G = order of stabilizer times order of orbit). The orbit size equals the index of the stabilizer.

# Core Definition

Let S be a finite set on which a group G operates, and let G_s and O_s be the stabilizer and orbit of an element s. Then |G| = |G_s| * |O_s|, or equivalently |O_s| = [G : G_s] (Artin, Proposition 6.9.2, p. 192). This follows from the bijection between G/G_s and O_s (Proposition 6.8.4). The partition into orbits gives |S| = |O_1| + |O_2| + ... + |O_k|.

# Prerequisites

- **Group action** — The formula applies to group actions
- **Orbit** — |O_s| appears in the formula
- **Stabilizer** — |G_s| appears in the formula
- **Operation on cosets** — The proof uses the bijection G/G_s -> O_s

# Key Properties

1. |G| = |G_s| * |O_s|
2. |O_s| = [G : G_s] divides |G|
3. |S| = sum of orbit sizes
4. Applies to every group action

# Construction / Recognition

## To Apply:
1. Identify the group G and the set S
2. Choose an element s and find either its orbit or its stabilizer
3. Use the formula to determine the other quantity

# Context & Application

The Counting Formula is one of the most frequently used tools in group theory. It determines the order of the icosahedral group (60 = 5 * 12 = 3 * 20 = 2 * 30), derives the class equation, and proves Sylow's theorems. It reduces geometric counting to algebraic computation.

# Examples

**Example 1** (p. 192): For the dodecahedron, the rotation group acts transitively on its 12 faces with stabilizer of order 5, giving |G| = 5 * 12 = 60. Checking: 60 = 3 * 20 (vertices) = 2 * 30 (edges).

**Example 2** (p. 192): Restricting to the stabilizer H of a face (order 5), the 12 faces decompose as 12 = 1 + 1 + 5 + 5 (two fixed faces, two orbits of 5).

# Relationships

## Builds Upon
- **Orbit** — One factor in the formula
- **Stabilizer** — The other factor

## Enables
- **Class equation** — Apply counting to conjugacy classes
- **Sylow theorems** — Proved using counting arguments
- **Finite subgroups of rotation group** — Classification by counting poles

# Common Errors

- **Error**: Applying the formula without verifying the action
  **Correction**: Ensure you have a genuine group action (check axioms)

# Common Confusions

- **Confusion**: Confusing the orbit of s with the orbit of a subset containing s
  **Clarification**: These are different actions with different orbits and stabilizers

# Source Reference

Chapter 6: Symmetry, Section 6.9, Proposition 6.9.2, pages 192-193.

# Verification Notes

- Definition source: Direct from Proposition 6.9.2
- Confidence rationale: Explicitly stated theorem, extensively applied
- Uncertainties: None
- Cross-reference status: Verified
