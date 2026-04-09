---
# === CORE IDENTIFICATION ===
concept: Levi Decomposition
slug: levi-decomposition

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 72
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Levi theorem"
  - "Levi-Malcev decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - radical
  - semisimple-lie-algebra
  - solvable-lie-algebra
extends:
  - radical
related:
  - reductive-lie-algebra
  - cohomology-vanishing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can any Lie algebra be decomposed into solvable and semisimple parts?"
---

# Quick Definition

The Levi decomposition writes any Lie algebra as a semidirect sum $\mathfrak{g} = \operatorname{rad}(\mathfrak{g}) \oplus \mathfrak{g}_{ss}$ where $\operatorname{rad}(\mathfrak{g})$ is the solvable radical and $\mathfrak{g}_{ss}$ is a semisimple subalgebra. This is stronger than the exact sequence $0 \to \operatorname{rad} \to \mathfrak{g} \to \mathfrak{g}_{ss} \to 0$: the sequence actually splits.

# Core Definition

**Theorem 6.25** (Kirillov, p. 72): Any Lie algebra can be written as a direct sum (of vector spaces)

$$\mathfrak{g} = \operatorname{rad}(\mathfrak{g}) \oplus \mathfrak{g}_{ss}$$

where $\mathfrak{g}_{ss}$ is a semisimple subalgebra (not an ideal!) in $\mathfrak{g}$. Such a decomposition is called a Levi decomposition for $\mathfrak{g}$.

# Prerequisites

- **Radical** — The solvable part of the decomposition
- **Semisimple Lie algebra** — The semisimple complement
- **Solvable Lie algebra** — The radical is solvable

# Key Properties

1. The radical $\operatorname{rad}(\mathfrak{g})$ is an ideal, but $\mathfrak{g}_{ss}$ is only a subalgebra
2. $\mathfrak{g}_{ss} \cong \mathfrak{g}/\operatorname{rad}(\mathfrak{g})$ as Lie algebras
3. The proof reduces to showing $H^2(\mathfrak{g}, \mathbb{C}) = 0$ for semisimple $\mathfrak{g}$
4. The decomposition is not unique in general (the semisimple complement can vary)

# Context & Application

The Levi decomposition is the fundamental structure theorem for arbitrary finite-dimensional Lie algebras. It reduces the study of general Lie algebras to two separate problems: the theory of solvable algebras and the theory of semisimple algebras.

# Examples

**Example 6.26** (p. 72): For the Poincare algebra $\mathfrak{g} = \mathfrak{so}(3, \mathbb{R}) \oplus \mathbb{R}^3$ with $[(A_1, b_1), (A_2, b_2)] = ([A_1, A_2], A_1 b_2 - A_2 b_1)$: the radical is $\mathbb{R}^3$ (abelian ideal) and the Levi complement is $\mathfrak{so}(3, \mathbb{R})$ (semisimple subalgebra).

# Relationships

## Builds Upon
- **Radical** — One component of the decomposition
- **Semisimple Lie algebra** — The other component

## Related
- **Cohomology vanishing** — The proof relies on $H^2(\mathfrak{g}, \mathbb{C}) = 0$

# Common Confusions

- **Confusion**: Thinking both summands are ideals
  **Clarification**: Only $\operatorname{rad}(\mathfrak{g})$ is an ideal; $\mathfrak{g}_{ss}$ is a subalgebra but generally not an ideal. The decomposition is a semidirect sum.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, pages 72. Theorem 6.25, Example 6.26.

# Verification Notes

- Definition source: Direct from Theorem 6.25
- Confidence rationale: Explicitly stated theorem; proof referenced to other texts
- Uncertainties: Proof not given in source
- Cross-reference status: Verified
