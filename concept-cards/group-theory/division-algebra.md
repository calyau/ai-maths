---
# === CORE IDENTIFICATION ===
concept: Division Algebra
slug: division-algebra

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 107
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "skew field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends:
  - f-algebra
  - simple-f-algebra
related:
  - schur-lemma
  - wedderburn-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a division algebra?"
  - "What role do division algebras play in the structure of simple algebras?"
---

# Quick Definition

An F-algebra is a division algebra if every nonzero element has a multiplicative inverse. It satisfies all the field axioms except possibly commutativity.

# Core Definition

An F-algebra is said to be a **division algebra** if every nonzero element a has an inverse, i.e., there exists b such that ab = 1 = ba. A division algebra satisfies all the axioms for a field except commutativity, and is sometimes called a **skew field**. It has no nonzero proper ideals (left, right, or two-sided) and hence is simple. (Milne, Example 7.18, p. 107)

# Prerequisites

- **F-algebra** — division algebras are F-algebras

# Key Properties

1. Every nonzero element is invertible
2. No nonzero proper ideals (left, right, or two-sided)
3. Hence a division algebra is simple
4. Finitely generated modules over a division algebra are free (have a basis)
5. All bases of a free D-module have the same cardinality (dimension)
6. Over an algebraically closed field, the only division algebra is the field itself (7.31)
7. All finite division algebras are commutative (Wedderburn's little theorem)

# Construction / Recognition

1. Check that every nonzero element has a multiplicative inverse
2. Equivalently, check that A is simple and has no zero divisors

# Context & Application

Division algebras are the atoms from which all simple algebras are built: every simple F-algebra is M_n(D) for some division algebra D (Wedderburn, 7.25). By Schur's lemma, the endomorphism algebra of any simple module is a division algebra. Over algebraically closed fields, D = F, so simple algebras = matrix algebras.

# Examples

**Example 1** (p. 107, 7.18): Any field is a (commutative) division algebra.

**Example 2** (p. 108, 7.20): The quaternion algebra H(-1,-1) over R is a division algebra.

**Example 3** (p. 110, 7.31): Over an algebraically closed field F, the only division algebra is F itself.

# Relationships

## Builds Upon
- **f-algebra** — division algebras are special F-algebras

## Enables
- **wedderburn-theorem** — simple algebras are M_n(D)
- Free modules over division algebras (linear algebra over D)

## Related
- **schur-lemma** — End_A(S) is a division algebra for simple S

## Contrasts With
- Matrix algebras M_n(D) for n > 1 (have zero divisors, hence not division algebras)

# Common Errors

- **Error**: Assuming all division algebras are commutative
  **Correction**: The quaternions H(-1,-1) over R are a noncommutative division algebra

# Common Confusions

- **Confusion**: Confusing "division algebra" with "field"
  **Clarification**: A field is a commutative division algebra; general division algebras may be noncommutative

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.18 (p. 107) and 7.31-7.32 (pp. 110-111).

# Verification Notes

- Definition source: Direct from Example 7.18, p. 107
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
