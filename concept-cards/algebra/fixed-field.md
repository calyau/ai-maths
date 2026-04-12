---
concept: Fixed Field
slug: fixed-field
category: galois-theory
subcategory: core-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.5 Fixed Fields"
extraction_confidence: high
aliases:
  - "K^H"
prerequisites:
  - field-extension
  - galois-group
extends: []
related:
  - fundamental-theorem-galois-theory
  - galois-extension
contrasts_with: []
answers_questions:
  - "What is a fixed field?"
---

# Quick Definition

The fixed field K^H of a group H of automorphisms of K is the set of all elements of K that are fixed by every automorphism in H. It is always a subfield of K.

# Core Definition

Let H be a group of automorphisms of a field K. The fixed field of H is K^H = {alpha in K | sigma(alpha) = alpha for all sigma in H} (Artin, p. 495, equation 16.5.1). The Fixed Field Theorem (16.5.4) states: if H is a finite group of automorphisms of K, and F = K^H, then [K:F] = |H|.

# Prerequisites

- **Field extension** -- Fixed fields create intermediate extensions
- **Galois group** -- Fixed fields arise from subgroups of the Galois group

# Key Properties

1. K^H is always a subfield of K
2. [K:K^H] = |H| (Fixed Field Theorem, 16.5.4)
3. H = G(K/K^H) -- the group equals the Galois group over its fixed field (16.6.2(b))
4. K is a Galois extension of K^H (16.6.2(b))
5. Every element of K has degree over K^H dividing |H| (16.5.2(b))

# Context & Application

Fixed fields are one side of the Galois correspondence. The Fixed Field Theorem is the key technical result underlying the Fundamental Theorem of Galois Theory.

# Examples

**Example 1** (p. 496): K = C(t), sigma(t) = it, tau(t) = t^{-1} generate a dihedral group D_4. The fixed field is C(u) where u = t^4 + t^{-4}.

# Relationships

## Builds Upon
- **Field extension** -- Fixed fields are intermediate extensions
- **Galois group** -- Fixed fields come from subgroups

## Enables
- **Fundamental theorem of Galois theory** -- Fixed fields are one side of the correspondence

# Source Reference

Chapter 16: Galois Theory, Section 16.5, pages 495-498. Theorem 16.5.4.

# Verification Notes

- Definition source: Direct from Artin, p. 495
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
