---
concept: Borel Subalgebra
slug: borel-subalgebra-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 313
section: "Subalgebras of split semisimple Lie algebras"
extraction_confidence: high
aliases: []
prerequisites:
  - split-semisimple-lie-algebra
  - base-of-root-system
  - positive-root
extends: []
related:
  - borel-subgroup
  - parabolic-subgroup
contrasts_with: []
answers_questions:
  - "What is a Borel subalgebra?"
  - "How do Borel subgroups relate to parabolic subgroups?"
---

# Quick Definition

A Borel subalgebra of a split semisimple Lie algebra (𝔤, 𝔥) is a maximal solvable subalgebra containing 𝔥. It has the form 𝔟 = 𝔥 ⊕ ⊕_{α>0} 𝔤^α for some base S of R.

# Core Definition

Let (𝔤, 𝔥) be a split semisimple Lie algebra. A **Borel subalgebra** of (𝔤, 𝔥) is a maximal solvable subalgebra of 𝔤 containing 𝔥. More generally, a Borel subalgebra of a semisimple Lie algebra 𝔤 is one that becomes a Borel subalgebra of (𝔤, 𝔥) for some splitting Cartan subalgebra 𝔥 (Milne, Definition 2.33, p. 313).

The Borel subalgebras containing 𝔥 are exactly the subalgebras 𝔟(S) = 𝔥 ⊕ ⊕_{α∈R⁺} 𝔤^α for bases S of R.

# Prerequisites

- **Split semisimple Lie algebra** — Borel subalgebras are defined in this context
- **Base of root system** — Each base determines a Borel subalgebra
- **Positive root** — The Borel subalgebra uses positive root spaces

# Key Properties

1. 𝔟(S) determines R⁺ and hence S
2. Borel subalgebras are in bijection with bases of R (and hence Weyl chambers)
3. A Borel subalgebra is a maximal closed subset P with P ∩ (−P) = ∅

# Examples

**Example 1** (p. 313): For sl_{n+1}, the Borel subalgebra for the standard base consists of upper triangular matrices of trace 0.

# Relationships

## Enables
- **Borel subgroup** — The algebraic group analogue

## Related
- **Parabolic subgroup** — Contains a Borel subalgebra/subgroup

# Source Reference

Chapter III, Section 2i, Definition 2.33, pages 313–314.

# Verification Notes

- Definition source: Direct from Definition 2.33
- Confidence: HIGH
- Uncertainties: None
