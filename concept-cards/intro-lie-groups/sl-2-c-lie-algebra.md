---
# === CORE IDENTIFICATION ===
concept: "Lie Algebra $\\mathfrak{sl}(2, \\mathbb{C})$"
slug: sl-2-c-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: examples
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 35
section: "3.10"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{sl}(2, \\mathbb{C})$"
  - "$\\mathfrak{sl}_2$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-linear-group
  - lie-algebra
extends: []
related:
  - su-2-lie-algebra
  - so-3-r-lie-algebra
  - complexification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

$\mathfrak{sl}(2, \mathbb{C})$ is the 3-dimensional complex Lie algebra of traceless $2 \times 2$ matrices, with standard basis $e, f, h$ satisfying $[e, f] = h$, $[h, e] = 2e$, $[h, f] = -2f$.

# Core Definition

**Equation (3.20)** (Kirillov): The standard basis of $\mathfrak{sl}(2, \mathbb{C})$ is:
$$e = \begin{pmatrix}0&1\\0&0\end{pmatrix}, \quad f = \begin{pmatrix}0&0\\1&0\end{pmatrix}, \quad h = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

Commutation relations (equation 3.21): $[e, f] = h$, $[h, e] = 2e$, $[h, f] = -2f$.

# Prerequisites

- **Special linear group** — $\mathfrak{sl}(2, \mathbb{C}) = \mathrm{Lie}(\mathrm{SL}(2, \mathbb{C}))$
- **Lie algebra** — abstract definition

# Key Properties

1. $\dim_\mathbb{C} \mathfrak{sl}(2, \mathbb{C}) = 3$.
2. $\mathfrak{sl}(2, \mathbb{C}) = \mathfrak{su}(2)_\mathbb{C} = \mathfrak{so}(3, \mathbb{R})_\mathbb{C}$.
3. Invariant form: $(h, h) = -2$, $(e, f) = (f, e) = -1$, all others zero.
4. $h$ spans a Cartan subalgebra; $e, f$ are root vectors.
5. The relation $[h, e] = 2e$ says $e$ is an eigenvector of $\mathrm{ad}\, h$ with eigenvalue $2$.

# Construction / Recognition

## To Construct/Create:
1. Take $2 \times 2$ complex traceless matrices.
2. Choose the standard basis $e, f, h$.

## To Identify/Recognize:
1. A 3-dimensional complex Lie algebra with generators $e, f, h$ satisfying $[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$.

# Context & Application

$\mathfrak{sl}(2, \mathbb{C})$ is the most important low-dimensional Lie algebra. Its representation theory is the foundation for the representation theory of all semisimple Lie algebras. The structure $e, f, h$ (an "$\mathfrak{sl}_2$-triple") appears throughout Lie theory.

# Examples

**Example** (p. 35, eq. 3.23): The inclusion $\mathfrak{su}(2) \hookrightarrow \mathfrak{sl}(2, \mathbb{C})$ is:
$i\sigma_1 \mapsto e - f$, $i\sigma_2 \mapsto i(e+f)$, $i\sigma_3 \mapsto ih$.

**Example** (p. 35, eq. 3.24): The isomorphism $\mathfrak{so}(3, \mathbb{C}) \xrightarrow{\sim} \mathfrak{sl}(2, \mathbb{C})$:
$J_x \mapsto \frac{1}{2}(e-f)$, $J_y \mapsto \frac{i}{2}(e+f)$, $J_z \mapsto \frac{ih}{2}$.

# Relationships

## Builds Upon
- **Special linear group** — $\mathfrak{sl}(2, \mathbb{C}) = \mathrm{Lie}(\mathrm{SL}(2, \mathbb{C}))$

## Enables
- **Representation theory** — $\mathfrak{sl}(2)$ reps are the building blocks (Chapter 4+)
- **Root system theory** — $\mathfrak{sl}_2$-triples appear in all semisimple algebras

## Related
- **$\mathfrak{su}(2)$** — compact real form
- **$\mathfrak{so}(3, \mathbb{R})$** — another real form (via complexification)

# Common Errors

- **Error**: Confusing the real algebra $\mathfrak{sl}(2, \mathbb{R})$ with the complex algebra $\mathfrak{sl}(2, \mathbb{C})$.
  **Correction**: $\mathfrak{sl}(2, \mathbb{R})$ is a 3-dimensional real algebra (non-compact real form); $\mathfrak{sl}(2, \mathbb{C})$ is 3-dimensional over $\mathbb{C}$.

# Common Confusions

- **Confusion**: Whether the standard basis $e, f, h$ is the "same" as the Pauli basis $i\sigma_k$.
  **Clarification**: They are related by the change of basis in equation (3.23), but they are different bases serving different purposes.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.10, equations (3.20)-(3.24), pages 35.

# Verification Notes

- Definition source: Direct from equations (3.20)-(3.21)
- Confidence rationale: Explicit basis and relations
- Uncertainties: None
- Cross-reference status: Verified with isomorphism maps (3.23)-(3.24)
