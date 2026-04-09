---
# === CORE IDENTIFICATION ===
concept: Definition by Cases
slug: definition-by-cases

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
section: "1.5. Disjoint union of two types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "D operator"
  - "case analysis"
  - "sum elimination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - disjoint-union-of-two-types
  - canonical-injections
  - pi-type
related:
  - primitive-recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by cases on A + B?"
---

# Quick Definition
The D operator is the elimination form for the disjoint union A + B. Given functions d and e handling the left and right cases respectively, D(c, d, e) defines a function out of A + B by cases.

# Core Definition
Martin-Lof defines: "Let C be a function which to an arbitrary object of type A+B assigns a type, and suppose that d and e are functions of types (Pi x in A)C(i(x)) and (Pi y in B)C(j(y)), respectively. Then we may define a function of type (Pi z in A+B)C(z) whose value for the argument c will be denoted D(c,d,e) by the schema: D(i(a), d, e) = d(a), D(j(b), d, e) = e(b)." (Section 1.5)

# Prerequisites
- **Disjoint union of two types**: D eliminates A + B.
- **Canonical injections**: D pattern-matches on the forms i(a) and j(b).
- **Cartesian product of a family of types (Pi type)**: The result type C may depend on the argument, and d, e are functions typed using Pi.

# Key Properties
1. D(i(a), d, e) = d(a) -- when the argument is a left injection, apply d.
2. D(j(b), d, e) = e(b) -- when the argument is a right injection, apply e.
3. The result type C(z) may depend on z in A + B, making this a dependent eliminator.
4. The two computation rules (for i and j) are exhaustive: every object of A + B is one or the other.

# Construction / Recognition
## To Construct/Create:
1. Have a type A + B and a type family C over A + B.
2. Provide d of type (Pi x in A)C(i(x)) -- what to do for left injections.
3. Provide e of type (Pi y in B)C(j(y)) -- what to do for right injections.
4. D(c, d, e) then has type C(c) for any c in A + B.

## To Identify/Recognize:
1. Look for a function defined on a sum type with separate clauses for each injection.
2. Look for the D operator or pattern matching on i(a) vs j(b).

# Context & Application
Definition by cases is the fundamental way to use (eliminate) a disjoint union. In the logical reading, it corresponds to disjunction elimination: if you can prove C assuming A, and prove C assuming B, then from A v B you can conclude C. This is also the basis for the more general finite-type eliminators R_n.

# Examples
From the source: if c = i(a), then D(c, d, e) reduces to d(a); if c = j(b), then D(c, d, e) reduces to e(b). The computation is determined by which injection was used to construct c.

# Relationships
## Builds Upon
- **disjoint-union-of-two-types**: D is the eliminator for A + B.
- **canonical-injections**: D dispatches on i vs j.
## Enables
- **disjunction**: D provides disjunction elimination in the logical reading.
## Related
- **primitive-recursion**: R is the eliminator for N, analogous to D for A + B.
- **finite-type**: R_n generalizes case analysis to n cases.

# Common Errors
- **Error**: Forgetting that the result type C can depend on the argument z in A + B.
  **Correction**: D supports dependent elimination. d must have type (Pi x in A)C(i(x)), not merely A -> C.

# Common Confusions
- **Confusion**: Conflating D with if-then-else on booleans.
  **Clarification**: D is more general: it works on any sum type A + B (not just booleans), and supports dependent result types.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.5.

# Verification Notes
Extracted directly from Section 1.5. Computation rules quoted verbatim. High confidence.
