---
# === CORE IDENTIFICATION ===
concept: Equivalence Relation
slug: equivalence-relation

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
pdf_page: 24
section: "Equivalence Relations and Partitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - relation
  - set
extends:
  - relation
related:
  - equivalence-class
  - partition
  - congruence-modulo-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is an equivalence relation?"
---

# Quick Definition

An equivalence relation on a set $X$ is a relation that is reflexive, symmetric, and transitive. Equivalence relations generalize the concept of equality and partition sets into equivalence classes.

# Core Definition

"An equivalence relation on a set $X$ is a relation $R \subset X \times X$ such that:
- $(x, x) \in R$ for all $x \in X$ (reflexive property);
- $(x, y) \in R$ implies $(y, x) \in R$ (symmetric property);
- $(x, y)$ and $(y, z) \in R$ imply $(x, z) \in R$ (transitive property)"
(Judson, p. 24). We usually write $x \sim y$ instead of $(x, y) \in R$.

# Prerequisites

- **Relation** — An equivalence relation is a special type of relation
- **Set** — Defined on a set $X$

# Key Properties

1. **Reflexive**: Every element is related to itself
2. **Symmetric**: If $x \sim y$ then $y \sim x$
3. **Transitive**: If $x \sim y$ and $y \sim z$ then $x \sim z$
4. Equivalence classes form a partition of $X$ (Theorem 1.25)
5. Two equivalence classes are either disjoint or equal (Corollary 1.26)

# Construction / Recognition

## To Verify an Equivalence Relation:
1. Check reflexivity: Is $x \sim x$ for all $x \in X$?
2. Check symmetry: Does $x \sim y$ imply $y \sim x$?
3. Check transitivity: Do $x \sim y$ and $y \sim z$ imply $x \sim z$?

# Context & Application

Equivalence relations are fundamental to constructing algebraic structures. The integers modulo $n$ are equivalence classes under the relation of congruence mod $n$. Many algebraic constructions (quotient groups, quotient rings) rely on equivalence relations.

# Examples

**Example 1** (p. 24): Define $p/q \sim r/s$ on fractions if $ps = qr$. This is reflexive ($ps = qp$ when $p/q = p/q$), symmetric, and transitive.

**Example 2** (p. 25): For $(x_1, y_1)$ and $(x_2, y_2)$ in $\mathbb{R}^2$, define $(x_1, y_1) \sim (x_2, y_2)$ if $x_1^2 + y_1^2 = x_2^2 + y_2^2$. The equivalence classes are circles centered at the origin.

**Example 3** (p. 26): Congruence modulo $n$: $r \equiv s \pmod{n}$ if $n \mid (r - s)$. This is an equivalence relation on $\mathbb{Z}$.

# Relationships

## Builds Upon
- **relation** — An equivalence relation is a specific type of relation

## Enables
- **equivalence-class** — Each element determines an equivalence class
- **partition** — Equivalence classes partition the set
- **congruence-modulo-n** — A key example of equivalence relation
- **integers-mod-n** — Constructed from congruence equivalence classes

# Common Errors

- **Error**: Checking only two of the three properties and concluding equivalence
  **Correction**: All three properties (reflexive, symmetric, transitive) must be verified

# Common Confusions

- **Confusion**: Thinking reflexivity is redundant given symmetry and transitivity
  **Clarification**: As shown in Exercise 28 (p. 28), reflexivity is NOT redundant. Symmetry and transitivity together do not imply reflexivity because there may be elements not related to any other element.

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 24-27.

# Verification Notes

- Definition source: Direct quote from p. 24
- Confidence: HIGH — explicit definition with three properties
- Cross-reference status: Verified
- Uncertainties: None
