---
concept: Ideal of a Lie Algebra
slug: ideal-of-lie-algebra
category: lie-algebras
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 241
section: "1b The isomorphism theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra
extends: []
related:
  - quotient-lie-algebra
contrasts_with:
  - lie-subalgebra
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

An ideal in a Lie algebra g is a subspace a such that [x,a] is in a for all x in g and a in a. Ideals are the kernels of homomorphisms, and the quotient g/a inherits a natural Lie algebra structure.

# Core Definition

An **ideal** in a Lie algebra g is a subspace a such that [g,a] is contained in a (Milne, p. 241). The quotient g/a becomes a Lie algebra with [x+a, y+a] = [x,y]+a. The standard isomorphism theorems hold (1.5-1.8).

# Prerequisites

- **Lie algebra** -- Ideals are a fundamental concept in Lie algebra theory

# Key Properties

1. The kernel of any homomorphism is an ideal (1.5)
2. Every ideal is the kernel of the quotient map g -> g/a (1.5)
3. If h and a are subalgebras with [h,a] in a, then h+a is a subalgebra and h/(h cap a) = (h+a)/a (1.7)
4. Normal algebraic subgroups of G correspond to ideals in Lie(G) (in char 0)

# Examples

**Example 1** (p. 241): The centre z(g) = {x in g | [x,g] = 0} is an ideal.

# Relationships

## Builds Upon
- **Lie algebra** -- Ideals are substructures of Lie algebras

## Contrasts With
- **Lie subalgebra** -- A subalgebra has [s,s] in s; an ideal has [g,a] in a

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1b, page 241.

# Verification Notes

- Definition source: Direct from p. 241
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
