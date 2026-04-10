---
concept: Shelah's Pigeon-Hole Principle
slug: shelahs-pigeon-hole-principle
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 209
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Lemma VI.24"
  - "Shelah function S(n,k)"
prerequisites:
  - hales-jewett-theorem
extends: []
related:
  - shelahs-theorem
contrasts_with: []
answers_questions:
  - "What is Shelah's pigeon-hole principle?"
---

# Quick Definition
Given n colourings c₁,...,cₙ of [m]^{2n−1} with k colours, if m is large enough, there exist 1 ≤ aⱼ < bⱼ ≤ m such that each cⱼ agrees at the "aⱼ" and "bⱼ" positions. The Shelah function S(n,k) is the minimal m.

# Core Definition
**Lemma 24** (Bollobás, p. 209): Given n and k, if m is large enough, then for any k-colourings c₁,...,cₙ of [m]^{2n−1}, there exist 1 ≤ aⱼ < bⱼ ≤ m such that for every j, cⱼ gives the same colour when position j takes value aⱼ vs. bⱼ (with other positions fixed).

The Shelah function: S(1,k) = k + 1 and S(n+1,k) ≤ k^{S(n,k)^{2n}} + 1.

# Prerequisites
- **Hales-Jewett theorem** — Shelah's principle is the key lemma for bounding it

# Key Properties
1. S(1,k) = k + 1
2. S(n+1,k) ≤ k^{S(n,k)^{2n}} + 1 (grows very fast but primitive recursively)
3. The proof uses induction on n, with pigeonhole at each step

# Relationships
## Enables
- **Shelah's theorem** — uses this as the key technical lemma

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Lemma 24, pages 209–210.

# Verification Notes
- Definition source: Direct lemma statement from p. 209
- Confidence rationale: Explicit lemma with proof
- Uncertainties: None
- Cross-reference status: Verified
