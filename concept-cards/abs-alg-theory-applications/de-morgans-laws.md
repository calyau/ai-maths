---
# === CORE IDENTIFICATION ===
concept: De Morgan's Laws
slug: de-morgans-laws

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 18
section: "Sets and Equivalence Relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set-union
  - set-intersection
  - set-complement
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

De Morgan's Laws state that the complement of a union equals the intersection of complements, and the complement of an intersection equals the union of complements.

# Core Definition

**Theorem 1.3 (De Morgan's Laws)**: Let $A$ and $B$ be sets. Then:
1. $(A \cup B)' = A' \cap B'$
2. $(A \cap B)' = A' \cup B'$

(Judson, p. 18).

# Prerequisites

- **Set union** — One of the operations related by the laws
- **Set intersection** — The other operation related by the laws
- **Set complement** — The laws describe how complement interacts with union and intersection

# Key Properties

1. Complement converts union to intersection and vice versa
2. Both laws are proven by showing subset containment in both directions

# Construction / Recognition

## To Apply De Morgan's Laws:
1. To find the complement of a union: take the intersection of the individual complements
2. To find the complement of an intersection: take the union of the individual complements

# Context & Application

De Morgan's Laws are a fundamental proof technique used throughout mathematics. They appear whenever one needs to negate a compound logical or set-theoretic statement.

# Examples

**Example 1** (p. 18-19): The proof of law (1) proceeds by showing $(A \cup B)' \subset A' \cap B'$ and $(A \cup B)' \supset A' \cap B'$. If $x \in (A \cup B)'$, then $x \notin A \cup B$, so $x \notin A$ and $x \notin B$, hence $x \in A'$ and $x \in B'$, giving $x \in A' \cap B'$.

# Relationships

## Builds Upon
- **set-union** — Appears in the laws
- **set-intersection** — Appears in the laws
- **set-complement** — The laws describe its interaction with union/intersection

## Enables
- **mathematical-proof** — Provides a tool for proofs involving set operations

# Common Errors

- **Error**: Applying De Morgan's Laws without swapping the operation (e.g., writing $(A \cup B)' = A' \cup B'$)
  **Correction**: The operation must change: union becomes intersection and vice versa

# Common Confusions

- **Confusion**: Thinking De Morgan's Laws only apply to sets
  **Clarification**: Analogous laws hold for logical statements: $\neg(p \lor q) = \neg p \land \neg q$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, Theorem 1.3, pages 18-19.

# Verification Notes

- Definition source: Direct from Theorem 1.3, p. 18
- Confidence: HIGH — explicit theorem statement and proof
- Cross-reference status: Verified
- Uncertainties: None
