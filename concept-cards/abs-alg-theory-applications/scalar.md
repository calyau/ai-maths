---
# === CORE IDENTIFICATION ===
concept: Scalar
slug: scalar

# === CLASSIFICATION ===
category: linear-algebra
subcategory: vector-spaces
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Vector Spaces"
chapter_number: 20
pdf_page: 266
section: "20.1 Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field
extends: []
related:
  - vector-space
  - vector
contrasts_with:
  - vector

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a scalar in a vector space?"
---

# Quick Definition

In a vector space $V$ over a field $F$, the elements of $F$ are called scalars. Scalars are used to multiply vectors via scalar multiplication.

# Core Definition

The elements of $F$ are called **scalars** (Judson, p. 266). Scalars are distinguished from vectors: in a vector space $V$ over $F$, elements of $V$ are vectors and elements of $F$ are scalars.

# Prerequisites

- **Field** — Scalars come from a field

# Key Properties

1. Scalars form a field (closed under $+, -, \times, \div$)
2. The scalar zero $0 \in F$ is distinct from the vector zero $\mathbf{0} \in V$
3. Scalar multiplication $\alpha v$ maps $F \times V \to V$

# Context & Application

The distinction between scalars and vectors is fundamental. Scalars control the "scaling" of vectors, while vectors live in the space being studied. The same set can serve as both scalars and vectors in different contexts (e.g., $\mathbb{R}$ is both the scalar field and a one-dimensional vector space over itself).

# Examples

**Example 1** (p. 266): In $\mathbb{R}^n$ as a vector space over $\mathbb{R}$, the real numbers are the scalars.

**Example 2** (p. 267): In $\mathbb{Q}(\sqrt{2})$ as a vector space over $\mathbb{Q}$, the rational numbers are the scalars.

# Relationships

## Related
- **Vector space** — Scalars are one component of the vector space structure
- **Vector** — The other component; elements of the vector space

## Contrasts With
- **Vector** — Scalars come from the field; vectors come from the space

# Source Reference

Chapter 20: Vector Spaces, Section 20.1, page 266.

# Verification Notes

- Definition source: Direct from p. 266
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
