---
concept: Elementary Automorphism
slug: elementary-automorphism
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 306
section: "Elementary automorphisms of a Lie algebra"
extraction_confidence: high
aliases:
  - "Aut_e(𝔤)"
prerequisites:
  - split-semisimple-lie-algebra
extends: []
related:
  - cartan-subalgebra
contrasts_with: []
answers_questions:
  - "What is an elementary automorphism of a Lie algebra?"
---

# Quick Definition

An elementary automorphism of a Lie algebra 𝔤 is a finite product of automorphisms of the form e^{ad(x)} where x ∈ 𝔤 with ad(x) nilpotent. They form a normal subgroup Aut_e(𝔤) of Aut(𝔤).

# Core Definition

If x is an element of a Lie algebra 𝔤 such that ad(x) is nilpotent, then e^{ad(x)} = ∑_{n≥0} ad(x)^n/n! is an automorphism of 𝔤 (Milne, 2.2–2.4, pp. 306–307). A finite product of such automorphisms is called **elementary**. The elementary automorphisms form a normal subgroup Aut_e(𝔤) of Aut(𝔤).

# Prerequisites

- **Split semisimple Lie algebra** — Elementary automorphisms conjugate Cartan subalgebras

# Key Properties

1. Any two splitting Cartan subalgebras are conjugate by an elementary automorphism (Theorem 2.18)
2. Aut_e(𝔤) is normal in Aut(𝔤) since u·e^{ad(x)}·u⁻¹ = e^{ad(ux)}
3. When 𝔤 is semisimple, Aut_e(𝔤) equals its own derived group

# Source Reference

Chapter III, Section 2a, 2.1–2.4, pages 306–307.

# Verification Notes

- Definition source: Direct from 2.4
- Confidence: HIGH
- Uncertainties: None
