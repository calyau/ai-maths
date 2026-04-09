---
# === CORE IDENTIFICATION ===
concept: "Isomorphisms: $\\mathfrak{so}(3) \\cong \\mathfrak{su}(2)$ and $\\mathfrak{su}(2)_\\mathbb{C} \\cong \\mathfrak{sl}(2, \\mathbb{C})$"
slug: isomorphism-so3-su2-sl2

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - so-3-r-lie-algebra
  - su-2-lie-algebra
  - sl-2-c-lie-algebra
  - complexification
extends: []
related:
  - spin-group
  - compact-real-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

$\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$ as real Lie algebras, and $\mathfrak{su}(2)_\mathbb{C} \cong \mathfrak{so}(3, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C})$ as complex Lie algebras. These isomorphisms connect three fundamental low-dimensional Lie algebras.

# Core Definition

**Section 3.10** (Kirillov):

Isomorphism $\mathfrak{su}(2) \xrightarrow{\sim} \mathfrak{so}(3, \mathbb{R})$:
$$i\sigma_1 \mapsto 2J_x, \quad i\sigma_2 \mapsto 2J_y, \quad i\sigma_3 \mapsto 2J_z$$

This lifts to a morphism $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$, a twofold cover.

Complexification $\mathfrak{su}(2) \hookrightarrow \mathfrak{sl}(2, \mathbb{C})$ (eq. 3.23):
$$i\sigma_1 \mapsto e - f, \quad i\sigma_2 \mapsto i(e+f), \quad i\sigma_3 \mapsto ih$$

Combined: $\mathfrak{so}(3, \mathbb{R})_\mathbb{C} = \mathfrak{so}(3, \mathbb{C}) \xrightarrow{\sim} \mathfrak{sl}(2, \mathbb{C})$ (eq. 3.24).

# Prerequisites

- **$\mathfrak{so}(3, \mathbb{R})$** — one of the algebras
- **$\mathfrak{su}(2)$** — another
- **$\mathfrak{sl}(2, \mathbb{C})$** — the complexification
- **Complexification** — the operation connecting real and complex algebras

# Key Properties

1. The real isomorphism $\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$ scales the generators by 2.
2. The group-level map $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$ is a 2:1 cover (not an isomorphism).
3. The invariant bilinear forms are compatible: $(J_k, J_k) = 2$ in $\mathfrak{so}(3)$; $(i\sigma_k, i\sigma_k) = 2$ in $\mathfrak{su}(2)$.

# Construction / Recognition

## To Construct/Create:
1. Match generators with proportional commutation relations.
2. The factor of 2 comes from $[i\sigma_1, i\sigma_2] = 2i\sigma_3$ vs $[J_x, J_y] = J_z$.

## To Identify/Recognize:
1. Any 3-dimensional Lie algebra with bracket $[e_i, e_j] = c \cdot \epsilon_{ijk} e_k$ is isomorphic to $\mathfrak{so}(3)$ (up to scaling).

# Context & Application

These isomorphisms are the simplest non-trivial examples of the general theory. They connect rotation groups in physics ($\mathrm{SO}(3)$), quantum spin ($\mathrm{SU}(2)$), and the algebraic theory ($\mathfrak{sl}(2, \mathbb{C})$).

# Examples

**Example** (Section 3.10): The complete chain: $\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$, with complexifications $\mathfrak{su}(2)_\mathbb{C} = \mathfrak{sl}(2, \mathbb{C}) = \mathfrak{so}(3, \mathbb{C})$.

At the group level: $\mathrm{SU}(2) \xrightarrow{2:1} \mathrm{SO}(3, \mathbb{R})$ and $\mathrm{SU}(2) \subset \mathrm{SL}(2, \mathbb{C})$ as compact real form.

# Relationships

## Builds Upon
- **$\mathfrak{so}(3, \mathbb{R})$**, **$\mathfrak{su}(2)$**, **$\mathfrak{sl}(2, \mathbb{C})$** — the three algebras

## Enables
- **Representation theory starting point** — all three give the same complex representations

## Related
- **Spin group** — $\mathrm{Spin}(3) \cong \mathrm{SU}(2)$ is the group-level statement

# Common Errors

- **Error**: Claiming $\mathrm{SU}(2) \cong \mathrm{SO}(3)$ as groups.
  **Correction**: Only the Lie algebras are isomorphic. The groups are related by a 2:1 cover.

# Common Confusions

- **Confusion**: Whether the isomorphism $\mathfrak{so}(3) \cong \mathfrak{su}(2)$ generalizes to higher dimensions.
  **Clarification**: No. For $n > 3$, $\dim \mathfrak{so}(n) = n(n-1)/2$ while $\dim \mathfrak{su}(n) = n^2 - 1$, so they cannot be isomorphic.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.10, "Isomorphisms" subsection, pages 35.

# Verification Notes

- Definition source: Direct from Section 3.10
- Confidence rationale: Explicit isomorphisms with change-of-basis formulas
- Uncertainties: None
- Cross-reference status: Verified with Exercises 2.12-2.14
