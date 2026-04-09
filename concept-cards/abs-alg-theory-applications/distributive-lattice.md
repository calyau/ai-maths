---
# === CORE IDENTIFICATION ===
concept: Distributive Lattice
slug: distributive-lattice

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
pdf_page: 256
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
  - "What is a distributive lattice?"
  - "When does the distributive law hold in a lattice?"
---

# Quick Definition

A distributive lattice is a lattice $L$ in which the distributive law holds: $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ for all $a, b, c \in L$.

# Core Definition

"We will say that a lattice $L$ is distributive if the following distributive law holds: $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ for all $a, b, c \in L$" (Judson, p. 256). By Theorem 19.15, this is equivalent to the dual distributive law $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$.

# Prerequisites

- **Lattice** — A distributive lattice is a lattice with an additional property

# Key Properties

1. $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$
2. Equivalently: $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$ (Theorem 19.15)
3. Not all lattices are distributive
4. Required for Boolean algebras

# Construction / Recognition

## To Verify:
1. Confirm $L$ is a lattice
2. Verify $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ for all $a, b, c$

# Context & Application

Distributivity is essential for Boolean algebras. The power set lattice $\mathcal{P}(X)$ is distributive since $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.

# Examples

**Example 1** (p. 256): $\mathcal{P}(X)$ is a distributive lattice.

**Example 2**: The lattice of divisors of a positive integer under divisibility is distributive.

# Relationships

## Builds Upon
- **Lattice** — Adds the distributive property

## Enables
- **Boolean algebra** — A Boolean algebra is a complemented distributive lattice

# Common Errors

- **Error**: Assuming all lattices are distributive
  **Correction**: The lattice of subgroups of a non-abelian group may not be distributive

# Common Confusions

- **Confusion**: Thinking one distributive law implies the other separately
  **Clarification**: In a lattice, the two distributive laws are equivalent (Theorem 19.15)

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, pages 256. See Theorem 19.15.

# Verification Notes

- Definition source: Direct from p. 256
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
