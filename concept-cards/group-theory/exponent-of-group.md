---
# === CORE IDENTIFICATION ===
concept: Exponent of a Group
slug: exponent-of-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: commutative-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 29
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - fundamental-theorem-finitely-generated-abelian-groups
  - burnside-problem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponent of a group?"
  - "When does a group have finite exponent?"
---

# Quick Definition

A group $G$ has finite exponent $e$ if $g^e = 1$ for all $g \in G$ and $e$ is the smallest positive integer with this property.

# Core Definition

"A group $G$ is said to have *finite exponent* if there exists an $m > 0$ such that $a^m = e$ for every $a$ in $G$; the smallest such $m$ is then called the *exponent* of $G$." (Milne, Exercise 1-6, p. 29)

# Prerequisites

- **Group** — the exponent is a property of a group

# Key Properties

1. The exponent divides the order of $G$ when $G$ is finite
2. Every group of exponent 2 is commutative (Exercise 1-6a)
3. For a finite abelian group $C_{n_1} \times \cdots \times C_{n_r}$ with $n_1 | \cdots | n_r$, the exponent is $n_r$
4. The Burnside problem asks whether a finitely generated group of finite exponent must be finite

# Context & Application

The exponent is central to the Burnside problem (Chapter 2). The relationship between exponent, order, and number of generators determines deep structural properties of groups.

# Examples

**Example 1**: $C_n$ has exponent $n$.

**Example 2**: $C_2 \times C_2$ has exponent 2.

**Example 3** (Exercise 1-6b): The Heisenberg group over $\mathbb{F}_p$ (upper triangular matrices with 1s on diagonal) has exponent $p$ for odd primes $p$.

# Relationships

## Related
- **fundamental-theorem-finitely-generated-abelian-groups** — exponent equals largest invariant factor
- **burnside-problem** — asks if finite exponent + finite generation implies finiteness

# Source Reference

Chapter 1, Exercise 1-6, page 29. Also Chapter 2, p. 37 (Burnside problem).

# Verification Notes

- Definition source: Direct from Exercise 1-6
- Confidence: HIGH — explicit definition
- Uncertainties: None
