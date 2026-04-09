---
# === CORE IDENTIFICATION ===
concept: Root Decomposition of sl(n,C)
slug: sln-root-decomposition

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 86
section: "7.3. Root decomposition and root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "type A root system"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - cartan-subalgebra
extends: []
related:
  - root-system-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root decomposition of sl(n,C)?"
  - "What does the root system of type A look like concretely?"
---

# Quick Definition

For $\mathfrak{sl}(n, \mathbb{C})$ with Cartan subalgebra $\mathfrak{h} = \{\text{diagonal traceless matrices}\}$, the roots are $R = \{e_i - e_j \mid i \neq j\}$ and the root subspaces are $\mathfrak{g}_{e_i - e_j} = \mathbb{C} E_{ij}$. This is the root system of type $A_{n-1}$.

# Core Definition

**Example 7.17** (Kirillov, p. 86): Let $\mathfrak{g} = \mathfrak{sl}(n, \mathbb{C})$, $\mathfrak{h} = \{\text{diagonal matrices with trace } 0\}$. Define $e_i\colon \mathfrak{h} \to \mathbb{C}$ by $e_i(h) = h_i$. Then $\sum e_i = 0$, $\mathfrak{h}^* = \bigoplus \mathbb{C}e_i / \mathbb{C}(e_1 + \cdots + e_n)$.

The matrix units $E_{ij}$ are eigenvectors: $[h, E_{ij}] = (h_i - h_j)E_{ij} = (e_i - e_j)(h) E_{ij}$.

Root decomposition: $R = \{e_i - e_j \mid i \neq j\}$, $\mathfrak{g}_{e_i - e_j} = \mathbb{C} E_{ij}$.

Killing form on $\mathfrak{h}$: $(h, h') = 2n \operatorname{tr}(hh')$. On $\mathfrak{h}^*$: $(\lambda, \mu) = \frac{1}{2n}\sum_i \lambda_i \mu_i$.

# Prerequisites

- **Root decomposition** — This is a specific instance
- **Cartan subalgebra** — $\mathfrak{h}$ is the standard one

# Key Properties

1. There are $n(n-1)$ roots (the type $A_{n-1}$ root system)
2. Rank = $n - 1$
3. Each root space is spanned by a single matrix unit
4. Positive roots: $\{e_i - e_j \mid i < j\}$ (the standard choice)

# Context & Application

This is the prototypical example of a root decomposition. It makes all abstract concepts concrete and is the most frequently used example throughout the theory.

# Relationships

## Builds Upon
- **Root decomposition** — Specific instance

## Related
- **Root system type A** — This is the $A_{n-1}$ root system

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, page 86. Example 7.17.

# Verification Notes

- Definition source: Direct from Example 7.17
- Confidence rationale: Detailed worked example
- Uncertainties: None
- Cross-reference status: Verified
