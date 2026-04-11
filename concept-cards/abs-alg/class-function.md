---
concept: Class Function
slug: class-function
category: representation-theory
subcategory: character-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 864
section: "18.3 Character Theory and the Orthogonality Relations"
extraction_confidence: high
aliases: []
prerequisites:
  - group
extends: []
related:
  - character
  - orthogonality-relations
contrasts_with: []
answers_questions:
  - "What is a class function?"
---

# Quick Definition
A class function on G is a function f: G → F that is constant on conjugacy classes: f(g) = f(hgh^{-1}) for all g,h. The irreducible characters form a basis for the space of class functions.

# Core Definition
A function f: G → F is a **class function** if f(g) = f(xgx^{-1}) for all g,x ∈ G (Definition, p. 864). The class functions form a vector space of dimension equal to the number of conjugacy classes. The irreducible characters form an orthonormal basis with respect to the inner product ⟨f,g⟩ = (1/|G|)Σf(g)ḡ(g).

# Prerequisites
- **group** — Defined on finite groups

# Key Properties
1. Dimension = number of conjugacy classes
2. Characters are class functions
3. Irreducible characters form an orthonormal basis

# Source Reference
Chapter 18, Section 18.3, Definition, page 864.

# Verification Notes
- Confidence: HIGH — standard definition
