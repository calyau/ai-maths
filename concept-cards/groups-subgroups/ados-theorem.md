---
concept: Ado's Theorem
slug: ados-theorem
category: lie-algebras
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 274
section: "4a Preliminaries on Lie algebras"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra
extends: []
related:
  - unipotent-nilpotent-equivalence
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

Ado's theorem states that every finite-dimensional Lie algebra over a field of characteristic zero has a faithful representation, with its largest nilpotent ideal acting by nilpotent endomorphisms.

# Core Definition

Let g be a finite-dimensional Lie algebra over a field of characteristic zero, and let n be its largest nilpotent ideal. Then there exists a faithful representation (V,r) of g such that r(n) consists of nilpotent elements (Milne, Theorem 4.1).

# Prerequisites

- **Lie algebra** -- The theorem applies to all finite-dimensional Lie algebras

# Key Properties

1. Every Lie algebra embeds in gl_V for some V
2. The nilpotent radical maps to nilpotent endomorphisms
3. Essential for constructing the unipotent-nilpotent equivalence

# Context & Application

Ado's theorem is used to embed nilpotent Lie algebras into gl_V with nilpotent image, which is needed to apply the Hausdorff series construction in the proof of the unipotent-nilpotent equivalence (Theorem 4.7).

# Examples

**Example 1**: Every abelian Lie algebra k^n has a faithful representation in gl_{n+1} via strictly upper triangular matrices (with nilpotent action).

# Relationships

## Enables
- **Unipotent-nilpotent equivalence** -- Ado's theorem provides the embedding needed for the Hausdorff construction

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 4a, page 274.

# Verification Notes

- Definition source: Direct from Theorem 4.1
- Confidence rationale: Explicit theorem (proof cited as Bourbaki LIE I, section 7, 3)
- Uncertainties: None
- Cross-reference status: Verified
