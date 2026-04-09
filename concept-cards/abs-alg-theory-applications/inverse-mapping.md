---
# === CORE IDENTIFICATION ===
concept: Inverse Mapping
slug: inverse-mapping

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 23
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - inverse function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
  - function-composition
  - identity-mapping
  - bijective-function
extends: []
related:
  - permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

An inverse mapping $g: B \to A$ of $f: A \to B$ is a map such that $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$. A map has an inverse if and only if it is bijective.

# Core Definition

"A map $g: B \to A$ is an inverse mapping of $f: A \to B$ if $g \circ f = \text{id}_A$ and $f \circ g = \text{id}_B$; in other words, the inverse function of a function simply 'undoes' the function. A map is said to be invertible if it has an inverse. We usually write $f^{-1}$ for the inverse of $f$" (Judson, p. 23).

**Theorem 1.20**: "A mapping is invertible if and only if it is both one-to-one and onto" (Judson, p. 24).

# Prerequisites

- **Mapping** — Inverse is a property of mappings
- **Function composition** — Inverse defined via composition
- **Identity mapping** — Inverse composes to identity
- **Bijective function** — Only bijective maps are invertible

# Key Properties

1. $f^{-1} \circ f = \text{id}_A$ and $f \circ f^{-1} = \text{id}_B$
2. A map is invertible $\iff$ it is bijective (Theorem 1.20)
3. $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$

# Construction / Recognition

## To Find $f^{-1}$:
1. Verify $f$ is bijective
2. For each $b \in B$, find the unique $a \in A$ with $f(a) = b$
3. Define $f^{-1}(b) = a$

# Context & Application

Inverses are central to group theory: every element in a group must have an inverse. The inverse of a permutation is another permutation that reverses its effect.

# Examples

**Example 1** (p. 23): $f(x) = x^3$ has inverse $f^{-1}(x) = \sqrt[3]{x}$.

**Example 2** (p. 23): $f(x) = \ln x$ and $f^{-1}(x) = e^x$ are inverses of each other.

**Example 3** (p. 24): The permutation $\pi = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}$ has inverse $\pi^{-1} = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}$.

# Relationships

## Builds Upon
- **bijective-function** — Only bijective maps have inverses

## Enables
- **group** — Group elements must have inverses
- **permutation** — Every permutation has an inverse permutation

# Common Errors

- **Error**: Attempting to find the inverse of a non-bijective function
  **Correction**: Verify bijectivity first; non-bijective functions are not invertible

# Common Confusions

- **Confusion**: Confusing $f^{-1}(x)$ with $1/f(x)$
  **Clarification**: $f^{-1}$ denotes the inverse function, not the reciprocal

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 23-24. Theorem 1.20, page 24.

# Verification Notes

- Definition source: Direct quote from p. 23
- Confidence: HIGH — explicit definition and theorem
- Cross-reference status: Verified
- Uncertainties: None
