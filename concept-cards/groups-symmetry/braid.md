---
# === CORE IDENTIFICATION ===
concept: Braid
slug: braid

# === CLASSIFICATION ===
category: equivalence-partitions
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Partitions"
chapter_number: 12
pdf_page: 68
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
extends: []
related:
  - braid-group
  - symmetric-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a braid in group theory?"
---

# Quick Definition

A braid (on three strings) is a configuration of non-intersecting strings connecting three points in a top plane to three corresponding points in a bottom plane, where each string meets each intermediate level exactly once.

# Core Definition

Begin with a pair of horizontal planes, three points in the top plane and the corresponding three vertically below them in the lower plane. Add strings which join the top points to the lower ones. These strings must not intersect, and an individual string should meet each level between the two planes exactly once. Such a configuration is called a **braid** (Armstrong, Ch. 12, Example (vi), p. 70).

Two braids can be "multiplied" by stacking one on top of the other. The trivial braid $e$ has vertical strings. Reflecting a braid $b$ in the lower plane gives $b^{-1}$, and $b^{-1}b$ is "to all intents and purposes trivial."

# Prerequisites

- **Equivalence relation** — Braids are made into precise algebraic objects via an equivalence relation

# Key Properties

1. Strings connect top points to bottom points without intersection
2. Each string meets each horizontal level exactly once
3. Braids can be multiplied by stacking
4. The trivial braid has vertical (straight) strings
5. Each braid has an inverse obtained by reflection

# Construction / Recognition

## To Construct:
1. Start with three points in a top plane and three corresponding points below
2. Connect top to bottom with non-intersecting strings
3. Ensure each string is monotone (meets each level once)

# Context & Application

Armstrong uses braids to illustrate how equivalence relations can define group elements. The "essential quality" of a braid is how its strings wind around one another, so braids that differ only by continuous deformation (keeping endpoints fixed, strings non-intersecting) should be considered the same. This motivates defining an equivalence relation whose classes form the braid group.

# Examples

**Example 1** (p. 70, Fig. 12.3): A braid with three strings winding around each other.

**Example 2** (p. 71, Fig. 12.4): Two braids $b_1, b_2$ multiplied by stacking $b_2$ on top of $b_1$.

**Example 3** (p. 71, Fig. 12.5): The trivial braid $e$ with vertical strings acting as identity.

# Relationships

## Enables
- **Braid group** — Equivalence classes of braids form the braid group $B_3$

## Related
- **Symmetric group** — Sliding along braid strings defines a surjection $B_3 \to S_3$ (Exercise 12.12)

# Common Errors

- **Error**: Allowing strings to intersect during the braid construction
  **Correction**: Strings must be non-intersecting; crossings are "over" or "under" in three dimensions

# Common Confusions

- **Confusion**: Thinking two braids are "the same" just because they connect the same pairs of points
  **Clarification**: Two braids connecting the same pairs may differ in how the strings wind around each other. They are equivalent only if one can be continuously deformed into the other.

# Source Reference

Chapter 12: Partitions, Example (vi), pp. 70-72 (pdf). Figures 12.3-12.6.

# Verification Notes

- Definition source: Direct from Example (vi), p. 70
- Confidence rationale: MEDIUM — defined concretely but the equivalence relation is described informally ("continuous deformation")
- Uncertainties: The precise topology is not formalised in the text
