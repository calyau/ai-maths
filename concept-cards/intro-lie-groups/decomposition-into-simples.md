---
# === CORE IDENTIFICATION ===
concept: Decomposition into Simple Algebras
slug: decomposition-into-simples

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
pdf_page: 76
section: "6.7. Properties of semisimple Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - simple-lie-algebra
  - complementary-ideal
extends:
  - complementary-ideal
related:
  - ideal-structure-of-semisimple
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a semisimple Lie algebra decompose?"
  - "What is the relationship between semisimple and simple Lie algebras?"
---

# Quick Definition

A Lie algebra is semisimple if and only if it is a direct sum of simple Lie algebras. This decomposition is unique, and every ideal is a partial sum of the simple summands.

# Core Definition

**Corollary 6.43** (Kirillov, p. 76): A Lie algebra is semisimple iff it is a direct sum of simple Lie algebras.

**Proposition 6.45** (p. 76): If $\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_k$ with $\mathfrak{g}_i$ simple, then any ideal $I$ in $\mathfrak{g}$ has the form $I = \bigoplus_{i \in \mathcal{I}} \mathfrak{g}_i$ for some subset $\mathcal{I} \subset \{1, \ldots, k\}$.

# Prerequisites

- **Semisimple Lie algebra** — The algebra being decomposed
- **Simple Lie algebra** — The building blocks
- **Complementary ideal** — Iterative splitting produces the decomposition

# Key Properties

1. The decomposition is unique (by Proposition 6.45)
2. The summands are ideals, not just subalgebras
3. $[\mathfrak{g}_i, \mathfrak{g}_j] = 0$ for $i \neq j$
4. $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$ (Corollary 6.44)
5. Every ideal and every quotient of a semisimple algebra is semisimple (Corollary 6.46)

# Context & Application

This is the fundamental structure theorem that reduces the study of semisimple algebras to simple algebras. The classification of simple complex Lie algebras (via root systems and Dynkin diagrams) thus gives a complete classification of all semisimple algebras.

# Examples

**Example**: $\mathfrak{so}(4, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C}) \oplus \mathfrak{sl}(2, \mathbb{C})$ — a semisimple algebra decomposing into two simple summands.

# Relationships

## Builds Upon
- **Complementary ideal** — Used iteratively to split

## Enables
- **Classification of semisimple algebras** — Reduces to classifying simple algebras

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, pages 76-77. Corollary 6.43, Corollary 6.44, Proposition 6.45, Corollary 6.46.

# Verification Notes

- Definition source: Direct from Corollary 6.43 and Proposition 6.45
- Confidence rationale: Explicit corollary with proof by induction
- Uncertainties: None
- Cross-reference status: Verified
