---
concept: Frobenius Reciprocity
slug: frobenius-reciprocity
category: representation-theory
subcategory: induction
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 903
section: "19.3 Introduction to the Theory of Induced Characters"
extraction_confidence: high
aliases: []
prerequisites:
  - induced-character
  - orthogonality-relations
extends: []
related:
  - induced-representation
contrasts_with: []
answers_questions:
  - "What is Frobenius reciprocity?"
---

# Quick Definition
Frobenius reciprocity states that ⟨Ind^G_H χ, ψ⟩_G = ⟨χ, Res^G_H ψ⟩_H. Induction from H to G is adjoint to restriction from G to H.

# Core Definition
**Frobenius Reciprocity** (Corollary 12, p. 903): For H ≤ G, a character χ of H, and a character ψ of G: ⟨Ind^G_H χ, ψ⟩_G = ⟨χ, Res^G_H ψ⟩_H. This means the multiplicity of an irreducible ψ of G in Ind^G_H χ equals the multiplicity of an irreducible χ of H in the restriction of ψ to H.

# Prerequisites
- **induced-character** — One side involves induction
- **orthogonality-relations** — Uses the inner product of characters

# Key Properties
1. Induction and restriction are adjoint functors
2. Determines multiplicities in induced representations
3. Fundamental tool for computing character tables

# Source Reference
Chapter 19, Section 19.3, Corollary 12, pages 903-904.

# Verification Notes
- Confidence: HIGH — named theorem explicitly stated
