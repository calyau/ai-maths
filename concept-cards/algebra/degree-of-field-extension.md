---
concept: Degree of a Field Extension
slug: degree-of-field-extension
category: field-theory
subcategory: basic-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.3 The Degree of a Field Extension"
extraction_confidence: high
aliases:
  - "degree [K:F]"
prerequisites:
  - field-extension
extends: []
related:
  - tower-law
  - algebraic-element
contrasts_with: []
answers_questions:
  - "What is the degree of a field extension?"
---

# Quick Definition

The degree [K:F] of a field extension K/F is the dimension of K as a vector space over F. A finite extension has finite degree; extensions of degree 2 are quadratic, degree 3 are cubic.

# Core Definition

A field extension K of F can always be regarded as an F-vector space. The dimension of K when regarded as an F-vector space is called the degree of the field extension, denoted [K:F] (Artin, p. 459, equation 15.3.1). A field extension is finite if its degree is finite.

# Prerequisites

- **Field extension** -- Degree is a property of field extensions

# Key Properties

1. [K:F] = 1 iff F = K (Lemma 15.3.2)
2. If alpha is algebraic over F, then [F(alpha):F] = degree of alpha over F (15.3.4)
3. Tower law: [L:F] = [L:K][K:F] for F in K in L (Theorem 15.3.5)
4. Both [L:K] and [K:F] divide [L:F]
5. If alpha has degree d over F, then d divides [K:F] for any finite extension K containing alpha (15.3.6(a))

# Context & Application

The degree is the most basic numerical invariant of a field extension. The tower law (multiplicative property) is the key computational tool, and the connection between degree and constructibility underlies the impossibility proofs for classical geometric constructions.

# Examples

**Example 1** (p. 459): [C:R] = 2, since C has the R-basis (1, i).

**Example 2** (p. 460): [Q(alpha_1, alpha_2):Q] = 6 for alpha_1 = cube root of 2 and alpha_2 = omega*alpha_1, where omega = e^{2pi*i/3}.

# Relationships

## Builds Upon
- **Field extension** -- Degree is defined for field extensions

## Enables
- **Tower law** -- Multiplicative property of degrees
- **Constructible numbers** -- Degree must be a power of 2

## Related
- **Algebraic element** -- Degree of element equals degree of simple extension

# Source Reference

Chapter 15: Fields, Section 15.3, pages 459-462. Theorem 15.3.5.

# Verification Notes

- Definition source: Direct from Artin, p. 459
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
