---
concept: "Maschke's Theorem"
slug: maschkes-theorem
category: representation-theory
subcategory: fundamental-theorems
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 849
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - fg-module
  - completely-reducible-module
extends: []
related:
  - wedderburns-theorem
contrasts_with: []
answers_questions:
  - "When is every FG-module completely reducible?"
---

# Quick Definition
If F is a field whose characteristic does not divide |G|, then every FG-module is completely reducible. The converse also holds.

# Core Definition
**Maschke's Theorem** (p. 849): Let G be a finite group and F a field. If char F does not divide |G|, then every FG-module is completely reducible. Conversely, if char F divides |G|, then FG is not completely reducible. The key idea: given a G-stable subspace W ⊆ V, average any projection onto W over the group to get a G-equivariant projection.

# Prerequisites
- **fg-module** — Applies to FG-modules
- **completely-reducible-module** — Guarantees this property

# Key Properties
1. char F ∤ |G| ⟹ all FG-modules are semisimple
2. char F | |G| ⟹ FG itself is NOT semisimple
3. The averaging trick produces G-equivariant projections
4. Foundation for all of ordinary representation theory

# Relationships
## Enables
- **wedderburns-theorem** — Combined with Maschke gives the Wedderburn decomposition of FG

# Source Reference
Chapter 18, Section 18.1, Theorem (Maschke's Theorem), pages 849-850.

# Verification Notes
- Confidence: HIGH — named theorem with proof
