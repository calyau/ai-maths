---
# === CORE IDENTIFICATION ===
concept: Cauchy's Theorem
slug: cauchy-theorem

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Cauchy's Theorem"
chapter_number: 13
pdf_page: 75
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lagrange-theorem
  - equivalence-relation
  - partition
extends: []
related:
  - classification-groups-order-6
  - classification-groups-order-8
  - sylow-theorems
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a group contain an element of prime order?"
  - "What is the partial converse to Lagrange's theorem?"
---

# Quick Definition

If $p$ is a prime divisor of the order of a finite group $G$, then $G$ contains an element of order $p$.

# Core Definition

**(13.1) Cauchy's Theorem.** If $p$ is a prime divisor of the order of a finite group $G$, then $G$ contains an element of order $p$ (Armstrong, p. 75).

Armstrong presents McKay's elegant proof using a counting argument on ordered strings. Let $X$ be the set of all ordered strings $(x_1, x_2, \ldots, x_p)$ of elements of $G$ with $x_1 x_2 \cdots x_p = e$. Since the first $p-1$ entries can be chosen freely, $|X| = |G|^{p-1}$, which is divisible by $p$.

Define an equivalence relation on $X$ by cyclic permutation of coordinates. Each equivalence class has either 1 or $p$ elements (since $p$ is prime). The string $(e, e, \ldots, e)$ has a singleton class. Since $|X|$ is divisible by $p$, there must be another singleton class — a string $(x, x, \ldots, x)$ with $x \neq e$ and $x^p = e$.

# Prerequisites

- **Lagrange's theorem** — Cauchy's theorem is described as a "partial converse"
- **Equivalence relation** — The proof uses an equivalence relation on strings
- **Partition** — The equivalence classes partition $X$, and their sizes must sum to $|X|$

# Key Properties

1. Provides elements of prime order whenever the prime divides the group order
2. The proof works for all groups, not just abelian ones (McKay's argument)
3. Each equivalence class under cyclic permutation has 1 or $p$ elements (since $p$ is prime)
4. The counting argument: $|X| \equiv$ (number of singleton classes) $\pmod{p}$, and $p | |X|$, so the number of singletons is divisible by $p$, hence $\geq p > 1$

# Construction / Recognition

## To Apply:
1. Compute $|G|$ and factor it
2. For each prime factor $p$ of $|G|$, conclude there exists $x \in G$ with $x^p = e$ and $x \neq e$
3. The subgroup $\langle x \rangle$ has order $p$

# Context & Application

Armstrong calls this "the partial converse to Lagrange's theorem promised in Chapter 11" (p. 75). While Lagrange's theorem says subgroup orders divide $|G|$, the converse fails (e.g., $A_4$ has no order-6 subgroup). Cauchy's theorem rescues the converse for prime divisors: if a prime $p$ divides $|G|$, then $G$ has a subgroup of order $p$. Armstrong notes that a second existence theorem (Sylow's theorems) handles prime powers.

The proof is notable for its elegance — McKay's argument uses only elementary counting and the primality of $p$.

# Examples

**Example 1** (p. 76): Applied to a group of order 6, Cauchy's theorem guarantees elements of order 2 and order 3, which Armstrong uses to classify all groups of order 6.

**Example 2** (p. 76): Applied to a group of order 8, the theorem guarantees an element of order 2.

# Relationships

## Builds Upon
- **Lagrange's theorem** — Cauchy's theorem is the partial converse

## Enables
- **Classification of groups of order 6** — Uses elements of orders 2 and 3
- **Classification of groups of order 8** — Uses elements of order 2
- **Sylow's theorems** — Generalise Cauchy's theorem to prime powers

# Common Errors

- **Error**: Applying Cauchy's theorem to composite (non-prime) divisors
  **Correction**: The theorem only guarantees subgroups of prime order. For composite divisors, no such guarantee exists ($A_4$ has order 12 but no subgroup of order 6).

# Common Confusions

- **Confusion**: Thinking Cauchy's theorem says $G$ has a *unique* element of order $p$
  **Clarification**: There may be many elements of order $p$. The theorem guarantees at least one.

# Source Reference

Chapter 13: Cauchy's Theorem, Theorem (13.1), pp. 75-76 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (13.1), p. 75
- Proof method: McKay's counting argument via cyclic permutation of strings
- Confidence rationale: HIGH — explicit theorem with complete proof
- Uncertainties: None
