---
# === CORE IDENTIFICATION ===
concept: Extension by Radicals
slug: extension-by-radicals

# === CLASSIFICATION ===
category: galois-theory
subcategory: solvability
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.3 Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "radical extension"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - simple-extension
extends:
  - extension-field
related:
  - solvable-by-radicals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an extension by radicals?"
---

# Quick Definition

An extension field $E$ of $F$ is an extension by radicals if there is a chain of subfields $F = F_0 \subset F_1 \subset \cdots \subset F_r = E$ where each $F_i = F_{i-1}(\alpha_i)$ and $\alpha_i^{n_i} \in F_{i-1}$ for some positive integer $n_i$.

# Core Definition

An extension field $E$ of a field $F$ is an **extension by radicals** if there exists a chain of subfields

$$F = F_0 \subset F_1 \subset F_2 \subset \cdots \subset F_r = E$$

such that for $i = 1, 2, \ldots, r$, we have $F_i = F_{i-1}(\alpha_i)$ and $\alpha_i^{n_i} \in F_{i-1}$ for some positive integer $n_i$ (Judson, p. 317).

# Prerequisites

- **Extension field** — Extensions by radicals are field extensions
- **Simple extension** — Each step in the chain is a simple extension

# Key Properties

1. Each step adjoins an $n_i$th root of an element already in the field
2. This captures the intuitive notion of "solving by taking roots"
3. The chain corresponds to successive extractions of roots

# Context & Application

Extensions by radicals formalize what it means to solve a polynomial equation using the arithmetic operations and root extractions. This concept is the link between solvability of polynomial equations and group theory.

# Examples

**Example 1**: The splitting field of $x^2 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt{2})$, which is an extension by radicals with $\alpha_1 = \sqrt{2}$ and $n_1 = 2$.

**Example 2** (p. 317): The quadratic formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ shows that the splitting field of $ax^2 + bx + c$ is obtained by adjoining $\sqrt{b^2 - 4ac}$, an extension by radicals.

# Relationships

## Builds Upon
- **Extension field** — An extension by radicals is an extension field
- **Simple extension** — Each step is a simple extension by a root

## Enables
- **Solvable by radicals** — A polynomial is solvable by radicals if its splitting field lies in an extension by radicals

# Source Reference

Chapter 23: Galois Theory, Section 23.3, page 317.

# Verification Notes

- Definition source: Direct from p. 317
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
