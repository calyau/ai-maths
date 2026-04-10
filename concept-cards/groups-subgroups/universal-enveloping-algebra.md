---
concept: Universal Enveloping Algebra
slug: universal-enveloping-algebra
category: lie-algebras
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 287
section: "6b Reduction to the case of an algebraically closed field"
extraction_confidence: high
aliases:
  - "U(g)"
prerequisites:
  - lie-algebra
  - representation-of-lie-algebra
extends: []
related:
  - casimir-operator
contrasts_with: []
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

The universal enveloping algebra U(g) of a Lie algebra g is the quotient of the tensor algebra T(g) by the relations x tensor y - y tensor x = [x,y]. Representations of g correspond exactly to modules over U(g).

# Core Definition

The **universal enveloping algebra** U(g) is constructed as the quotient of T(g) by the relations x tensor y - y tensor x = [x,y] for x,y in g (Milne, p. 287). The map g -> U(g) is injective, and any homomorphism g -> gl_V extends uniquely to U(g) -> End(V). Thus Rep_k(U(g)) = Rep_k(g) (isomorphism of categories, equation 157).

# Prerequisites

- **Lie algebra** -- U(g) is built from g
- **Representation of Lie algebra** -- U(g)-modules = g-modules

# Key Properties

1. g -> U(g) is injective
2. Rep_k(U(g)) -> Rep_k(g) is an isomorphism of categories (157)
3. The Casimir element lives in the centre of U(g) (Aside 6.9)
4. k' tensor U(g) = U(g_{k'}) for field extensions (p. 287)

# Context & Application

The universal enveloping algebra converts the study of Lie algebra representations into the study of associative algebra modules. This allows the use of tools from ring theory (e.g., semisimplicity of algebras) in representation theory.

# Examples

**Example 1** (p. 287): For the trivial Lie algebra k (one-dimensional, abelian), U(k) = k[x] (polynomial ring).

# Relationships

## Builds Upon
- **Lie algebra** -- U(g) is the universal associative algebra for g

## Related
- **Casimir operator** -- The Casimir element lives in Z(U(g))

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 6b, page 287.

# Verification Notes

- Definition source: Direct from p. 287
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
