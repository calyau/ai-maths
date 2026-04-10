---
concept: Real Algebraic Envelope
slug: real-algebraic-envelope
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 331
section: "Compact topological groups"
extraction_confidence: high
aliases:
  - "algebraic envelope"
prerequisites:
  - real-lie-group
  - reductive-algebraic-group
extends: []
related:
  - complex-algebraic-envelope
  - anisotropic-algebraic-group
contrasts_with: []
answers_questions:
  - "What is the real algebraic envelope of a compact group?"
---

# Quick Definition

The real algebraic envelope of a topological group K is the real affine algebraic group G such that the continuous representations of K correspond to the representations of G, via a continuous homomorphism K → G(ℝ).

# Core Definition

Let K be a topological group. The category Rep_ℝ(K) of continuous representations of K on finite-dimensional real vector spaces is a neutral tannakian category. The **real algebraic envelope** of K is the real affine algebraic group G, together with a continuous homomorphism K → G(ℝ), inducing an equivalence of tensor categories Rep_ℝ(K) → Rep_ℝ(G) (Milne, §3, p. 331).

# Prerequisites

- **Real Lie group** — K is typically a Lie group
- **Reductive algebraic group** — The envelope is reductive when K is compact

# Key Properties

1. If K is a compact Lie group, then Rep_ℝ(K) is semisimple, so G is reductive (p. 332)
2. The complex algebraic envelope of K is G_ℂ (Proposition 3.2)
3. If K is compact and dense in G(ℝ) (Zariski topology), then G is anisotropic and K = G(ℝ) (Proposition 3.4)

# Context & Application

The algebraic envelope translates compact group theory into algebraic group theory. For compact connected Lie groups, this gives a complete bridge between the two worlds.

# Source Reference

Chapter IV, Section 3, pages 331–332.

# Verification Notes

- Definition source: Direct from §3, p. 331
- Confidence: HIGH
- Uncertainties: None
