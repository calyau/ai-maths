---
concept: "Schur's Lemma"
slug: schurs-lemma
category: representation-theory
subcategory: fundamental-theorems
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 852
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - irreducible-representation
extends: []
related:
  - wedderburns-theorem
contrasts_with: []
answers_questions:
  - "What does Schur's Lemma say about homomorphisms between irreducible representations?"
---

# Quick Definition
Any nonzero FG-homomorphism between irreducible FG-modules is an isomorphism. Over algebraically closed F, the only FG-endomorphisms of an irreducible module are scalars.

# Core Definition
**Schur's Lemma** (p. 852): (1) If V and W are irreducible FG-modules and φ: V → W is a nonzero FG-homomorphism, then φ is an isomorphism. (2) If F is algebraically closed and V is an irreducible FG-module, then End_FG(V) = F (every FG-endomorphism is a scalar multiple of the identity).

# Prerequisites
- **irreducible-representation** — Applies to irreducible modules

# Key Properties
1. Hom_FG(V,W) = 0 for nonisomorphic irreducibles
2. End_FG(V) is a division ring (by (1))
3. Over algebraically closed fields: End_FG(V) = F

# Relationships
## Enables
- **wedderburns-theorem** — Schur's Lemma is essential to the structure theory
- **orthogonality-relations** — Used in proving orthogonality of characters

# Source Reference
Chapter 18, Section 18.1, Schur's Lemma, page 852.

# Verification Notes
- Confidence: HIGH — named lemma with proof
