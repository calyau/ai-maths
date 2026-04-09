---
# === CORE IDENTIFICATION ===
concept: "Tait's Method of Computability"
slug: taits-method-of-computability

# === CLASSIFICATION ===
category: normalization
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "The Normalization Theorem and Its Consequences"
chapter_number: 4
pdf_page: 34
section: "4.1"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "computability method"
  - "Tait computability"
  - "method of computability"
  - "logical relations method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - normal-form
  - reduction
extends: []
related:
  - computability-predicate
  - normalization-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding the normalization theorem?"
---

# Quick Definition

Tait's method of computability is a proof technique for normalization theorems. One defines a "computability" predicate on terms by induction on type structure, proves all terms satisfy it, and extracts normalizability as a consequence.

# Core Definition

Martin-Lof writes: "My proof of normalization uses an extension of the method of computability introduced by Tait 1967 in order to prove normalization for the terms of Godel's 1958 theory of primitive recursive functionals of finite type and systematically exploited in the Proceedings of the Second Scandinavian Logic Symposium." (Section 4.1)

The method has three steps:

1. **Define** a predicate phi_A on closed terms, by induction on the type A, such that phi_A is stronger than normalizability for compound types.
2. **Prove** that every well-typed term satisfies phi_A (the "main lemma" or verification, Section 4.1.4).
3. **Conclude** normalizability, since phi_A(a) implies a is normalizable (Lemma 4.1.2, third property).

The extension Martin-Lof requires is necessitated by the fact that "in the present theory, however, the definition of the notion of computability and the proof that an arbitrary term is computable can no longer be separated, because the terms and the types are generated simultaneously."

# Prerequisites

- **type**: The predicate is defined by induction on type structure.
- **normal-form**: The target property that computability implies.
- **reduction**: The predicate's definition involves reduction.

# Key Properties

1. The computability predicate is strictly stronger than normalizability for compound types (e.g., for Pi types, it requires that application to computable arguments yields computable results).
2. The extra strength is precisely what makes the inductive proof go through -- simple normalizability would not have a strong enough induction hypothesis.
3. In Tait's original setting (simple types), the definition of phi and the proof that terms satisfy it can be done in two separate stages. In Martin-Lof's dependent type theory, they must be interleaved.
4. For the universe V, the definition requires transfinite induction (Section 4.1.1.5).

# Construction / Recognition

## The Method in Outline:
1. For each type former, define what phi means for terms of that type. The definition should:
   - Make canonical (introduction-form) terms computable when their parts are computable.
   - Make stuck normal terms (non-introduction form) automatically computable.
   - Close under backward reduction from elimination form.
2. Prove the three key properties of phi (Lemma 4.1.2).
3. Verify by induction on typing derivations that every typed term is computable (Section 4.1.4).
4. Extract normalizability from computability.

# Context & Application

Tait's method is the standard technique for proving normalization in typed lambda calculi. It was introduced by Tait (1967) for Godel's System T and has since been adapted to many type theories. Martin-Lof's extension to handle dependent types (where types and terms are generated simultaneously) was a significant technical contribution, as it required interleaving the definition of computability with the proof that terms are computable.

The method is also known in the literature as the "logical relations" method or "reducibility candidates" method (the latter name due to Girard's related but distinct technique).

# Examples

In Tait's original setting (simple types):
- phi_N = normalizable terms of type N.
- phi_{A -> B}(f) iff for all a with phi_A(a), phi_B(f(a)).

In Martin-Lof's extension, the same pattern holds but must be defined simultaneously with the proof that terms are computable, because forming a type like (Pi x in A)B[x] requires a term x of type A, so the type structure and term structure are interleaved.

# Relationships

## Builds Upon
- type, normal-form, reduction: Conceptual prerequisites.

## Enables
- computability-predicate: The specific instance of the method in this paper.
- normalization-theorem: The result the method proves.

## Related
- No direct contrasts within this extraction scope.

# Common Errors

- **Error**: Thinking the computability predicate can always be defined separately from the proof that terms are computable.
  **Correction**: This separation works for simple types but fails for dependent types where types and terms are generated simultaneously.

# Common Confusions

- **Confusion**: Equating Tait's computability method with Girard's reducibility candidates.
  **Clarification**: Both are techniques for proving normalization by defining predicates on terms indexed by types. Girard's method (for System F / polymorphic lambda calculus) uses a different definition adapted to type quantification. Tait's method predates Girard's and is simpler for non-polymorphic systems.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.1, opening paragraphs. References: Tait 1967; Proceedings of the Second Scandinavian Logic Symposium.

# Verification Notes

Confidence: medium. Martin-Lof describes using Tait's method and explains how he extends it, but does not call it "Tait's method of computability" as a fixed term. The concept is synthesized from his description.
