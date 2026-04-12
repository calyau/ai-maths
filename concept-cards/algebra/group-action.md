---
concept: Group Action
slug: group-action
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.7 Abstract Symmetry: Group Operations"
extraction_confidence: high
aliases:
  - "group operation"
  - "G-action"
  - "G-set"
prerequisites: []
extends: []
related:
  - orbit
  - stabilizer
  - transitive-action
  - faithful-action
  - permutation-representation
  - counting-formula
contrasts_with: []
answers_questions:
  - "What is a group action?"
  - "How do orbits and stabilizers relate via the counting formula?"
---

# Quick Definition

An operation (action) of a group G on a set S is a map G x S -> S, written (g, s) -> gs, satisfying 1*s = s and (gg')s = g(g's) for all g, g' in G and s in S. Each group element acts as a permutation of S.

# Core Definition

An operation of a group G on a set S is a map G x S -> S satisfying: (a) 1*s = s for all s in S, and (b) the associative law (gg')*s = g*(g'*s) for all g, g' in G and all s in S (Artin, (6.7.1), p. 187). For each g in G, left multiplication m_g: S -> S defined by m_g(s) = gs is a permutation (bijection) of S.

# Prerequisites

This concept requires only basic group theory from earlier chapters.

# Key Properties

1. Each group element acts as a permutation of S
2. The action decomposes S into orbits
3. Each element s has a stabilizer subgroup G_s
4. The Counting Formula relates |G|, |G_s|, and |O_s|
5. An action corresponds bijectively to a permutation representation G -> Perm(S)

# Construction / Recognition

## To Define an Action:
1. Specify how each generator of G acts on S
2. Verify the axioms: identity acts trivially, and the associative law holds

## To Recognize:
1. A rule assigning to each group element a permutation of S
2. Consistent with the group multiplication

# Context & Application

Group actions are one of the most powerful tools in algebra. They generalize the notion of symmetry from geometry to arbitrary algebraic structures. Artin introduces them via the concrete example of isometries acting on the plane before giving the abstract definition. Important examples include: conjugation (Chapter 7), action on cosets (Section 6.8), action on subsets (Section 6.10).

# Examples

**Example 1** (p. 187): The isometry group M acts on the set of points, lines, and triangles in the plane.

**Example 2** (p. 187): The symmetric group S_n acts on the set {1, ..., n}.

**Example 3** (p. 188): The orbit of a triangle under M is the set of all congruent triangles.

# Relationships

## Enables
- **Orbit** — The G-orbit of an element s
- **Stabilizer** — The subgroup fixing s
- **Counting formula** — |G| = |G_s| * |O_s|
- **Permutation representation** — Homomorphism G -> Perm(S)

## Related
- **Transitive action** — Only one orbit
- **Faithful action** — Only the identity fixes everything

# Common Errors

- **Error**: Confusing the stabilizer of a subset with pointwise fixing
  **Correction**: The stabilizer of a subset U consists of g with gU = U (set preserved), not gu = u for all u in U

# Common Confusions

- **Confusion**: Thinking every action must be faithful
  **Clarification**: An action's kernel (elements acting trivially on all of S) can be nontrivial

# Source Reference

Chapter 6: Symmetry, Section 6.7, (6.7.1), pages 187-190.

# Verification Notes

- Definition source: Direct from (6.7.1)
- Confidence rationale: Core concept, extensively developed
- Uncertainties: None
- Cross-reference status: Verified
