---
# === CORE IDENTIFICATION ===
concept: Ideal Structure of Semisimple Algebras
slug: ideal-structure-of-semisimple

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
  - decomposition-into-simples
extends:
  - decomposition-into-simples
related:
  - simple-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the ideals of a semisimple Lie algebra?"
---

# Quick Definition

Every ideal in a semisimple Lie algebra $\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_k$ (with $\mathfrak{g}_i$ simple) is a partial direct sum $\bigoplus_{i \in \mathcal{I}} \mathfrak{g}_i$. Every ideal and quotient of a semisimple algebra is semisimple.

# Core Definition

**Proposition 6.45** (Kirillov, p. 76): Let $\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_k$ with $\mathfrak{g}_i$ simple. Then any ideal $I$ in $\mathfrak{g}$ is of the form $I = \bigoplus_{i \in \mathcal{I}} \mathfrak{g}_i$ for some $\mathcal{I} \subset \{1, \ldots, k\}$.

**Corollary 6.46**: Any ideal in a semisimple Lie algebra is semisimple. Any quotient of a semisimple algebra is semisimple.

# Prerequisites

- **Decomposition into simples** — The algebra must be decomposed first

# Key Properties

1. This is not just "up to isomorphism" — $I$ is literally equal to such a partial sum as a subspace
2. The proof uses induction on $k$ and the fact that simple algebras have no proper ideals
3. In particular, a semisimple algebra has only finitely many ideals

# Context & Application

This rigid ideal structure explains why semisimple algebras are so well-behaved: their ideals are completely determined by the simple decomposition.

# Examples

**Example**: For $\mathfrak{g} = \mathfrak{sl}(2) \oplus \mathfrak{sl}(3) \oplus \mathfrak{sl}(5)$, the ideals are: $0$, $\mathfrak{sl}(2)$, $\mathfrak{sl}(3)$, $\mathfrak{sl}(5)$, $\mathfrak{sl}(2) \oplus \mathfrak{sl}(3)$, $\mathfrak{sl}(2) \oplus \mathfrak{sl}(5)$, $\mathfrak{sl}(3) \oplus \mathfrak{sl}(5)$, and $\mathfrak{g}$ itself — exactly $2^3 = 8$ ideals.

# Relationships

## Builds Upon
- **Decomposition into simples** — The ideals are partial sums of the simple factors

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.7, pages 76-77. Proposition 6.45, Corollary 6.46.

# Verification Notes

- Definition source: Direct from Proposition 6.45
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
