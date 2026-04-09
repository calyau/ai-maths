---
concept: Algebraic Elements Form a Field
slug: algebraic-elements-form-field
category: field-theory
subcategory: field-extensions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"
extraction_confidence: high
aliases: []
prerequisites:
  - algebraic-element
  - algebraic-extension
extends: []
related:
  - algebraic-closure
  - algebraic-number
contrasts_with: []
answers_questions:
  - "Do algebraic elements form a field?"
---

# Quick Definition

If $E$ is an extension of $F$, then the set of all elements in $E$ that are algebraic over $F$ forms a subfield of $E$. In particular, the algebraic numbers form a field.

# Core Definition

**Theorem 21.23.** Let $E$ be an extension field of $F$. The set of elements in $E$ that are algebraic over $F$ form a field (Judson, p. 281).

**Corollary 21.24.** The set of all algebraic numbers (complex numbers algebraic over $\mathbb{Q}$) forms a field (p. 281).

# Prerequisites

- **Algebraic element** — The elements forming the field
- **Algebraic extension** — The resulting field is an algebraic extension

# Key Properties

1. If $\alpha, \beta$ are algebraic over $F$, then $\alpha \pm \beta$, $\alpha\beta$, and $\alpha/\beta$ are also algebraic
2. The proof uses the fact that $F(\alpha, \beta)$ is a finite extension when $\alpha, \beta$ are algebraic
3. The algebraic numbers form the algebraic closure of $\mathbb{Q}$ in $\mathbb{C}$

# Examples

**Example 1** (p. 281): $\sqrt{2} + \sqrt{3}$ is algebraic over $\mathbb{Q}$ because both $\sqrt{2}$ and $\sqrt{3}$ are algebraic, and algebraic elements form a field.

# Relationships

## Builds Upon
- **Algebraic element** — The elements that form the field

## Related
- **Algebraic closure** — The maximal such field
- **Algebraic number** — The algebraic closure of $\mathbb{Q}$

# Source Reference

Chapter 21: Fields, Section 21.1, page 281. Theorem 21.23, Corollary 21.24.

# Verification Notes

- Definition source: Direct from Theorem 21.23, p. 281
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
