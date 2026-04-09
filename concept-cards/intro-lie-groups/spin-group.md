---
# === CORE IDENTIFICATION ===
concept: Spin Group
slug: spin-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 17
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{Spin}(n)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-orthogonal-group
  - universal-cover-of-lie-group
extends:
  - special-orthogonal-group
related:
  - special-unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The spin group $\mathrm{Spin}(n)$ is the universal cover of $\mathrm{SO}(n, \mathbb{R})$ for $n \geq 3$. Since $\pi_1(\mathrm{SO}(n, \mathbb{R})) = \mathbb{Z}_2$, it is a twofold cover.

# Core Definition

(Kirillov, p. 17): The universal cover of $\mathrm{SO}(n, \mathbb{R})$ is called the spin group and is denoted $\mathrm{Spin}(n)$; since $\pi_1(\mathrm{SO}(n, \mathbb{R})) = \mathbb{Z}_2$, this is a twofold cover.

# Prerequisites

- **Special orthogonal group** — the group being covered
- **Universal cover of a Lie group** — the construction used

# Key Properties

1. $\mathrm{Spin}(n) \to \mathrm{SO}(n, \mathbb{R})$ is a 2:1 cover.
2. $\mathrm{Spin}(n)$ is simply connected.
3. $\mathrm{Lie}(\mathrm{Spin}(n)) = \mathfrak{so}(n, \mathbb{R})$.
4. $\mathrm{Spin}(3) \cong \mathrm{SU}(2) \cong S^3$.

# Construction / Recognition

## To Construct/Create:
1. Take the universal cover of $\mathrm{SO}(n, \mathbb{R})$.
2. Alternatively, construct via Clifford algebras (not covered in this text).

## To Identify/Recognize:
1. A simply-connected compact Lie group with Lie algebra $\mathfrak{so}(n)$.

# Context & Application

Spin groups are essential in physics (spinors, quantum mechanics) and in topology (spin structures on manifolds). $\mathrm{Spin}(3) \cong \mathrm{SU}(2)$ underlies the distinction between integer and half-integer angular momentum in quantum mechanics.

# Examples

**Example** (pp. 18-19): $\mathrm{Spin}(3) \cong \mathrm{SU}(2)$. The double cover $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$ is constructed via the adjoint action (Exercise 2.12).

# Relationships

## Builds Upon
- **Special orthogonal group** — $\mathrm{Spin}(n)$ is its universal cover
- **Universal cover of a Lie group** — the construction

## Enables
- **Spinor representations** — representations of $\mathrm{Spin}(n)$ that do not factor through $\mathrm{SO}(n)$

## Related
- **$\mathrm{SU}(2)$** — isomorphic to $\mathrm{Spin}(3)$

# Common Errors

- **Error**: Thinking $\mathrm{Spin}(n)$ is a subgroup of $\mathrm{GL}(n)$.
  **Correction**: $\mathrm{Spin}(n)$ naturally lives in the Clifford algebra $\mathrm{Cl}(n)$, not in $\mathrm{GL}(n)$.

# Common Confusions

- **Confusion**: Whether $\mathrm{Spin}(n)$ and $\mathrm{SO}(n)$ have the same representations.
  **Clarification**: No. $\mathrm{Spin}(n)$ has additional "spinor" representations that do not descend to $\mathrm{SO}(n)$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, page 17.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Brief mention in source; full construction not given
- Uncertainties: Construction details not provided in the text
- Cross-reference status: Verified with Exercises 2.12-2.14
