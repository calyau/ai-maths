---
concept: Operation on Subsets
slug: operation-on-subsets
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.10 Operations on Subsets"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
extends:
  - group-action
related:
  - orbit
  - stabilizer
contrasts_with: []
answers_questions:
  - "How does a group act on the subsets of a set?"
---

# Quick Definition

If G acts on S, it also acts on the subsets of S of any given size r: g sends a subset U to gU = {gu | u in U}. The stabilizer of U consists of elements permuting U within itself.

# Core Definition

Suppose a group G operates on a set S. If U is a subset of order r, then gU = {gu | u in U} is another subset of order r. This defines an operation of G on the set of subsets of order r (Artin, (6.10.1), p. 193).

# Prerequisites

- **Group action** — This extends an action on elements to subsets

# Key Properties

1. gU = U means g permutes elements within U (not necessarily fixing them)
2. The stabilizer of U consists of g with gU = U
3. Different from the pointwise stabilizer {g | gu = u for all u in U}

# Context & Application

Operations on subsets are used in the proof of the First Sylow Theorem, where G acts on the set of all subsets of order p^e. The stabilizer of such a subset turns out to be a Sylow subgroup.

# Examples

**Example 1** (p. 193): The octahedral group O (24 rotations of a cube) acts on pairs of faces. The 15 pairs form two orbits: 3 pairs of opposite faces and 12 pairs of adjacent faces.

# Relationships

## Builds Upon
- **Group action** — Extends an action on S to subsets of S

## Enables
- **First Sylow theorem** — Proved via action on subsets of order p^e

# Common Errors

- **Error**: Confusing "gU = U" with "g fixes each element of U"
  **Correction**: gU = U means g permutes the elements of U; individual elements may move

# Source Reference

Chapter 6: Symmetry, Section 6.10, (6.10.1), pages 193-194.

# Verification Notes

- Definition source: Direct from (6.10.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
