---
concept: Representation of a Lie Algebra
slug: representation-of-lie-algebra
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 257
section: "2c Representations; stabilizers; isotropy groups"
extraction_confidence: high
aliases:
  - "g-module"
prerequisites:
  - lie-algebra
extends: []
related:
  - adjoint-representation-of-lie-algebra
  - universal-enveloping-algebra
  - weyls-theorem
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

A representation of a Lie algebra g on a vector space V is a homomorphism rho: g -> gl_V. The vector space V is then called a g-module, with action xv = rho(x)(v) satisfying [x,y]v = x(yv) - y(xv).

# Core Definition

A **representation** of a Lie algebra g on a k-vector space V is a homomorphism rho: g -> gl_V (Milne, p. 257). Thus rho sends x in g to a linear endomorphism rho(x) of V with rho([x,y]) = rho(x)rho(y) - rho(y)rho(x). V is called a **g-module** with notation xv = rho(x)(v). The representation is **faithful** if rho is injective.

# Prerequisites

- **Lie algebra** -- Representations are defined for Lie algebras

# Key Properties

1. [x,y]v = x(yv) - y(xv) (equation 140)
2. The stabilizer g_W = {x in g | xW is in W} is a Lie subalgebra (p. 258)
3. The isotropy algebra g_v = {x in g | xv = 0} is a Lie subalgebra
4. For G -> GL_V and char 0: W stable under G iff W stable under Lie(G) (Corollary 2.16)
5. Rep_k(G) -> Rep_k(g) is fully faithful for connected G in char 0 (Corollary 2.21)

# Context & Application

Representations of Lie algebras are more elementary than representations of algebraic groups but carry the same information in characteristic zero (for connected groups). The functor Rep(G) -> Rep(Lie(G)) identifies stable subspaces when G is connected and char(k) = 0.

# Examples

**Example 1** (p. 257): The adjoint representation ad: g -> gl_g sends x to the map y -> [x,y].

# Relationships

## Builds Upon
- **Lie algebra** -- Representations are homomorphisms to gl_V

## Enables
- **Weyl's theorem** -- Characterizes semisimple Lie algebras via representations
- **Universal enveloping algebra** -- g-modules = U(g)-modules

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 2c, pages 257-260.

# Verification Notes

- Definition source: Direct from p. 257
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
