---
# === CORE IDENTIFICATION ===
concept: Topology of Classical Groups
slug: classical-groups-topology

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
  - special-linear-group
  - orthogonal-group
  - unitary-group
  - special-unitary-group
  - symplectic-group
  - homotopy-exact-sequence
extends: []
related:
  - spin-group
  - universal-cover-of-lie-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The classical groups have the following topological invariants ($\pi_0 = $ connected components, $\pi_1 = $ fundamental group), which are computed using fiber bundles and the homotopy exact sequence.

# Core Definition

**Tables on pp. 16-17** (Kirillov): For real classical groups:

| $G$ | $\dim$ | $\pi_0$ | $\pi_1$ ($n \geq 3$) |
|---|---|---|---|
| $\mathrm{GL}(n,\mathbb{R})$ | $n^2$ | $\mathbb{Z}_2$ | $\mathbb{Z}_2$ |
| $\mathrm{SL}(n,\mathbb{R})$ | $n^2-1$ | $\{1\}$ | $\mathbb{Z}_2$ |
| $\mathrm{O}(n,\mathbb{R})$ | $n(n-1)/2$ | $\mathbb{Z}_2$ | $\mathbb{Z}_2$ |
| $\mathrm{SO}(n,\mathbb{R})$ | $n(n-1)/2$ | $\{1\}$ | $\mathbb{Z}_2$ |
| $\mathrm{U}(n)$ | $n^2$ | $\{1\}$ | $\mathbb{Z}$ |
| $\mathrm{SU}(n)$ | $n^2-1$ | $\{1\}$ | $\{1\}$ |
| $\mathrm{Sp}(2n,\mathbb{R})$ | $n(2n+1)$ | $\{1\}$ | $\mathbb{Z}$ |

# Prerequisites

- **Classical groups** — the groups being classified
- **Homotopy exact sequence** — the computation tool

# Key Properties

1. $\mathrm{SU}(n)$ is the only simply-connected classical group (for $n \geq 2$).
2. $\mathrm{GL}(n, \mathbb{R})$ and $\mathrm{O}(n, \mathbb{R})$ are not connected ($\pi_0 = \mathbb{Z}_2$).
3. $\mathrm{GL}(n, \mathbb{R})$ is homotopy equivalent to $\mathrm{O}(n, \mathbb{R})$ (Exercise 2.9, Gram-Schmidt).
4. $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}_2$ gives rise to the Spin group.
5. Complex classical groups have different topology: $\mathrm{GL}(n, \mathbb{C})$ is connected; $\mathrm{SL}(n, \mathbb{C})$ is simply connected.

# Construction / Recognition

## To Construct/Create:
Not applicable (a summary table).

## To Identify/Recognize:
1. Reference this table when needing topological data of classical groups.

# Context & Application

These topological invariants determine which classical groups are simply connected (hence have the simplest relationship with their Lie algebra) and which have non-trivial covers.

# Examples

**Example** (Exercise 2.8): $\pi_1(\mathrm{SU}(n))$ is computed inductively using $\mathrm{SU}(n-1) \to \mathrm{SU}(n) \to S^{2n-1}$.

**Example** (Exercise 2.9): $\mathrm{GL}(n, \mathbb{R})/\mathrm{O}(n, \mathbb{R}) \cong$ positive definite upper-triangular matrices (Gram-Schmidt).

# Relationships

## Builds Upon
- **All classical groups** — the groups in the table
- **Homotopy exact sequence** — the computation method

## Enables
- **Spin groups** — universal covers of $\mathrm{SO}(n)$
- **Classification of groups with given algebra** — via $\pi_1$

## Related
- **Universal cover** — determined by $\pi_1$

# Common Errors

- **Error**: Assuming $\pi_1(\mathrm{SO}(2)) = \mathbb{Z}_2$.
  **Correction**: $\mathrm{SO}(2) \cong S^1$, so $\pi_1(\mathrm{SO}(2)) = \mathbb{Z}$. The $\mathbb{Z}_2$ applies for $n \geq 3$.

# Common Confusions

- **Confusion**: Whether real and complex versions have the same topology.
  **Clarification**: No. For example, $\mathrm{GL}(n, \mathbb{R})$ is disconnected but $\mathrm{GL}(n, \mathbb{C})$ is connected.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, tables on pages 16-17.

# Verification Notes

- Definition source: Direct from tables
- Confidence rationale: Explicit tables with exercises for proofs
- Uncertainties: None
- Cross-reference status: Verified with Exercises 2.8, 2.9
