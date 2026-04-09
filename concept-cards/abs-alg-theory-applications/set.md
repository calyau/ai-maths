---
# === CORE IDENTIFICATION ===
concept: Set
slug: set

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 16
section: "Sets and Equivalence Relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - subset
  - empty-set
  - set-union
  - set-intersection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is a set?"
---

# Quick Definition

A set is a well-defined collection of objects, where for any given object one can determine whether or not it belongs to the set. The objects in a set are called its elements or members.

# Core Definition

"A set is a well-defined collection of objects; that is, it is defined in such a manner that we can determine for any given object $x$ whether or not $x$ belongs to the set. The objects that belong to a set are called its elements or members" (Judson, p. 16). Sets are denoted by capital letters such as $A$ or $X$; if $a$ is an element of set $A$, we write $a \in A$.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A set can be specified by listing elements: $X = \{x_1, x_2, \ldots, x_n\}$
2. A set can be specified by a property: $X = \{x : x \text{ satisfies } \mathcal{P}\}$
3. For any object $x$ and set $A$, either $x \in A$ or $x \notin A$
4. Two sets are equal ($A = B$) if and only if $A \subset B$ and $B \subset A$

# Construction / Recognition

## To Construct a Set:
1. Specify by listing elements inside braces: $\{2, 4, 6, \ldots\}$
2. Or specify by stating a defining property: $\{x : x \text{ is an even integer and } x > 0\}$

## To Verify Membership:
1. Check whether the object satisfies the defining condition of the set

# Context & Application

Sets are the most fundamental mathematical structure, underlying all of abstract algebra. Groups, rings, and fields are all defined as sets equipped with operations satisfying certain axioms. The standard number sets $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are essential throughout the text.

# Examples

**Example 1** (p. 16): The set of even positive integers can be written as $E = \{2, 4, 6, \ldots\}$ or $E = \{x : x \text{ is an even integer and } x > 0\}$.

**Example 2** (p. 16): Important number sets:
- $\mathbb{N} = \{1, 2, 3, \ldots\}$ (natural numbers)
- $\mathbb{Z} = \{\ldots, -1, 0, 1, 2, \ldots\}$ (integers)
- $\mathbb{Q} = \{p/q : p, q \in \mathbb{Z}, q \neq 0\}$ (rationals)
- $\mathbb{R}$ (real numbers)
- $\mathbb{C}$ (complex numbers)

with containment $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$.

# Relationships

## Enables
- **subset** — Defined in terms of set membership
- **set-union** — Operation on sets
- **set-intersection** — Operation on sets
- **cartesian-product** — Constructed from sets
- **group** — A group is a set with an operation satisfying axioms

## Related
- **empty-set** — The set with no elements

# Common Errors

- **Error**: Defining a set with an ambiguous or subjective criterion (e.g., "the set of large numbers")
  **Correction**: The defining property must be well-defined so membership can be determined for any object

# Common Confusions

- **Confusion**: Confusing a set with an ordered list
  **Clarification**: Sets have no inherent ordering and no duplicate elements; $\{1, 2, 3\} = \{3, 1, 2\}$

# Source Reference

Chapter 1: Preliminaries, Section 1.2 "Sets and Equivalence Relations," pages 16-18.

# Verification Notes

- Definition source: Direct quote from p. 16
- Confidence: HIGH — explicit definition in source
- Cross-reference status: Verified
- Uncertainties: None
