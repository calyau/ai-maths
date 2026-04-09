---
# === CORE IDENTIFICATION ===
concept: Quaternions
slug: quaternions

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 205
section: "16.1 Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Hamilton's quaternions"
  - "ring of quaternions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - division-ring
extends: []
related:
  - field
contrasts_with:
  - field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the quaternions?"
  - "What is an example of a noncommutative division ring?"
---

# Quick Definition

The quaternions $\mathbb{H}$ form a noncommutative division ring consisting of elements $a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ where $a, b, c, d \in \mathbb{R}$ and $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$.

# Core Definition

The ring of quaternions $\mathbb{H}$ consists of elements of the form $a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ where $a, b, c, d$ are real numbers. The generators satisfy $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$, $\mathbf{ij} = \mathbf{k}$, $\mathbf{jk} = \mathbf{i}$, $\mathbf{ki} = \mathbf{j}$, and $\mathbf{ji} = -\mathbf{k}$, $\mathbf{kj} = -\mathbf{i}$, $\mathbf{ik} = -\mathbf{j}$ (Judson, pp. 205-206). The inverse of a nonzero quaternion is $(a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k})^{-1} = \frac{a - b\mathbf{i} - c\mathbf{j} - d\mathbf{k}}{a^2 + b^2 + c^2 + d^2}$.

# Prerequisites

- **Division ring** — The quaternions are the primary example of a noncommutative division ring

# Key Properties

1. $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = -1$
2. Multiplication is not commutative: $\mathbf{ij} = \mathbf{k}$ but $\mathbf{ji} = -\mathbf{k}$
3. Every nonzero quaternion has an inverse
4. Can be represented as $2 \times 2$ complex matrices

# Construction / Recognition

## To Construct:
1. Take elements $a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ with $a, b, c, d \in \mathbb{R}$
2. Add component-wise
3. Multiply using the generator relations and distributivity

# Context & Application

The quaternions are the standard example showing that division rings need not be commutative. They have applications in physics (rotations in 3D), computer graphics, and spacecraft orientation.

# Examples

**Example 1** (p. 206): The conjugate of $q = a + b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$ is $\bar{q} = a - b\mathbf{i} - c\mathbf{j} - d\mathbf{k}$, and $q\bar{q} = a^2 + b^2 + c^2 + d^2$.

# Relationships

## Builds Upon
- **Division ring** — The quaternions are a division ring

## Contrasts With
- **Field** — The quaternions are not a field because multiplication is noncommutative

# Common Errors

- **Error**: Assuming $\mathbf{ij} = \mathbf{ji}$
  **Correction**: $\mathbf{ij} = \mathbf{k}$ but $\mathbf{ji} = -\mathbf{k}$; quaternion multiplication is anticommutative on the generators

# Common Confusions

- **Confusion**: Thinking the quaternions are just $\mathbb{R}^4$ with component-wise multiplication
  **Clarification**: Quaternion multiplication is determined by the generator relations, not component-wise

# Source Reference

Chapter 16: Rings, Section 16.1, Example 16.7, pages 205-207.

# Verification Notes

- Definition source: Direct from pp. 205-206
- Confidence: HIGH — explicit construction and verification
- Cross-reference status: Verified
- Uncertainties: None
