---
# === CORE IDENTIFICATION ===
concept: Type Conversion Rule
slug: type-conversion-rule

# === CLASSIFICATION ===
category: formal-system
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.3.14"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "type conversion"
  - "structural rule"
  - "conversion rule"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-formation-rules
  - term-formation-rules
extends: []
related:
  - v-introduction-rule
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The type conversion rule (rule 2.3.14) is a structural rule stating that if a is a term of type A and A converts to B, then a is also a term of type B.

# Core Definition

Martin-Lof writes in Section 2.3.14: "This is a structural rule, that is, a rule which is to be considered neither as an introduction rule nor as an elimination rule. If a is a term of type A which converts to a type B, then a is a term of type B."

The schema is:

```
  a in A    A conv B
  ──────────────────
  a in B
```

Here "A conv B" means that A and B are convertible: there exists an expression C such that both A reduces to C and B reduces to C (as defined in Section 2.4).

# Prerequisites

- type-formation-rules: Both A and B must be types.
- term-formation-rules: The term a must be well-formed.

# Key Properties

1. Type conversion is neither an introduction rule nor an elimination rule -- it is a structural rule.
2. The rule does not change the term a; it only changes the type ascribed to a.
3. Conversion (A conv B) is an equivalence relation (reflexive, symmetric, transitive) as proved in Section 2.4.4.
4. A sequence of successive type conversion applications can be condensed into a single application (Section 2.4.4).
5. Between two successive applications of non-structural rules, at most one application of type conversion is needed.

# Construction / Recognition

## To Apply Type Conversion:
1. Have a term a of type A.
2. Show that A conv B (i.e., A and B reduce to a common expression).
3. Conclude that a is a term of type B.

## When Is It Needed:
Type conversion is needed when a term has been constructed with one type but is required to have a convertible type in the next step of a derivation. For example, after a contraction changes the form of a type expression.

# Context & Application

Type conversion is the rule that connects the term formation rules with the reduction/conversion machinery of Section 2.4. Without it, the type system would be too rigid: two types that differ only by reducible expressions would be treated as distinct. Type conversion ensures that types are identified up to computational equivalence.

This rule is essential for the interaction of V-introduction with the rest of the system: a term of type V is a small type by rule 2.2.6, but type conversion is needed when the same expression appears sometimes as a term of V and sometimes as a type.

# Examples

If A reduces to B (A red B), then A conv B, and any term of type A is also a term of type B.

If (lambda x)B[x](a) is a type that contracts to B[a], then a term of type (lambda x)B[x](a) is also a term of type B[a] by type conversion.

# Relationships

## Builds Upon
- type-formation-rules: The types A and B must be well-formed.
- term-formation-rules: The term a must be well-formed.

## Enables
- Smooth interaction between term formation and the reduction/conversion relation.
- Use of small types (terms of V) as types in derivations.

## Related
- v-introduction-rule: Type conversion mediates between V-terms and their use as types.

# Common Errors

- **Error**: Treating type conversion as an introduction or elimination rule.
  **Correction**: It is explicitly classified as a structural rule, distinct from both.

- **Error**: Assuming type conversion can relate any two types.
  **Correction**: It only applies when A and B are convertible (reduce to a common expression). Not all types are convertible.

# Common Confusions

- **Confusion**: Confusing type conversion with type coercion or casting.
  **Clarification**: Type conversion does not change the term or its computational meaning. It recognizes that two type expressions denote the same abstract type because they are computationally equivalent.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.14: Type conversion. Conversion defined in Section 2.4.

# Verification Notes

Confidence: high. Rule 2.3.14 is explicitly stated and classified as structural.
