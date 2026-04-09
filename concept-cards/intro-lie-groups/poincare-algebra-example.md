---
# === CORE IDENTIFICATION ===
concept: "Poincare Algebra Example"
slug: poincare-algebra-example

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: intermediate

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
  - "Euclidean group Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - levi-decomposition
  - radical
extends: []
related:
  - semisimple-lie-algebra
  - solvable-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a concrete example of the Levi decomposition?"
---

# Quick Definition

The Lie algebra of the Poincare group $SO(3, \mathbb{R}) \ltimes \mathbb{R}^3$ provides a concrete example of the Levi decomposition: $\mathfrak{g} = \mathfrak{so}(3, \mathbb{R}) \oplus \mathbb{R}^3$ where $\mathbb{R}^3$ is the solvable radical and $\mathfrak{so}(3, \mathbb{R})$ is the semisimple Levi factor.

# Core Definition

**Example 6.26** (Kirillov, p. 72): Let $G = SO(3, \mathbb{R}) \ltimes \mathbb{R}^3$ be the group of maps $x \mapsto Ax + b$, $A \in SO(3, \mathbb{R})$, $b \in \mathbb{R}^3$. The Lie algebra $\mathfrak{g} = \mathfrak{so}(3, \mathbb{R}) \oplus \mathbb{R}^3$ with bracket $[(A_1, b_1), (A_2, b_2)] = ([A_1, A_2], A_1 b_2 - A_2 b_1)$.

Here $\mathbb{R}^3$ is an abelian ideal (hence solvable), and $\mathfrak{so}(3, \mathbb{R})$ is semisimple (since $\mathfrak{so}(3, \mathbb{R})^{\mathbb{C}} \cong \mathfrak{sl}(2, \mathbb{C})$). This gives the Levi decomposition.

# Prerequisites

- **Levi decomposition** — This is an example
- **Radical** — $\operatorname{rad}(\mathfrak{g}) = \mathbb{R}^3$

# Key Properties

1. $\mathbb{R}^3$ is both an ideal and the radical
2. $\mathfrak{so}(3, \mathbb{R})$ is a subalgebra but NOT an ideal
3. The decomposition is a semidirect sum, not a direct sum as Lie algebras

# Relationships

## Illustrates
- **Levi decomposition** — Concrete example with physical significance

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, page 72. Example 6.26.

# Verification Notes

- Definition source: Direct from Example 6.26
- Confidence rationale: Explicit worked example
- Uncertainties: None
- Cross-reference status: Verified
