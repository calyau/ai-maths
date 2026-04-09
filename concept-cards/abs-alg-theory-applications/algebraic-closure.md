---
# === CORE IDENTIFICATION ===
concept: Algebraic Closure
slug: algebraic-closure

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-extension
  - algebraically-closed-field
extends: []
related:
  - algebraic-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the algebraic closure of a field?"
  - "Does every field have an algebraic closure?"
---

# Quick Definition

The algebraic closure of a field $F$ in an extension $E$ is the subfield of $E$ consisting of all elements algebraic over $F$. Every field has a unique algebraic closure.

# Core Definition

Let $E$ be a field extension of a field $F$. The **algebraic closure** of $F$ in $E$ is the field consisting of all elements in $E$ that are algebraic over $F$ (Judson, p. 281). By Theorem 21.23, this set is indeed a field.

Every field $F$ has a unique algebraic closure (Theorem 21.27).

# Prerequisites

- **Algebraic extension** — The algebraic closure collects all algebraic elements
- **Algebraically closed field** — The algebraic closure is algebraically closed

# Key Properties

1. The set of elements algebraic over $F$ forms a field (Theorem 21.23)
2. The set of all algebraic numbers (complex numbers algebraic over $\mathbb{Q}$) forms a field (Corollary 21.24)
3. Every field has a unique algebraic closure (Theorem 21.27)
4. An algebraically closed field has no proper algebraic extension (Corollary 21.26)

# Context & Application

The algebraic closure is the "universal" extension in which all polynomial equations over $F$ can be solved. The algebraic closure of $\mathbb{Q}$ is denoted $\overline{\mathbb{Q}}$ and consists of all algebraic numbers.

# Examples

**Example 1** (p. 281): The algebraic closure of $\mathbb{Q}$ in $\mathbb{C}$ is the field of all algebraic numbers.

**Example 2** (p. 282): $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$ (Fundamental Theorem of Algebra).

# Relationships

## Builds Upon
- **Algebraic extension** — The algebraic closure is the maximal algebraic extension
- **Algebraically closed field** — An algebraic closure is algebraically closed

## Related
- **Algebraic number** — Elements of the algebraic closure of $\mathbb{Q}$

# Source Reference

Chapter 21: Fields, Section 21.1, pages 281–282. See Theorems 21.23, 21.25, 21.27.

# Verification Notes

- Definition source: Direct from p. 281
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
