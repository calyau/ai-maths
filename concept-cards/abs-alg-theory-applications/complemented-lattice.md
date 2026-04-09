---
# === CORE IDENTIFICATION ===
concept: Complemented Lattice
slug: complemented-lattice

# === CLASSIFICATION ===
category: lattice-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Lattices and Boolean Algebras"
chapter_number: 19
pdf_page: 255
section: "19.2 Boolean Algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lattice
extends:
  - lattice
related:
  - boolean-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a complemented lattice?"
---

# Quick Definition

A lattice $L$ with a largest element $I$ and smallest element $O$ is complemented if for each $a \in L$, there exists $a' \in L$ such that $a \vee a' = I$ and $a \wedge a' = O$.

# Core Definition

"A lattice $L$ with a largest element $I$ and a smallest element $O$ is complemented if for each $a \in L$, there exists an $a'$ such that $a \vee a' = I$ and $a \wedge a' = O$" (Judson, p. 255).

# Prerequisites

- **Lattice** — A complemented lattice is a lattice with additional structure

# Key Properties

1. Has a largest element $I$ and smallest element $O$
2. Every element $a$ has a complement $a'$
3. $a \vee a' = I$ and $a \wedge a' = O$
4. Complements need not be unique in general lattices
5. In a distributive lattice, complements are unique

# Construction / Recognition

## To Verify:
1. Confirm $L$ is a lattice with largest element $I$ and smallest element $O$
2. For each $a$, find $a'$ with $a \vee a' = I$ and $a \wedge a' = O$

# Context & Application

Complementation generalizes set complement ($A' = X \setminus A$) and logical negation. A complemented distributive lattice is a Boolean algebra.

# Examples

**Example 1** (p. 255): $\mathcal{P}(X)$ is complemented: $A' = X \setminus A$, with $A \cup A' = X$ and $A \cap A' = \emptyset$.

# Relationships

## Builds Upon
- **Lattice** — Adds complement operation

## Enables
- **Boolean algebra** — Complemented + distributive = Boolean algebra

# Common Errors

- **Error**: Assuming complements are unique in any lattice
  **Correction**: Uniqueness of complements requires distributivity

# Common Confusions

- **Confusion**: Confusing complement with inverse
  **Clarification**: Complement is defined by $a \vee a' = I$ and $a \wedge a' = O$, not by $a \cdot a' = 1$

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, page 255.

# Verification Notes

- Definition source: Direct from p. 255
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
