---
concept: Equivalence Relation
slug: equivalence-relation
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
  - equivalence-class
  - partition
  - coset
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

An equivalence relation on a set S is a relation ~ that is transitive (a~b and b~c implies a~c), symmetric (a~b implies b~a), and reflexive (a~a for all a). It partitions S into equivalence classes.

# Core Definition

An equivalence relation on a set S is a relation ~ satisfying: transitive (a~b and b~c implies a~c), symmetric (a~b implies b~a), and reflexive (a~a for all a) (Artin, p. 68). The concepts of partition and equivalence relation are logically equivalent (Proposition 2.7.4).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Determines a partition of S into equivalence classes
2. a and b are in the same class iff a ~ b
3. Equivalence classes are disjoint and cover S
4. Any map f: S -> T defines an equivalence relation: a ~ b iff f(a) = f(b)
5. The fibres of a map are the equivalence classes

# Construction / Recognition

## To Construct:
1. Define a relation ~ on S
2. Verify transitivity, symmetry, and reflexivity

## To Recognize:
1. A relation satisfying the three axioms

# Context & Application

Equivalence relations underpin cosets, quotient groups, and modular arithmetic. Congruence modulo n is an equivalence relation on Z. Conjugacy is an equivalence relation on any group.

# Examples

**Example 1** (p. 68): Congruence of triangles is an equivalence relation.

**Example 2** (p. 68): Conjugacy in a group: a ~ b if b = gag^(-1) for some g.

**Example 3** (p. 69): The partition {1}, {y, xy, x^2y}, {x, x^2} of S_3 by element order.

# Relationships

## Enables
- **Equivalence class** — The subsets in the partition
- **Coset** — Cosets are equivalence classes for congruence mod H
- **Quotient group** — Elements are equivalence classes

## Related
- **Partition** — Logically equivalent to an equivalence relation

# Common Errors

- **Error**: Forgetting to check reflexivity
  **Correction**: a ~ a must hold for all a (often the easiest axiom to forget)

# Common Confusions

- **Confusion**: Confusing equivalence relation with equality
  **Clarification**: An equivalence relation identifies elements that are "the same" in some weaker sense

# Source Reference

Chapter 2: Groups, Section 2.7, pages 68-70.

# Verification Notes

- Definition source: Direct from Section 2.7
- Confidence rationale: Standard definition
- Uncertainties: None
- Cross-reference status: Verified
