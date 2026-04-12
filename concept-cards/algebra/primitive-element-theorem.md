---
concept: Primitive Element Theorem
slug: primitive-element-theorem
category: field-theory
subcategory: main-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.8 Primitive Elements"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
  - algebraic-element
extends: []
related:
  - simple-extension
  - galois-group
contrasts_with: []
answers_questions:
  - "What is the Primitive Element Theorem?"
---

# Quick Definition

The Primitive Element Theorem states that every finite extension of a field of characteristic zero has a primitive element -- a single generator alpha such that K = F(alpha).

# Core Definition

Every finite extension K of a field F of characteristic zero contains a primitive element (Artin, Theorem 15.8.1). That is, K = F(alpha) for some alpha in K. The proof reduces to the case K = F(alpha, beta), and Lemma 15.8.2 shows that gamma = beta + c*alpha is primitive for all but finitely many c in F.

# Prerequisites

- **Field extension** -- The theorem applies to finite field extensions
- **Algebraic element** -- All elements of a finite extension are algebraic

# Key Properties

1. Works for any field of characteristic zero
2. Also true for finite fields (different proof)
3. For K = F(alpha, beta), gamma = beta + c*alpha is primitive for almost all c (15.8.2)
4. The choice of c must avoid finitely many "bad" values

# Context & Application

The Primitive Element Theorem simplifies the study of finite extensions by reducing to the case of simple extensions. It is used in the proof of the Galois correspondence and in constructing Galois groups.

# Examples

**Example 1** (p. 480): K = Q(sqrt(2), sqrt(3)). The element gamma = sqrt(2) + sqrt(3) is a primitive element.

# Relationships

## Builds Upon
- **Field extension** -- The theorem is about finite extensions

## Enables
- **Galois group computation** -- Reduces to finding roots of a single polynomial
- **Simple extension** -- Every finite extension is simple in characteristic zero

# Source Reference

Chapter 15: Fields, Section 15.8, pages 479-481. Theorem 15.8.1, Lemma 15.8.2.

# Verification Notes

- Definition source: Direct from Artin, Theorem 15.8.1
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
