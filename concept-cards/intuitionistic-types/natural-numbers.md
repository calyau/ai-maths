---
# === CORE IDENTIFICATION ===
concept: Natural Numbers
slug: natural-numbers

# === CLASSIFICATION ===
category: type-formers
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Löf"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: null
section: "1.7. Natural numbers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "N"
  - "type of natural numbers"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
related:
  - successor-function
  - primitive-recursion
  - mathematical-induction
  - finite-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by recursion on natural numbers?"
---

# Quick Definition
N is the type of natural numbers. It is introduced by two constructors: 0 is an object of type N, and if n is an object of type N then s(n) (the successor of n) is an object of type N.

# Core Definition
Martin-Lof states: "N is a type, namely, the type of natural numbers. 0 is an object of type N and, if n is an object of type N, so is its successor s(n). These are the first two Peano axioms." (Section 1.7)

# Prerequisites
- **Type**: Must understand what a type is and how types are defined by their constructors.

# Key Properties
1. 0 is a canonical object of type N (base case).
2. s(n) is a canonical object of type N whenever n is (successor case).
3. These correspond to the first two Peano axioms.
4. N is the prime example of a type introduced by an ordinary inductive definition.
5. Functions out of N are defined by the recursion schema using the R operator.

# Construction / Recognition
## To Construct/Create:
1. 0 is a natural number.
2. If n is a natural number, then s(n) is a natural number.
3. These are the only ways to construct natural numbers.

## To Identify/Recognize:
1. The type whose objects are built from 0 by iterated application of the successor.
2. The canonical inductive type with a base element and a successor operation.

# Context & Application
The natural numbers type N is fundamental to Martin-Lof's theory. It serves as the basic inductive type from which arithmetic is developed. Functions on N are defined by primitive recursion (the R operator), and propositions about N are proved by mathematical induction (which is recursion when types represent propositions). Martin-Lof notes that N "is just the prime example of a type introduced by an ordinary inductive definition" and that the general formulation of inductive definitions would include Sigma, +, N_n, and N as special cases (Section 1.7).

# Examples
The equality function E on natural numbers (from Section 1.8) is defined by recursion on N:
- E(0,0) = top
- E(s(m),0) = bottom
- E(0,s(n)) = bottom
- E(s(m),s(n)) = E(m,n)

This gives the third and fourth Peano axioms.

# Relationships
## Builds Upon
- **type**: N is a type.
## Enables
- **successor-function**: s is the successor constructor for N.
- **primitive-recursion**: The R operator defines functions out of N.
- **mathematical-induction**: Induction is the propositional reading of recursion.
## Related
- **finite-type**: N is the infinite analogue of the finite types N_n.

# Common Errors
- **Error**: Assuming the Peano axioms of distinctness and injectivity are separate postulates.
  **Correction**: Martin-Lof notes that the third and fourth Peano axioms (0 != s(n), injectivity of s) follow from defining equality by recursion using the universe V (Section 1.8).

# Common Confusions
- **Confusion**: Thinking N is defined as a set satisfying the Peano axioms.
  **Clarification**: N is defined inductively by its constructors (0 and s). The Peano axioms are consequences of this definition together with the recursion principle and the universe.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.7.

# Verification Notes
Extracted directly from Section 1.7. High confidence.
