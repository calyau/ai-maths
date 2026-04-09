---
# === CORE IDENTIFICATION ===
concept: Composition Series
slug: composition-series

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
  - subnormal-series
  - simple-group
extends:
  - subnormal-series
related:
  - composition-factors
  - jordan-holder-theorem
  - solvable-group
contrasts_with:
  - solvable-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a composition series?"
  - "What is the difference between a composition series and a subnormal series?"
  - "How do composition factors relate to simple groups?"
---

# Quick Definition

A composition series is a subnormal series that cannot be properly refined: each quotient G_{i-1}/G_i is simple and nontrivial. Every finite group has a composition series, and the Jordan-Holder theorem says the composition factors are unique up to order and isomorphism.

# Core Definition

A subnormal series is a *composition series* if it has no proper refinement that is also a subnormal series. Equivalently, G_i is maximal among the proper normal subgroups of G_{i-1} for each i. Thus a subnormal series is a composition series if and only if each quotient group G_{i-1}/G_i is simple and nontrivial.

Every finite group has a composition series (choose G_1 to be a maximal proper normal subgroup of G, then G_2 maximal proper normal in G_1, etc.). An infinite group may or may not have a finite composition series.

(Milne, p. 86)

# Prerequisites

- **subnormal-series** -- a composition series is a special case
- **simple-group** -- the quotients must be simple

# Key Properties

1. Each quotient G_{i-1}/G_i is simple (has no normal subgroups other than 1 and itself)
2. The series has no proper refinement that remains subnormal
3. Every finite group has at least one composition series
4. The group G is "built up" from its composition factors by successive extensions
5. |G| = product of |G_{i-1}/G_i|

# Construction / Recognition

## To Construct (for finite G):
1. Choose G_1 as a maximal proper normal subgroup of G
2. Choose G_2 as a maximal proper normal subgroup of G_1
3. Continue until reaching {1}

## To Verify:
Check that each quotient G_{i-1}/G_i is simple (nontrivial, no proper normal subgroups).

# Context & Application

Composition series decompose a group into its "building blocks" (simple groups), analogous to prime factorization of integers. The Jordan-Holder theorem ensures this decomposition is essentially unique. The classification of finite simple groups thus provides a catalogue of all possible building blocks.

# Examples

**Example 1** (p. 87, 6.1a): S_3 > A_3 > 1 with composition factors C_2, C_3.

**Example 2** (p. 87, 6.1b): S_4 > A_4 > V > <(13)(24)> > 1 with factors C_2, C_3, C_2, C_2.

**Example 3** (p. 87, 6.1d): For C_m with m = p_1 ... p_r, the composition series has length r with factors C_{p_1}, ..., C_{p_r}. The Jordan-Holder theorem applied to C_m recovers unique factorization of integers.

**Example 4** (p. 87, 6.1f): For n >= 5, S_n > A_n > {1} is the *only* composition series.

# Relationships

## Builds Upon
- **subnormal-series** -- composition series are subnormal series without proper refinements

## Enables
- **composition-factors** -- the simple quotients of a composition series
- **jordan-holder-theorem** -- uniqueness of composition factors
- **solvable-group** -- solvable iff all composition factors are cyclic of prime order

## Contrasts With
- **solvable-series** -- has abelian (not necessarily simple) quotients

# Common Errors

- **Error**: Assuming a composition series is unique
  **Correction**: The series itself is generally not unique; the Jordan-Holder theorem says the *factors* (up to order and isomorphism) are unique

- **Error**: Thinking a composition series for G must consist of normal subgroups of G
  **Correction**: Each G_i is normal in G_{i-1}, not necessarily in G

# Common Confusions

- **Confusion**: Thinking that knowing the composition factors determines the group
  **Clarification**: The composition factors determine the "ingredients" but not the "recipe" (the extensions). Many non-isomorphic groups can have the same composition factors.

# Source Reference

Chapter 6, pp. 86-87. Examples 6.1, pp. 87-88.

# Verification Notes

- Definition source: Direct from p. 86
- Confidence rationale: HIGH -- explicit definition with multiple examples
- Uncertainties: None
