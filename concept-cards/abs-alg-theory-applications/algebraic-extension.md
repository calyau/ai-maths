---
# === CORE IDENTIFICATION ===
concept: Algebraic Extension
slug: algebraic-extension

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
  - algebraic-element
  - extension-field
extends:
  - extension-field
related:
  - finite-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an algebraic extension?"
  - "How do algebraic extensions relate to finite extensions?"
---

# Quick Definition

An extension field $E$ of $F$ is an algebraic extension if every element in $E$ is algebraic over $F$.

# Core Definition

An extension field $E$ of a field $F$ is an **algebraic extension** of $F$ if every element in $E$ is algebraic over $F$ (Judson, p. 276).

# Prerequisites

- **Algebraic element** — An algebraic extension requires all elements to be algebraic
- **Extension field** — An algebraic extension is a specific type of extension

# Key Properties

1. Every finite extension is algebraic (Theorem 21.15)
2. The converse is false: there exist algebraic extensions that are not finite (Remark 21.16)
3. A finite extension $E = F(\alpha_1, \ldots, \alpha_n)$ with each $\alpha_i$ algebraic over $F$ is an algebraic extension (Theorem 21.22)
4. The set of elements in an extension $E$ algebraic over $F$ forms a field (Theorem 21.23)

# Construction / Recognition

## To Recognize:
1. Take an arbitrary element $\alpha \in E$
2. Verify it satisfies some nonzero polynomial over $F$
3. If this holds for every element, the extension is algebraic

# Context & Application

Algebraic extensions are the "well-behaved" extensions — the elements are tightly connected to the base field via polynomial equations. Most of Galois theory concerns algebraic (and moreover, finite) extensions.

# Examples

**Example 1** (p. 276): $\mathbb{Q}(\sqrt{2})$ is an algebraic extension of $\mathbb{Q}$ since every $a + b\sqrt{2}$ satisfies $x^2 - 2ax + (a^2 - 2b^2) = 0$.

**Example 2** (p. 280): The set of all algebraic numbers (elements of $\mathbb{C}$ algebraic over $\mathbb{Q}$) forms an algebraic extension of $\mathbb{Q}$ that is not finite.

# Relationships

## Builds Upon
- **Algebraic element** — Requires all elements to be algebraic
- **Extension field** — A special type of extension

## Enables
- **Galois theory** — Galois theory studies finite normal separable algebraic extensions

## Related
- **Finite extension** — Every finite extension is algebraic, but not conversely

# Common Confusions

- **Confusion**: Believing algebraic extensions must be finite-dimensional
  **Clarification**: The algebraic closure of $\mathbb{Q}$ is an infinite algebraic extension (Remark 21.16)

# Source Reference

Chapter 21: Fields, Section 21.1, pages 276, 279–281. See Theorems 21.15, 21.22, 21.23.

# Verification Notes

- Definition source: Direct from p. 276
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
