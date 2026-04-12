---
concept: Partition
slug: partition
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.7 Equivalence Relations and Partitions"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - equivalence-relation
  - equivalence-class
  - coset
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

A partition of a set S is a subdivision of S into nonoverlapping, nonempty subsets whose union is all of S. Partitions and equivalence relations are logically equivalent concepts.

# Core Definition

A partition of a set S is a subdivision of S into nonoverlapping, nonempty subsets (Artin, p. 68, formula 2.7.1). The concepts of partition and equivalence relation are logically equivalent (Proposition 2.7.4): given a partition, declare a ~ b iff they are in the same subset; given an equivalence relation, the equivalence classes form a partition.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Subsets are nonempty, disjoint, and cover S
2. Equivalent to an equivalence relation
3. Left cosets of a subgroup partition the group

# Construction / Recognition

## To Construct:
1. Divide S into nonoverlapping nonempty subsets covering all of S

## To Recognize:
1. A collection of subsets that are pairwise disjoint and whose union is S

# Context & Application

Partitions arise from equivalence relations and from cosets of subgroups. They are the conceptual foundation for quotient constructions.

# Examples

**Example 1** (p. 68): {1}, {y, xy, x^2y}, {x, x^2} partition S_3 by element order.

**Example 2** (p. 68): Even and Odd integers partition Z.

# Relationships

## Related
- **Equivalence relation** — Logically equivalent concept
- **Coset** — Cosets partition a group

# Common Errors

- **Error**: Allowing empty subsets in a partition
  **Correction**: All subsets must be nonempty

# Common Confusions

- **Confusion**: Confusing partition with any collection of subsets
  **Clarification**: Subsets must be disjoint and cover all of S

# Source Reference

Chapter 2: Groups, Section 2.7, page 68.

# Verification Notes

- Definition source: Direct from (2.7.1), p. 68
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
