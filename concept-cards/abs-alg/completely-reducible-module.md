---
concept: Completely Reducible Module
slug: completely-reducible-module
category: representation-theory
subcategory: linear-representations
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 849
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases:
  - "semisimple module"
  - "completely reducible representation"
prerequisites:
  - irreducible-representation
extends: []
related:
  - maschkes-theorem
contrasts_with: []
answers_questions:
  - "What is a completely reducible representation?"
---

# Quick Definition
An FG-module is completely reducible (semisimple) if it is a direct sum of irreducible submodules. By Maschke's theorem, every FG-module is completely reducible when char F does not divide |G|.

# Core Definition
An FG-module V is **completely reducible** (or **semisimple**) if V is a direct sum of irreducible FG-submodules (p. 849). Equivalently, every submodule has a complement.

# Prerequisites
- **irreducible-representation** — The summands must be irreducible

# Key Properties
1. Equivalent to every submodule having a complement
2. By Maschke's theorem: guaranteed when char F ∤ |G|
3. Decomposition into irreducibles is essentially unique (Krull-Schmidt)

# Relationships
## Builds Upon
- **irreducible-representation** — Direct sum of irreducibles

## Related
- **maschkes-theorem** — Guarantees complete reducibility

# Source Reference
Chapter 18, Section 18.1, page 849.

# Verification Notes
- Confidence: HIGH — standard definition
