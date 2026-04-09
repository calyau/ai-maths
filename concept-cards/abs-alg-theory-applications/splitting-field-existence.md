---
concept: Splitting Field Existence
slug: splitting-field-existence
category: field-theory
subcategory: field-extensions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.2 Splitting Fields"
extraction_confidence: high
aliases: []
prerequisites:
  - kronecker-theorem
  - extension-field
extends: []
related:
  - splitting-field
  - splitting-field-uniqueness
contrasts_with: []
answers_questions:
  - "Does every polynomial have a splitting field?"
---

# Quick Definition

Every nonconstant polynomial $p(x) \in F[x]$ has a splitting field: an extension of $F$ in which $p(x)$ factors completely into linear factors. The proof is by induction on degree, using Kronecker's Theorem.

# Core Definition

**Theorem 21.31.** Let $p(x) \in F[x]$ be a nonconstant polynomial. Then there exists a splitting field $E$ for $p(x)$ (Judson, p. 282).

# Prerequisites

- **Kronecker's Theorem** — Guarantees existence of a root in some extension
- **Extension field** — The splitting field is an extension

# Key Properties

1. Existence is proved by induction on $\deg p(x)$
2. Find one root $\alpha_1$ using Kronecker's Theorem
3. Factor: $p(x) = (x - \alpha_1)q(x)$ in $F(\alpha_1)[x]$
4. Apply induction to $q(x)$ to find remaining roots
5. The splitting field satisfies $[E:F] \leq (\deg p(x))!$

# Examples

**Example 1** (p. 282): $x^4 + 2x^2 - 8 = (x^2 - 2)(x^2 + 4)$ splits over $\mathbb{Q}(\sqrt{2}, i)$.

# Relationships

## Builds Upon
- **Kronecker's Theorem** — Provides roots one at a time

## Related
- **Splitting field** — The object whose existence is proved
- **Splitting field uniqueness** — Complementary result

# Source Reference

Chapter 21: Fields, Section 21.2, page 282. Theorem 21.31.

# Verification Notes

- Definition source: Direct from Theorem 21.31, p. 282
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
