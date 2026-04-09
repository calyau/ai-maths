---
# === CORE IDENTIFICATION ===
concept: Symmetry
slug: symmetry

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
pdf_page: 44
section: "Integer Equivalence Classes and Symmetries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rigid motion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
  - function-composition
extends: []
related:
  - group
  - nonabelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is a group?"
---

# Quick Definition

A symmetry of a geometric figure is a rearrangement that preserves the figure's shape, distances, and angles. Symmetries form groups under composition.

# Core Definition

"A symmetry of a geometric figure is a rearrangement of the figure preserving the arrangement of its sides and vertices as well as its distances and angles. A map from the plane to itself preserving the symmetry of an object is called a rigid motion" (Judson, p. 44).

# Prerequisites

- **Permutation** — Symmetries correspond to permutations of vertices
- **Function composition** — Symmetries compose via function composition

# Key Properties

1. Symmetries correspond to permutations of the figure's vertices
2. Composition of symmetries is a symmetry (closure)
3. The identity (doing nothing) is a symmetry
4. Every symmetry has an inverse symmetry
5. Composition is associative
6. Composition of symmetries is generally NOT commutative

# Construction / Recognition

## To Find Symmetries of a Figure:
1. List all permutations of the vertices
2. Check which permutations preserve distances and angles
3. Those that preserve the geometry are the symmetries

# Context & Application

Symmetries provide one of the most important motivating examples for group theory. The symmetry groups of geometric figures (such as the dihedral groups $D_n$) are fundamental objects in algebra, physics, chemistry, and crystallography.

# Examples

**Example 1** (p. 44-46): The symmetries of an equilateral triangle $\triangle ABC$ consist of 6 motions: the identity $\text{id}$, two rotations $\rho_1$ (120 degrees), $\rho_2$ (240 degrees), and three reflections $\mu_1$, $\mu_2$, $\mu_3$. This is the group $S_3$ (or $D_3$).

**Example 2** (p. 46): The composition $\mu_1 \rho_1 = \mu_2$ but $\rho_1 \mu_1 = \mu_3$, showing $\mu_1 \rho_1 \neq \rho_1 \mu_1$ (non-commutativity).

# Relationships

## Builds Upon
- **permutation** — Symmetries are permutations of vertices
- **function-composition** — The group operation

## Enables
- **group** — Symmetries form a group
- **nonabelian-group** — Symmetry groups are often nonabelian

# Common Errors

- **Error**: Assuming all permutations of vertices are symmetries
  **Correction**: Only permutations that preserve distances and angles are symmetries; for a non-square rectangle, a 90-degree rotation is not a symmetry

# Common Confusions

- **Confusion**: Thinking symmetry composition is commutative
  **Clarification**: For most geometric figures with 3+ vertices, the symmetry group is nonabelian

# Source Reference

Chapter 3: Groups, Section 3.1, pages 44-46. Figure 3.7 (multiplication table).

# Verification Notes

- Definition source: Direct quote from p. 44
- Confidence: HIGH — explicit definition with detailed example
- Cross-reference status: Verified
- Uncertainties: None
