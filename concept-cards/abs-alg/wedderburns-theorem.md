---
concept: "Wedderburn's Theorem"
slug: wedderburns-theorem
category: representation-theory
subcategory: fundamental-theorems
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 854
section: "18.2 Wedderburn's Theorem and Some Consequences"
extraction_confidence: high
aliases:
  - "Wedderburn's theorem on semisimple rings"
  - "Artin-Wedderburn theorem"
prerequisites:
  - maschkes-theorem
  - schurs-lemma
extends: []
related:
  - character-table
contrasts_with: []
answers_questions:
  - "What is Wedderburn's theorem?"
  - "How does the group ring decompose?"
---

# Quick Definition
If char F does not divide |G|, the group ring FG is isomorphic to a direct product of matrix rings: FG ≅ M_{n_1}(D_1) × ··· × M_{n_r}(D_r) where the D_i are division rings.

# Core Definition
**Wedderburn's Theorem** (p. 854): A ring R in which every module is completely reducible (a semisimple ring) is isomorphic to a finite direct product of matrix rings over division rings: R ≅ M_{n_1}(D_1) × ··· × M_{n_r}(D_r). Applied to FG when char F ∤ |G| (via Maschke's theorem): FG ≅ M_{n_1}(D_1) × ··· × M_{n_r}(D_r). Over algebraically closed F: FG ≅ M_{n_1}(F) × ··· × M_{n_r}(F) and |G| = n_1^2 + ··· + n_r^2.

# Prerequisites
- **maschkes-theorem** — Makes FG semisimple
- **schurs-lemma** — Identifies endomorphism algebras

# Key Properties
1. r = number of irreducible representations = number of conjugacy classes (over alg. closed F)
2. n_i = degree of the i-th irreducible representation
3. |G| = Σn_i^2 (dimension formula)
4. Z(FG) has dimension equal to the number of conjugacy classes

# Relationships
## Builds Upon
- **maschkes-theorem** — Ensures semisimplicity of FG
- **schurs-lemma** — Determines the division rings D_i

## Enables
- **character-table** — The decomposition determines the character theory

# Source Reference
Chapter 18, Section 18.2, Wedderburn's Theorem and corollaries, pages 854-862.

# Verification Notes
- Confidence: HIGH — major structure theorem with proof
