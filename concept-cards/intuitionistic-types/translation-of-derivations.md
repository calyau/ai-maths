---
# === CORE IDENTIFICATION ===
concept: Translation of Derivations
slug: translation-of-derivations

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
section: "3.1.2.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "proofs-to-terms translation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - translation-of-first-order-predicate-logic
extends:
  - translation-of-first-order-predicate-logic
related:
  - translation-of-first-order-arithmetic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I translate a first order derivation into a term of the theory of types?"
---

# Quick Definition

The translation of derivations maps each proof rule of intuitionistic first order predicate logic to the corresponding term-formation rule of type theory, producing a term of the translated type. This is the proof-level content of the propositions-as-types correspondence.

# Core Definition

Section 3.1.2.2 defines the translation by induction on the length of a derivation. Each rule of inference maps to a term former:

| Inference rule | Term construction |
|---|---|
| Assumption A | Variable x* of type A* |
| supset-introduction | Lambda abstraction: (lambda x*)b*[x*] |
| supset-elimination | Application: b*(a*) |
| &-introduction | Pairing: (a*, b*) |
| &-elimination (left) | Left projection: p[c*] = E(c*, (lambda x)(lambda y)x) |
| &-elimination (right) | Right projection: q[c*] = E(c*, (lambda x)(lambda y)y) |
| v-introduction (left) | Left injection: i(a*) |
| v-introduction (right) | Right injection: j(b*) |
| v-elimination | Definition by cases: D(c*, (lambda x*)d*[x*], (lambda y*)e*[y*]) |
| forall-introduction | Lambda abstraction: (lambda x*)b*[x*] |
| forall-elimination | Application: b*(a*) |
| exists-introduction | Pairing: (a*, b*) |
| exists-elimination | Sigma elimination: E(c*, (lambda x*)(lambda y*)d*[x*, y*]) |
| bottom-elimination | N_0-elimination: R_0(c*) |

# Prerequisites

- translation-of-first-order-predicate-logic: The language translation must be in place first.

# Key Properties

1. The translation is an isomorphic embedding (3.1.3): if a red b in the derivation reduction (Prawitz's rules), then a* red b* in type theory, and conversely.
2. Open assumptions in the derivation become free variables in the term.
3. Discharge of an assumption (in supset-introduction or exists-elimination) corresponds to lambda abstraction over the corresponding variable.
4. The translation preserves the reduction relation, so Prawitz's normalization theorem for first order logic follows as a corollary of the normalization theorem for type theory.

# Construction / Recognition

## To Translate a Derivation:
1. For each open assumption A, introduce a variable x* of type A*.
2. For each inference step, apply the corresponding term constructor from the table above.
3. The resulting term has type equal to the translation of the conclusion.

## To Verify:
Check that the term is well-typed in the theory of types by verifying each step follows the appropriate term-formation rule.

# Context & Application

This translation makes precise the Curry-Howard correspondence for first order logic. Each proof becomes a computational object (a term), and proof normalization (eliminating detours) corresponds to term reduction. This connection allows proof-theoretic results about first order logic to be derived from the normalization theorem for type theory.

Martin-Lof notes (3.1.3): "Prawitz's 1965 normalization theorem for first order logic is a corollary of the normalization theorem for the theory of types that will be proved later on."

# Examples

A proof of A supset A (identity):

Derivation: Assume A, conclude A, discharge by supset-introduction.
Translation: (lambda x*)x* of type A* -> A*.

A proof of A & B supset B & A (commutativity of conjunction):

Derivation: Assume A & B, eliminate to get A and B, then introduce B & A.
Translation: (lambda z*)(q[z*], p[z*]) of type (A* x B*) -> (B* x A*).

# Relationships

## Builds Upon
- translation-of-first-order-predicate-logic: Uses the language translation.

## Enables
- translation-of-first-order-arithmetic: The arithmetic translation extends this with induction and formula conversion.

# Common Errors

- **Error**: Forgetting that assumption discharge corresponds to lambda abstraction.
  **Correction**: Each discharged assumption becomes a bound variable. An assumption A used in a proof of B becomes the variable x* in (lambda x*)b*[x*] of type A* -> B*.

# Common Confusions

- **Confusion**: Whether the translation of a derivation is unique.
  **Clarification**: The translation is determined by the derivation (including the structure of assumption discharge). Different derivations of the same formula may yield different terms.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.1.2.2: Translation of the derivations, and 3.1.3: Isomorphic embedding property.

# Verification Notes

Confidence: high. Every inference rule is translated explicitly in 3.1.2.2.1-3.1.2.2.12.
