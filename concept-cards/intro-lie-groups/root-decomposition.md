---
# === CORE IDENTIFICATION ===
concept: Root Decomposition
slug: root-decomposition

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
  - "Cartan decomposition"
  - "root space decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
  - killing-form
extends:
  - root-space-decomposition-toroidal
related:
  - root
  - root-subspace
  - root-system-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root decomposition of a semisimple Lie algebra?"
  - "How do I find the root decomposition of a semisimple Lie algebra?"
---

# Quick Definition

The root decomposition is the fundamental structural decomposition $\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in R} \mathfrak{g}_\alpha$ of a semisimple Lie algebra with respect to a Cartan subalgebra. The set $R$ of nonzero weights is the root system, and the $\mathfrak{g}_\alpha$ are root subspaces.

# Core Definition

**Theorem 7.16** (Kirillov, p. 85): Let $\mathfrak{g}$ be a semisimple Lie algebra with Cartan subalgebra $\mathfrak{h}$. Then:

$$\mathfrak{g} = \mathfrak{h} \oplus \bigoplus_{\alpha \in R} \mathfrak{g}_\alpha$$

where $\mathfrak{g}_\alpha = \{x \mid [h, x] = \langle \alpha, h \rangle x \text{ for all } h \in \mathfrak{h}\}$, and $R = \{\alpha \in \mathfrak{h}^* \setminus \{0\} \mid \mathfrak{g}_\alpha \neq 0\}$.

Additionally: $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$; if $\alpha + \beta \neq 0$, then $\mathfrak{g}_\alpha \perp \mathfrak{g}_\beta$; the Killing form pairs $\mathfrak{g}_\alpha \otimes \mathfrak{g}_{-\alpha}$ non-degenerately.

# Prerequisites

- **Cartan subalgebra** — The decomposition is with respect to $\mathfrak{h}$
- **Killing form** — Provides non-degenerate pairing and orthogonality

# Key Properties

1. This is the most important result about semisimple Lie algebras (per Kirillov, p. 85)
2. $\mathfrak{g}_0 = \mathfrak{h}$ by definition of Cartan subalgebra
3. Each $\mathfrak{g}_\alpha$ is one-dimensional (Theorem 7.21, part 2)
4. $R$ spans $\mathfrak{h}^*$ (Theorem 7.21, part 1)
5. Roots come in pairs: $\alpha \in R \implies -\alpha \in R$
6. The Killing form restricted to $\mathfrak{h}$ is non-degenerate, giving an identification $\mathfrak{h} \cong \mathfrak{h}^*$

# Construction / Recognition

## To Find the Root Decomposition:
1. Find a Cartan subalgebra $\mathfrak{h}$ (e.g., maximal set of commuting semisimple elements)
2. Simultaneously diagonalize $\operatorname{ad} h$ for all $h \in \mathfrak{h}$
3. The common eigenvalues $\alpha \in \mathfrak{h}^*$ are the roots
4. The eigenspaces are the root subspaces $\mathfrak{g}_\alpha$

# Context & Application

The root decomposition is the bridge between the abstract theory of semisimple Lie algebras and the combinatorics of root systems. It reduces the structure of the algebra to a finite set of vectors in a Euclidean space, enabling the complete classification via Dynkin diagrams.

Kirillov emphasizes (p. 85): "This decomposition is the most important result one should know about semisimple Lie algebras — much more important than the definition of semisimple algebras."

# Examples

**Example 7.17** (p. 86): For $\mathfrak{sl}(n, \mathbb{C})$ with $\mathfrak{h} = \{\text{diagonal traceless}\}$:
- Functionals $e_i\colon h \mapsto h_i$ satisfy $\sum e_i = 0$
- Roots: $R = \{e_i - e_j \mid i \neq j\}$
- Root subspaces: $\mathfrak{g}_{e_i - e_j} = \mathbb{C} E_{ij}$
- Killing form: $(h, h') = 2n \operatorname{tr}(hh')$

# Relationships

## Builds Upon
- **Cartan subalgebra** — The decomposition is relative to $\mathfrak{h}$
- **Killing form** — Provides orthogonality and non-degeneracy

## Enables
- **Root system of Lie algebra** — $R$ is the root system
- **Root subspace** — The spaces $\mathfrak{g}_\alpha$
- **Classification of semisimple algebras** — Via root systems and Dynkin diagrams

# Common Errors

- **Error**: Forgetting that $\mathfrak{g}_0 = \mathfrak{h}$, not a root subspace
  **Correction**: The zero weight space is $\mathfrak{h}$ itself; $R$ excludes $\alpha = 0$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.3, pages 85-86. Theorem 7.16, Example 7.17.

# Verification Notes

- Definition source: Direct from Theorem 7.16
- Confidence rationale: Central theorem, explicitly marked as most important result
- Uncertainties: None
- Cross-reference status: Verified
