---
concept: Operation on Cosets
slug: operation-on-cosets
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.8 The Operation on Cosets"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - stabilizer
extends:
  - group-action
related:
  - counting-formula
  - transitive-action
contrasts_with: []
answers_questions:
  - "How does a group act on the cosets of a subgroup?"
  - "How can any transitive action be described via cosets?"
---

# Quick Definition

For any subgroup H of G, the group G acts on the set G/H of left cosets by g[aH] = [gaH]. This action is always transitive, with stabilizer of [H] being H itself. Every transitive action is isomorphic to such an action on cosets.

# Core Definition

If H is a subgroup of G, then G operates on G/H by g[C] = [gC] (Artin, p. 191). The operation is transitive, and the stabilizer of [H] is H (Proposition 6.8.1). Proposition 6.8.4 shows there is a bijective map epsilon: G/H -> O_s for any transitive action with stabilizer H, compatible with the group action.

# Prerequisites

- **Group action** — This is a specific type of action
- **Stabilizer** — The stabilizer of [H] is H

# Key Properties

1. Always transitive (Proposition 6.8.1(a))
2. Stabilizer of [H] is H (Proposition 6.8.1(b))
3. Every transitive action is isomorphic to an action on cosets (Proposition 6.8.4)
4. G/H is not a group unless H is normal, but G still acts on it

# Context & Application

The action on cosets is the universal model for transitive actions. This is used in the proof of the Sylow theorems and throughout group theory. The S_3 example (6.8.2) makes the construction concrete.

# Examples

**Example 1** (p. 191): S_3 acts on the 3 cosets of H = {1, y} by: x acts as (123) and y acts as (23).

**Example 2** (p. 191): D_5 acts on the vertices of a regular pentagon, which is the same as D_5/H where H is the stabilizer of a vertex.

# Relationships

## Builds Upon
- **Group action** — Specializes to cosets

## Enables
- **Counting formula** — |G| = |H| * |G/H|
- **Permutation representation** — Action on cosets gives a homomorphism G -> S_n

# Source Reference

Chapter 6: Symmetry, Section 6.8, Propositions 6.8.1 and 6.8.4, pages 191-192.

# Verification Notes

- Definition source: From p. 191
- Confidence rationale: Explicitly developed
- Uncertainties: None
- Cross-reference status: Verified
