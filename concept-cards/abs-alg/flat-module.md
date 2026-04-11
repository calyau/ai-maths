---
concept: Flat Module
slug: flat-module
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 414
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases: []
prerequisites:
  - tensor-product
  - exact-sequence
extends: []
related:
  - projective-module
  - injective-module
contrasts_with: []
answers_questions:
  - "What is a flat module?"
---

# Quick Definition
A right R-module A is flat if the functor $A \otimes_R \_$ is exact, meaning tensoring with A preserves injections.

# Core Definition
A right R-module A is called flat if for any injective map $\psi: L \to M$ of left R-modules, the induced map $1 \otimes \psi: A \otimes_R L \to A \otimes_R M$ is also injective. Equivalently, $A \otimes_R \_$ takes short exact sequences to short exact sequences (Dummit & Foote, Proposition 40, p. 414).

# Prerequisites
- **tensor-product** — Flatness is a property of the tensor product functor
- **exact-sequence** — Flat = tensor product preserves exactness

# Key Properties
1. Free modules are flat (Corollary 42)
2. Projective modules are flat (Corollary 42)
3. $\mathbb{Q}$ is a flat $\mathbb{Z}$-module (but not projective)
4. Over a PID, flat = torsion-free
5. $\mathbb{Z}/n\mathbb{Z}$ is NOT flat over $\mathbb{Z}$ for $n \geq 2$
6. $\mathbb{Q}/\mathbb{Z}$ is injective but NOT flat
7. The tensor product of flat modules over a commutative ring is flat

# Context & Application
Flatness lies between free and general modules: free $\Rightarrow$ projective $\Rightarrow$ flat, but none of the converses hold in general. The $\mathbb{Z}$-module $\mathbb{Q}$ is flat but not projective; $\mathbb{Q}/\mathbb{Z}$ is injective but not flat.

# Examples
**Example 1** (p. 415): $\mathbb{Z}$ is flat over $\mathbb{Z}$ (projective). $\mathbb{Z}/2\mathbb{Z}$ is NOT flat.
**Example 2** (p. 415): $\mathbb{Q}$ is flat over $\mathbb{Z}$ (torsion-free).
**Example 3** (p. 415): $\mathbb{Q}/\mathbb{Z}$ is injective but not flat.

# Relationships
## Builds Upon
- **tensor-product**, **exact-sequence**

## Related
- **projective-module** — Projective implies flat
- **injective-module** — Neither implies the other with flat

# Source Reference
Chapter 10, Section 10.5, Proposition 40, pp. 414-417. See Corollary 42.

# Verification Notes
- Confidence: HIGH — explicit definition with hierarchy established
