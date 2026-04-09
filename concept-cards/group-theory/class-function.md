---
# === CORE IDENTIFICATION ===
concept: Class Function
slug: class-function

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 113
section: "The representations of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-algebra
extends: []
related:
  - character-of-a-representation
  - irreducible-character
  - conjugacy-classes-and-centre-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a class function?"
  - "How do class functions relate to the centre of the group algebra?"
---

# Quick Definition

A class function on G is a function f: G -> F that is constant on conjugacy classes, i.e., f(gag^{-1}) = f(a) for all g, a in G.

# Core Definition

A function f: G -> F is a **class function** if it is constant on each conjugacy class, i.e., f(gag^{-1}) = f(a) for all g, a in G. The class functions form an F-vector space of dimension t (the number of conjugacy classes). The elements of the centre of F[G] correspond exactly to class functions under the identification sum m_a a <-> (a -> m_a). (Milne, Remark 7.39, p. 113)

# Prerequisites

- **Group algebra** — class functions correspond to central elements of F[G]

# Key Properties

1. Class functions form an F-vector space of dimension t (number of conjugacy classes)
2. Characters are class functions
3. The simple characters form an F-basis for the space of class functions (7.47)
4. The simple characters form an orthonormal basis with respect to the inner product (f_1|f_2) = (1/|G|) sum f_1(a) conjugate(f_2(a)) (7.52)

# Construction / Recognition

1. A function f: G -> F is a class function if f(gag^{-1}) = f(a) for all g, a
2. Equivalently, f is constant on conjugacy classes
3. The space of class functions has dimension equal to the number of conjugacy classes

# Context & Application

Class functions are the natural domain for character theory. Every character is a class function, and the irreducible characters form a basis for the space of all class functions. The inner product on class functions provides the orthogonality relations.

# Examples

**Example 1** (p. 113): The function a -> m_a: G -> F corresponding to a central element sum m_a a of F[G] is a class function.

# Relationships

## Builds Upon
- **group-algebra** — class functions correspond to central elements

## Enables
- **character-of-a-representation** — characters are class functions
- **character-inner-product** — inner product on class functions

## Related
- **conjugacy-classes-and-centre-of-f-g** — dimension = number of conjugacy classes

# Source Reference

Chapter 7: Representations of Finite Groups, Remark 7.39, p. 113 and Proposition 7.47, p. 116.

# Verification Notes

- Definition source: Direct from Remark 7.39
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
