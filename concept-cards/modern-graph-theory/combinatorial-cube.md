---
concept: Combinatorial Cube
slug: combinatorial-cube
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 208
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "A^n"
  - "cube over alphabet A"
prerequisites: []
extends: []
related:
  - combinatorial-line
  - hales-jewett-theorem
contrasts_with: []
answers_questions:
  - "What is a combinatorial cube?"
---

# Quick Definition
The combinatorial cube A^n of dimension n over alphabet A is the set of all n-tuples from A: {(a₁,...,aₙ) : aᵢ ∈ A}. It has |A|^n elements and (|A|+1)^n − |A|^n combinatorial lines.

# Core Definition
For a finite set A and integer n ≥ 1, the cube of dimension n over alphabet A is A^n = A^{[n]} = {(a₁,...,aₙ) : aᵢ ∈ A for every i}. The cube [p]^n has p^n elements and (p+1)^n − p^n combinatorial lines (Bollobás, p. 208).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. |A^n| = |A|^n elements
2. Number of lines: (|A|+1)^n − |A|^n
3. [p]^2 has 2p + 1 lines: p vertical, p horizontal, 1 diagonal
4. The Hales-Jewett theorem guarantees monochromatic lines in A^n for large n

# Relationships
## Enables
- **Hales-Jewett theorem** — stated for cubes
- **Combinatorial line** — lines within cubes

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, page 208.

# Verification Notes
- Definition source: Direct from p. 208
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
