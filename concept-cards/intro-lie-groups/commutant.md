---
# === CORE IDENTIFICATION ===
concept: Commutant
slug: commutant

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
section: "6.1. Ideals and commutant"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "derived subalgebra"
  - "[g,g]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - derived-series
  - solvable-lie-algebra
  - abelian-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the commutant of a Lie algebra?"
  - "How does the commutant measure non-commutativity?"
---

# Quick Definition

The commutant of a Lie algebra $\mathfrak{g}$ is the ideal $[\mathfrak{g}, \mathfrak{g}]$, i.e., the subspace spanned by all brackets $[x, y]$ for $x, y \in \mathfrak{g}$. It measures how far $\mathfrak{g}$ is from being abelian.

# Core Definition

**Definition 6.3** (Kirillov, p. 67): The commutant of a Lie algebra $\mathfrak{g}$ is the ideal $[\mathfrak{g}, \mathfrak{g}]$.

The quotient $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is an abelian Lie algebra, and $[\mathfrak{g}, \mathfrak{g}]$ is the smallest ideal with this property: if $\mathfrak{g}/I$ is abelian for some ideal $I \subset \mathfrak{g}$, then $I \supset [\mathfrak{g}, \mathfrak{g}]$ (Lemma 6.4).

# Prerequisites

- **Lie algebra** — The commutant is defined for any Lie algebra
- **Lie algebra ideal** — The commutant is itself an ideal, and the definition involves quotients by ideals

# Key Properties

1. $[\mathfrak{g}, \mathfrak{g}]$ is an ideal in $\mathfrak{g}$
2. $\mathfrak{g}/[\mathfrak{g}, \mathfrak{g}]$ is abelian
3. $[\mathfrak{g}, \mathfrak{g}]$ is the smallest ideal with abelian quotient
4. For a commutative $\mathfrak{g}$, $[\mathfrak{g}, \mathfrak{g}] = 0$
5. For a semisimple $\mathfrak{g}$, $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$ (Corollary 6.44)

# Construction / Recognition

## To Compute the Commutant:
1. Take all pairs $x, y \in \mathfrak{g}$
2. Compute all brackets $[x, y]$
3. The commutant is the span of all such brackets

## To Recognize:
1. If given an ideal $I$, check whether $\mathfrak{g}/I$ is abelian
2. If so, $I \supset [\mathfrak{g}, \mathfrak{g}]$
3. $I = [\mathfrak{g}, \mathfrak{g}]$ iff $I$ is the smallest such ideal

# Context & Application

The commutant is the starting point for measuring "how far" a Lie algebra is from being commutative. The smaller $[\mathfrak{g}, \mathfrak{g}]$ is, the closer $\mathfrak{g}$ is to being abelian. This leads directly to the derived series and the definition of solvable Lie algebras.

# Examples

**Example 6.5** (p. 67): $[\mathfrak{gl}(n, \mathbb{K}), \mathfrak{gl}(n, \mathbb{K})] = \mathfrak{sl}(n, \mathbb{K})$. Indeed, for any $z = [x, y]$ we have $\operatorname{tr} z = 0$. Conversely, $E_{ii} - E_{jj} = [E_{ij}, E_{ji}]$ and $2E_{ij} = [E_{ii} - E_{jj}, E_{ij}]$ for $i \neq j$, showing all traceless matrices lie in the commutant.

# Relationships

## Builds Upon
- **Lie algebra** — Defined for any Lie algebra
- **Lie algebra ideal** — The commutant is an ideal

## Enables
- **Derived series** — Iterated commutants define the derived series
- **Solvable Lie algebra** — Defined by vanishing of the derived series

## Related
- **Abelian Lie algebra** — The commutant is zero iff the algebra is abelian

# Common Errors

- **Error**: Assuming $[\mathfrak{g}, \mathfrak{g}]$ consists only of single brackets $[x, y]$
  **Correction**: It is the *span* of all brackets; a general element is a sum $\sum [x_i, y_i]$

# Common Confusions

- **Confusion**: Confusing the commutant $[\mathfrak{g}, \mathfrak{g}]$ with the center $\mathfrak{z}(\mathfrak{g})$
  **Clarification**: The center consists of elements that commute with everything; the commutant is the span of all commutators. They measure complementary aspects of non-commutativity.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.1, pages 67-67. Definition 6.3, Lemma 6.4, Example 6.5.

# Verification Notes

- Definition source: Direct from Definition 6.3
- Confidence rationale: Explicitly defined in source with clear terminology
- Uncertainties: None
- Cross-reference status: Slugs refer to planned cards from earlier chapters
