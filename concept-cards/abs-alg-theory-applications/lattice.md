---
# === CORE IDENTIFICATION ===
concept: Lattice
slug: lattice

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
pdf_page: 254
section: "19.1 Lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - partially-ordered-set
  - least-upper-bound
  - greatest-lower-bound
extends:
  - partially-ordered-set
related:
  - boolean-algebra
  - distributive-lattice
contrasts_with:
  - boolean-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a lattice?"
  - "How do lattices relate to Boolean algebras?"
---

# Quick Definition

A lattice is a poset $L$ in which every pair of elements has both a least upper bound (join, $a \vee b$) and a greatest lower bound (meet, $a \wedge b$).

# Core Definition

"A lattice is a poset $L$ such that every pair of elements in $L$ has a least upper bound and a greatest lower bound. The least upper bound of $a, b \in L$ is called the join of $a$ and $b$ and is denoted by $a \vee b$. The greatest lower bound of $a, b \in L$ is called the meet of $a$ and $b$ and is denoted by $a \wedge b$" (Judson, p. 254).

# Prerequisites

- **Partially ordered set** — A lattice is a poset with additional structure
- **Least upper bound** — Every pair must have a join
- **Greatest lower bound** — Every pair must have a meet

# Key Properties (Theorem 19.13)

1. Commutative: $a \vee b = b \vee a$ and $a \wedge b = b \wedge a$
2. Associative: $a \vee (b \vee c) = (a \vee b) \vee c$ and $a \wedge (b \wedge c) = (a \wedge b) \wedge c$
3. Idempotent: $a \vee a = a$ and $a \wedge a = a$
4. Absorption: $a \vee (a \wedge b) = a$ and $a \wedge (a \vee b) = a$
5. Conversely, any set with operations satisfying these laws is a lattice (Theorem 19.14)

# Construction / Recognition

## To Verify (Order-Theoretic):
1. Confirm $(L, \preceq)$ is a poset
2. Show every pair $\{a, b\}$ has a LUB (join) and GLB (meet)

## To Verify (Algebraic):
1. Show $L$ has operations $\vee, \wedge$ satisfying commutative, associative, idempotent, and absorption laws

# Context & Application

Lattices generalize both order structures (like divisibility) and algebraic structures (like power sets). They provide the foundation for Boolean algebras and have applications in logic, topology, and computer science.

# Examples

**Example 1** (p. 254): $\mathcal{P}(X)$ under $\subset$ is a lattice with $A \vee B = A \cup B$ and $A \wedge B = A \cap B$.

**Example 2** (p. 254): The subgroups of a group $G$, ordered by inclusion, form a lattice with meet $H \wedge K = H \cap K$.

**Example 3** (p. 253): The divisors of 24 under divisibility form a lattice.

# Relationships

## Builds Upon
- **Partially ordered set** — A lattice is a poset with joins and meets for all pairs

## Enables
- **Distributive lattice** — A lattice satisfying the distributive law
- **Boolean algebra** — A complemented distributive lattice

## Contrasts With
- **Boolean algebra** — A Boolean algebra is a lattice that is also distributive and complemented

# Common Errors

- **Error**: Assuming every poset is a lattice
  **Correction**: Some posets lack joins or meets for certain pairs

# Common Confusions

- **Confusion**: Confusing the lattice join $\vee$ with logical OR and lattice meet $\wedge$ with logical AND
  **Clarification**: While analogous, lattice operations are defined in terms of order, not logic; they coincide for Boolean algebras

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.1, pages 254-256. See Theorems 19.13 and 19.14.

# Verification Notes

- Definition source: Direct from p. 254
- Confidence: HIGH — explicit definition with algebraic characterization
- Cross-reference status: Verified
- Uncertainties: None
