---
concept: Orbit
slug: orbit
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
  - "G-orbit"
prerequisites:
  - group-action
extends: []
related:
  - stabilizer
  - counting-formula
  - transitive-action
contrasts_with: []
answers_questions:
  - "What is an orbit of a group action?"
  - "How do orbits and stabilizers relate via the counting formula?"
---

# Quick Definition

The orbit O_s of an element s under a group action is the set of all elements that s can be sent to: O_s = {s' in S | s' = gs for some g in G}. Orbits partition the set S.

# Core Definition

Given an operation of a group G on a set S, the orbit O_s of an element s is O_s = {s' in S | s' = gs for some g in G} (Artin, (6.7.3), p. 188). The orbits are equivalence classes for the relation s ~ s' if s' = gs for some g, and they partition S (6.7.5).

# Prerequisites

- **Group action** — Orbits are defined from group actions

# Key Properties

1. O_s = {gs | g in G}
2. Orbits partition S into disjoint subsets
3. |O_s| = [G : G_s] (index of stabilizer)
4. |G| = |G_s| * |O_s| (Counting Formula)
5. Elements in the same orbit have conjugate stabilizers

# Construction / Recognition

## To Compute:
1. Start with an element s
2. Apply all group elements to s
3. Collect all distinct results

# Context & Application

Orbits are the fundamental decomposition of any G-set. The partition of S into orbits gives the formula |S| = |O_1| + |O_2| + ... + |O_k|, which is used to derive the class equation and other counting results. When M acts on triangles, orbits are congruence classes.

# Examples

**Example 1** (p. 188): Under the action of the isometry group M on triangles, the orbit of a triangle is its congruence class.

**Example 2** (p. 192): The dodecahedron has 12 faces forming one orbit under its rotation group (60 = 5 * 12).

# Relationships

## Builds Upon
- **Group action** — Orbits arise from actions

## Enables
- **Counting formula** — Relates orbit size to stabilizer
- **Class equation** — Partitions a group by conjugacy orbits

## Related
- **Transitive action** — The entire set is one orbit

# Common Errors

- **Error**: Assuming elements with the same properties are in the same orbit
  **Correction**: Being in the same orbit requires an actual group element connecting them

# Common Confusions

- **Confusion**: Confusing orbit of an element with orbit of a set
  **Clarification**: The orbit of a subset U is {gU | g in G}, a set of subsets, not a set of elements

# Source Reference

Chapter 6: Symmetry, Section 6.7, (6.7.3)-(6.7.5), pages 188-189.

# Verification Notes

- Definition source: Direct from (6.7.3)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
