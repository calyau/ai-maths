---
# === CORE IDENTIFICATION ===
concept: Translation of First Order Predicate Logic
slug: translation-of-first-order-predicate-logic

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
section: "3.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "embedding of predicate logic"
  - "propositions-as-types translation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - lambda-abstraction
  - application
  - pairing
  - sigma-elimination
  - definition-by-cases
extends: []
related:
  - translation-of-derivations
  - translation-of-first-order-arithmetic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does first order predicate logic embed into the theory of types?"
---

# Quick Definition

Intuitionistic first order predicate logic embeds into the theory of types by translating individual variables into variables of a type I* (for individuals), function symbols into constants of the appropriate type, predicate constants into type constants, and logical connectives into the corresponding type-forming operations.

# Core Definition

Section 3.1.2 gives the translation in two parts: the language and the derivations.

**Translation of the language** (3.1.2.1):
- Individual variable x maps to variable x* of type I* (a 0-ary type constant)
- n-ary function symbol f maps to constant f* of type I* -> ... -> I* -> I* (n+1 copies)
- n-ary predicate constant P maps to n-ary type constant P* with all arguments of type I*
- Atomic formula P(a_1, ..., a_n) maps to type P*(a_1*, ..., a_n*)

**Logical connectives**:
| First order logic | Type theory |
|---|---|
| bottom | N_0 |
| A supset B | A* -> B* |
| A & B | A* x B* |
| A v B | A* + B* |
| forall x B[x] | (Pi x* in I*)B*[x*] |
| exists x B[x] | (Sigma x* in I*)B*[x*] |

For every formula A, the type A* is normal.

# Prerequisites

- type: The target of the translation.
- lambda-abstraction, application, pairing, sigma-elimination, definition-by-cases: The term formers that interpret the proof rules.

# Key Properties

1. The translation is structure-preserving: each logical connective maps to its type-theoretic counterpart.
2. Translated formulae are always normal types (no computation needed at the type level).
3. The translation extends to derivations (see translation-of-derivations).
4. The embedding is isomorphic: it preserves the reduction relation on derivations (3.1.3).
5. Prawitz's normalization theorem for first order logic becomes a corollary of the normalization theorem for the theory of types.

# Construction / Recognition

## To Translate a Formula:
1. Introduce a 0-ary type constant I* for individuals.
2. Map each function symbol to a constant of appropriate arrow type over I*.
3. Map each predicate symbol to a type constant over I*.
4. Replace each logical connective with its type-theoretic counterpart per the table above.

# Context & Application

This translation is the formal core of the propositions-as-types correspondence (Curry-Howard isomorphism) for first order logic. It shows that intuitionistic first order predicate logic is a subsystem of the theory of types. Combined with the translation of derivations, it provides a complete embedding that preserves computational content.

# Examples

The formula forall x (P(x) supset exists y Q(x,y)) translates to:
(Pi x* in I*)(P*(x*) -> (Sigma y* in I*)Q*(x*, y*))

The formula (A & B) supset A translates to: (A* x B*) -> A*

# Relationships

## Builds Upon
- The type-forming operations Pi, Sigma, +, N_0 and the term formers.

## Enables
- translation-of-derivations: The derivation translation builds on the language translation.
- translation-of-first-order-arithmetic: Extends this translation with arithmetic.

# Common Errors

- **Error**: Forgetting that the translation uses a type constant I* for individuals, not the natural numbers N.
  **Correction**: First order predicate logic is uninterpreted -- the domain of individuals is represented by the unspecified type constant I*. Arithmetic (3.2) uses N instead.

# Common Confusions

- **Confusion**: Whether this translation works for classical logic.
  **Clarification**: Only intuitionistic first order logic embeds. Classical logic includes the law of excluded middle A v ~A, which is not provable (and not even consistent relative to the theory, per 3.3.3).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.1: Intuitionistic first order predicate logic.

# Verification Notes

Confidence: high. The translation is given explicitly in 3.1.2.1 with a complete table of connective mappings.
