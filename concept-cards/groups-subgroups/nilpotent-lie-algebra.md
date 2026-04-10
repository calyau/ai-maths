---
concept: Nilpotent Lie Algebra
slug: nilpotent-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 264
section: "3a Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra
  - ideal-of-lie-algebra
extends: []
related:
  - solvable-lie-algebra
  - engels-theorem
  - unipotent-algebraic-group
contrasts_with:
  - solvable-lie-algebra
answers_questions:
  - "What distinguishes a nilpotent Lie algebra from a solvable Lie algebra?"
---

# Quick Definition

A Lie algebra g is nilpotent if its descending central series g > [g,g] > [g,[g,g]] > ... terminates with zero -- equivalently, if iterated brackets of sufficiently many elements always vanish.

# Core Definition

A Lie algebra g is **nilpotent** if it admits a filtration g = a_0 > a_1 > ... > a_r = 0 by ideals such that each a_i/a_{i+1} is contained in the centre of g/a_{i+1} (Milne, Definition 3.1). Equivalently, the **descending central series** g > g^1 = [g,g] > g^2 = [g,g^1] > ... > g^{i+1} = [g,g^i] > ... terminates with zero (Proposition 3.2).

# Prerequisites

- **Lie algebra** -- Nilpotent is a property of Lie algebras
- **Ideal of Lie algebra** -- The filtration consists of ideals

# Key Properties

1. Nilpotent implies solvable, but not conversely
2. Subalgebras and quotients of nilpotent algebras are nilpotent (Proposition 3.6a)
3. g is nilpotent iff ad(x) is nilpotent for every x in g (Engel's theorem, 3.9)
4. An extension of nilpotent algebras is solvable but not necessarily nilpotent (3.7)
5. In char 0, the category of nilpotent Lie algebras is equivalent to the category of unipotent algebraic groups (Theorem 4.7)

# Context & Application

Nilpotent Lie algebras are the Lie algebra counterpart of unipotent algebraic groups. In characteristic zero, the Hausdorff series provides an explicit equivalence between the two categories: given a nilpotent Lie algebra g, the group structure on g_a defined by the Hausdorff formula is a unipotent group with Lie algebra g.

# Examples

**Example 1** (p. 264): n_n (strictly upper triangular matrices) is nilpotent.

**Example 2** (p. 264): <x,y,z | [x,y] = z, [x,z] = [y,z] = 0> (the Heisenberg algebra) is nilpotent.

**Example 3** (p. 264): b_n (upper triangular matrices) is solvable but NOT nilpotent for n >= 3.

# Relationships

## Builds Upon
- **Lie algebra** -- Nilpotent is a property of Lie algebras

## Enables
- **Unipotent algebraic group** -- In char 0, nilpotent Lie algebras <-> unipotent groups

## Contrasts With
- **Solvable Lie algebra** -- Every nilpotent algebra is solvable; the converse fails

# Common Errors

- **Error**: Confusing the descending central series g^i = [g, g^{i-1}] with the derived series g^{(i)} = [g^{(i-1)}, g^{(i-1)}]
  **Correction**: The descending central series tests nilpotency; the derived series tests solvability

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Sections 3a-3b, pages 264-267.

# Verification Notes

- Definition source: Direct from Definition 3.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
