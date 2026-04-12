---
# === CORE IDENTIFICATION ===
concept: Special Linear Group
slug: special-linear-group

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
  - "SL_n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends:
  - general-linear-group
related:
  - lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the special linear group?"
---

# Quick Definition

The special linear group SL_n is the group of n x n matrices with determinant 1. Its Lie algebra consists of trace-zero matrices.

# Core Definition

The real special linear group SL_n is defined as SL_n = {P in GL_n(R) | det P = 1} (Artin, (9.1.1), p. 264). It has dimension n^2 - 1 (one equation det P = 1 removes one degree of freedom). Its Lie algebra consists of the trace-zero matrices (Proposition 9.6.4).

# Prerequisites

- **General linear group** — SL_n is the kernel of det: GL_n -> R*

# Key Properties

1. Defined by det P = 1
2. Normal subgroup of GL_n (kernel of det homomorphism)
3. Dimension n^2 - 1
4. Lie algebra = trace-zero matrices
5. For n = 2, SL_2 has dimension 3 and is one of the most important low-dimensional groups
6. One-parameter groups are t -> e^{tA} where trace A = 0 (Proposition 9.5.10)

# Construction / Recognition

## To Recognize:
1. Check det P = 1

# Context & Application

SL_n is the volume-preserving linear group. SL_2 is particularly important: it is closely related to SU_2 and SO_3, and its finite quotients PSL_2(F_q) provide families of finite simple groups.

# Examples

**Example 1** (p. 264): SL_2 has dimension 3 because det P = 1 is one equation on 4 variables.

# Relationships

## Builds Upon
- **General linear group** — SL_n is a subgroup of GL_n

## Enables
- **Lie algebra** — Lie(SL_n) = trace-zero matrices

# Source Reference

Chapter 9: Linear Groups, Section 9.1, page 264. Section 9.6 for the Lie algebra.

# Verification Notes

- Definition source: Direct from (9.1.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
