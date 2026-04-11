---
concept: Character
slug: character
category: representation-theory
subcategory: character-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 862
section: "18.3 Character Theory and the Orthogonality Relations"
extraction_confidence: high
aliases:
  - "irreducible character"
  - "character of a representation"
prerequisites:
  - representation
extends: []
related:
  - character-table
  - orthogonality-relations
  - class-function
contrasts_with: []
answers_questions:
  - "What is a character of a representation?"
  - "How do characters relate to representations?"
---

# Quick Definition
The character χ of a representation φ: G → GL(V) is the function χ(g) = tr(φ(g)). Characters are class functions (constant on conjugacy classes) and completely determine representations over algebraically closed fields of characteristic 0.

# Core Definition
If φ: G → GL(V) is a representation of the finite group G over F, the **character** afforded by φ is the function χ: G → F defined by χ(g) = tr(φ(g)) (the trace of the matrix of φ(g)) (Definition, p. 862). The character is **irreducible** if the representation is irreducible. Characters are class functions, and over algebraically closed fields of characteristic 0, two representations are isomorphic iff they have the same character.

# Prerequisites
- **representation** — Characters are traces of representations

# Key Properties
1. χ(1) = degree of the representation
2. χ is constant on conjugacy classes (a class function)
3. Irreducible characters form a basis for the space of class functions
4. χ determines the representation up to isomorphism (char F = 0, F alg. closed)
5. χ(g^{-1}) = χ(g)̄ (complex conjugate, when F = C)

# Relationships
## Builds Upon
- **representation** — Characters encode representations

## Enables
- **character-table** — Organized collection of irreducible characters
- **orthogonality-relations** — Inner product relations among characters

# Source Reference
Chapter 18, Section 18.3, Definition and properties, pages 862-870.

# Verification Notes
- Confidence: HIGH — explicit definition with key properties
