---
# === CORE IDENTIFICATION ===
concept: Solvable Lie Algebra
slug: solvable-lie-algebra

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
pdf_page: 67
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - derived-series
  - commutant
extends: []
related:
  - nilpotent-lie-algebra
  - radical
  - semisimple-lie-algebra
  - lie-theorem
contrasts_with:
  - nilpotent-lie-algebra
  - semisimple-lie-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a solvable Lie algebra?"
  - "What distinguishes a solvable Lie algebra from a nilpotent one?"
  - "How do I determine if a Lie algebra is solvable?"
---

# Quick Definition

A solvable Lie algebra is one whose derived series terminates at zero, meaning the algebra can be built up by successive abelian extensions. Informally, it is an "almost commutative" Lie algebra.

# Core Definition

**Definition 6.8** (Kirillov, p. 68): A Lie algebra $\mathfrak{g}$ is called solvable if $D^n\mathfrak{g} = 0$ for large enough $n$, where $D^i\mathfrak{g}$ is the derived series.

Equivalently (Proposition 6.7): $\mathfrak{g}$ is solvable iff there exists a chain of subalgebras $\mathfrak{a}^0 = \mathfrak{g} \supset \mathfrak{a}^1 \supset \cdots \supset \mathfrak{a}^k = \{0\}$ where each $\mathfrak{a}^{i+1}$ is an ideal in $\mathfrak{a}^i$ with abelian quotient, iff every commutator $[\ldots[[x_1,x_2],[x_3,x_4]]\ldots]$ ($2^n$ terms in a binary tree) is zero for large $n$.

# Prerequisites

- **Derived series** — Solvability is defined by vanishing of the derived series
- **Commutant** — The derived series iterates the commutant operation

# Key Properties

1. A real Lie algebra is solvable iff its complexification is solvable (Theorem 6.13)
2. Any subalgebra or quotient of a solvable Lie algebra is solvable (Theorem 6.13)
3. Every nilpotent Lie algebra is solvable (Theorem 6.13)
4. If $I \subset \mathfrak{g}$ is an ideal with both $I$ and $\mathfrak{g}/I$ solvable, then $\mathfrak{g}$ is solvable (Theorem 6.13)
5. $\mathfrak{g}$ is solvable iff $[\mathfrak{g}, \mathfrak{g}]$ is nilpotent (Corollary 6.16)
6. Every irreducible representation of a solvable Lie algebra is 1-dimensional (Corollary 6.16)

# Construction / Recognition

## To Construct:
1. Start with an abelian Lie algebra
2. Form extensions by abelian algebras (the resulting algebra is solvable)

## To Identify/Recognize:
1. Compute the derived series: $D^0\mathfrak{g} = \mathfrak{g}$, $D^{i+1}\mathfrak{g} = [D^i\mathfrak{g}, D^i\mathfrak{g}]$
2. If $D^n\mathfrak{g} = 0$ for some $n$, then $\mathfrak{g}$ is solvable
3. Alternatively, use the Cartan criterion: $\mathfrak{g}$ is solvable iff $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$

# Context & Application

Solvable Lie algebras represent one extreme of the structure theory: they are "close to abelian." Every Lie algebra contains a largest solvable ideal (the radical), and the quotient by the radical is semisimple. This dichotomy is central to the classification of Lie algebras.

# Examples

**Example 6.12** (p. 68): The Lie algebra $\mathfrak{b}$ of upper-triangular matrices in $\mathfrak{gl}(n, \mathbb{K})$ is solvable. The commutant $D^1\mathfrak{b} \subset \mathfrak{n}$ (strictly upper-triangular), and successive derived subalgebras shift further above the diagonal: $D^{i+1}\mathfrak{b} \subset \mathfrak{a}_{2^i}$.

Note: $\mathfrak{b}$ is solvable but not nilpotent, since $D_2\mathfrak{b} = [\mathfrak{b}, D_1\mathfrak{b}] = D_1\mathfrak{b} = \mathfrak{n}$ does not decrease further.

# Relationships

## Builds Upon
- **Derived series** — Solvability is vanishing of the derived series
- **Commutant** — First step of the derived series

## Enables
- **Radical** — The maximal solvable ideal of any Lie algebra
- **Lie theorem** — Representations of solvable algebras can be upper-triangularized
- **Levi decomposition** — Decomposes any Lie algebra into solvable and semisimple parts

## Related
- **Nilpotent Lie algebra** — Every nilpotent algebra is solvable, but not conversely

## Contrasts With
- **Semisimple Lie algebra** — Contains no nonzero solvable ideals; the opposite extreme
- **Nilpotent Lie algebra** — Defined by the lower central series instead of the derived series

# Common Errors

- **Error**: Assuming a solvable Lie algebra must be nilpotent
  **Correction**: The algebra of upper-triangular matrices $\mathfrak{b}$ is solvable but not nilpotent

# Common Confusions

- **Confusion**: Confusing "solvable" with "nilpotent"
  **Clarification**: Nilpotent requires $[\mathfrak{g}, [\mathfrak{g}, \ldots [\mathfrak{g}, \mathfrak{g}]\ldots]] = 0$ (linear nesting); solvable requires $[[\ldots[\mathfrak{g},\mathfrak{g}],[\mathfrak{g},\mathfrak{g}]]\ldots] = 0$ (binary tree nesting). The solvable condition is weaker.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 67-69. Definition 6.8, Proposition 6.7, Theorem 6.13, Example 6.12.

# Verification Notes

- Definition source: Direct from Definition 6.8
- Confidence rationale: Central definition with explicit characterization theorem and examples
- Uncertainties: None
- Cross-reference status: Verified against source
