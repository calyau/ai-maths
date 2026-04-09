---
# === CORE IDENTIFICATION ===
concept: Computability Predicate
slug: computability-predicate

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
section: "4.1.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "phi_A"
  - "computability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - normal-form
  - reduction
extends: []
related:
  - taits-method-of-computability
  - normalization-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a computable term (in the sense of the normalization proof)?"
---

# Quick Definition

The computability predicate phi_A is a property of closed terms of type A, defined by induction on the structure of A, used as the key proof device in establishing the normalization theorem.

# Core Definition

For each type A, the predicate phi_A expresses "computability" for closed terms of type A. It is defined in Section 4.1.1 by cases on the form of A:

- **Atomic types** (4.1.1.1): phi_{P(a_1,...,a_n)} is the species of normalizable closed terms of type P(a_1,...,a_n).
- **Pi types** (4.1.1.2): phi_{(Pi x in A)B[x]} is defined by three clauses:
  - (i) A lambda (lambda x)b[x] satisfies phi if phi_{B[a]}(b[a]) for all a with phi_A(a).
  - (ii) A closed normal term not of lambda form satisfies phi.
  - (iii) A term of elimination form that reduces to a phi-satisfying term itself satisfies phi.
- **Sigma types** (4.1.1.3): Analogous three clauses, with pairs (a,b) in place of lambdas.
- **Sum types** (4.1.1.4): Analogous three clauses, with canonical injections i(a) or j(b).
- **Universe V** (4.1.1.5): Defined by transfinite induction. Simultaneously defines what it means for a small type A to satisfy phi_V(A) and defines the associated predicate phi_A.

Martin-Lof writes: "we have to show by induction on the construction of a type or term, in case A is a type, how to define the predicate phi_A which expresses the computability of a term of type A, and, in case a is a term of type A, that phi_A is defined and that phi_A(a) holds."

# Prerequisites

- **type**: The predicate is indexed by types.
- **normal-form**: The base case (atomic types) and the second clause for compound types both refer to normal terms.
- **reduction**: The third clause for compound types refers to reduction.

# Key Properties

Lemma 4.1.2 establishes three key properties of phi_A (when defined):

1. **Normal non-introduction terms are computable**: If a is a closed normal term of type A that does not have introduction form, then phi_A(a).
2. **Closure under reduction from elimination form**: If b has elimination form and reduces to a term a with phi_A(a), then phi_A(b).
3. **Computability implies normalizability**: phi_A(a) implies that a is normalizable.

Additionally, Lemma 4.1.3 establishes:

4. **Invariance under conversion**: If phi_A and phi_B are both defined and A conv B, then phi_A(a) iff phi_B(a).

# Construction / Recognition

## To Determine phi_A for a Given Type:
1. If A is atomic: phi_A = normalizable closed terms of type A.
2. If A = (Pi x in C)D[x]: use the three-clause definition (lambda, normal non-lambda, elimination reducing to computable).
3. If A = (Sigma x in C)D[x]: analogous with pairs.
4. If A = C + D: analogous with canonical injections.
5. If A is a small type (term of type V): use the transfinite induction of 4.1.1.5.

## Three-Clause Pattern:
Each compound type's phi follows the same pattern:
- Clause 1 (introduction form): canonical terms are computable if their components are.
- Clause 2 (stuck normal terms): normal terms not of introduction form are automatically computable.
- Clause 3 (elimination form reducing to computable): backward closure under reduction from elimination form.

# Context & Application

The computability predicate is not a concept internal to the theory of types; it is a meta-theoretic proof device. It bridges between the syntactic notion of normalizability and the inductive structure of types, enabling the normalization proof to proceed by induction on type/term construction.

The key insight is that phi_A is stronger than mere normalizability for compound types. For Pi types, phi requires not just that the term normalizes but that applying it to any computable argument yields a computable result. This extra strength is what makes the inductive proof go through.

# Examples

For type N (natural numbers), phi_N is simply the species of normalizable closed terms of type N (since N is atomic via 4.1.1.5.1). So phi_N(0), phi_N(s(0)), etc.

For type N -> N, phi_{N -> N}((lambda x)b[x]) holds iff phi_N(b[a]) for all closed a of type N with phi_N(a) -- i.e., iff b[a] is normalizable for every normalizable closed numeral a.

# Relationships

## Builds Upon
- type, normal-form, reduction: The predicate is defined in terms of these.

## Enables
- normalization-theorem: The predicate is the main proof tool.

## Related
- taits-method-of-computability: The general technique that phi_A instantiates.

# Common Errors

- **Error**: Identifying computability with normalizability.
  **Correction**: For atomic types they coincide, but for compound types (Pi, Sigma, +), computability is strictly stronger. A Pi-type term must normalize AND yield computable results when applied to computable arguments.

- **Error**: Thinking phi_A depends only on the type A.
  **Correction**: For small types, phi_A also depends on the proof of phi_V(A), as Martin-Lof notes: "phi_A depends not only on A but also on the proof of phi_V(A) although my notation does not indicate that explicitly" (4.1.1.5).

# Common Confusions

- **Confusion**: Conflating "computable" in this technical sense with Church-Turing computability.
  **Clarification**: Here "computable" is a technical property used in the normalization proof. It has no direct connection to recursive functions or Turing machines. Every well-typed term turns out to be "computable" in this sense.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.1.1: Definition of phi_A for a type symbol A.

# Verification Notes

Confidence: high. The definition is given explicitly and in full detail in Section 4.1.1, with subclauses 4.1.1.1 through 4.1.1.6.
