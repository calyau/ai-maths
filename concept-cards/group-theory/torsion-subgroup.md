---
# === CORE IDENTIFICATION ===
concept: Torsion Subgroup
slug: torsion-subgroup

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 9
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "G_tors"
  - torsion part

# === TYPED RELATIONSHIPS ===
prerequisites:
  - abelian-group
  - subgroup
  - order-of-an-element
extends:
  - subgroup
related:
  - order-of-an-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the torsion subgroup of an abelian group?"
  - "Do the elements of finite order always form a subgroup?"
---

# Quick Definition

In a commutative group G, the torsion subgroup G_tors is the subgroup consisting of all elements of finite order. This is only guaranteed to be a subgroup when G is abelian.

# Core Definition

In a commutative group G, the elements of finite order form a subgroup G_tors of G, called the **torsion subgroup** (p. 9).

# Prerequisites

- **Abelian group** — the torsion elements form a subgroup only when G is commutative
- **Subgroup** — G_tors is a subgroup of G
- **Order of an element** — torsion elements are those with finite order

# Key Properties

1. G_tors = {a in G | a has finite order}
2. G_tors is a subgroup of G when G is abelian
3. In a non-abelian group, elements of finite order need not form a subgroup
4. If G is finite, then G_tors = G

# Construction / Recognition

## To Construct:
1. Identify all elements of G that have finite order
2. Collect them into the set G_tors
3. (Commutativity of G guarantees this set is closed under the group operation)

# Context & Application

The torsion subgroup separates the "finite-order" part of an abelian group from the "torsion-free" part. This decomposition is fundamental in the structure theory of abelian groups.

# Examples

**Example 1** (p. 9): In (Z, +), every nonzero element has infinite order, so the torsion subgroup is {0}.

**Example 2**: In C_n, every element has finite order, so the torsion subgroup is the entire group.

# Relationships

## Builds Upon
- **abelian-group** — commutativity is needed for closure
- **order-of-an-element** — torsion elements have finite order

## Enables
- Structure theory of abelian groups (later chapters)

## Related
- **subgroup** — G_tors is a subgroup of G

# Common Errors

- **Error**: Assuming elements of finite order form a subgroup in any group
  **Correction**: This fails in non-abelian groups; if a and b have finite order, ab may have infinite order

# Common Confusions

- **Confusion**: Confusing "torsion" with "torsion-free"
  **Clarification**: Torsion elements have finite order; a torsion-free group has no nontrivial torsion elements

# Source Reference

Chapter 1: Basic Definitions and Results, page 9.

# Verification Notes

- Definition source: Direct from text, p. 9
- Confidence rationale: HIGH — explicitly named and defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
