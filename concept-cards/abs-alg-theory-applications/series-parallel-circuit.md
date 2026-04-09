---
# === CORE IDENTIFICATION ===
concept: Series-Parallel Circuit
slug: series-parallel-circuit

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
pdf_page: 260
section: "19.3 The Algebra of Electrical Circuits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "switching circuit"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-algebra
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Boolean algebras relate to electrical circuits?"
  - "What is a series-parallel circuit?"
---

# Quick Definition

A series-parallel circuit is a circuit built from switches connected in series ($a \wedge b$: both must be closed) or parallel ($a \vee b$: either can be closed), forming a Boolean algebra where circuit simplification corresponds to Boolean algebra identities.

# Core Definition

"Two switches $a$ and $b$ are in series if current can pass only if both are closed, denoted $a \wedge b$. Two switches are in parallel if current can pass if either is closed, denoted $a \vee b$" (Judson, p. 260). "The set of all circuits is a Boolean algebra" (Theorem 19.30, p. 261). The complement $a'$ denotes a switch always in the opposite state of $a$.

# Prerequisites

- **Boolean algebra** — Circuits form a Boolean algebra

# Key Properties

1. Series = $a \wedge b$ (AND): current flows iff both switches closed
2. Parallel = $a \vee b$ (OR): current flows iff at least one switch closed
3. Complement $a'$: always in opposite state of $a$
4. Always closed = $I$; always open = $O$
5. $a \wedge a' = O$ and $a \vee a' = I$
6. All Boolean algebra identities apply for circuit simplification

# Construction / Recognition

## To Simplify a Circuit:
1. Express the circuit as a Boolean expression
2. Apply Boolean algebra identities to simplify
3. Build the simplified circuit

# Context & Application

Boolean algebras found their most impactful application in circuit design. George Boole's work, combined with Claude Shannon's insight, showed that switching circuits obey Boolean algebra laws. This is the foundation of digital computer design.

# Examples

**Example 1** (p. 261): The circuit $(a \vee b) \wedge (a \vee b') \wedge (a \vee b)$ simplifies to just $a$:
$(a \vee b) \wedge (a \vee b') = a \vee (b \wedge b') = a \vee O = a$.

# Relationships

## Builds Upon
- **Boolean algebra** — Circuits form a Boolean algebra

# Common Errors

- **Error**: Forgetting that $a \wedge a' = O$ (always open)
  **Correction**: A switch and its complement in series blocks all current

# Common Confusions

- **Confusion**: Thinking series and parallel are commutative only in special cases
  **Clarification**: Both are always commutative: $a \wedge b = b \wedge a$ and $a \vee b = b \vee a$

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.3, pages 260-262. See Theorem 19.30 and Example 19.31.

# Verification Notes

- Definition source: Direct from pp. 260-261
- Confidence: HIGH — explicit definitions and theorem
- Cross-reference status: Verified
- Uncertainties: None
