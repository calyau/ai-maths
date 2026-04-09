---
# === CORE IDENTIFICATION ===
concept: Radical
slug: radical

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 71
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rad(g)"
  - "solvable radical"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - semisimple-lie-algebra
  - levi-decomposition
  - reductive-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the radical of a Lie algebra?"
  - "How does the radical relate to semisimplicity?"
---

# Quick Definition

The radical $\operatorname{rad}(\mathfrak{g})$ of a Lie algebra $\mathfrak{g}$ is its unique maximal solvable ideal. A Lie algebra is semisimple precisely when its radical is zero.

# Core Definition

**Proposition 6.23** (Kirillov, p. 71): In any Lie algebra $\mathfrak{g}$, there is a unique solvable ideal which contains any other solvable ideal. This ideal is called the radical of $\mathfrak{g}$ and denoted $\operatorname{rad}(\mathfrak{g})$.

**Theorem 6.24**: The quotient $\mathfrak{g}/\operatorname{rad}(\mathfrak{g})$ is semisimple. Conversely, if $\mathfrak{b}$ is a solvable ideal with $\mathfrak{g}/\mathfrak{b}$ semisimple, then $\mathfrak{b} = \operatorname{rad}(\mathfrak{g})$.

# Prerequisites

- **Solvable Lie algebra** — The radical is defined as the maximal solvable ideal
- **Lie algebra ideal** — The radical is an ideal

# Key Properties

1. $\operatorname{rad}(\mathfrak{g})$ is unique
2. $\operatorname{rad}(\mathfrak{g})$ contains every solvable ideal
3. $\mathfrak{g}/\operatorname{rad}(\mathfrak{g})$ is semisimple
4. $\mathfrak{g}$ is semisimple iff $\operatorname{rad}(\mathfrak{g}) = 0$
5. $\mathfrak{g}$ is solvable iff $\operatorname{rad}(\mathfrak{g}) = \mathfrak{g}$

# Construction / Recognition

## To Find the Radical:
1. Identify all solvable ideals of $\mathfrak{g}$
2. Their sum is $\operatorname{rad}(\mathfrak{g})$ (the sum of solvable ideals is solvable, by Theorem 6.13)
3. Alternatively, use the Killing form: $\operatorname{rad}(\mathfrak{g})$ contains $\operatorname{Ker} K$

# Context & Application

The radical separates the "solvable part" from the "semisimple part" of a Lie algebra. Every Lie algebra fits in an exact sequence $0 \to \operatorname{rad}(\mathfrak{g}) \to \mathfrak{g} \to \mathfrak{g}_{ss} \to 0$ with $\mathfrak{g}_{ss}$ semisimple. The Levi decomposition strengthens this to a semidirect product.

# Examples

**Example 6.26** (p. 72): For the Poincare group $G = SO(3, \mathbb{R}) \ltimes \mathbb{R}^3$, the Lie algebra is $\mathfrak{g} = \mathfrak{so}(3, \mathbb{R}) \oplus \mathbb{R}^3$. Here $\operatorname{rad}(\mathfrak{g}) = \mathbb{R}^3$ (abelian, hence solvable) and $\mathfrak{g}/\operatorname{rad}(\mathfrak{g}) \cong \mathfrak{so}(3, \mathbb{R})$ is semisimple.

# Relationships

## Builds Upon
- **Solvable Lie algebra** — The radical is the maximal solvable ideal

## Enables
- **Semisimple Lie algebra** — Characterized by $\operatorname{rad}(\mathfrak{g}) = 0$
- **Levi decomposition** — Splits $\mathfrak{g}$ as $\operatorname{rad}(\mathfrak{g}) \oplus \mathfrak{g}_{ss}$
- **Reductive Lie algebra** — Characterized by $\operatorname{rad}(\mathfrak{g}) = \mathfrak{z}(\mathfrak{g})$

# Common Confusions

- **Confusion**: Thinking the radical is always zero or all of $\mathfrak{g}$
  **Clarification**: The radical can be any solvable ideal; it measures the "solvable content" of $\mathfrak{g}$

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, pages 71-72. Proposition 6.23, Theorem 6.24.

# Verification Notes

- Definition source: Direct from Proposition 6.23
- Confidence rationale: Explicitly defined with existence and uniqueness proof
- Uncertainties: None
- Cross-reference status: Verified
