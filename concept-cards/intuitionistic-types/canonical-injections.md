---
# === CORE IDENTIFICATION ===
concept: Canonical Injections
slug: canonical-injections

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
  - "i and j"
  - "left injection"
  - "right injection"
  - "inl and inr"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - disjoint-union-of-two-types
related:
  - definition-by-cases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the disjoint union A + B of two types?"
---

# Quick Definition
The canonical injections i and j are the introduction forms for the disjoint union A + B: i tags an object of type A, and j tags an object of type B, producing objects of type A + B.

# Core Definition
Martin-Lof states that A + B "is the type of objects of the form i(a) with a of type A or j(b) with b of type B. Here i and j denote the canonical injections." (Section 1.5)

# Prerequisites
- **Type**: Must understand what a type is.
- **Disjoint union of two types**: i and j are the introduction forms specifically for A + B.

# Key Properties
1. i takes an object a of type A and produces i(a) of type A + B.
2. j takes an object b of type B and produces j(b) of type A + B.
3. Every object of A + B is either of the form i(a) or j(b) -- these are the only canonical forms.
4. The tags i and j make the union disjoint: i(a) and j(b) are always distinguishable.

# Construction / Recognition
## To Construct/Create:
1. Given a in A, form i(a) to get an object of A + B.
2. Given b in B, form j(b) to get an object of A + B.

## To Identify/Recognize:
1. Look for tagged elements where the tag indicates which component of a sum type the element comes from.

# Context & Application
The canonical injections are the introduction rules for the sum type A + B. They are dual to pairing for the product type. In the logical reading, applying i corresponds to proving a disjunction A v B by proving A, and applying j corresponds to proving it by proving B.

# Examples
If A and B are propositions and a is a proof of A, then i(a) is a proof of A v B. Similarly, if b is a proof of B, then j(b) is a proof of A v B.

# Relationships
## Builds Upon
- **disjoint-union-of-two-types**: i and j are the introduction forms for A + B.
## Enables
- **definition-by-cases**: The D operator pattern-matches on i(a) and j(b).
- **disjunction**: i and j provide the two ways to prove A v B.
## Related
- **lambda-abstraction**: As lambda is the introduction form for Pi types, i and j are the introduction forms for sum types.

# Common Errors
- **Error**: Forgetting the tags and treating objects of A + B as bare objects of A or B.
  **Correction**: Objects of A + B are always tagged with i or j; the tag is essential for case analysis.

# Common Confusions
- **Confusion**: Thinking i and j are the same as pairing (a, b).
  **Clarification**: Pairing constructs an object of a product type; i and j construct objects of a sum type. They are dual operations.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.5.

# Verification Notes
Extracted directly from Section 1.5. High confidence.
