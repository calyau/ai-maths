---
# === CORE IDENTIFICATION ===
concept: Mathematical Induction
slug: mathematical-induction

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
  - "induction principle"
  - "proof by induction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - natural-numbers
  - primitive-recursion
  - proposition
related:
  - pi-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by recursion on natural numbers?"
---

# Quick Definition
Mathematical induction is the special case of primitive recursion on natural numbers when the type family C represents a proposition. A proof of the base case C(0) and a proof of the inductive step (for all x in N)(C(x) -> C(s(x))) combine via the recursion operator R to yield a proof of (for all x in N)C(x).

# Core Definition
Martin-Lof states: "If C(n) represents a proposition for every natural number n, then (lambda x)R(x,d,e) is the proof of the universal proposition (forall x in N)C(x) which we get by applying the principle of mathematical induction to the proof d of C(0) and the proof e of (forall x in N)(C(x) -> C(s(x)))." (Section 1.7)

# Prerequisites
- **Natural numbers**: Induction is about proving properties of N.
- **Primitive recursion**: Induction is recursion when types represent propositions.
- **Proposition**: One must understand the propositions-as-types correspondence to see recursion as induction.

# Key Properties
1. Induction is not a separate principle but a consequence of recursion under propositions-as-types.
2. The base case d is a proof of C(0).
3. The inductive step e is a proof of (forall x in N)(C(x) -> C(s(x))).
4. The resulting function (lambda x)R(x,d,e) is a proof of (forall x in N)C(x).
5. This unification of recursion and induction is a hallmark of Martin-Lof's type theory.

# Construction / Recognition
## To Construct/Create:
1. Formulate the proposition C(n) to be proved for all n in N.
2. Prove the base case: construct d of type C(0).
3. Prove the inductive step: construct e of type (Pi x in N)(C(x) -> C(s(x))).
4. Apply the recursion operator: (lambda x)R(x, d, e) is the proof.

## To Identify/Recognize:
1. A proof that proceeds by establishing a base case and an inductive step for natural numbers.
2. In type-theoretic notation, a term built using R where the result type is propositional.

# Context & Application
The identification of mathematical induction with primitive recursion is one of the key insights of the propositions-as-types correspondence. It shows that the logical principle of induction and the computational principle of recursion are the same operation viewed from different perspectives. This is central to the constructive character of Martin-Lof's theory: a proof by induction is simultaneously a program defined by recursion.

# Examples
If C(n) is a proposition about natural numbers, d proves C(0), and e proves the step, then (lambda x)R(x, d, e) proves (forall x in N)C(x). The computation rules R(0,d,e) = d and R(s(n),d,e) = e(n,R(n,d,e)) show how the proof unfolds.

# Relationships
## Builds Upon
- **primitive-recursion**: Induction is the propositional reading of the R operator.
- **natural-numbers**: Induction is about properties of N.
- **proposition**: The logical reading requires propositions-as-types.
## Enables
- Proofs of universal statements about natural numbers.
## Related
- **cartesian-product-of-a-family-of-types**: The result (forall x in N)C(x) is a Pi type.

# Common Errors
- **Error**: Treating induction as a separate axiom rather than a consequence of recursion.
  **Correction**: In Martin-Lof's framework, induction is not postulated separately; it is simply what recursion becomes when the type family represents a proposition.

# Common Confusions
- **Confusion**: Thinking recursion and induction are fundamentally different.
  **Clarification**: They are the same operation (the R eliminator for N). The difference is only in how we read the types: as data types (recursion) or as propositions (induction).

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.7.

# Verification Notes
Extracted directly from Section 1.7. High confidence.
