---
concept: Hindman's Theorem
slug: hindmans-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 219
section: "VI.5 Subsequences"
extraction_confidence: high
aliases:
  - "Theorem VI.32"
  - "finite sums theorem"
prerequisites:
  - ramsey-theorem-infinite
  - galvin-prikry-theorem
extends: []
related:
  - rados-theorem
  - ultrafilter-proof
contrasts_with: []
answers_questions:
  - "Does every colouring of ℕ have an infinite set with monochromatic finite sums?"
---

# Quick Definition
For any k-colouring of ℕ, there is an infinite set A ⊂ ℕ such that all finite subset sums Σ_{x∈X} x (∅ ≠ X ⊂ A) have the same colour.

# Core Definition
**Theorem 32** (Bollobás, p. 219): For any k-colouring of ℕ there is an infinite set A ⊂ ℕ such that all sums Σ_{x∈X} x, ∅ ≠ X ⊂ A, have the same colour. This was conjectured by Graham and Rothschild and first proved by Hindman (1974). The elegant proof by Glazer uses idempotent ultrafilters in βℕ (the Stone-Čech compactification of ℕ).

# Prerequisites
- **Ramsey theorem (infinite)** — Hindman's theorem extends Ramsey-type results
- **Galvin-Prikry theorem** — related topological Ramsey theory

# Key Properties
1. All finite subset sums from A are monochromatic
2. Glazer's proof uses an idempotent ultrafilter P (P + P = P)
3. The idempotent exists by a topological fixed-point argument in βℕ
4. Extends results about monochromatic sums from Rado's theorem

# Context & Application
Hindman's theorem is one of the most beautiful results in infinite Ramsey theory. Glazer's proof using ultrafilters in βℕ is "at least as beautiful as the theorem and considerably more surprising" (p. 219). It illustrates how algebra and topology interact with combinatorics.

# Examples
**Example** (p. 219): The proof constructs a₁ ∈ A₁ ∈ P, then a₂ ∈ A₂ ⊂ A₁ \ {a₁} with a₁ + A₂ ⊂ A₁, etc. The set A = {a₁, a₂, ...} has all finite sums in the same colour class.

# Relationships
## Related
- **Rado's theorem** — finite version of monochromatic sums is a consequence
- **Ultrafilter proof** — Glazer's technique

# Source Reference
Chapter VI: Ramsey Theory, Section VI.5, Theorem 32, pages 219–221.

# Verification Notes
- Definition source: Direct theorem statement from p. 219
- Confidence rationale: Explicit theorem with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
