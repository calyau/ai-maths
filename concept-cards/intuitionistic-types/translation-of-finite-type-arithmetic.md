---
# === CORE IDENTIFICATION ===
concept: Translation of Finite Type Arithmetic
slug: translation-of-finite-type-arithmetic

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
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "embedding of HA-omega with AC"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - translation-of-first-order-arithmetic
  - axiom-of-choice
  - finite-type
extends:
  - translation-of-first-order-arithmetic
related:
  - translation-of-arithmetical-analysis
  - law-of-excluded-middle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the axiom of choice relate to the Sigma and Pi types?"
  - "What distinguishes the intuitionistic axiom of choice from its classical counterpart?"
---

# Quick Definition

Intuitionistic arithmetic of finite type with the axiom of choice embeds into the theory of types by translating the simple type hierarchy into iterated arrow types over N, and by recognizing the axiom of choice as an instance of the type-theoretic axiom of choice proved in section 2.5.

# Core Definition

Section 3.3 defines the system and its translation:

**The system** (3.3.1):
- Types: 0 is a type; if sigma and tau are types, so is sigma -> tau.
- Terms: variables, 0 and successor, lambda abstraction, recursion R, and application.
- Formulae: built from numerical equations using connectives and quantifiers over all finite types.
- Contraction rules: beta-reduction, recursion contractions, and equality contractions (same as first order arithmetic).
- Rules: intuitionistic first order arithmetic rules extended with quantifiers over all finite types, plus the axiom of choice: forall x exists y C[x,y] supset exists f forall x C[x, f(x)] with x, y, f of types sigma, tau, sigma -> tau.

**Translation** (3.3.2):
- Type 0* = N
- (sigma -> tau)* = sigma* -> tau*
- Variables, 0, successor, lambda, R, and application translate homomorphically.
- Formulae translate as in first order arithmetic, with quantifiers over type tau using the translated type tau*.
- The axiom of choice translates to: (Pi x* in sigma*)(Sigma y* in tau*)C*[x*,y*] -> (Sigma f* in sigma* -> tau*)(Pi x* in sigma*)C*[x*, f*(x*)]

This is exactly an instance of the axiom of choice proved in section 2.5.

# Prerequisites

- translation-of-first-order-arithmetic: The base case (ground type) uses the arithmetic translation.
- axiom-of-choice: The AC of the source theory is an instance of the type-theoretic AC.
- finite-type: The simple type hierarchy 0, sigma -> tau maps to iterated arrow types.

# Key Properties

1. The simple types of the source theory translate homomorphically: 0 maps to N, arrow maps to arrow.
2. The term translation is also homomorphic -- each constructor maps to its namesake in type theory.
3. The axiom of choice is NOT an additional axiom in the translation; it is an instance of the theorem proved in 2.5.
4. Higher-type quantifiers forall x^tau and exists x^tau translate to Pi and Sigma over tau*.
5. This system is a subsystem of the theory of types.

# Construction / Recognition

## To Translate:
1. Map simple types to arrow types over N: 0 -> N, (sigma -> tau) -> sigma* -> tau*.
2. Map terms homomorphically.
3. Map formulae as in arithmetic, extending quantifiers to all types.
4. The axiom of choice instances become instances of the type-theoretic AC.

# Context & Application

This translation shows that the theory of types subsumes a significant system of higher-type arithmetic with choice. The result is notable because adding the law of excluded middle to this system would yield full simple type theory (Spector 1962), which is proof-theoretically much stronger. This observation leads to section 3.3.3's result about the inconsistency of excluded middle.

# Examples

The axiom of choice at ground type: forall n:0 exists m:0 P(n,m) supset exists f:(0->0) forall n:0 P(n, f(n))

Translates to: (Pi n* in N)(Sigma m* in N)P*(n*, m*) -> (Sigma f* in N -> N)(Pi n* in N)P*(n*, f*(n*))

This is an instance of the AC proved in 2.5 with A = N, B[x] = N, C[x,y] = P*(x,y).

# Relationships

## Builds Upon
- translation-of-first-order-arithmetic: Ground-type base.
- axiom-of-choice: The AC instances are proved by the type-theoretic AC.

## Enables
- law-of-excluded-middle: The discussion in 3.3.3 uses this embedding to show LEM is inconsistent.

## Related
- translation-of-arithmetical-analysis: The next extension, to second-order quantification.

# Common Errors

- **Error**: Thinking the axiom of choice needs to be separately justified in the translation.
  **Correction**: It is automatic -- each instance is an instance of the theorem from 2.5.

# Common Confusions

- **Confusion**: Whether this translation covers classical finite-type arithmetic.
  **Clarification**: No. Only the intuitionistic version embeds. Adding classical logic (excluded middle) would yield a system too strong to embed (see 3.3.3).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 3.3: Intuitionistic arithmetic of finite type with the axiom of choice.

# Verification Notes

Confidence: high. The system and translation are fully specified in 3.3.1-3.3.2.
