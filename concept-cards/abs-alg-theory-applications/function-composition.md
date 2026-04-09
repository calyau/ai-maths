---
# === CORE IDENTIFICATION ===
concept: Function Composition
slug: function-composition

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
pdf_page: 21
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - composition of mappings

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends: []
related:
  - identity-mapping
  - inverse-mapping
  - binary-operation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The composition of two functions $f: A \to B$ and $g: B \to C$ is the function $g \circ f: A \to C$ defined by $(g \circ f)(x) = g(f(x))$.

# Core Definition

"Let $f: A \to B$ and $g: B \to C$ be mappings. Define a new map, the composition of $f$ and $g$ from $A$ to $C$, by $(g \circ f)(x) = g(f(x))$" (Judson, p. 21).

# Prerequisites

- **Mapping** — Composition operates on mappings

# Key Properties

1. Associative: $(h \circ g) \circ f = h \circ (g \circ f)$ (Theorem 1.15)
2. Not generally commutative: $f \circ g \neq g \circ f$ in general
3. Composition of injective maps is injective (Theorem 1.15)
4. Composition of surjective maps is surjective (Theorem 1.15)
5. Composition of bijective maps is bijective (Theorem 1.15)

# Construction / Recognition

## To Compute $g \circ f$:
1. Apply $f$ first to the input
2. Apply $g$ to the result of $f$
3. Note: $g \circ f$ is read "g composed with f" but $f$ is applied first

# Context & Application

Composition is the binary operation for permutation groups and symmetry groups. The group of symmetries of a geometric figure uses composition as its operation. Associativity of composition is what makes these groups well-defined.

# Examples

**Example 1** (p. 21): Let $f(x) = x^2$ and $g(x) = 2x + 5$. Then $(f \circ g)(x) = (2x+5)^2 = 4x^2 + 20x + 25$ and $(g \circ f)(x) = 2x^2 + 5$. Note $f \circ g \neq g \circ f$.

**Example 2** (p. 21): Let $f(x) = x^3$ and $g(x) = \sqrt[3]{x}$. Then $(f \circ g)(x) = x$ and $(g \circ f)(x) = x$, so $f \circ g = g \circ f$ in this special case.

# Relationships

## Builds Upon
- **mapping** — Composition operates on mappings

## Enables
- **inverse-mapping** — Defined via composition with identity
- **symmetry** — Symmetries compose to form groups
- **binary-operation** — Composition is the binary operation for permutation groups

# Common Errors

- **Error**: Applying functions in the wrong order; computing $f(g(x))$ instead of $g(f(x))$ for $g \circ f$
  **Correction**: In $g \circ f$, apply $f$ first, then $g$

# Common Confusions

- **Confusion**: Assuming $f \circ g = g \circ f$ always holds
  **Clarification**: Composition is generally not commutative; order matters

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 21-22. Theorem 1.15, page 22.

# Verification Notes

- Definition source: Direct quote from p. 21
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
