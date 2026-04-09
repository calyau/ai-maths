---
# === CORE IDENTIFICATION ===
concept: Trace Form
slug: trace-form

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 73
section: "6.5. Invariant bilinear forms and semisimplicity of classical Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "B_V"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invariant-bilinear-form
  - representation-lie-algebra
extends:
  - invariant-bilinear-form
related:
  - killing-form
  - reductive-lie-algebra
contrasts_with:
  - killing-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the trace form associated to a representation?"
  - "How does the trace form detect semisimplicity?"
---

# Quick Definition

The trace form $B_V(x,y) = \operatorname{tr}_V(\rho(x)\rho(y))$ is a symmetric invariant bilinear form on $\mathfrak{g}$ associated to any representation $V$. Non-degeneracy of a trace form implies reductivity.

# Core Definition

**Proposition 6.31** (Kirillov, p. 73): Let $V$ be a representation of $\mathfrak{g}$ and define

$$B_V(x,y) = \operatorname{tr}_V(\rho(x)\rho(y)).$$

Then $B_V$ is a symmetric invariant bilinear form on $\mathfrak{g}$.

**Theorem 6.32**: If $B_V$ is non-degenerate for some representation $V$, then $\mathfrak{g}$ is reductive.

# Prerequisites

- **Invariant bilinear form** — The trace form is a special case
- **Representation of a Lie algebra** — Defined using a representation

# Key Properties

1. $B_V$ is symmetric: $B_V(x,y) = B_V(y,x)$
2. $B_V$ is invariant: $B_V([x,y], z) + B_V(y, [x,z]) = 0$
3. If $0 \to V_1 \to W \to V_2 \to 0$ is exact, then $B_W = B_{V_1} + B_{V_2}$ (Exercise 6.1)
4. Non-degeneracy of $B_V$ implies $[\mathfrak{g}, \operatorname{rad}(\mathfrak{g})] = 0$

# Construction / Recognition

## To Compute:
1. Choose a basis for the representation $V$
2. Write out the matrices $\rho(x_i)$ for a basis of $\mathfrak{g}$
3. Compute $B_V(x_i, x_j) = \operatorname{tr}(\rho(x_i)\rho(x_j))$

# Context & Application

The trace form in the defining representation is often the easiest invariant form to compute for classical Lie algebras. Theorem 6.33 uses trace forms to prove semisimplicity of $\mathfrak{sl}(n)$, $\mathfrak{so}(n)$, $\mathfrak{su}(n)$, $\mathfrak{sp}(2n)$.

# Examples

**Example 6.30** (p. 73): For $\mathfrak{gl}(n, \mathbb{C})$ with the standard representation, $B(x,y) = \operatorname{tr}(xy) = \sum x_{ij}y_{ji}$ is non-degenerate.

**Theorem 6.33** (p. 74): For $\mathfrak{so}(n)$, $B(x,y) = -2\sum_{i>j} x_{ij}y_{ij}$ (non-degenerate). For $\mathfrak{u}(n)$, $B(x,y) = -\sum |x_{ij}|^2$ (negative definite).

# Relationships

## Builds Upon
- **Invariant bilinear form** — The trace form is a construction method

## Enables
- **Reductive Lie algebra** — Non-degeneracy implies reductivity
- **Semisimplicity of classical algebras** — Proved via trace forms

## Contrasts With
- **Killing form** — The Killing form uses the adjoint representation; trace forms can use any representation

# Common Confusions

- **Confusion**: Thinking the trace form and Killing form always coincide
  **Clarification**: For $\mathfrak{sl}(n, \mathbb{C})$, $K(x,y) = 2n \operatorname{tr}(xy)$ while $B_{\text{std}}(x,y) = \operatorname{tr}(xy)$. They differ by a scalar.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.5, pages 73-74. Proposition 6.31, Theorem 6.32, Theorem 6.33.

# Verification Notes

- Definition source: Direct from Proposition 6.31
- Confidence rationale: Explicit definition with applications
- Uncertainties: None
- Cross-reference status: Verified
