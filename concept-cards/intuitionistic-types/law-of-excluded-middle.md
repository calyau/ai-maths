---
# === CORE IDENTIFICATION ===
concept: Law of Excluded Middle (Inconsistency with Type Theory)
slug: law-of-excluded-middle

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
section: "3.3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "LEM"
  - "A v ~A"
  - "tertium non datur"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - translation-of-finite-type-arithmetic
  - axiom-of-choice
extends: []
related:
  - translation-of-first-order-predicate-logic
contrasts_with:
  - axiom-of-choice

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the intuitionistic axiom of choice from its classical counterpart?"
---

# Quick Definition

The law of excluded middle (A v ~A) is not consistent relative to the theory of types. Adding it would make the system proof-theoretically as strong as full simple type theory, and the double negation interpretation cannot rescue it.

# Core Definition

Section 3.3.3 argues: "When the law of the excluded middle A v ~A (or, equivalently, reductio ad absurdum ~~A supset A) is added to intuitionistic arithmetic of finite type with the axiom of choice, the resulting system contains full simple type theory."

Since intuitionistic arithmetic of finite type with AC is a subsystem of the theory of types (by the translation of section 3.3.2), the same holds for the theory of types itself. Consequently:

1. The axiom schema A + ~A (or equivalently, ~~A -> A) is NOT consistent relative to the theory of types.
2. The double negation interpretation (Kolmogorov 1925, Godel 1933, Gentzen 1933) does NOT work for this theory.

The reason the double negation interpretation fails is that "the axioms for + and Sigma are stronger than the usual intuitionistic axioms for v and exists." In type theory, A + B (disjoint union) carries a tag indicating which disjunct holds, and (Sigma x in A)B[x] carries the witness. These are strictly stronger than the classical disjunction and existence, which merely assert truth without providing computational content.

# Prerequisites

- translation-of-finite-type-arithmetic: The argument uses the embedding of finite-type arithmetic with AC.
- axiom-of-choice: The combination of AC with LEM produces full simple type theory.

# Key Properties

1. A + ~A is NOT a theorem of the theory of types for general A.
2. Adding A + ~A as an axiom schema would be inconsistent relative to the theory (in the sense of making it proof-theoretically too strong, not in the sense of deriving a contradiction from consistent axioms).
3. The failure is specific to the CONSTRUCTIVE meaning of disjunction (+) and existence (Sigma): they carry witnesses that classical logic does not require.
4. This is referenced in the context of Spector 1962's result that AC + LEM yields full simple type theory.
5. The theory of types, without LEM, has a controlled proof-theoretic strength; with LEM, it would jump dramatically.

# Construction / Recognition

## To Understand the Argument:
1. Note that intuitionistic finite-type arithmetic + AC embeds in type theory (section 3.3.2).
2. Adding LEM to this system yields full simple type theory (Spector 1962).
3. Therefore adding LEM to the theory of types would yield at least full simple type theory.
4. This is inconsistent with the intended proof-theoretic strength of the system.

# Context & Application

This result is one of the key ways in which the theory of types differs from classical mathematics. It is not merely that excluded middle is unprovable (as in Heyting arithmetic) -- it is that adding it would fundamentally change the character of the system. The axiom of choice, which is innocuous in the type-theoretic setting, becomes dangerous when combined with classical logic because the witnesses carried by Sigma types can be exploited to define arbitrary choice functions.

This also explains why the Curry-Howard correspondence works only for intuitionistic logic: the computational content of proofs requires that disjunction and existence be witnessed.

# Examples

Consider A = "the Goldbach conjecture." In classical logic, A v ~A is a tautology. In type theory, a term of type A + ~A would be either i(p) where p is a proof of A, or j(q) where q is a refutation. Since we do not know which case holds, we cannot construct such a term.

# Relationships

## Builds Upon
- translation-of-finite-type-arithmetic: The embedding that makes the argument work.
- axiom-of-choice: AC + LEM = full simple type theory.

## Contrasts With
- axiom-of-choice: AC is provable and harmless in type theory; LEM is not consistent relative to it. The combination is what is dangerous.

# Common Errors

- **Error**: Thinking "inconsistent relative to the theory" means a contradiction is derivable.
  **Correction**: It means the proof-theoretic strength would increase beyond what the theory is intended to capture. The theory of types is meant to have constructive strength; adding LEM would push it to impredicative classical strength.

# Common Confusions

- **Confusion**: If AC is provable and LEM seems harmless, why can't they coexist?
  **Clarification**: In classical set theory, AC is strong and LEM is trivial. In type theory, the situation is reversed: AC is trivial (because Sigma types carry witnesses) but LEM is strong (because it would provide witnesses for every disjunction without computation).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.3.3.

# Verification Notes

Confidence: high. The argument is explicitly stated in 3.3.3, citing Spector 1962.
