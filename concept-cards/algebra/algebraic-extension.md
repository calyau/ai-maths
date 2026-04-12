---
concept: Algebraic Extension
slug: algebraic-extension
category: field-theory
subcategory: extension-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Fields"
chapter_number: 15
pdf_page: 453
section: "15.3 The Degree of a Field Extension"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
  - algebraic-element
extends: []
related:
  - transcendental-extension
  - finite-field-extension
contrasts_with:
  - transcendental-extension
answers_questions:
  - "What is an algebraic extension?"
---

# Quick Definition

A field extension K/F is algebraic if every element of K is algebraic over F. Every finite extension is algebraic, but not every algebraic extension is finite.

# Core Definition

A field extension K/F is an algebraic extension if every element of K is algebraic over F (Artin, p. 462, Exercise 3.10). A finite extension is always algebraic (Corollary 15.3.6(a)), since any element in a degree-n extension has degree dividing n. The algebraic elements of any extension K form a subfield (15.3.6(d)).

# Prerequisites

- **Field extension** -- Algebraic extensions are a type of field extension
- **Algebraic element** -- All elements must be algebraic

# Key Properties

1. Every finite extension is algebraic (15.3.6(a))
2. A field generated over F by finitely many algebraic elements is a finite (hence algebraic) extension (15.3.6(c))
3. The algebraic elements in any extension form a subfield (15.3.6(d))
4. If K/F and L/K are algebraic, then L/F is algebraic (Exercise 3.10)

# Context & Application

Algebraic extensions are the extensions where field-theoretic tools (degree, minimal polynomial, Galois theory) apply most naturally. They contrast with transcendental extensions, which behave more like function fields.

# Examples

**Example 1** (p. 461): Q(sqrt(2), sqrt(3))/Q is algebraic of degree 4.

**Example 2** (p. 457): Q(t)/Q where t is transcendental is NOT algebraic.

# Relationships

## Builds Upon
- **Algebraic element** -- All elements must be algebraic

## Related
- **Finite extension** -- Every finite extension is algebraic

## Contrasts With
- **Transcendental extension** -- Contains transcendental elements

# Source Reference

Chapter 15: Fields, Section 15.3, pages 459-462. Corollary 15.3.6.

# Verification Notes

- Definition source: From Artin Exercise 3.10 and Corollary 15.3.6
- Confidence rationale: Standard definition used throughout
- Uncertainties: None
- Cross-reference status: Verified
