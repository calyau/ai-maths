---
# === CORE IDENTIFICATION ===
concept: Subnormal Series
slug: subnormal-series

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 86
section: "Subnormal Series"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - normal-subgroup
extends: []
related:
  - normal-series
  - composition-series
  - solvable-series
contrasts_with:
  - normal-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subnormal series?"
  - "What is the difference between a composition series and a subnormal series?"
  - "What background is needed for the Jordan-Holder theorem?"
---

# Quick Definition

A subnormal series of a group G is a chain of subgroups from G down to {1} where each subgroup is normal in the preceding one (but not necessarily normal in G). The successive quotients are called the factor groups of the series.

# Core Definition

A chain of subgroups

G = G_0 superset G_1 superset ... superset G_n = {1}

is called a *subnormal series* if G_i is normal in G_{i-1} for every i. The series is *without repetitions* if all inclusions G_{i-1} superset G_i are proper, in which case n is the *length* of the series. The quotient groups G_{i-1}/G_i are called the *quotient* (or *factor*) *groups* of the series.

(Milne, p. 86)

# Prerequisites

- **group** -- the ambient group G
- **normal-subgroup** -- each G_i must be normal in G_{i-1}

# Key Properties

1. Each G_i is normal in G_{i-1}, but *not* necessarily normal in G
2. The group G can be reconstructed from the quotients by successive extensions
3. |G| = product of |G_{i-1}/G_i| for all i
4. From a subnormal series one obtains a sequence of short exact sequences: 1 -> G_{i+1} -> G_i -> G_i/G_{i+1} -> 1

# Construction / Recognition

## To Construct:
1. Start with G = G_0
2. Choose G_1 normal in G_0
3. Choose G_2 normal in G_1
4. Continue until reaching {1}

## To Verify:
Check that G_i is normal in G_{i-1} (not in G) for each i.

# Context & Application

Subnormal series are the basic building blocks for understanding how a group is assembled from simpler pieces. Composition series are the "finest" subnormal series, and the Jordan-Holder theorem says that the composition factors are essentially unique.

# Examples

**Example 1** (p. 87, 6.1a): S_3 has subnormal series S_3 > A_3 > 1 with quotients C_2, C_3.

**Example 2** (p. 87, 6.1b): S_4 has subnormal series S_4 > A_4 > V > <(13)(24)> > 1 with quotients C_2, C_3, C_2, C_2.

# Relationships

## Builds Upon
- **normal-subgroup** -- the defining condition

## Enables
- **composition-series** -- a subnormal series with no proper refinements
- **solvable-series** -- a subnormal series with abelian quotients
- **jordan-holder-theorem** -- uniqueness of composition factors

## Contrasts With
- **normal-series** -- in a normal series, every G_i is normal in G (not just in G_{i-1})

# Common Errors

- **Error**: Assuming each G_i is normal in G
  **Correction**: In a subnormal series, G_i need only be normal in G_{i-1}. Normality in G is the stronger condition defining a *normal series*.

# Common Confusions

- **Confusion**: Confusing subnormal series with normal series
  **Clarification**: Some authors use "normal series" for what Milne calls "subnormal series." Milne reserves "normal series" for the stronger condition where every G_i is normal in G.

# Source Reference

Chapter 6, p. 86. See footnote 1 for terminological variations.

# Verification Notes

- Definition source: Direct from p. 86
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: Terminological note: some authors swap "normal" and "subnormal" (footnote 1)
