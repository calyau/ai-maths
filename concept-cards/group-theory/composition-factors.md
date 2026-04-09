---
# === CORE IDENTIFICATION ===
concept: Composition Factors
slug: composition-factors

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
pdf_page: 89
section: "Subnormal Series"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - composition-series
  - simple-group
extends: []
related:
  - jordan-holder-theorem
  - solvable-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do composition factors relate to simple groups?"
  - "What are the building blocks of a finite group?"
---

# Quick Definition

The composition factors of a group G are the quotients G_{i-1}/G_i of any composition series. They are simple groups, and the Jordan-Holder theorem guarantees they are independent (up to order and isomorphism) of the choice of composition series.

# Core Definition

The quotients of a composition series are sometimes called *composition factors*. Each composition factor is a simple group. By the Jordan-Holder theorem, the multiset of composition factors (up to isomorphism) is an invariant of G.

(Milne, p. 89)

# Prerequisites

- **composition-series** -- composition factors are the quotients of a composition series
- **simple-group** -- each composition factor is simple

# Key Properties

1. Every composition factor is a simple group
2. The multiset of composition factors is a group invariant (Jordan-Holder)
3. G is solvable iff all composition factors are cyclic of prime order
4. |G| = product of the orders of the composition factors
5. Different groups can share the same composition factors

# Context & Application

Composition factors are the "atoms" from which a finite group is assembled. The classification of finite simple groups enumerates all possible composition factors. However, knowing the composition factors does not determine the group uniquely -- the extension problem (how to reassemble) is a separate, difficult question.

# Examples

**Example 1** (p. 87, 6.1b): S_4 has composition factors C_2, C_3, C_2, C_2.

**Example 2** (p. 87, 6.1d): C_m has composition factors C_{p_1}, ..., C_{p_r} where m = p_1 ... p_r.

**Example 3** (p. 87, 6.1e): A direct product H_1 x ... x H_r of simple groups has composition factors H_1, ..., H_r (in any order).

# Relationships

## Builds Upon
- **composition-series** -- composition factors are the quotients

## Enables
- **solvable-group** -- characterized by having abelian (cyclic of prime order) composition factors

## Related
- **jordan-holder-theorem** -- guarantees uniqueness of composition factors

# Common Confusions

- **Confusion**: Thinking that two groups with the same composition factors are isomorphic
  **Clarification**: C_4 and C_2 x C_2 both have composition factors {C_2, C_2} but are not isomorphic

# Source Reference

Chapter 6, p. 89. Term introduced after Remark 6.3.

# Verification Notes

- Definition source: Direct from p. 89
- Confidence rationale: HIGH -- explicit terminology
- Uncertainties: None
