---
# === CORE IDENTIFICATION ===
concept: Translation of Arithmetical Analysis
slug: translation-of-arithmetical-analysis

# === CLASSIFICATION ===
category: translations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Reduction of Some Other Formal Theories to the Theory of Types"
chapter_number: 3
pdf_page: 24
section: "3.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "embedding of second-order arithmetic"
  - "analysis with AC"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - translation-of-first-order-arithmetic
  - axiom-of-choice
  - universe
extends:
  - translation-of-first-order-arithmetic
  - translation-of-finite-type-arithmetic
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the axiom of choice relate to the Sigma and Pi types?"
---

# Quick Definition

Intuitionistic arithmetical analysis with the axiom of choice embeds into the theory of types by translating predicate variables as variables of type N -> ... -> N -> V (using the universe), and by recognizing the second-order axiom of choice as another instance of the type-theoretic AC from section 2.5.

# Core Definition

Section 3.4 extends first order arithmetic with:
- n-ary predicate variables X, Y, ... for every n
- Atomic formulae: a = b or B(a_1, ..., a_n) where B is a predicate term
- Predicate terms: predicate variables or (lambda x_1 ... x_n)B[x_1, ..., x_n] (with no bound predicate variables in B)
- Second-order quantifiers: forall X and exists X
- Axiom of choice: forall x exists X C[x, X] supset exists Y forall x C[x, Y(x)]

**Translation** (3.4.2):
- n-ary predicate variable X maps to X* of type N -> ... -> N -> V (n arrows then V)
- B(a_1, ..., a_n)* is B*(a_1*, ..., a_n*)
- forall X B[X] maps to (Pi X* in N -> ... -> N -> V)B*[X*]
- exists X B[X] maps to (Sigma X* in N -> ... -> N -> V)B*[X*]
- (lambda x_1 ... x_n)B[x_1, ..., x_n]* is (lambda x_1*) ... (lambda x_n*)B*[x_1*, ..., x_n*], which is a term of type N -> ... -> N -> V by repeated use of the reflection principle
- Second-order quantifier rules are interpreted like first-order ones
- The axiom of choice translates to an instance of the AC from 2.5

# Prerequisites

- translation-of-first-order-arithmetic: The base numerical and logical translation.
- axiom-of-choice: The AC instances are handled by the theorem from 2.5.
- universe: Predicate variables range over types in V, so the universe is essential.

# Key Properties

1. The universe V plays a central role: predicate variables range over V-valued functions, making predicates into type-forming operations.
2. The reflection principle ensures that predicate lambda terms translate to terms of type N -> ... -> N -> V.
3. The restriction to predicates without bound predicate variables ensures the translation stays within the predicative universe V.
4. The axiom of choice at second order is just another instance of the type-theoretic AC.
5. This is the most expressive system embedded in Chapter 3, incorporating both higher-type functions and second-order quantification over predicates.

# Construction / Recognition

## To Translate:
1. Translate the arithmetic base as in 3.2.
2. Map n-ary predicate variables to variables of type N -> ... -> N -> V.
3. Map predicate application B(a_1, ..., a_n) to B*(a_1*, ..., a_n*).
4. Map second-order quantifiers to Pi and Sigma over the predicate type.
5. Translate predicate lambda terms using the reflection principle.
6. Axiom of choice instances become instances of the theorem from 2.5.

# Context & Application

This embedding demonstrates the expressive power of the theory of types: it subsumes not only first-order arithmetic and finite-type arithmetic but also a significant fragment of second-order arithmetic (analysis). The universe V is what makes this possible -- it provides a "type of types" over which predicate variables can range.

The restriction to predicates without bound predicate variables (in predicate lambda terms) keeps the system predicative. Full impredicative second-order arithmetic would require V in V, which leads to Girard's paradox.

# Examples

The axiom of choice for analysis: forall n exists X P(n, X) supset exists Y forall n P(n, Y(n))
with X an n-ary predicate variable and Y having one more argument.

Translates to:
(Pi n* in N)(Sigma X* in N^n -> V)P*(n*, X*) -> (Sigma Y* in N -> N^n -> V)(Pi n* in N)P*(n*, Y*(n*))

This is an instance of AC from 2.5 with A = N, B[x] = N^n -> V.

# Relationships

## Builds Upon
- translation-of-first-order-arithmetic: Base numerical translation.
- axiom-of-choice: Handles the AC instances.
- universe: Predicate variables live in V.

## Extends
- translation-of-finite-type-arithmetic: Adds second-order quantification.

# Common Errors

- **Error**: Thinking predicate variables can range over arbitrary types.
  **Correction**: They range over functions into V (small types only). This predicativity restriction is essential; without it, the system would be inconsistent.

# Common Confusions

- **Confusion**: How the reflection principle is used for predicate lambdas.
  **Clarification**: The reflection principle guarantees that if B*[x_1*, ..., x_n*] is a term of type V (which it is, since atomic formula translations land in V), then (lambda x_1*) ... (lambda x_n*)B*[...] is a term of type N -> ... -> N -> V.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.4: Intuitionistic arithmetical analysis with the axiom of choice.

# Verification Notes

Confidence: high. The translation is given explicitly in 3.4.2.1-3.4.2.6.
