---
concept: Irreducible Representation
slug: irreducible-representation
category: representation-theory
subcategory: linear-representations
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 848
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases:
  - "simple FG-module"
prerequisites:
  - fg-module
extends: []
related:
  - completely-reducible-module
  - schurs-lemma
contrasts_with: []
answers_questions:
  - "What is an irreducible representation?"
---

# Quick Definition
A representation (or FG-module) is irreducible if it has no proper nonzero G-stable subspaces. These are the building blocks of representation theory.

# Core Definition
An FG-module V is **irreducible** (or **simple**) if V ≠ 0 and V has no FG-submodules other than 0 and V (p. 848). Equivalently, the corresponding representation has no proper nonzero G-stable subspace.

# Prerequisites
- **fg-module** — Irreducible means simple as an FG-module

# Key Properties
1. Every degree 1 representation is irreducible
2. By Schur's Lemma, Hom_FG(V,W) = 0 if V, W are nonisomorphic irreducibles
3. Over algebraically closed F with char F ∤ |G|: number of irreducible representations = number of conjugacy classes

# Relationships
## Enables
- **completely-reducible-module** — Built from irreducibles via Maschke's theorem
- **character** — Characters of irreducible representations are key tools

# Source Reference
Chapter 18, Section 18.1, Definition, page 848.

# Verification Notes
- Confidence: HIGH — standard definition
