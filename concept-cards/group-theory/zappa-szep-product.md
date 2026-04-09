---
# === CORE IDENTIFICATION ===
concept: "Zappa-Sz\xE9p Product"
slug: zappa-szep-product

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 49
section: "Semidirect products"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - knit product

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semidirect-product
extends: []
related:
  - direct-product-of-groups
contrasts_with:
  - semidirect-product
  - direct-product-of-groups

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when neither subgroup is normal in a factorization G = H1 H2?"
---

# Quick Definition

When $G = H_1 H_2$ with $H_1 \cap H_2 = \{e\}$ but neither $H_1$ nor $H_2$ is normal, $G$ is the Zappa-Szep (or knit) product.

# Core Definition

"If neither $H_1$ nor $H_2$ is normal, then $G$ is the Zappa-Szep (or knit) product of $H_1$ and $H_2$" (Milne, Summary 3.20(c), p. 49).

# Prerequisites

- **Semidirect product** — The Zappa-Szep product generalizes the case where one factor is normal

# Key Properties

1. Summary 3.20: Given $G = H_1 H_2$, $H_1 \cap H_2 = \{e\}$:
   - Both normal $\Rightarrow$ direct product
   - One normal $\Rightarrow$ semidirect product
   - Neither normal $\Rightarrow$ Zappa-Szep product

# Relationships

## Contrasts With
- **direct-product-of-groups** — Both factors normal
- **semidirect-product** — One factor normal

# Source Reference

Chapter 3: Automorphisms and Extensions, Summary 3.20, page 49.

# Verification Notes

- Definition source: Summary 3.20(c), p. 49
- Confidence: MEDIUM — briefly mentioned, details referred to Wikipedia
- Uncertainties: No detailed construction given in source
