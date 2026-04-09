---
# === CORE IDENTIFICATION ===
concept: Root System of a Lie Algebra
slug: root-system-of-lie-algebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 85
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "R"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - root
extends: []
related:
  - abstract-root-system
  - root-system-axioms
  - killing-form-on-h
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root system of a semisimple Lie algebra?"
  - "How does the root system determine the Lie algebra?"
---

# Quick Definition

The root system $R$ of a semisimple Lie algebra $\mathfrak{g}$ (with Cartan subalgebra $\mathfrak{h}$) is the finite set of nonzero linear functionals $\alpha \in \mathfrak{h}^*$ for which $\mathfrak{g}_\alpha \neq 0$. It satisfies the axioms of an abstract root system and determines $\mathfrak{g}$ up to isomorphism.

# Core Definition

From **Theorem 7.16** (Kirillov, p. 85): $R = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$ is the root system.

**Theorem 7.21** (p. 87) establishes that $R$ satisfies:
1. $R$ spans $\mathfrak{h}^*$
2. $\langle h_\alpha, \beta \rangle = \frac{2(\alpha, \beta)}{(\alpha, \alpha)} \in \mathbb{Z}$ for all $\alpha, \beta \in R$
3. $s_\alpha(\beta) = \beta - \langle h_\alpha, \beta \rangle \alpha \in R$ for all $\alpha, \beta \in R$
4. The only multiples of $\alpha$ in $R$ are $\pm\alpha$

# Prerequisites

- **Root decomposition** — The root system emerges from this decomposition
- **Root** — The elements of $R$

# Key Properties

1. $R$ is finite (since $\mathfrak{g}$ is finite-dimensional)
2. $R$ lives in $\mathfrak{h}_{\mathbb{R}}^*$, a real form of $\mathfrak{h}^*$ (Theorem 7.22)
3. The Killing form restricted to $\mathfrak{h}_{\mathbb{R}}$ is positive definite (Theorem 7.22)
4. $R$ is independent of the choice of $\mathfrak{h}$ (up to isomorphism, by Cartan conjugacy)
5. $R$ determines $\mathfrak{g}$ up to isomorphism

# Context & Application

The root system is the key to classifying semisimple Lie algebras. It reduces an infinite-dimensional algebraic problem (classifying algebras) to a finite combinatorial problem (classifying root systems). Root systems are classified by Dynkin diagrams.

# Examples

**Example 7.17** (p. 86): For $\mathfrak{sl}(n, \mathbb{C})$: $R = \{e_i - e_j \mid i \neq j\} \subset \mathfrak{h}^*$. This is the root system of type $A_{n-1}$.

# Relationships

## Builds Upon
- **Root decomposition** — $R$ is extracted from this decomposition

## Enables
- **Abstract root system** — $R$ satisfies the axioms
- **Classification of semisimple algebras** — Via Dynkin diagrams

## Related
- **Killing form on $\mathfrak{h}$** — Gives the inner product $(\alpha, \beta)$ on roots

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 85-89. Theorems 7.16, 7.21, 7.22.

# Verification Notes

- Definition source: Direct from Theorem 7.16
- Confidence rationale: Central definition, axioms proved in Theorem 7.21
- Uncertainties: None
- Cross-reference status: Verified
