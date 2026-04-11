---
concept: Set
slug: set
category: foundations
subcategory: set-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Preliminaries"
chapter_number: 0
pdf_page: 14
section: "0.1 Basics"
extraction_confidence: high
aliases:
  - "collection"
prerequisites: []
extends: []
related:
  - cartesian-product
  - cardinality
  - function
contrasts_with: []
answers_questions:
  - "What is the basic notation for sets in abstract algebra?"
  - "What does the order or cardinality of a set mean?"
---

# Quick Definition
A set is a collection of elements, with standard operations of union, intersection, and membership. The order or cardinality of a set A, denoted |A|, is the number of elements in A when A is finite.

# Core Definition
The basics of set theory — sets, intersection ($\cap$), union ($\cup$), membership ($\in$), etc. — are assumed as background. The notation $B = \{a \in A \mid \dots \text{(conditions on } a) \dots\}$ is used for subsets. The *order* or *cardinality* of a set A is denoted by |A|; for finite sets this is simply the number of elements (Dummit & Foote, p. 1).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Sets are described using set-builder notation with conditions on elements
2. The order |A| of a finite set A is the number of elements in A
3. Standard number sets are denoted: $\mathbb{Z}$ (integers), $\mathbb{Q}$ (rationals), $\mathbb{R}$ (reals), $\mathbb{C}$ (complex numbers)
4. $\mathbb{Z}^+$, $\mathbb{Q}^+$, $\mathbb{R}^+$ denote the positive (nonzero) elements

# Construction / Recognition
## To Construct/Create:
1. Specify a universe set and conditions that elements must satisfy
2. Use set-builder notation: $\{a \in A \mid \text{conditions}\}$

## To Identify/Recognize:
1. A set is any well-defined collection of objects
2. Membership is determined by checking conditions

# Context & Application
Sets form the foundation for all algebraic structures. Every group, ring, and field is defined as a set equipped with operations satisfying certain axioms. The cardinality notation |A| will later be used for the order of groups and the order of elements.

# Examples
**Example 1** (p. 1): $\mathbb{Z} = \{0, \pm 1, \pm 2, \pm 3, \dots\}$ denotes the integers.
**Example 2** (p. 1): $\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}, i^2 = -1\}$ denotes the complex numbers.

# Relationships
## Builds Upon
No prerequisites.

## Enables
- **cartesian-product** — Cartesian products are built from sets
- **function** — Functions are defined between sets
- **binary-operation** — Operations act on sets

## Related
- **cardinality** — Measures the size of a set

## Contrasts With
None within this source.

# Common Errors
- **Error**: Confusing the order of a set with the order of an element in a group. **Correction**: The notation |A| for a set means cardinality; for a group element x, |x| means the smallest positive power giving the identity. Context determines which meaning applies.

# Common Confusions
- **Confusion**: Believing that |A| is only defined for finite sets. **Clarification**: For infinite sets, cardinality is defined using cardinal numbers, though for most of Part I the text works primarily with finite sets.

# Source Reference
Chapter 0: Preliminaries, Section 0.1 "Basics," pages 1-2.

# Verification Notes
- Definition source: direct from source p. 1
- Confidence rationale: explicitly presented as foundational material
- Uncertainties: none
- Cross-reference status: verified
