---
# === CORE IDENTIFICATION ===
concept: Lie Algebra as Tangent Space at Identity
slug: lie-algebra-tangent-space-definition

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 17
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{g} = T_1G$"
  - "tangent Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - lie-algebra
  - classical-group-theorem
  - exponential-map
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The vector space $\mathfrak{g} = T_1G$ (tangent space at the identity of a Lie group $G$) is called the Lie algebra of $G$. It inherits a bracket operation from the group multiplication, making it a Lie algebra in the abstract sense (Definition 3.16).

# Core Definition

(Kirillov, p. 17): The vector space $\mathfrak{g} = T_1G$ is called the Lie algebra of the corresponding group $G$. Traditionally, the Lie algebra is denoted by lowercase Gothic letters: e.g., the Lie algebra of $\mathrm{SU}(n)$ is denoted $\mathfrak{su}(n)$.

The bracket operation is defined later (Section 3.2, equation 3.2) via the group law in logarithmic coordinates.

# Prerequisites

- **Lie group** — the group whose tangent space we take

# Key Properties

1. $\dim \mathfrak{g} = \dim G$.
2. For matrix groups, $\mathfrak{g}$ is identified with a subspace of $\mathfrak{gl}(n)$ via Theorem 2.29.
3. The exponential map provides a local diffeomorphism between $\mathfrak{g}$ and $G$.
4. The bracket makes $\mathfrak{g}$ a Lie algebra (Theorem 3.17).

# Construction / Recognition

## To Construct/Create:
1. For matrix groups: use Theorem 2.29 to find $\mathfrak{g}$ as a linear condition on matrices.
2. For abstract groups: $\mathfrak{g} = T_1G$.

## To Identify/Recognize:
1. The tangent space at the identity element of a Lie group.

# Context & Application

This is the bridge between Lie groups (nonlinear, geometric) and Lie algebras (linear, algebraic). The tangent space at the identity captures the "infinitesimal" structure of the group.

# Examples

**Example** (p. 17, table):
- $\mathrm{Lie}(\mathrm{GL}(n)) = \mathfrak{gl}(n)$ (all matrices)
- $\mathrm{Lie}(\mathrm{SL}(n)) = \{x \mid \mathrm{tr}(x) = 0\}$
- $\mathrm{Lie}(\mathrm{O}(n)) = \{x \mid x + x^t = 0\}$
- $\mathrm{Lie}(\mathrm{U}(n)) = \{x \mid x + x^* = 0\}$

# Relationships

## Builds Upon
- **Lie group** — the group whose tangent space is taken

## Enables
- **Lie algebra** — $T_1G$ with the bracket is a Lie algebra
- **Exponential map** — maps from $\mathfrak{g}$ to $G$
- **All of Lie theory** — the algebra encodes the group structure

## Related
- **Classical group theorem** — computes $\mathfrak{g}$ for matrix groups

# Common Errors

- **Error**: Thinking $\mathfrak{g}$ is defined only for matrix groups.
  **Correction**: $\mathfrak{g} = T_1G$ is defined for any Lie group. The matrix description is a special case.

# Common Confusions

- **Confusion**: Whether $\mathfrak{g}$ has any structure beyond being a vector space before Section 3.2.
  **Clarification**: Before Section 3.2, $\mathfrak{g}$ is just a vector space. The bracket operation comes from the group multiplication and is defined in Section 3.2.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, page 17. Also Theorem 3.17, page 24.

# Verification Notes

- Definition source: Direct from p. 17 and Corollary 2.30
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 2.29, 3.17
