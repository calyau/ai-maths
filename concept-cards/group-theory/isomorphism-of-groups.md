---
# === CORE IDENTIFICATION ===
concept: Isomorphism of Groups
slug: isomorphism-of-groups

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 7
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - group isomorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - order-of-a-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two groups considered the same?"
  - "What does it mean for two groups to be isomorphic?"
---

# Quick Definition

Two groups (G, *) and (G', *') are isomorphic if there exists a one-to-one correspondence between them that preserves the group operation. The source uses the symbol ≈ for isomorphic.

# Core Definition

Two groups (G, *) and (G', *') are **isomorphic** if there exists a one-to-one correspondence a <-> a', G <-> G', such that (a * b)' = a' *' b' for all a, b in G (p. 7).

Milne uses ≈ for isomorphic and ≃ for canonically isomorphic.

# Prerequisites

- **Group** — isomorphism is a relationship between groups

# Key Properties

1. An isomorphism is a bijective map that preserves the group operation
2. Isomorphic groups have the same order
3. Isomorphic groups are structurally identical — they differ only in the labeling of elements
4. "Up to isomorphism" is the standard equivalence relation on groups

# Construction / Recognition

## To Construct:
1. Define a bijection f: G -> G'
2. Verify that f(a * b) = f(a) *' f(b) for all a, b in G

## To Recognize:
1. Groups must have the same order
2. Groups must have the same structure (same multiplication table up to relabeling)

# Context & Application

Isomorphism is the fundamental equivalence relation in group theory. When classifying groups (as in the table of groups of small order), one always classifies "up to isomorphism." For example, there is exactly one cyclic group of order n up to isomorphism (1.16, p. 12).

# Examples

**Example 1** (p. 12, 1.16): C_n is isomorphic to Z/nZ via r^i <-> i mod n.

**Example 2** (p. 9, 1.7): GL(V) is isomorphic to GL_n(F) once a basis for V is chosen.

# Relationships

## Builds Upon
- **group** — isomorphism relates two groups

## Enables
- **groups-of-small-order** — classification is done up to isomorphism
- **cyclic-group** — characterized up to isomorphism

## Related
- **order-of-a-group** — isomorphic groups have the same order

# Common Errors

- **Error**: Concluding two groups are isomorphic just because they have the same order
  **Correction**: Same order is necessary but not sufficient; e.g., C_4 and C_2 x C_2 both have order 4 but are not isomorphic

# Common Confusions

- **Confusion**: Confusing isomorphism with equality
  **Clarification**: Isomorphic groups are structurally the same but may be presented differently (different sets, different operations)

# Source Reference

Chapter 1: Basic Definitions and Results, page 7 (after Remark 1.2).

# Verification Notes

- Definition source: Direct from text, p. 7
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
