---
# === CORE IDENTIFICATION ===
concept: Root
slug: root

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - cartan-subalgebra
extends: []
related:
  - root-subspace
  - root-system-of-lie-algebra
  - coroot-of-lie-algebra
contrasts_with:
  - weight-of-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a root of a semisimple Lie algebra?"
---

# Quick Definition

A root is a nonzero element $\alpha \in \mathfrak{h}^*$ such that the root subspace $\mathfrak{g}_\alpha = \{x \mid [h, x] = \langle \alpha, h \rangle x\}$ is nonzero. Roots are the eigenvalues of the adjoint representation restricted to the Cartan subalgebra.

# Core Definition

From **Theorem 7.16** (Kirillov, p. 85): The set $R = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$ is called the root system of $\mathfrak{g}$, and elements $\alpha \in R$ are called roots.

# Prerequisites

- **Root decomposition** — Roots are defined by the root decomposition
- **Cartan subalgebra** — Roots are elements of $\mathfrak{h}^*$

# Key Properties

1. $R$ is a finite subset of $\mathfrak{h}^*$
2. $R$ spans $\mathfrak{h}^*$ (Theorem 7.21)
3. If $\alpha \in R$, then $-\alpha \in R$
4. If $\alpha \in R$, the only multiples of $\alpha$ in $R$ are $\pm\alpha$ (Theorem 7.21)
5. Each root subspace $\mathfrak{g}_\alpha$ is one-dimensional (Theorem 7.21)
6. $\langle h_\alpha, \beta \rangle \in \mathbb{Z}$ for all roots $\alpha, \beta$ (Theorem 7.21)

# Context & Application

Roots are the fundamental combinatorial data of a semisimple Lie algebra. They encode the bracket structure: $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$. The root system $R$ determines the algebra up to isomorphism.

# Examples

**Example 7.17** (p. 86): For $\mathfrak{sl}(n, \mathbb{C})$: $R = \{e_i - e_j \mid i \neq j\}$, where $e_i$ extracts the $i$-th diagonal entry. This gives $n(n-1)$ roots.

# Relationships

## Builds Upon
- **Root decomposition** — Roots come from this decomposition

## Enables
- **Root system of Lie algebra** — The set $R$ with its properties
- **sl(2) subalgebra** — Each root gives an $\mathfrak{sl}(2)$ copy

## Contrasts With
- **Weight of representation** — Roots are weights of the adjoint representation; general weights are eigenvalues in other representations

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 85-89. Theorem 7.16, Theorem 7.21.

# Verification Notes

- Definition source: Direct from Theorem 7.16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
