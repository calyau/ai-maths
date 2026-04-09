---
# === CORE IDENTIFICATION ===
concept: Orthogonal Group
slug: orthogonal-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 16
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{O}(n, \\mathbb{K})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends:
  - general-linear-group
related:
  - special-orthogonal-group
  - so-n-lie-algebra
contrasts_with:
  - unitary-group
  - symplectic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{O}(n, \mathbb{K}) = \{A \in \mathrm{GL}(n, \mathbb{K}) \mid AA^t = I\}$ is the group of orthogonal matrices. Its Lie algebra is $\mathfrak{o}(n, \mathbb{K}) = \{x \mid x + x^t = 0\}$, the skew-symmetric matrices.

# Core Definition

**Theorem 2.29** (Kirillov): $\exp(x) \in \mathrm{O}(n, \mathbb{K})$ iff $x + x^t = 0$. Thus $\mathfrak{o}(n, \mathbb{K}) = \{x \in \mathfrak{gl}(n, \mathbb{K}) \mid x + x^t = 0\}$.

# Prerequisites

- **General linear group** — $\mathrm{O}(n) \subset \mathrm{GL}(n)$

# Key Properties

1. $\dim \mathrm{O}(n, \mathbb{K}) = n(n-1)/2$.
2. $\pi_0(\mathrm{O}(n, \mathbb{R})) = \mathbb{Z}_2$ (components with $\det = \pm 1$).
3. $\pi_1(\mathrm{O}(n, \mathbb{R})) = \mathbb{Z}_2$ for $n \geq 3$.
4. $\mathrm{O}(n)$ and $\mathrm{SO}(n)$ have the same Lie algebra since $\mathrm{SO}(n)$ is the identity component.

# Construction / Recognition

## To Construct/Create:
1. Take all $n \times n$ matrices satisfying $AA^t = I$.
2. Equivalently: matrices preserving the standard inner product on $\mathbb{K}^n$.

## To Identify/Recognize:
1. Matrices whose columns (or rows) form an orthonormal basis.

# Context & Application

$\mathrm{O}(n)$ is the symmetry group of the Euclidean inner product. It is compact and plays a central role in the topology of other classical groups (e.g., $\mathrm{GL}(n, \mathbb{R})$ is homotopy equivalent to $\mathrm{O}(n, \mathbb{R})$, Exercise 2.9).

# Examples

**Example** (p. 16): The condition $x + x^t = 0$ implies diagonal entries are zero, so $\mathrm{tr}(x) = 0$ automatically. Hence $\mathfrak{o}(n) = \mathfrak{so}(n)$.

**Example** (p. 12): $\mathrm{SO}(n, \mathbb{R})$ acts transitively on $S^{n-1}$, giving the fiber bundle $\mathrm{SO}(n-1) \to \mathrm{SO}(n) \to S^{n-1}$.

# Relationships

## Builds Upon
- **General linear group** — $\mathrm{O}(n) \subset \mathrm{GL}(n)$

## Enables
- **Special orthogonal group** — connected component of identity
- **Spin group** — universal cover of $\mathrm{SO}(n)$

## Related
- **$\mathfrak{so}(n)$ Lie algebra** — skew-symmetric matrices

## Contrasts With
- **Unitary group** — preserves Hermitian form instead of symmetric bilinear form
- **Symplectic group** — preserves skew-symmetric bilinear form

# Common Errors

- **Error**: Thinking $\mathrm{O}(n)$ and $\mathrm{SO}(n)$ have different Lie algebras.
  **Correction**: They have the same Lie algebra because $\mathrm{SO}(n)$ is the identity component of $\mathrm{O}(n)$.

# Common Confusions

- **Confusion**: Whether $\mathrm{O}(n, \mathbb{C})$ is compact.
  **Clarification**: $\mathrm{O}(n, \mathbb{R})$ is compact, but $\mathrm{O}(n, \mathbb{C})$ is not.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, page 16. Tables on pp. 16-17.

# Verification Notes

- Definition source: Direct from Theorem 2.29
- Confidence rationale: Explicit computation in source
- Uncertainties: None
- Cross-reference status: Verified with tables
