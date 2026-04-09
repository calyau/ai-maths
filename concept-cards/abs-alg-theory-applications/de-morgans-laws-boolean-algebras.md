---
# === CORE IDENTIFICATION ===
concept: "De Morgan's Laws for Boolean Algebras"
slug: de-morgans-laws-boolean-algebras

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
pdf_page: 257
section: "19.2 Boolean Algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-algebra
extends: []
related:
  - principle-of-duality-lattices
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are De Morgan's Laws for Boolean algebras?"
---

# Quick Definition

De Morgan's Laws state that in a Boolean algebra, the complement of a join is the meet of the complements, and the complement of a meet is the join of the complements: $(a \vee b)' = a' \wedge b'$ and $(a \wedge b)' = a' \vee b'$.

# Core Definition

"$(a \vee b)' = a' \wedge b'$ and $(a \wedge b)' = a' \vee b'$ (De Morgan's Laws)" (Judson, Theorem 19.17, part 6, p. 257).

# Prerequisites

- **Boolean algebra** — De Morgan's Laws hold in Boolean algebras

# Key Properties

1. $(a \vee b)' = a' \wedge b'$
2. $(a \wedge b)' = a' \vee b'$
3. Generalize set-theoretic De Morgan's Laws: $(A \cup B)^c = A^c \cap B^c$
4. Connect complementation with the duality principle

# Construction / Recognition

## To Apply:
1. To complement a join: take the meet of complements
2. To complement a meet: take the join of complements

# Context & Application

De Morgan's Laws are essential for circuit simplification (complementing complex circuits) and logical reasoning (negating compound propositions).

# Examples

**Example 1**: In $\mathcal{P}(X)$: $(A \cup B)^c = A^c \cap B^c$.

**Example 2**: In circuits: the complement of a parallel circuit ($a \vee b$) is a series circuit ($a' \wedge b'$).

# Relationships

## Related
- **Principle of duality** — De Morgan's Laws are an instance of duality with complementation

# Common Errors

- **Error**: Applying De Morgan's Laws without taking complements of all terms
  **Correction**: $(a \vee b)' = a' \wedge b'$, not $a \wedge b$

# Common Confusions

- **Confusion**: Thinking De Morgan's Laws only apply to sets
  **Clarification**: They hold in any Boolean algebra, including circuit algebras and propositional logic

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, Theorem 19.17(6), page 257.

# Verification Notes

- Definition source: Direct from Theorem 19.17
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
