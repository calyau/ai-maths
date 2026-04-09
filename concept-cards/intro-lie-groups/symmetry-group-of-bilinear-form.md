---
# === CORE IDENTIFICATION ===
concept: Symmetry Group of a Bilinear Form
slug: symmetry-group-of-bilinear-form

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 28
section: "3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{O}(V, B)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - stabilizer-lie-algebra
  - representation-of-lie-group
extends:
  - stabilizer-subgroup
related:
  - orthogonal-group
  - symplectic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the Lie algebra of a matrix Lie group?"
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The symmetry group $\mathrm{O}(V, B) = \{g \in \mathrm{GL}(V) \mid B(gv, gw) = B(v, w)\}$ of a bilinear form $B$ is a Lie group with Lie algebra $\mathfrak{o}(V, B) = \{x \in \mathfrak{gl}(V) \mid B(xv, w) + B(v, xw) = 0\}$.

# Core Definition

**Example 3.29** (Kirillov): Let $V$ be a vector space with a bilinear form $B$. Then $\mathrm{O}(V, B) = \{g \in \mathrm{GL}(V) \mid B(gv, gw) = B(v,w) \text{ for all } v, w\}$ is a Lie group with Lie algebra $\mathfrak{o}(V, B) = \{x \in \mathfrak{gl}(V) \mid B(xv, w) + B(v, xw) = 0 \text{ for all } v, w\}$.

The proof uses the stabilizer framework: $\mathrm{O}(V, B) = \mathrm{Stab}(B)$ under the action $(gF)(v, w) = F(g^{-1}v, g^{-1}w)$.

# Prerequisites

- **Stabilizer Lie algebra** — the method used
- **Representation of Lie group** — the action on bilinear forms

# Key Properties

1. The Lie algebra condition $B(xv, w) + B(v, xw) = 0$ follows from the Leibniz rule.
2. This recovers $\mathrm{O}(n, \mathbb{R})$ when $B$ is the standard symmetric form.
3. This recovers $\mathrm{Sp}(2n, \mathbb{R})$ when $B = \omega$ is the standard symplectic form.

# Construction / Recognition

## To Construct/Create:
1. Start with a bilinear form $B$ on $V$.
2. $\mathrm{O}(V, B) = \{g \mid B(gv, gw) = B(v, w)\}$.
3. Differentiate: $\mathfrak{o}(V, B) = \{x \mid B(xv, w) + B(v, xw) = 0\}$.

## To Identify/Recognize:
1. A group preserving a bilinear form.

# Context & Application

This provides a unified framework for understanding orthogonal and symplectic groups. Any group preserving a bilinear form fits this pattern.

# Examples

**Example 3.29** (p. 28): As special cases, we recover $\mathrm{O}(n, \mathbb{R})$ and $\mathrm{Sp}(2n, \mathbb{R})$.

# Relationships

## Builds Upon
- **Stabilizer Lie algebra** — computed via stabilizer method

## Enables
- **Unified understanding of classical groups** — $\mathrm{O}(n)$, $\mathrm{SO}(p,q)$, $\mathrm{Sp}(2n)$ as special cases

## Related
- **Orthogonal group** — $B$ symmetric
- **Symplectic group** — $B$ skew-symmetric

# Common Errors

- **Error**: Forgetting the minus sign in the Lie algebra condition.
  **Correction**: The action on forms uses $g^{-1}$, giving the infinitesimal condition $-B(xv, w) - B(v, xw) = 0$, equivalent to $B(xv, w) + B(v, xw) = 0$.

# Common Confusions

- **Confusion**: Whether this works for degenerate forms.
  **Clarification**: The stabilizer method works for any form, but the resulting group is most interesting for non-degenerate forms.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, Example 3.29, page 28.

# Verification Notes

- Definition source: Direct from Example 3.29
- Confidence rationale: Explicit example with proof
- Uncertainties: None
- Cross-reference status: Verified
