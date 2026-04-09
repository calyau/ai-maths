---
# === CORE IDENTIFICATION ===
concept: Nilpotent Lie Algebra
slug: nilpotent-lie-algebra

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 68
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lower-central-series
extends: []
related:
  - solvable-lie-algebra
  - engel-theorem
contrasts_with:
  - solvable-lie-algebra
  - semisimple-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a nilpotent Lie algebra?"
  - "What distinguishes a solvable Lie algebra from a nilpotent one?"
---

# Quick Definition

A nilpotent Lie algebra is one whose lower central series terminates at zero, meaning all sufficiently long iterated brackets $[x_1, [x_2, \ldots [x_{n-1}, x_n]\ldots]]$ vanish. Nilpotency is strictly stronger than solvability.

# Core Definition

**Definition 6.11** (Kirillov, p. 68): A Lie algebra $\mathfrak{g}$ is called nilpotent if $D_n\mathfrak{g} = 0$ for large enough $n$, where $D_i\mathfrak{g}$ is the lower central series.

Equivalently (Proposition 6.10): $\mathfrak{g}$ is nilpotent iff there exists a chain of ideals $\mathfrak{a}^0 = \mathfrak{g} \supset \mathfrak{a}^1 \supset \cdots \supset \mathfrak{a}^k = \{0\}$ with $[\mathfrak{g}, \mathfrak{a}^i] \subset \mathfrak{a}^{i+1}$, iff every iterated commutator $[\ldots[[x_1, x_2], x_3], \ldots x_n]$ ($n$ terms) is zero for large $n$.

# Prerequisites

- **Lower central series** — Nilpotency is defined by vanishing of this series

# Key Properties

1. A real Lie algebra is nilpotent iff its complexification is nilpotent (Theorem 6.13)
2. Any subalgebra or quotient of a nilpotent algebra is nilpotent (Theorem 6.13)
3. Every nilpotent Lie algebra is solvable (Theorem 6.13)
4. The converse fails: solvable does not imply nilpotent
5. A Lie algebra is nilpotent iff $\operatorname{ad} x$ is nilpotent for every $x$ (Engel theorem, Theorem 6.18)

# Construction / Recognition

## To Construct:
1. Take any Lie algebra consisting of strictly upper-triangular matrices
2. More generally, any algebra with $[\mathfrak{g}, [\mathfrak{g}, \ldots [\mathfrak{g}, \mathfrak{g}]\ldots]] = 0$

## To Identify/Recognize:
1. Compute the lower central series
2. Alternatively, check if $\operatorname{ad} x$ is nilpotent for every $x$ (Engel criterion)

# Context & Application

Nilpotent Lie algebras form a natural class between abelian algebras and solvable algebras. By Engel's theorem, they are precisely the algebras where every element acts nilpotently in the adjoint representation. In the structure theory, they appear as the nilradical of solvable algebras.

# Examples

**Example 6.12** (p. 68): The Lie algebra $\mathfrak{n}$ of strictly upper-triangular matrices is nilpotent. If $\mathfrak{a}_k$ denotes matrices with entries only $k$ positions above the diagonal, then $[\mathfrak{a}_k, \mathfrak{a}_l] \subset \mathfrak{a}_{k+l}$, so $D_i\mathfrak{n} \subset \mathfrak{a}_{i+1}$.

The upper-triangular algebra $\mathfrak{b}$ is solvable but NOT nilpotent: $D_2\mathfrak{b} = [\mathfrak{b}, \mathfrak{n}] = \mathfrak{n}$ does not decrease.

# Relationships

## Builds Upon
- **Lower central series** — Nilpotency is vanishing of this series

## Enables
- **Engel theorem** — Characterizes nilpotency via nilpotent operators

## Contrasts With
- **Solvable Lie algebra** — Every nilpotent algebra is solvable, but not conversely (e.g., $\mathfrak{b}$)
- **Semisimple Lie algebra** — A semisimple algebra has no nonzero nilpotent ideals

# Common Errors

- **Error**: Assuming "solvable" and "nilpotent" are synonymous
  **Correction**: The upper-triangular Borel subalgebra is the standard counterexample: solvable but not nilpotent

# Common Confusions

- **Confusion**: Confusing nilpotent Lie algebra with nilpotent element
  **Clarification**: A nilpotent algebra has $D_n\mathfrak{g} = 0$; a nilpotent element $x$ has $(\operatorname{ad} x)^n = 0$. By Engel's theorem, an algebra is nilpotent iff all its elements are nilpotent (in the adjoint sense).

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 68-69. Definition 6.11, Proposition 6.10, Theorem 6.13, Example 6.12.

# Verification Notes

- Definition source: Direct from Definition 6.11
- Confidence rationale: Explicitly defined with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
