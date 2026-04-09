---
# === CORE IDENTIFICATION ===
concept: Translation of First Order Arithmetic
slug: translation-of-first-order-arithmetic

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
section: "3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "embedding of Heyting arithmetic"
  - "HA translation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - translation-of-first-order-predicate-logic
  - translation-of-derivations
  - natural-numbers
  - primitive-recursion
  - universe
extends:
  - translation-of-first-order-predicate-logic
related:
  - equality-type
  - translation-of-finite-type-arithmetic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does first order arithmetic embed into the theory of types?"
  - "What must I know before understanding the translation of arithmetic?"
---

# Quick Definition

Intuitionistic first order arithmetic (Heyting arithmetic) embeds into the theory of types by translating numerical variables to variables of type N, arithmetic operations to primitive recursion terms, numerical equality to the recursively-defined type E(a,b), and the induction schema to N-elimination.

# Core Definition

Section 3.2.2 gives the translation:

**Language translation** (3.2.2.1):
- Numerical variable x maps to x* of type N
- 0* is the term 0 of type N
- (a')* is s(a*)
- (a + b)* is R(b*, a*, (lambda x*)(lambda y*)s(y*))
- (a . b)* is R(b*, 0, (lambda x*)(lambda y*)(y + a)*)
- Equation a = b translates to E(a*, b*) where E(a,b) is defined by double recursion (see equality-type)
- Composite formulae translate as in predicate logic, with top mapped to N_1

**Derivation translation** (3.2.2.2):
- The axiom top translates to the term 1 of type N_1
- The induction schema translates to N-elimination: R(a*, d*, (lambda x*)(lambda y*)e*[x*, y*])
- The rule of formula conversion translates to the rule of type conversion (since A conv B implies A* conv B*)

# Prerequisites

- translation-of-first-order-predicate-logic: The logical connectives are translated as before.
- translation-of-derivations: The proof rules of predicate logic are translated as before.
- natural-numbers: The type N is the target of numerical term translation.
- primitive-recursion: Addition and multiplication are defined by primitive recursion (R).
- universe: The type V is needed to ensure E(a,b) is a type (via the reflection principle).

# Key Properties

1. Arithmetic operations (+, .) are defined by primitive recursion on the second argument.
2. Numerical equality is NOT primitive but is defined by the recursively-defined type E(a,b) which lives in V.
3. The formula conversion rule of arithmetic maps to the type conversion rule of type theory.
4. Induction contractions in arithmetic map precisely to the contraction rules for R:
   - R(0, d*, ...) contr d*
   - R(s(a*), d*, (lambda x*)(lambda y*)e*[x*,y*]) contr e*[a*, R(a*, d*, ...)]
5. The usual axioms for number theory (Kleene 1952) can be derived in this system.

# Construction / Recognition

## To Translate:
1. Replace all numerical variables with variables of type N.
2. Replace 0 with 0 and successor ' with s.
3. Define + and . using R (primitive recursion).
4. Replace equations a = b with the type E(a*, b*).
5. Translate logical structure as in predicate logic.
6. Translate induction as N-elimination.
7. Use type conversion for formula conversion.

# Context & Application

The formulation of arithmetic with a rule of formula conversion (rather than explicit equality axioms) is specifically designed to interact well with derivation reduction. Martin-Lof explains (3.2.1) that without formula conversion, reducing a derivation that uses induction on a reducible term would require inserting logically complex sub-derivations that destroy the structural properties of the proof.

The key technical innovation is the equality type E(a,b), defined by double recursion using the reflection principle, which gives a type-theoretic analogue of decidable equality on natural numbers.

# Examples

Translation of the induction schema for C[x]:
- Given proofs d* of C[0]* and e*[x*,y*] of C[x']* (assuming x* in N and y* in C[x]*),
- The proof of C[a]* is R(a*, d*, (lambda x*)(lambda y*)e*[x*, y*]).

Translation of addition: (2 + 3)* = R(s(s(s(0))), s(s(0)), (lambda x)(lambda y)s(y))
This reduces: R(s(s(s(0))), 2, ...) -> e[s(s(0)), R(s(s(0)), 2, ...)] -> ... -> s(s(s(s(s(0))))) = 5.

# Relationships

## Builds Upon
- translation-of-first-order-predicate-logic: Extends the predicate logic translation.
- natural-numbers, primitive-recursion: The arithmetic operations are defined using these.
- universe: Needed for the equality type E(a,b).

## Enables
- translation-of-finite-type-arithmetic: Further extends to higher types.

# Common Errors

- **Error**: Thinking numerical equality is translated as a primitive type constant.
  **Correction**: Equality is defined by the recursively-constructed type E(a,b) using double recursion and the reflection principle (V-introduction).

# Common Confusions

- **Confusion**: Why is formula conversion needed as a separate rule?
  **Clarification**: Without it, when a numerical term a reduces to b, rewriting C[a] as C[b] in a derivation would require a complex logical sub-proof that disrupts the derivation structure and prevents a clean reduction theory.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.2: Intuitionistic first order arithmetic.

# Verification Notes

Confidence: high. The translation is given in full detail in 3.2.2, with explicit definitions of +, ., and E(a,b).
