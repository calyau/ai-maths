---
# === CORE IDENTIFICATION ===
concept: Nilpotent Element
slug: nilpotent-element

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
pdf_page: 82
section: "7.1. Semisimple elements and toroidal subalgebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
extends: []
related:
  - semisimple-element
  - jordan-decomposition-lie-algebras
contrasts_with:
  - semisimple-element

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a nilpotent element of a Lie algebra?"
---

# Quick Definition

An element $x \in \mathfrak{g}$ is nilpotent if $\operatorname{ad} x\colon \mathfrak{g} \to \mathfrak{g}$ is a nilpotent operator, meaning $(\operatorname{ad} x)^n = 0$ for some $n$. In a semisimple algebra, every element has a unique decomposition into semisimple and nilpotent parts.

# Core Definition

**Definition 7.1** (Kirillov, p. 82): An element $x \in \mathfrak{g}$ is called nilpotent if $\operatorname{ad} x$ is a nilpotent operator $\mathfrak{g} \to \mathfrak{g}$.

# Prerequisites

- **Semisimple Lie algebra** — Used primarily in this context

# Key Properties

1. If the only semisimple elements are zero, the algebra is nilpotent (contradicting semisimplicity)
2. Every element decomposes as $x = x_s + x_n$ (Jordan decomposition)
3. For $\mathfrak{gl}(n)$, nilpotent elements are precisely the nilpotent matrices

# Context & Application

Nilpotent elements form the root spaces $\mathfrak{g}_\alpha$ for $\alpha \neq 0$. The generators $e_\alpha \in \mathfrak{g}_\alpha$ and $f_\alpha \in \mathfrak{g}_{-\alpha}$ are nilpotent, while $h_\alpha \in \mathfrak{h}$ is semisimple.

# Examples

**Example**: In $\mathfrak{sl}(2, \mathbb{C})$, the elements $e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ are nilpotent.

# Relationships

## Related
- **Jordan decomposition in Lie algebras** — Provides the unique decomposition $x = x_s + x_n$

## Contrasts With
- **Semisimple element** — Diagonalizable vs. nilpotent adjoint action

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, page 82. Definition 7.1.

# Verification Notes

- Definition source: Direct from Definition 7.1
- Confidence rationale: Explicitly defined alongside semisimple element
- Uncertainties: None
- Cross-reference status: Verified
