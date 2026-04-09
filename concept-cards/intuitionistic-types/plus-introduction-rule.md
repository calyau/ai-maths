---
# === CORE IDENTIFICATION ===
concept: Plus-Introduction Rule
slug: plus-introduction-rule

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
section: "2.3.7"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "injection"
  - "+-introduction"
  - "canonical injection (formal)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-formation-rules
  - disjoint-union-of-two-types
extends:
  - canonical-injections
related:
  - plus-elimination-rule
contrasts_with:
  - plus-elimination-rule

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

The +-introduction rule (rule 2.3.7) states that i(a) and j(b) are the canonical injections that inject terms into the disjoint union type A + B.

# Core Definition

Martin-Lof writes in Section 2.3.7: "If a is a term of type A, then i(a) is a term of type A+B. Similarly, if b is a term of type B, then j(b) is a term of type A+B."

The Gentzen-style schemata are:

```
  a in A                b in B
  ──────────────        ──────────────
  i(a) in A + B         j(b) in A + B
```

There are two introduction forms: i (left injection) and j (right injection), corresponding to the two summands of the disjoint union.

# Prerequisites

- type-formation-rules: The type A + B must be well-formed (rule 2.2.4).
- disjoint-union-of-two-types: The informal explanation from Chapter 1.

# Key Properties

1. There are exactly two introduction forms for A + B: i (left) and j (right).
2. i(a) injects a term of type A into A + B; j(b) injects a term of type B into A + B.
3. Every canonical term of type A + B has one of these two forms.
4. The injections tag terms with their origin, enabling case analysis via +-elimination.

# Construction / Recognition

## To Inject into A + B:
- From a term a of type A: form i(a).
- From a term b of type B: form j(b).

## To Recognize:
A term of the form i(t) is a left injection; j(t) is a right injection. Both are +-introductions.

# Context & Application

In the propositions-as-types reading, +-introduction corresponds to disjunction introduction: a proof of A gives a proof of A v B (via i), and a proof of B gives a proof of A v B (via j). The formal rule makes precise the informal notion of canonical injection from Section 1.8.

# Examples

If n is a term of type N, then i(n) is a term of type N + B for any type B.

If b is a term of type Bool (if defined), then j(b) is a term of type A + Bool for any type A.

# Relationships

## Builds Upon
- disjoint-union-of-two-types: The + type being introduced into.

## Enables
- plus-elimination-rule: The D operator dispatches on i and j forms.

## Related
- canonical-injection: The informal counterpart from Chapter 1.

## Contrasts With
- plus-elimination-rule: Introduction injects; elimination case-splits.

# Common Errors

- **Error**: Forgetting to specify which summand is being injected into.
  **Correction**: i always injects from the left summand A; j always injects from the right summand B. The choice of i or j determines the tag.

# Common Confusions

- **Confusion**: Thinking i(a) and j(a) are the same when a has both type A and type B.
  **Clarification**: Even if a is a term of both types (e.g., via type conversion), i(a) and j(a) are distinct terms of A + B. The tag (i vs. j) carries information.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.3.7: +-introduction or injection.

# Verification Notes

Confidence: high. Rule 2.3.7 is explicitly stated.
