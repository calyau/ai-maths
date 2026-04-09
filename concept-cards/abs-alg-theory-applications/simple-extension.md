---
# === CORE IDENTIFICATION ===
concept: Simple Extension
slug: simple-extension

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
extends:
  - extension-field
related:
  - minimal-polynomial
  - primitive-element-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple extension?"
  - "When is a field extension simple?"
---

# Quick Definition

A simple extension is a field extension of the form $E = F(\alpha)$ for some element $\alpha \in E$ — that is, the smallest field containing both $F$ and $\alpha$.

# Core Definition

If $E$ is a field extension of $F$ and $\alpha_1, \ldots, \alpha_n$ are contained in $E$, we denote the smallest field containing $F$ and $\alpha_1, \ldots, \alpha_n$ by $F(\alpha_1, \ldots, \alpha_n)$. If $E = F(\alpha)$ for some $\alpha \in E$, then $E$ is a **simple extension** of $F$ (Judson, p. 276).

# Prerequisites

- **Extension field** — Simple extensions are a special type of field extension

# Key Properties

1. If $\alpha$ is algebraic over $F$ with minimal polynomial of degree $n$, then $\{1, \alpha, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over $F$ (Theorem 21.13)
2. If $\alpha$ is transcendental, then $F(\alpha) \cong F(x)$, the field of rational functions (Theorem 21.9)
3. Every finite extension of a finite field is simple (Corollary 22.12)
4. Every finite separable extension is simple (Primitive Element Theorem, Theorem 23.13)

# Context & Application

Simple extensions are the building blocks of field theory. Understanding $F(\alpha)$ completely — via the minimal polynomial — gives control over the entire extension. The Primitive Element Theorem guarantees that most extensions encountered in practice are simple.

# Examples

**Example 1** (p. 276): $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} : a, b \in \mathbb{Q}\}$ is a simple extension of $\mathbb{Q}$.

**Example 2** (p. 280): $\mathbb{Q}(\sqrt{3} + \sqrt{5}) = \mathbb{Q}(\sqrt{3}, \sqrt{5})$ — this extension by two elements is actually simple.

**Example 3** (p. 278): $\mathbb{R}(i) = \mathbb{C}$ is a simple extension of $\mathbb{R}$.

# Relationships

## Builds Upon
- **Extension field** — A simple extension is the smallest extension containing one element

## Enables
- **Degree of field extension** — For simple algebraic extensions, $[F(\alpha):F] = \deg(\text{min poly})$

## Related
- **Minimal polynomial** — Determines the structure of a simple algebraic extension
- **Primitive Element Theorem** — Guarantees many extensions are simple

# Common Confusions

- **Confusion**: Thinking $F(\alpha_1, \alpha_2)$ cannot be a simple extension
  **Clarification**: Many multi-generator extensions are actually simple, e.g., $\mathbb{Q}(\sqrt{3}, \sqrt{5}) = \mathbb{Q}(\sqrt{3} + \sqrt{5})$

# Source Reference

Chapter 21: Fields, Section 21.1, pages 276, 280.

# Verification Notes

- Definition source: Direct from p. 276
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
