---
concept: Highest Weight Representation
slug: highest-weight-representation
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 314
section: "Representations of split semisimple Lie algebras"
extraction_confidence: high
aliases:
  - "highest weight module"
prerequisites:
  - split-semisimple-lie-algebra
  - dominant-weight
  - borel-subalgebra-lie-algebra
extends: []
related:
  - representations-of-split-reductive-groups
contrasts_with: []
answers_questions:
  - "What is a highest weight representation?"
  - "What must I know before understanding representations of split reductive groups?"
---

# Quick Definition

Every simple module over a semisimple Lie algebra has a unique highest weight (a dominant weight), and this establishes a bijection between isomorphism classes of simple modules and the set P₊₊ of dominant weights.

# Core Definition

Let (𝔤, 𝔥) be a split semisimple Lie algebra with Borel subalgebra 𝔟 attached to a base S. For a simple 𝔤-module V (Milne, Theorems 2.37–2.39, p. 314):

(a) There is a unique one-dimensional subspace L stabilized by 𝔟.
(b) L = V_{ϖ_V} is a weight space for 𝔥, with weight ϖ_V called the **highest weight**.
(c) ϖ_V is dominant (ϖ_V ∈ P₊₊).
(d) Every other weight ϖ of V satisfies ϖ = ϖ_V − ∑ m_α α with m_α ∈ ℕ.

Moreover, V ↦ ϖ_V is a bijection from isomorphism classes of simple 𝔤-modules onto P₊₊.

# Prerequisites

- **Split semisimple Lie algebra** — The representation theory requires this structure
- **Dominant weight** — Highest weights are dominant
- **Borel subalgebra** — Stabilizes the highest weight line

# Key Properties

1. Every dominant weight occurs as a highest weight (Theorem 2.38)
2. Two simple modules are isomorphic iff they have the same highest weight (Theorem 2.39)
3. End(V, r) ≅ k for any simple module V (Corollary 2.40)

# Examples

**Example 1** (p. 315): For sl(W) with dim W = n+1, the simple module with highest weight ϖ_r (the r-th fundamental weight) is ∧^r W.

# Source Reference

Chapter III, Section 2k, Theorems 2.37–2.39, pages 314–316.

# Verification Notes

- Definition source: Direct from Theorems 2.37–2.39
- Confidence: HIGH
- Uncertainties: None
