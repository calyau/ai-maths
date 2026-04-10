---
concept: Ultrafilter Proof Technique
slug: ultrafilter-proof
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
  - "Glazer's proof"
  - "idempotent ultrafilter"
prerequisites:
  - ramsey-theorem-infinite
extends: []
related:
  - hindmans-theorem
contrasts_with: []
answers_questions:
  - "How are ultrafilters used in Ramsey theory?"
---

# Quick Definition
Ultrafilters on ℕ provide elegant proofs of Ramsey-type results. A nonprincipal ultrafilter gives a simple proof of the infinite Ramsey theorem for r=2. An idempotent ultrafilter (P + P = P) in βℕ gives Glazer's proof of Hindman's theorem.

# Core Definition
An **ultrafilter** U on ℕ is a maximal filter: a non-empty collection of subsets closed under intersection and superset, with ∅ ∉ U, such that for every A ⊂ ℕ, either A ∈ U or ℕ \ A ∈ U. The set βℕ of all ultrafilters is a compact semigroup under U + V = {A ⊂ ℕ : {n ∈ ℕ : A − n ∈ U} ∈ V}. An **idempotent** P with P + P = P exists by a topological fixed-point argument, and Glazer used this to prove Hindman's theorem (Bollobás, pp. 219–221).

# Prerequisites
- **Ramsey theorem (infinite)** — ultrafilters provide alternative proofs

# Key Properties
1. Every ultrafilter defines a finitely additive {0,1}-measure on 2^ℕ
2. Nonprincipal ultrafilters contain no finite sets
3. βℕ is a compact right-topological semigroup
4. Idempotent elements exist in βℕ
5. The idempotent property A ∈ P ⟹ {n : A − n ∈ P} ∈ P drives the proof

# Context & Application
Ultrafilter methods in Ramsey theory illustrate how algebra and topology can solve combinatorial problems. Glazer's proof of Hindman's theorem is "at least as beautiful as the theorem and considerably more surprising."

# Relationships
## Enables
- **Hindman's theorem** — Glazer's proof

# Source Reference
Chapter VI: Ramsey Theory, Section VI.5, pages 219–221.

# Verification Notes
- Definition source: Direct from pp. 219–221
- Confidence rationale: Explicitly discussed with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
