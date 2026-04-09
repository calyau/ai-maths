---
# === CORE IDENTIFICATION ===
concept: Special Linear Group
slug: special-linear-group

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
  - "$\\mathrm{SL}(n, \\mathbb{K})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends:
  - general-linear-group
related:
  - sl-n-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{SL}(n, \mathbb{K}) = \{A \in \mathrm{GL}(n, \mathbb{K}) \mid \det A = 1\}$ is the group of matrices with determinant 1. Its Lie algebra is $\mathfrak{sl}(n, \mathbb{K}) = \{x \in \mathfrak{gl}(n, \mathbb{K}) \mid \mathrm{tr}(x) = 0\}$.

# Core Definition

**Theorem 2.29** (Kirillov): $\exp(x) \in \mathrm{SL}(n, \mathbb{K})$ iff $\mathrm{tr}(x) = 0$, since $\det \exp(x) = \exp(\mathrm{tr}(x))$. Thus $\mathfrak{sl}(n, \mathbb{K}) = \{x \in \mathfrak{gl}(n, \mathbb{K}) \mid \mathrm{tr}(x) = 0\}$.

# Prerequisites

- **General linear group** — $\mathrm{SL}(n)$ is a subgroup of $\mathrm{GL}(n)$

# Key Properties

1. $\dim \mathrm{SL}(n, \mathbb{K}) = n^2 - 1$.
2. $\mathrm{SL}(n, \mathbb{K})$ is connected ($\pi_0 = \{1\}$).
3. $\pi_1(\mathrm{SL}(n, \mathbb{R})) = \mathbb{Z}_2$ for $n \geq 3$; $\pi_1(\mathrm{SL}(n, \mathbb{C})) = \{1\}$.
4. The condition $\det A = 1$ becomes $\mathrm{tr}(x) = 0$ at the Lie algebra level.

# Construction / Recognition

## To Construct/Create:
1. Take all $n \times n$ matrices with determinant exactly 1.

## To Identify/Recognize:
1. The kernel of $\det: \mathrm{GL}(n) \to \mathbb{K}^*$.

# Context & Application

$\mathrm{SL}(n, \mathbb{C})$ is the simplest example of a semisimple Lie group. Its representations are a central topic in later chapters.

# Examples

**Example** (p. 16): $\mathrm{SL}(2, \mathbb{C})$ has Lie algebra $\mathfrak{sl}(2, \mathbb{C})$ with basis $e, f, h$ and relations $[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$ (Section 3.10).

# Relationships

## Builds Upon
- **General linear group** — $\mathrm{SL}(n) \subset \mathrm{GL}(n)$

## Enables
- **$\mathfrak{sl}(2, \mathbb{C})$** — the most important low-dimensional Lie algebra
- **Semisimple Lie groups** — $\mathrm{SL}(n)$ is the prototypical example

## Related
- **$\mathrm{SU}(n)$** — compact real form of $\mathrm{SL}(n, \mathbb{C})$

# Common Errors

- **Error**: Confusing the conditions $\det A = 1$ and $|\det A| = 1$.
  **Correction**: $\det A = 1$ defines $\mathrm{SL}$; $|\det A| = 1$ does not define a classical group.

# Common Confusions

- **Confusion**: Whether $\mathrm{SL}(n, \mathbb{R})$ is connected.
  **Clarification**: Yes, $\mathrm{SL}(n, \mathbb{R})$ is connected (unlike $\mathrm{GL}(n, \mathbb{R})$).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, page 16. Tables on pp. 16-17.

# Verification Notes

- Definition source: Direct from Theorem 2.29
- Confidence rationale: Explicit computation in source
- Uncertainties: None
- Cross-reference status: Verified with tables and Section 3.10
