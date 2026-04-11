---
concept: Orthogonality Relations
slug: orthogonality-relations
category: representation-theory
subcategory: character-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 866
section: "18.3 Character Theory and the Orthogonality Relations"
extraction_confidence: high
aliases:
  - "first orthogonality relation"
  - "second orthogonality relation"
prerequisites:
  - character
  - schurs-lemma
extends: []
related:
  - character-table
  - class-function
contrasts_with: []
answers_questions:
  - "What are the orthogonality relations for characters?"
---

# Quick Definition
The irreducible characters satisfy (1/|G|)Σ_{g∈G} χ_i(g)χ_j(g)̄ = δ_{ij}. Column orthogonality: Σ_i χ_i(g)χ_i(h)̄ = |C_G(g)|δ_{g~h}.

# Core Definition
Define the inner product ⟨χ,ψ⟩ = (1/|G|)Σ_{g∈G} χ(g)ψ(g)̄. The **first (row) orthogonality relation**: ⟨χ_i,χ_j⟩ = δ_{ij} — the irreducible characters form an orthonormal set (p. 866). The **second (column) orthogonality relation**: Σ_{i=1}^r χ_i(g)χ_i(h)̄ = |C_G(g)| if g and h are conjugate, 0 otherwise.

# Prerequisites
- **character** — The orthogonality is among characters
- **schurs-lemma** — Used in the proof

# Key Properties
1. Irreducible characters form an orthonormal basis of class functions
2. ⟨χ,χ⟩ = 1 iff χ is irreducible
3. Multiplicity of an irreducible χ_i in χ equals ⟨χ,χ_i⟩
4. Column orthogonality relates to centralizer sizes

# Relationships
## Enables
- **character-table** — Orthogonality constrains and determines the table

# Source Reference
Chapter 18, Section 18.3, Theorems and properties, pages 866-870.

# Verification Notes
- Confidence: HIGH — explicitly stated and proved
