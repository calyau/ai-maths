---
# === CORE IDENTIFICATION ===
concept: Disjoint Union of a Family of Types (Sigma Type)
slug: sigma-type

# === CLASSIFICATION ===
category: type-formers
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: 0
section: "1.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Sigma type"
  - "dependent pair type"
  - "dependent sum"
  - "disjoint union of a family of types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - mathematical-object
extends: []
related:
  - pairing
  - sigma-elimination
  - sigma-elimination
  - existential-quantification
  - such-that-type
  - cartesian-product-of-two-types
contrasts_with:
  - pi-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the disjoint union (Sigma type) of a family of types?"
  - "How does existential quantification relate to the Sigma type?"
  - "What distinguishes the Pi type from the Sigma type?"
---

# Quick Definition

The Sigma type (Sigma x in A)B(x) is the type of pairs (a, b) where a is an object of type A and b is an object of type B(a), with the second component's type depending on the first.

# Core Definition

Martin-Lof writes: "Given a type A and a function B which to an object a of type A assigns a type B(a), we may form the *disjoint union* (Sigma x in A)B(x) which is the type of pairs (a,b) where a and b are objects of type A and B(a), respectively." (Section 1.4)

Logical reading: "When B(a) represents a proposition for every object a of type A, (Sigma x in A)B(x) represents the *existential* proposition (exists x in A)B(x) which we prove by exhibiting a pair (a,b) where a is an object of type A and b a proof of the proposition B(a)." (Section 1.4)

Non-dependent special case: "In the special case when B(a) is defined to be one and the same type B for every object a of type A, (Sigma x in A)B(x) is abbreviated [A x B]. It is the *cartesian product* of the two types A and B." (Section 1.4)

# Prerequisites

- **type**: A and B(x) must be types.
- **mathematical-object**: The components of the pair are mathematical objects.

# Key Properties

1. Objects of the Sigma type are dependent pairs (a, b) with a in A and b in B(a).
2. The type of the second component depends on the value of the first.
3. When B(a) represents propositions, the Sigma type represents existential quantification.
4. When B is constant, the Sigma type reduces to the ordinary Cartesian product A x B.
5. The Sigma type also serves as the "such that" type: the type of all a in A such that B(a).

# Construction / Recognition

## To Construct/Create:
1. Specify a type A and a family B of types indexed by objects of A.
2. Form (Sigma x in A)B(x).
3. To construct an object, form a pair (a, b) with a in A and b in B(a).

## To Identify/Recognize:
1. Notation: (Sigma x in A)B(x).
2. A type described as "pairs where the second component's type depends on the first."
3. Special case: A x B when B is constant.

# Context & Application

The Sigma type is the second fundamental type-forming operation alongside the Pi type. It has three important interpretations: (1) existential quantification in logic, (2) the "such that" type for constrained objects, and (3) the ordinary Cartesian product in the non-dependent case. The "such that" reading is particularly important for formalizing mathematical definitions (e.g., real numbers as Cauchy sequences together with their convergence proofs).

# Examples

From Section 1.4: The type R of real numbers is (Sigma x in N -> Q)(Pi m in N)(Pi n in N)(|x_{m+n} - x_m| <= 2^{-m}). A real number is a pair (a, b) where a is a sequence of rationals and b is a proof of the Cauchy condition.

From Section 1.4: If A and B are propositions, (Sigma x in A)B(x) represents (exists x in A)B(x), proved by exhibiting a witness a and a proof b of B(a).

# Relationships

## Builds Upon
- type, mathematical-object

## Enables
- pairing: The introduction form for Sigma types.
- sigma-elimination: The general elimination form.
- left-and-right-projection: Derived elimination forms.
- existential-quantification: The logical reading of Sigma.
- such-that-type: The "such that" reading of Sigma.
- cartesian-product-of-two-types: The non-dependent special case.
- conjunction: The logical reading of the non-dependent case.

## Related
- proof-object: The "such that" interpretation requires treating proofs as objects.

## Contrasts With
- pi-type: Pi is the type of functions over a family (for all); Sigma is the type of pairs from a family (there exists). Pi corresponds to universal quantification; Sigma to existential.

# Common Errors

- **Error**: Forming a pair (a, b) where b is of type B(a') for some a' != a.
  **Correction**: In a pair (a, b) of type (Sigma x in A)B(x), the second component b must be of type B(a) -- the type determined by the *first* component a.

# Common Confusions

- **Confusion**: Thinking "disjoint union" means the same as A + B (disjoint union of two types).
  **Clarification**: (Sigma x in A)B(x) is the disjoint union of a *family* of types B(a) indexed by a in A. The binary disjoint union A + B (Section 1.5) is a different construction.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. The Sigma type is explicitly defined in Section 1.4 with clear notation, logical reading, and the non-dependent special case stated directly.
