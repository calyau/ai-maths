---
# === CORE IDENTIFICATION ===
concept: Group
slug: group

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
pdf_page: 6
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - abelian-group
  - subgroup
  - order-of-a-group
  - isomorphism-of-groups
contrasts_with:
  - magma
  - semigroup
  - monoid

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What are the group axioms?"
  - "What conditions must a set with a binary operation satisfy to be a group?"
---

# Quick Definition

A group is a set G together with a binary operation satisfying associativity, existence of a neutral element, and existence of inverses. It is the fundamental algebraic structure studied in group theory.

# Core Definition

A *group* is a set G together with a mapping (a, b) -> a * b : G x G -> G satisfying:

- **(G1)** (associativity): (a * b) * c = a * (b * c) for all a, b, c in G;
- **(G2)** (existence of a neutral element): there exists an element e in G such that a * e = a = e * a for all a in G;
- **(G3)** (existence of inverses): for each a in G, there exists a' in G such that a * a' = e = a' * a.

(Milne, Definition 1.1, p. 6)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The binary operation is closed (the mapping is G x G -> G)
2. The operation is associative (G1)
3. There is a unique neutral element (proved in 1.2a)
4. Each element has a unique inverse (proved in 1.2b)
5. Products of any finite ordered tuple of elements are unambiguously defined (1.2c)
6. The cancellation laws hold: ab = ac implies b = c, and ba = ca implies b = c (1.2e)
7. The inverse of a product is the product of inverses in reverse order (1.2d)

# Construction / Recognition

## To Construct:
1. Specify a set G
2. Define a binary operation * : G x G -> G
3. Verify associativity (G1)
4. Identify a neutral element e satisfying (G2)
5. Verify that every element has an inverse satisfying (G3)

## To Recognize:
1. Check that the binary operation is closed on G
2. Check associativity for all triples
3. Check for a neutral element
4. Check that every element has an inverse

# Context & Application

Group theory is described by Milne as "the study of symmetries" (p. 6). Groups arise throughout mathematics as symmetry groups of geometric objects, automorphism groups of algebraic structures, and transformation groups in physics.

The group axioms can be weakened: one can replace (G2) and (G3) with left-sided versions (G2': left neutral element, G3': left inverses), and the full axioms follow (Aside 1.10a). Alternatively, a group can be defined by: (g1) associativity, (g2) nonemptiness, (g3) existence of left quasi-inverses (Aside 1.10b). These are minimal in the sense that any two without the third can be satisfied by a non-group.

Groups can be written multiplicatively (using juxtaposition for the operation and 1 for the neutral element) or additively (using + and 0). Multiplicative notation is the default; additive notation is typically reserved for commutative groups.

# Examples

**Example 1** (p. 8, 1.3): The integers under addition (Z, +) form a group, denoted C_infinity. For any integer m >= 1, the group (Z/mZ, +) is denoted C_m.

**Example 2** (p. 8, 1.4): For any set S, the set Sym(S) of bijections S -> S forms a group under composition, called the group of symmetries of S. The symmetric group S_n = Sym({1, ..., n}) has order n!.

**Example 3** (p. 9, 1.7): The set of n x n matrices with coefficients in a field F and nonzero determinant forms the general linear group GL_n(F).

# Relationships

## Builds Upon
- No prerequisites; this is the foundational definition.

## Enables
- **subgroup** — defined as a subset of a group satisfying certain closure properties
- **order-of-a-group** — the cardinality of the underlying set
- **abelian-group** — a group with an additional commutativity condition
- **isomorphism-of-groups** — structure-preserving bijection between groups

## Related
- **direct-product-of-groups** — method for constructing new groups from existing ones

## Contrasts With
- **magma** — has a binary operation but no axioms beyond closure
- **semigroup** — has associativity but no neutral element or inverses
- **monoid** — has associativity and a neutral element but not necessarily inverses

# Common Errors

- **Error**: Forgetting to verify associativity when checking if a structure is a group
  **Correction**: Associativity must always be checked; for finite groups with n elements this requires checking n^3 equalities (p. 11)

- **Error**: Assuming closure is automatic for subsets
  **Correction**: The binary operation must map G x G into G (or S x S into S for subgroups)

# Common Confusions

- **Confusion**: Thinking that left identity and left inverses automatically give a group
  **Clarification**: They do, but the proof is nontrivial (Aside 1.10a, p. 10); the full two-sided axioms follow from the left-sided versions

- **Confusion**: Confusing a group with its underlying set
  **Clarification**: A group is the pair (G, *) of a set and its operation; the same set can carry different group structures

# Source Reference

Chapter 1: Basic Definitions and Results, Definition 1.1 and remarks 1.2, pages 6-8. See also Aside 1.10 (pp. 10-11) for alternative axiomatizations.

# Verification Notes

- Definition source: Direct from Definition 1.1, p. 6
- Confidence rationale: HIGH — explicit, formal definition with labeled axioms
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
