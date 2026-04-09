---
# === CORE IDENTIFICATION ===
concept: Decidability of Definitional Equality
slug: decidability-of-definitional-equality

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
section: "4.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "decidability of conversion"
  - "Corollary 4.3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normalization-theorem
  - normalization-for-types
  - conversion
  - church-rosser-property
extends:
  - normalization-theorem
related:
  - normal-term-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Church-Rosser property?"
---

# Quick Definition

It can be mechanically decided whether or not two terms or two types are definitionally equal: normalize both sides and check if their normal forms are syntactically identical (up to bound variable renaming).

# Core Definition

Martin-Lof states: "It can be mechanically decided whether or not two terms or two types are definitionally equal." (Section 4.3)

The decision procedure for types: "Let A and B be two types. In order to decide whether or not A conv B we simply normalize A and B, which is possible according to the previous corollary, and check whether or not their normal forms are syntactically equal except possibly for differences in the naming of their bound variables."

The decision procedure for terms: "if a is a term of type A and b a term of type B, we first decide whether or not A conv B and then, in case the answer is positive, whether or not a conv b. According to the normalization theorem, the latter decision can also be reached by normalizing a and b and checking if their normal forms are the same."

# Prerequisites

- **normalization-theorem**: Guarantees that terms can be normalized.
- **normalization-for-types**: Guarantees that types can be normalized.
- **conversion**: The equivalence relation (definitional equality) being decided.
- **church-rosser-property**: Guarantees that if two terms are convertible, they share a common reduct, hence the same normal form.

# Key Properties

1. The decision procedure is fully mechanical (algorithmic).
2. It relies on two facts: (a) normal forms exist (normalization), and (b) convertible terms have the same normal form (Church-Rosser).
3. For terms, one must first check type equality before comparing terms.
4. Syntactic comparison is up to alpha-equivalence (renaming of bound variables).

# Construction / Recognition

## Decision Procedure for Type Equality (A conv B?):
1. Normalize A to its normal form A'.
2. Normalize B to its normal form B'.
3. Check whether A' and B' are syntactically identical up to bound variable renaming.
4. If yes: A conv B. If no: A and B are not definitionally equal.

## Decision Procedure for Term Equality (a conv b?):
1. First check whether their types are definitionally equal (using the above).
2. If types are not equal, the question is ill-formed.
3. If types are equal, normalize a to a' and b to b'.
4. Check whether a' and b' are syntactically identical up to bound variable renaming.

# Context & Application

Decidability of definitional equality is a fundamental property of a type theory. It means that type-checking can be made algorithmic: whenever a typing rule requires checking that two types or terms are definitionally equal (e.g., the type conversion rule), this check can be performed mechanically.

Without normalization, conversion would be undecidable in general (one would have to search for a common reduct without knowing if the search would terminate).

# Examples

- To check if (lambda x)(x + 0) conv (lambda x)x at type N -> N: normalize both. If the contraction rules for + reduce x + 0 to x, the normal forms are the same.
- To check if (Pi x in N)N conv (Pi x in N)N: the types are already in normal form and syntactically identical, so they are convertible.
- To check if (lambda x)(lambda y)x conv (lambda u)(lambda v)u: the normal forms differ only in bound variable names, so they are convertible (alpha-equivalent).

# Relationships

## Builds Upon
- normalization-theorem, normalization-for-types: Provide the normalization step.
- church-rosser-property: Guarantees that conversion is captured by normal form comparison.

## Enables
- Algorithmic type-checking for the theory of types.

## Related
- normal-term-structure: Normal forms have predictable structure, making comparison straightforward.

# Common Errors

- **Error**: Forgetting to check type equality before comparing terms.
  **Correction**: The decision procedure for term equality requires first establishing that the two terms have convertible types.

# Common Confusions

- **Confusion**: Thinking decidability of definitional equality implies decidability of type inhabitation.
  **Clarification**: Decidability of conversion means we can check whether two given terms/types are equal. This does not tell us whether a given type has any term at all (the inhabitation problem, which is undecidable in sufficiently expressive type theories).

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.3: Corollary.

# Verification Notes

Confidence: high. Explicitly stated as Corollary 4.3 with a clear algorithmic description.
