---
concept: Gradation on a Tensor Category
slug: gradation-on-tensor-category
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 236
section: "21c Gradations on tensor categories"
extraction_confidence: high
aliases:
  - "M-gradation"
  - "tensor map"
prerequisites:
  - neutral-tannakian-category
  - tannaka-dual
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
---

# Quick Definition

An M-gradation on a tensor category C assigns to each object X a decomposition X = direct sum X^m (m in M) compatible with morphisms and tensor products. For a tannakian category, M-gradations correspond to central homomorphisms D(M) -> G.

# Core Definition

An **M-gradation** on a tensor category C (where M is a finitely generated abelian group) is an M-gradation on each object X compatible with all arrows and with tensor products: (X tensor Y)^m = direct sum_{r+s=m} X^r tensor Y^s (Milne, 21.19). For a neutral tannakian category (C, omega) with Tannaka dual G, giving an M-gradation is the same as giving a central homomorphism D(M) -> G (21.19).

# Prerequisites

- **Neutral tannakian category** -- Gradations are studied on tannakian categories
- **Tannaka dual** -- Gradations correspond to central homomorphisms

# Key Properties

1. For semisimple C with End(V) = k for simple V: gradations correspond to tensor maps I(C) -> M (21.20a)
2. The universal tensor grading group M(C) satisfies M(C) = X*(Z(G)) when the centre Z of G is split (21.21)
3. M(C) = I(C)/~ where a ~ a' iff a, a' appear as factors of the same tensor product (21.22)

# Context & Application

Gradations on tensor categories provide a way to compute the centre of the Tannaka dual group. This is used in Chapter III to compute the centre of the algebraic group attached to a semisimple Lie algebra.

# Examples

**Example 1** (21.21): For semisimple C, the centre Z = D(N) with N = M(C), and a simple object X defines a character of Z.

# Relationships

## Builds Upon
- **Tannaka dual** -- Gradations compute the centre of G

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21c, pages 236-237.

# Verification Notes

- Definition source: Direct from 21.19
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
