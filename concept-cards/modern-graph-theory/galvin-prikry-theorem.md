---
concept: Galvin-Prikry Theorem
slug: galvin-prikry-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 217
section: "VI.5 Subsequences"
extraction_confidence: high
aliases:
  - "Theorem VI.29"
  - "open sets are Ramsey"
prerequisites:
  - ramsey-theorem-infinite
extends:
  - ramsey-theorem-infinite
related:
  - hindmans-theorem
contrasts_with: []
answers_questions:
  - "Are open subsets of 2^ℕ Ramsey?"
---

# Quick Definition
Every open subset of 2^ℕ (the power set with product topology) is Ramsey: for any open F ⊂ 2^ℕ, there exists an infinite M ⊂ ℕ with M^(ω) ⊂ F or M^(ω) ⊂ 2^ℕ \ F.

# Core Definition
**Theorem 29** (Bollobás, p. 218): Every open subset of 2^ℕ is Ramsey. A family F ⊂ 2^ℕ is **Ramsey** if there exists M ∈ ℕ^(ω) such that either M^(ω) ⊂ F or M^(ω) ⊂ 2^ℕ − F. The proof uses Lemma 28: if ℕ rejects ∅ (no infinite subset accepts ∅), construct M rejecting every X ⊂ M; then openness of F forces M^(ω) ⊂ 2^ℕ − F.

# Prerequisites
- **Ramsey theorem (infinite)** — extended by this result

# Key Properties
1. Not every subset of ℕ^(ω) is Ramsey (Exercise 45)
2. Open sets are Ramsey (this theorem)
3. Sets "insensitive to small changes" (open sets) are Ramsey
4. Implies results about subsequences of functions (application at start of §5)

# Context & Application
The Galvin-Prikry theorem connects Ramsey theory to topology. It provides the foundation for infinite Ramsey theory with structural constraints.

# Relationships
## Builds Upon
- **Ramsey theorem (infinite)** — generalized to topological setting

## Enables
- **Hindman's theorem** — via ultrafilter techniques
- Corollaries about thin and dense families

# Source Reference
Chapter VI: Ramsey Theory, Section VI.5, Theorem 29, pages 217–218.

# Verification Notes
- Definition source: Direct theorem statement from p. 218
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
