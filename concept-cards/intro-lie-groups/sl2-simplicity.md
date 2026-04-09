---
# === CORE IDENTIFICATION ===
concept: Simplicity of sl(2,C)
slug: sl2-simplicity

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
pdf_page: 71
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-lie-algebra
extends: []
related:
  - semisimple-lie-algebra
  - sl2-subalgebra-of-root
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is sl(2,C) simple?"
---

# Quick Definition

$\mathfrak{sl}(2, \mathbb{C})$ is the fundamental example of a simple Lie algebra. The proof uses that $\operatorname{ad} h$ has distinct eigenvalues $2, -2, 0$, so any ideal is spanned by a subset of $\{e, f, h\}$, and any nonzero choice generates all of $\mathfrak{sl}(2, \mathbb{C})$.

# Core Definition

**Example 6.22** (Kirillov, p. 71): $\mathfrak{sl}(2, \mathbb{C})$ is simple. Any ideal must be $\operatorname{ad} h$-invariant, hence spanned by a subset of the eigenvectors $\{e, f, h\}$. If an ideal contains $h$, then $[h,e] = 2e \in I$ and $[h,f] = -2f \in I$, giving $I = \mathfrak{sl}(2)$. Similarly for $e$ or $f$.

# Prerequisites

- **Simple Lie algebra** — $\mathfrak{sl}(2, \mathbb{C})$ is shown to satisfy the definition

# Key Properties

1. This is the only simple Lie algebra of dimension 3
2. The proof technique — using a diagonalizable element with distinct eigenvalues — previews the role of Cartan subalgebras
3. $\mathfrak{sl}(2, \mathbb{C})$ is the building block for all semisimple algebras via $\mathfrak{sl}(2)$ triples

# Relationships

## Illustrates
- **Simple Lie algebra** — The prototypical example

## Enables
- **sl(2) subalgebra of a root** — Every root gives a copy of $\mathfrak{sl}(2)$

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, page 71. Example 6.22.

# Verification Notes

- Definition source: Direct from Example 6.22
- Confidence rationale: Detailed proof by cases
- Uncertainties: None
- Cross-reference status: Verified
