---
# === CORE IDENTIFICATION ===
concept: Group
slug: group

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Axioms"
chapter_number: 2
pdf_page: 13
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends:
  - symmetry-group
related:
  - associativity
  - identity-element
  - inverse-element
  - abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

A group is a set G together with a multiplication (binary operation) on G that satisfies three axioms: associativity, existence of an identity element, and existence of inverses. It is the central algebraic structure of the text.

# Core Definition

"A group is a set G together with a multiplication on G which satisfies three axioms:
(a) The multiplication is associative, that is to say (xy)z = x(yz) for any three (not necessarily distinct) elements from G.
(b) There is an element e in G, called an identity element, such that xe = x = ex for every x in G.
(c) Each element x of G has a (so-called) inverse x^{-1} which belongs to the set G and satisfies x^{-1}x = e = xx^{-1}" (Armstrong, Ch. 2, p. 13).

# Prerequisites

This is a foundational concept with no prerequisites within this source. (The symmetry group examples in Chapter 1 motivate the definition but are not logically required.)

# Key Properties

1. The set is closed under the multiplication: for any x, y in G, the product xy is in G
2. The multiplication is associative: (xy)z = x(yz)
3. There exists a unique identity element e with xe = x = ex for all x
4. Each element x has a unique inverse x^{-1} with x^{-1}x = e = xx^{-1}
5. The group need not be commutative: xy may differ from yx
6. The "multiplication" may be any binary operation (addition, composition, matrix multiplication, etc.)

# Construction / Recognition

## To Verify a Group:
1. Identify the set G and the binary operation
2. Check closure: the operation on any two elements of G produces an element of G
3. Check associativity: (xy)z = x(yz) for all x, y, z in G
4. Identify an identity element e with xe = x = ex for all x in G
5. For each x in G, find an inverse x^{-1} in G with x^{-1}x = e = xx^{-1}

# Context & Application

The group is the fundamental algebraic structure studied throughout the text. Armstrong motivates it from symmetry groups: "Starting from the axioms for a group, we shall build up a body of results which may be used whenever these axioms are satisfied" (Ch. 2, p. 15). Groups appear in symmetry (rotations of solids), number theory (integers under addition), physics (Lorentz group), and geometry (similarities, isometries).

# Examples

**Example 1** (p. 13): The real numbers under addition form a group: addition is associative, 0 is the identity, and -x is the inverse of x.

**Example 2** (p. 14): The Lorentz group consists of 2x2 matrices of the form [[cosh u, sinh u], [sinh u, cosh u]] under matrix multiplication.

**Example 3** (p. 15): The similarities of the plane form a group under composition.

# Relationships

## Builds Upon
- **Symmetry Group** — The abstract group definition generalizes symmetry groups

## Enables
- **Abelian Group** — A group with commutativity
- **Subgroup** — A subset that is itself a group
- **Dihedral Group** — A specific family of groups

## Related
- **Associativity** — Group axiom (a)
- **Identity Element** — Group axiom (b)
- **Inverse Element** — Group axiom (c)

# Common Errors

- **Error**: Forgetting to verify closure (that the operation stays within the set)
  **Correction**: Closure is implicit in the phrase "multiplication on G" but must be checked in practice

- **Error**: Forgetting to check that the inverse of each element is in the set
  **Correction**: The inverse must belong to G, not just exist in some larger structure

# Common Confusions

- **Confusion**: Thinking "multiplication" means ordinary number multiplication
  **Clarification**: "The rule which enables us to combine our elements is invariably referred to as a multiplication, but may have nothing to do with multiplication of numbers in the usual sense" (Armstrong, p. 13)

- **Confusion**: Believing groups must be commutative
  **Clarification**: Commutativity is not a group axiom; groups where xy = yx for all x, y are given the special name "abelian"

# Source Reference

Chapter 2: Axioms, pages 6-10 (pdf pp. 13-17).

# Verification Notes

- Definition source: Direct quote from p. 13
- Confidence rationale: High — formal axiomatic definition given explicitly
- Uncertainties: None
- Cross-reference status: Verified
