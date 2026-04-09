---
# === CORE IDENTIFICATION ===
concept: Cancellation Laws
slug: cancellation-laws

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
  - left cancellation law
  - right cancellation law

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - inverse-element
extends: []
related:
  - subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can you cancel elements in a group equation?"
  - "How are cancellation laws related to the existence of inverses?"
---

# Quick Definition

The cancellation laws state that in a group, ab = ac implies b = c (left cancellation) and ba = ca implies b = c (right cancellation).

# Core Definition

In a group G, the cancellation laws hold: ab = ac implies b = c, and ba = ca implies b = c. This follows from (G3) by multiplying on the left or right by a^{-1} (1.2e, p. 7).

Conversely, if G is **finite**, the cancellation laws imply (G3): the map x -> ax is injective and hence (by counting) bijective, so e is in the image, giving a right inverse. Similarly a left inverse exists, and the two are equal (1.2e, p. 7).

# Prerequisites

- **Group** — cancellation laws are a consequence of the group axioms
- **Inverse element** — the proof uses multiplication by a^{-1}

# Key Properties

1. Left cancellation: ab = ac implies b = c
2. Right cancellation: ba = ca implies b = c
3. In finite sets with an associative binary operation, cancellation laws imply the existence of inverses
4. In infinite sets, cancellation laws do not imply inverses (counterexample: (N, +))

# Construction / Recognition

## To Recognize:
1. In any group, the cancellation laws hold automatically
2. For a finite semigroup, check if each row and column of the multiplication table contains each element exactly once

# Context & Application

The cancellation laws connect the abstract axiom of inverses to the concrete property that each element appears exactly once in each row and column of the multiplication table. For finite structures, they provide an equivalent characterization of the inverse axiom.

# Examples

**Example 1** (p. 7): The counterexample (N, +) subset of (Z, +) satisfies cancellation but not (G3), showing that cancellation does not imply inverses for infinite sets.

# Relationships

## Builds Upon
- **inverse-element** — cancellation follows from multiplying by a^{-1}

## Enables
- **multiplication-table** — cancellation means each element appears once per row and column
- **subgroup** — for finite subsets, closure (S1) implies inverses (S2) via cancellation

## Related
- **group** — cancellation is equivalent to (G3) in finite associative structures

# Common Errors

- **Error**: Assuming cancellation laws hold in any algebraic structure
  **Correction**: Cancellation requires inverses (or finiteness plus associativity)

# Common Confusions

- **Confusion**: Thinking cancellation laws always imply a group structure
  **Clarification**: For infinite structures, cancellation does not imply inverses; the counterexample is (N, +)

# Source Reference

Chapter 1: Basic Definitions and Results, Remark 1.2e, page 7.

# Verification Notes

- Definition source: Direct from 1.2e
- Confidence rationale: HIGH — explicitly stated with proof and counterexample
- Uncertainties: None
- Cross-reference status: Verified against planned cards
