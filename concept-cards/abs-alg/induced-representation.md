---
concept: Induced Representation
slug: induced-representation
category: representation-theory
subcategory: induction
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 900
section: "19.3 Introduction to the Theory of Induced Characters"
extraction_confidence: high
aliases:
  - "Ind^G_H"
prerequisites:
  - representation
  - fg-module
extends: []
related:
  - induced-character
  - frobenius-reciprocity
contrasts_with: []
answers_questions:
  - "What is an induced representation?"
---

# Quick Definition
Given a representation of a subgroup H ≤ G on a space W, the induced representation Ind^G_H(W) = FG ⊗_{FH} W is a representation of G of degree [G:H] · dim W.

# Core Definition
If W is an FH-module for a subgroup H of G, the **induced module** (or induced representation) is Ind^G_H(W) = FG ⊗_{FH} W (p. 900). This is an FG-module of dimension [G:H] · dim_F W. The induced representation extends the action from H to all of G.

# Prerequisites
- **representation** — Starts with a representation of a subgroup
- **fg-module** — Uses tensor product of modules

# Key Properties
1. deg(Ind^G_H(W)) = [G:H] · deg(W)
2. Frobenius reciprocity: ⟨Ind^G_H χ, ψ⟩_G = ⟨χ, Res^G_H ψ⟩_H
3. The regular representation is induced from the trivial representation of {1}

# Relationships
## Enables
- **induced-character** — The character of the induced representation
- **frobenius-reciprocity** — Relates induction and restriction

# Source Reference
Chapter 19, Section 19.3, pages 900-910.

# Verification Notes
- Confidence: HIGH — explicit construction
