---
# === CORE IDENTIFICATION ===
concept: Compact Real Form
slug: compact-real-form

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
pdf_page: 78
section: "6.8. Relation with compact groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "compact form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
  - killing-form
extends: []
related:
  - negative-definite-killing-form
  - complete-reducibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a compact real form of a complex semisimple Lie algebra?"
  - "What distinguishes a compact real form from other real forms?"
---

# Quick Definition

A compact real form of a complex semisimple Lie algebra $\mathfrak{g}$ is a real subalgebra $\mathfrak{k}$ with $\mathfrak{g} = \mathfrak{k} \otimes \mathbb{C}$ that is the Lie algebra of a compact Lie group. It exists for every complex semisimple algebra and is unique up to conjugation.

# Core Definition

**Theorem 6.52** (Kirillov, p. 78): Let $\mathfrak{g}$ be a complex semisimple Lie algebra. Then there exists a real subalgebra $\mathfrak{k}$ such that $\mathfrak{g} = \mathfrak{k} \otimes \mathbb{C}$ and $\mathfrak{k}$ is a Lie algebra of a compact Lie group $K$. The Lie algebra $\mathfrak{k}$ is called the compact real form of $\mathfrak{g}$; it is unique up to conjugation.

If $G$ is a connected complex Lie group with Lie algebra $\mathfrak{g}$, then $K$ can be chosen so that $K \subset G$.

# Prerequisites

- **Semisimple Lie algebra** — The theorem applies to semisimple algebras
- **Killing form** — Compact forms are characterized by negative definite Killing form

# Key Properties

1. The Killing form of $\mathfrak{k}$ is negative definite (Theorem 6.49)
2. $\mathfrak{k}$ is unique up to conjugation by $\operatorname{Aut}(\mathfrak{g})$
3. A semisimple real algebra has negative definite Killing form iff it is compact (Theorem 6.49)
4. Every complex representation of $\mathfrak{g}$ restricts to a unitary representation of $K$

# Context & Application

Compact real forms provide the bridge between the algebraic theory of complex semisimple algebras and the analytic theory of compact groups. Weyl's "unitary trick" uses this correspondence to prove complete reducibility: every representation of $\mathfrak{g}$ is completely reducible because every representation of $K$ is unitary.

# Examples

**Example 6.53** (p. 78): For $\mathfrak{g} = \mathfrak{sl}(n, \mathbb{C})$, $G = SL(n, \mathbb{C})$, the compact form is $\mathfrak{k} = \mathfrak{su}(n)$, $K = SU(n)$.

# Relationships

## Builds Upon
- **Semisimple Lie algebra** — Exists for every such algebra

## Enables
- **Complete reducibility** — Via Weyl's unitary trick

## Related
- **Negative definite Killing form** — Characterizes compact real forms

# Common Confusions

- **Confusion**: Thinking "compact real form" means the algebra itself is compact
  **Clarification**: It means the corresponding Lie group is compact. The algebra is a real form of the complex algebra.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.8, pages 77-78. Theorem 6.49, Theorem 6.52, Example 6.53.

# Verification Notes

- Definition source: Direct from Theorem 6.52
- Confidence rationale: Explicit theorem; proof referenced to other texts
- Uncertainties: Proof not given
- Cross-reference status: Verified
