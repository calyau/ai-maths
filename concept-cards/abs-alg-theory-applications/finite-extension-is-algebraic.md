---
# === CORE IDENTIFICATION ===
concept: Every Finite Extension is Algebraic
slug: finite-extension-is-algebraic

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
  - finite-extension
  - algebraic-extension
  - degree-of-field-extension
extends: []
related:
  - algebraic-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all finite extensions algebraic?"
  - "Is every algebraic extension finite?"
---

# Quick Definition

Every finite extension field $E$ of $F$ is an algebraic extension. The converse is false: algebraic extensions can be infinite-dimensional.

# Core Definition

**Theorem 21.15.** Every finite extension field $E$ of a field $F$ is an algebraic extension (Judson, p. 279).

**Proof sketch:** If $[E:F] = n$ and $\alpha \in E$, then $1, \alpha, \ldots, \alpha^n$ are $n+1$ elements in an $n$-dimensional space, hence linearly dependent. This gives a polynomial relation $a_n\alpha^n + \cdots + a_0 = 0$ with coefficients in $F$.

# Prerequisites

- **Finite extension** — The hypothesis
- **Algebraic extension** — The conclusion
- **Degree of field extension** — The proof uses finite dimension

# Key Properties

1. Finite implies algebraic (Theorem 21.15)
2. Algebraic does not imply finite (Remark 21.16): the algebraic closure of $\mathbb{Q}$ is algebraic but infinite
3. The proof is a dimension argument from linear algebra
4. Characterization: $E$ is a finite extension of $F$ if and only if $E = F(\alpha_1, \ldots, \alpha_n)$ with each $\alpha_i$ algebraic (Theorem 21.22)

# Context & Application

This theorem shows that finite extensions are the "controlled" case of algebraic extensions. It justifies studying finite extensions as the primary setting for Galois theory.

# Examples

**Example 1** (p. 279): $[\mathbb{Q}(\sqrt{2}):\mathbb{Q}] = 2$ is finite, so every element $a + b\sqrt{2}$ is algebraic over $\mathbb{Q}$.

**Example 2** (p. 280): The algebraic closure of $\mathbb{Q}$ is algebraic but infinite-dimensional over $\mathbb{Q}$ (Remark 21.16).

# Relationships

## Builds Upon
- **Finite extension** — The hypothesis
- **Algebraic extension** — The conclusion

## Related
- **Algebraic element** — Each element in a finite extension is algebraic

# Source Reference

Chapter 21: Fields, Section 21.1, pages 279–281. Theorems 21.15, 21.22. Remark 21.16.

# Verification Notes

- Definition source: Direct from Theorem 21.15, p. 279
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
