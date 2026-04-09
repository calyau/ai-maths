---
# === CORE IDENTIFICATION ===
concept: Complexification and Representation Equivalence
slug: complexification-of-representations

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 39
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-algebra
extends: []
related:
  - equivalence-of-group-and-algebra-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do representations of a real Lie algebra relate to representations of its complexification?"
---

# Quick Definition

The categories of complex representations of a real Lie algebra $\mathfrak{g}$ and its complexification $\mathfrak{g}^{\mathbb{C}}$ are equivalent: extending $\rho$ by $\rho(x + iy) = \rho(x) + i\rho(y)$ gives a bijection.

# Core Definition

**Lemma 4.4** (Kirillov, p. 39): Let $\mathfrak{g}$ be a real Lie algebra and $\mathfrak{g}^{\mathbb{C}}$ its complexification. Then any complex representation of $\mathfrak{g}$ has a unique structure of representation of $\mathfrak{g}^{\mathbb{C}}$, and $\mathrm{Hom}_{\mathfrak{g}}(V, W) = \mathrm{Hom}_{\mathfrak{g}^{\mathbb{C}}}(V, W)$. Categories of complex representations of $\mathfrak{g}$ and $\mathfrak{g}^{\mathbb{C}}$ are equivalent.

# Prerequisites

- **Representation of a Lie algebra** — The representations being related

# Key Properties

1. Extension is by $\mathbb{C}$-linearity: $\rho(x + iy) = \rho(x) + i\rho(y)$
2. Morphisms are preserved: same intertwining operators
3. This combines with the group-algebra equivalence for powerful results

# Examples

**Example 4.5** (p. 39): Categories of representations of $SL(2,\mathbb{C})$, $SU(2)$, $\mathfrak{sl}(2,\mathbb{C})$, and $\mathfrak{su}(2)$ are all equivalent. The chain: $SU(2)$ representations $\leftrightarrow$ $\mathfrak{su}(2)$ representations $\leftrightarrow$ $\mathfrak{sl}(2,\mathbb{C})$ representations.

# Relationships

## Related
- **Equivalence of group and algebra representations** — Combined, these give the full chain

# Source Reference

Chapter 4, Section 4.1, Lemma 4.4, Example 4.5, p. 39.

# Verification Notes

- Definition source: Direct from Lemma 4.4
- Confidence rationale: Explicit lemma
- Uncertainties: None
- Cross-reference status: Verified
