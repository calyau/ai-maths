---
concept: Stabilizer
slug: stabilizer
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
  - "isotropy subgroup"
prerequisites:
  - group-action
extends: []
related:
  - orbit
  - counting-formula
  - centralizer
contrasts_with: []
answers_questions:
  - "What is the stabilizer of an element under a group action?"
  - "How do orbits and stabilizers relate via the counting formula?"
---

# Quick Definition

The stabilizer G_s of an element s is the subgroup of G consisting of all elements that fix s: G_s = {g in G | gs = s}. It is a subgroup of G whose index equals the orbit size.

# Core Definition

The stabilizer of an element s of S is the set G_s = {g in G | gs = s} (Artin, (6.7.6), p. 189). It is a subgroup of G. If as = s', then the stabilizer of s' is the conjugate subgroup aG_s a^{-1} (Proposition 6.7.7(b)). The stabilizer tells us when two group elements act the same on s: as = bs iff a^{-1}b is in G_s (Proposition 6.7.7(a)).

# Prerequisites

- **Group action** — Stabilizers arise from group actions

# Key Properties

1. G_s is a subgroup of G
2. |G| = |G_s| * |O_s| (Counting Formula)
3. Elements in the same orbit have conjugate stabilizers
4. as = bs iff b is in the coset aG_s
5. G_s = G iff s is a fixed point

# Construction / Recognition

## To Compute:
1. Check which group elements fix the given element s
2. These form the stabilizer subgroup G_s

# Context & Application

Stabilizers measure "how much symmetry" a particular element has. The stabilizer of a vertex of a regular polygon is the group of symmetries fixing that vertex. The orbit-stabilizer relation |G| = |G_s| * |O_s| is one of the most useful counting tools in group theory.

# Examples

**Example 1** (p. 189): The stabilizer of the origin for the isometry group M is isomorphic to O_2.

**Example 2** (p. 189): The stabilizer of the index n for S_n is isomorphic to S_{n-1}.

**Example 3** (p. 189): The stabilizer of an equilateral triangle in the plane (under M) is its symmetry group D_3.

# Relationships

## Builds Upon
- **Group action** — Stabilizers are defined from actions

## Enables
- **Counting formula** — |G| = |G_s| * |O_s|
- **Operation on cosets** — G acts on G/G_s

## Related
- **Centralizer** — Stabilizer for the conjugation action

# Common Errors

- **Error**: Confusing "stabilizes a set U" with "fixes every element of U"
  **Correction**: Stabilizing U means gU = U (permutes elements within U); fixing means gu = u for all u in U

# Common Confusions

- **Confusion**: Thinking elements in different orbits can have the same stabilizer
  **Clarification**: Stabilizers of elements in the same orbit are conjugate; elements in different orbits may have non-conjugate stabilizers

# Source Reference

Chapter 6: Symmetry, Section 6.7, (6.7.6), Proposition 6.7.7, pages 189-190.

# Verification Notes

- Definition source: Direct from (6.7.6)
- Confidence rationale: Explicitly defined with properties
- Uncertainties: None
- Cross-reference status: Verified
