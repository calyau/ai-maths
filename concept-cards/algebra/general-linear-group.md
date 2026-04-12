---
# === CORE IDENTIFICATION ===
concept: General Linear Group
slug: general-linear-group

# === CLASSIFICATION ===
category: linear-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.1 The Classical Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "GL_n"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - special-linear-group
  - classical-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the general linear group?"
---

# Quick Definition

The general linear group GL_n is the group of all invertible n x n matrices, with matrix multiplication as the group operation. It is the ambient group containing all classical groups.

# Core Definition

GL_n(R) is the group of invertible real n x n matrices; GL_n(C) is the group of invertible complex n x n matrices. All classical groups are subgroups of GL_n. In Chapter 9, GL_n, SL_n, O_n, and Sp_{2n} denote the real groups unless otherwise stated (Artin, p. 265).

# Prerequisites

This is a foundational concept for the chapter.

# Key Properties

1. The group operation is matrix multiplication
2. Contains all classical groups as subgroups
3. GL_n(R) has dimension n^2
4. Has two connected components (det > 0 and det < 0 for GL_n(R))
5. The group GL(V) of invertible linear operators on V is isomorphic to GL_n for a choice of basis

# Construction / Recognition

## To Recognize:
1. An invertible n x n matrix (det != 0)

# Context & Application

GL_n is the natural home for linear algebra. Group representations are homomorphisms into GL_n. The study of subgroups of GL_n leads to Lie theory.

# Examples

**Example 1** (p. 264): Every invertible matrix is in GL_n.

# Relationships

## Enables
- **Special linear group** — SL_n = {P in GL_n | det P = 1}
- **Classical groups** — All are subgroups of GL_n

# Source Reference

Chapter 9: Linear Groups, Section 9.1, page 264.

# Verification Notes

- Definition source: Direct from p. 264
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
