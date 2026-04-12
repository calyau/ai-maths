---
# === CORE IDENTIFICATION ===
concept: Inverse of a Product
slug: inverse-of-a-product

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Dihedral Groups"
chapter_number: 4
pdf_page: 22
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - shoes-and-socks property
  - reverse-order law for inverses

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - inverse-element
  - general-associative-law
extends:
  - inverse-element
related:
  - dihedral-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The inverse of a product reverses the order of factors: (xy)^{-1} = y^{-1}x^{-1}. More generally, (x_1 x_2 ... x_n)^{-1} = x_n^{-1} ... x_2^{-1} x_1^{-1}.

# Core Definition

Armstrong proves: "xyy^{-1}x^{-1} = xex^{-1} = xx^{-1} = e, and similarly y^{-1}x^{-1}xy = e. Therefore, if x and y are elements of a group, then (xy)^{-1} = y^{-1}x^{-1}" (Armstrong, Ch. 4, p. 24). The general formula is (x_1 x_2 ... x_n)^{-1} = x_n^{-1} ... x_2^{-1} x_1^{-1}.

# Prerequisites

- **Group** — The result holds in any group
- **Inverse Element** — Uses the concept of inverses
- **General Associative Law** — Used to manipulate products freely

# Key Properties

1. (xy)^{-1} = y^{-1}x^{-1} (order reverses)
2. Generalizes to any finite product: (x_1...x_n)^{-1} = x_n^{-1}...x_1^{-1}
3. The reversal of order is essential in non-abelian groups
4. In abelian groups, (xy)^{-1} = x^{-1}y^{-1} = y^{-1}x^{-1}

# Construction / Recognition

## Proof:
1. Compute (y^{-1}x^{-1})(xy) = y^{-1}(x^{-1}x)y = y^{-1}ey = y^{-1}y = e
2. Compute (xy)(y^{-1}x^{-1}) = x(yy^{-1})x^{-1} = xex^{-1} = xx^{-1} = e
3. Since y^{-1}x^{-1} satisfies both conditions, it is (xy)^{-1}

# Context & Application

This result is used constantly in group calculations. For example, in Exercise 1.5, the inverse of rs is sr^2 = s * r^{-1}, which follows from (rs)^{-1} = s^{-1}r^{-1} = sr^2 (since s^{-1} = s and r^{-1} = r^2 in D_3).

# Examples

**Example 1** (p. 24): The proof that (xy)^{-1} = y^{-1}x^{-1}, computed by showing xyy^{-1}x^{-1} = e.

**Example 2** (Exercise 1.5, p. 12): In D_3: (rs)^{-1} = s^{-1}r^{-1} = sr^2, and (sr)^{-1} = r^{-1}s^{-1} = r^2s.

# Relationships

## Builds Upon
- **Inverse Element** — Extends the concept to products
- **General Associative Law** — Needed for the computation

## Related
- **Dihedral Group** — Frequently applied in dihedral group calculations

# Common Errors

- **Error**: Writing (xy)^{-1} = x^{-1}y^{-1} (preserving order)
  **Correction**: The order must reverse: (xy)^{-1} = y^{-1}x^{-1}

# Common Confusions

- **Confusion**: Thinking the order reversal is optional
  **Clarification**: In non-abelian groups, x^{-1}y^{-1} is generally not equal to y^{-1}x^{-1}, so the order matters

# Source Reference

Chapter 4: Dihedral Groups, page 17 (pdf p. 24). Also Exercise 2.8 (p. 17).

# Verification Notes

- Definition source: Direct proof from p. 24
- Confidence rationale: High — explicitly proved
- Uncertainties: None
- Cross-reference status: Verified
