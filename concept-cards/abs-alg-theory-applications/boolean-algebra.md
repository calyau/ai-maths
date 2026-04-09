---
# === CORE IDENTIFICATION ===
concept: Boolean Algebra
slug: boolean-algebra

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
  - distributive-lattice
  - complemented-lattice
extends:
  - distributive-lattice
  - complemented-lattice
related:
  - series-parallel-circuit
  - atom-boolean-algebra
contrasts_with:
  - lattice

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Boolean algebra?"
  - "How do lattices relate to Boolean algebras?"
---

# Quick Definition

A Boolean algebra is a lattice $B$ with a greatest element $I$ and a smallest element $O$ that is both distributive and complemented. Equivalently, it is a set with operations $\vee$ and $\wedge$ satisfying commutativity, associativity, distributivity, identity, and complement axioms.

# Core Definition

"A Boolean algebra is a lattice $B$ with a greatest element $I$ and a smallest element $O$ such that $B$ is both distributive and complemented" (Judson, p. 256). The axiomatic characterization (Theorem 19.16) states that $B$ is a Boolean algebra iff there exist operations $\vee, \wedge$ satisfying: (1) commutativity; (2) associativity; (3) distributivity; (4) identity elements $I, O$; (5) complements.

# Prerequisites

- **Distributive lattice** — Boolean algebras are distributive
- **Complemented lattice** — Boolean algebras are complemented

# Key Properties

1. Commutative: $a \vee b = b \vee a$, $a \wedge b = b \wedge a$
2. Associative: $a \vee (b \vee c) = (a \vee b) \vee c$
3. Distributive: $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$
4. Identity: $a \vee O = a$, $a \wedge I = a$
5. Complement: $a \vee a' = I$, $a \wedge a' = O$
6. De Morgan's Laws: $(a \vee b)' = a' \wedge b'$ and $(a \wedge b)' = a' \vee b'$ (Theorem 19.17)
7. Complements are unique (Theorem 19.17)
8. $(a')' = a$ (Theorem 19.17)
9. Every finite Boolean algebra has order $2^n$ (Corollary 19.24)
10. Every finite Boolean algebra is isomorphic to $\mathcal{P}(X)$ for some finite set $X$ (Theorem 19.23)

# Construction / Recognition

## To Verify:
1. Check all five axiom groups (Theorem 19.16)
2. Or verify it is a complemented distributive lattice

# Context & Application

Boolean algebras bridge algebra, logic, and computer science. They model propositional logic (propositions with AND, OR, NOT), digital circuit design (series/parallel switches), and set operations. Every finite Boolean algebra is a power set algebra.

# Examples

**Example 1** (p. 256): The power set $\mathcal{P}(X)$ with $\cup, \cap$, complement $X \setminus A$ is the prototype Boolean algebra.

**Example 2** (p. 261): The set of all switching circuits forms a Boolean algebra under series ($\wedge$) and parallel ($\vee$) connections.

# Relationships

## Builds Upon
- **Distributive lattice** — Boolean algebras satisfy distributivity
- **Complemented lattice** — Boolean algebras have complements

## Enables
- **Series-parallel circuits** — Circuit algebra is a Boolean algebra
- **Propositional logic** — Boolean algebras model logical operations

## Contrasts With
- **Lattice** — Not every lattice is a Boolean algebra (must be distributive and complemented)

# Common Errors

- **Error**: Assuming all lattices are Boolean algebras
  **Correction**: A Boolean algebra must be both distributive and complemented

# Common Confusions

- **Confusion**: Confusing Boolean algebra with the two-element set $\{0, 1\}$
  **Clarification**: $\{0, 1\}$ is the simplest Boolean algebra, but Boolean algebras can have $2^n$ elements for any $n$

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, pages 256-260. See Theorems 19.16, 19.17, 19.23.

# Verification Notes

- Definition source: Direct from p. 256
- Confidence: HIGH — explicit definition with multiple characterizations
- Cross-reference status: Verified
- Uncertainties: None
