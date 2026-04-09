---
# === CORE IDENTIFICATION ===
concept: V-Introduction Rule
slug: v-introduction-rule

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
section: "2.3.13"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "reflection principle (formal)"
  - "V-introduction"
  - "universe introduction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-formation-rules
  - universe
  - reflection-principle
extends:
  - reflection-principle
related:
  - type-conversion-rule
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The V-introduction rule (rule 2.3.13) is the formal reflection principle: it declares which types are terms of the universe V, namely N_0, N_1, ..., N, and any type built from small types using +, Pi, and Sigma.

# Core Definition

Martin-Lof writes in Section 2.3.13: "N_0, N_1, ... and N are terms of type V. If A and B are terms of type V, then so is A+B. If A and B[x] are terms of type V, x being a variable of type A, then (Pi x in A)B[x] and (Sigma x in A)B[x] are terms of type V."

Additionally: "N_0 and N_1 are alternatively denoted by (bottom) and (top), respectively."

The Gentzen-style schemata include:

```
  N_0 in V    N_1 in V    ...    N in V

  A in V    B in V          A in V    B[x] in V
  ────────────────          ────────────────────────
  A + B in V                (Pi x in A)B[x] in V

                            A in V    B[x] in V
                            ────────────────────────
                            (Sigma x in A)B[x] in V
```

# Prerequisites

- type-formation-rules: V is a type (rule 2.2.5); terms of V are small types (rule 2.2.6).
- universe: The informal concept from Chapter 1.
- reflection-principle: The informal principle that V-introduction formalizes.

# Key Properties

1. V-introduction is the sole introduction rule for the universe V.
2. There is no V-elimination rule -- the universe has only introduction.
3. The rule precisely characterizes the small types: they are N_0, N_1, ..., N, and closures under +, Pi, and Sigma.
4. V itself is NOT a term of V (V is large). This avoids the paradox that would arise from V in V.
5. Type constants P are not terms of V, so types involving type constants are large.
6. This rule is the formal expression of the reflection principle: every small type can be "reflected" into the universe V.

# Construction / Recognition

## To Show a Type is Small (a term of V):
1. Check if it is one of the base types: N_0, N_1, ..., N.
2. Or check if it is built from small types using +, Pi, or Sigma.
3. If so, it is a term of V by V-introduction.

## To Recognize Large Types:
A type is large if it contains V or a type constant P. This is mechanically decidable.

# Context & Application

The V-introduction rule closes the loop between types and terms: it populates the universe V with exactly the small types. This is fundamental for the stratification that avoids Girard's paradox. The original 1971 version of the theory had V in V, leading to inconsistency; the corrected version presented here excludes V from its own membership.

The absence of a V-elimination rule is noteworthy: one can reflect types into V but there is no general principle for "unreflecting" or pattern-matching on elements of V. Instead, the type conversion rule (2.3.14) allows using small types as types.

# Examples

- N is a term of type V (N is a small type).
- N_0 (bottom/falsehood) is a term of type V.
- If A and B are small types, then A + B, A -> B, and A x B are small types (terms of V).
- V is NOT a term of type V (V is large).
- If P is a type constant, P(...) is NOT a term of type V.

# Relationships

## Builds Upon
- universe: The informal notion of universe from Chapter 1.
- reflection-principle: V-introduction IS the formal reflection principle.

## Enables
- type-conversion-rule: Terms of V can be used as types via conversion.

## Related
- type-formation-rules: Rule 2.2.6 links V-introduction to type formation.

# Common Errors

- **Error**: Assuming V is a term of V.
  **Correction**: V is a large type and is not a member of itself. This is essential for consistency.

- **Error**: Assuming every type is small.
  **Correction**: Types containing V or type constants are large and not terms of V.

# Common Confusions

- **Confusion**: Wondering why there is no V-elimination rule.
  **Clarification**: The universe is a "collection of codes" for types. One does not case-split on types; instead, one uses the type conversion rule to move between a type's role as a term of V and its role as a type.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.13: V-introduction or the reflection principle.

# Verification Notes

Confidence: high. Rule 2.3.13 is explicitly stated with all clauses enumerated.
