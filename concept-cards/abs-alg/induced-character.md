---
concept: Induced Character
slug: induced-character
category: representation-theory
subcategory: induction
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 902
section: "19.3 Introduction to the Theory of Induced Characters"
extraction_confidence: high
aliases:
  - "Ind^G_H χ"
prerequisites:
  - induced-representation
  - character
extends: []
related:
  - frobenius-reciprocity
contrasts_with: []
answers_questions:
  - "What is an induced character?"
---

# Quick Definition
The induced character Ind^G_H(χ) of a character χ of H is the character of the induced representation. Its formula is Ind^G_H(χ)(g) = (1/|H|)Σ_{x∈G, x^{-1}gx∈H} χ(x^{-1}gx).

# Core Definition
If χ is the character of an FH-module W, then the **induced character** Ind^G_H(χ) is the character of the FG-module FG ⊗_{FH} W (p. 902). The formula: Ind^G_H(χ)(g) = (1/|H|)Σ_{x∈G} χ°(x^{-1}gx) where χ°(h) = χ(h) for h ∈ H and 0 otherwise.

# Prerequisites
- **induced-representation** — The character of the induced module
- **character** — χ is a character of H

# Source Reference
Chapter 19, Section 19.3, pages 902-905.

# Verification Notes
- Confidence: HIGH — explicit formula given
