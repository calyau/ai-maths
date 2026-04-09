---
# === CORE IDENTIFICATION ===
concept: Quotient Representation
slug: quotient-representation

# === CLASSIFICATION ===
category: representations
subcategory: operations
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 40
section: "4.2 Operations on representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "factor representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subrepresentation
extends: []
related:
  - direct-sum-of-representations
  - irreducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quotient representation?"
---

# Quick Definition

If $W \subset V$ is a subrepresentation, the quotient space $V/W$ inherits a canonical representation structure, called the quotient (or factor) representation.

# Core Definition

(Kirillov, p. 40): If $W \subset V$ is a subrepresentation, then the quotient space $V/W$ has a canonical structure of a representation: $\rho(g)(v + W) = \rho(g)v + W$. This is well-defined because $W$ is $G$-invariant.

# Prerequisites

- **Subrepresentation** — Required to form the quotient

# Key Properties

1. $\dim(V/W) = \dim V - \dim W$
2. The representation fits in a short exact sequence $0 \to W \to V \to V/W \to 0$
3. The sequence splits (i.e., $V \cong W \oplus V/W$) iff $V$ is completely reducible or more specifically iff $W$ has a complementary invariant subspace

# Context & Application

Quotient representations appear in the construction of Verma modules and their irreducible quotients. The irreducible representations $V_n$ of $\mathfrak{sl}(2,\mathbb{C})$ are constructed as quotients of Verma modules (Theorem 5.6).

# Examples

**Theorem 5.6** (p. 60): The irreducible representation $V_n$ of $\mathfrak{sl}(2,\mathbb{C})$ is the quotient $M^n / M'$ where $M^n$ is a Verma module and $M'$ is the submodule spanned by $v^{n+1}, v^{n+2}, \ldots$.

# Relationships

## Builds Upon
- **Subrepresentation** — The subspace being quotiented out

## Enables
- **Construction of irreducible representations** — As quotients of larger representations

# Source Reference

Chapter 4, Section 4.2, p. 40.

# Verification Notes

- Definition source: Direct from text, p. 40
- Confidence rationale: Explicit construction
- Uncertainties: None
- Cross-reference status: Verified
