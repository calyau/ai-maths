---
concept: Cartan Subalgebra
slug: cartan-subalgebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 307
section: "Split semisimple Lie algebras"
extraction_confidence: high
aliases:
  - "splitting Cartan subalgebra"
  - "maximal toral subalgebra"
prerequisites:
  - semisimple-algebraic-group
extends: []
related:
  - split-semisimple-lie-algebra
  - root-space-decomposition
  - split-maximal-torus
contrasts_with: []
answers_questions:
  - "What is a Cartan subalgebra?"
---

# Quick Definition

A Cartan subalgebra of a semisimple Lie algebra is a maximal toral (abelian, ad-semisimple) subalgebra. It is the Lie algebra analogue of a maximal torus.

# Core Definition

A **Cartan subalgebra** of a semisimple Lie algebra 𝔤 is a maximal toral subalgebra, where "toral" means that ad_𝔤(x) is semisimple for every element x (Milne, Definition 2.13, p. 307).

A Cartan subalgebra 𝔥 is **splitting** if the eigenvalues of ad(h): 𝔤 → 𝔤 lie in k for all h ∈ 𝔥 (Definition 2.16, p. 308).

A toral subalgebra is a Cartan subalgebra if and only if it equals its own centralizer (Proposition 2.15).

# Prerequisites

- **Semisimple algebraic group** — Cartan subalgebras live inside semisimple Lie algebras

# Key Properties

1. Every toral Lie algebra is abelian (Proposition 2.12)
2. A Cartan subalgebra equals its own centralizer in 𝔤 (Proposition 2.15)
3. Any two splitting Cartan subalgebras are conjugate by an elementary automorphism (Theorem 2.18)
4. The common dimension of splitting Cartan subalgebras is the rank of 𝔤 (Definition 2.19)
5. For a maximal torus T in a semisimple group G, Lie(T) is a Cartan subalgebra (Example 2.14)

# Context & Application

Cartan subalgebras play the role in Lie algebra theory that maximal tori play for algebraic groups. The adjoint action of a Cartan subalgebra 𝔥 on 𝔤 gives the root space decomposition, from which the root system is extracted.

# Examples

**Example 1** (p. 308): The subalgebra of diagonal elements is a splitting Cartan subalgebra of sl_n.

**Example 2** (p. 308): For any split maximal torus T in a semisimple algebraic group G, Lie(T) is a splitting Cartan subalgebra of Lie(G).

# Relationships

## Enables
- **Root space decomposition** — Eigenspace decomposition of 𝔤 under ad(𝔥)
- **Split semisimple Lie algebra** — A pair (𝔤, 𝔥)

## Related
- **Split maximal torus** — The algebraic group analogue

# Common Confusions

- **Confusion**: The usual definition of Cartan subalgebra (nilpotent, self-normalizing) differs from the one given here
  **Clarification**: For semisimple Lie algebras, the two definitions are equivalent (Milne, footnote 2, p. 307)

# Source Reference

Chapter III, Section 2c, Definitions 2.13 and 2.16, pages 307–308.

# Verification Notes

- Definition source: Direct from Definition 2.13
- Confidence: HIGH — explicit definition
- Uncertainties: None
