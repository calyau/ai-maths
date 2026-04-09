---
# === CORE IDENTIFICATION ===
concept: Successor Function
slug: successor-function

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
  - "s"
  - "successor"
  - "succ"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - natural-numbers
related:
  - primitive-recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by recursion on natural numbers?"
---

# Quick Definition
The successor function s takes a natural number n and produces s(n), the next natural number. Together with 0, it is one of the two constructors for the type N.

# Core Definition
Martin-Lof states: "0 is an object of type N and, if n is an object of type N, so is its successor s(n)." (Section 1.7)

# Prerequisites
- **Natural numbers**: s is a constructor of the type N.

# Key Properties
1. s takes an object n of type N and produces s(n) of type N.
2. s is one of the two canonical constructors of N (the other being 0).
3. Every natural number is either 0 or s(n) for some n -- these are the only canonical forms.
4. The recursion schema R pattern-matches on 0 vs s(n).

# Construction / Recognition
## To Construct/Create:
1. Given any natural number n, apply s to get s(n).

## To Identify/Recognize:
1. A natural number of the form s(n) is a successor; 0 is the only non-successor.

# Context & Application
The successor function is the inductive step in building natural numbers. In the recursion schema, the case R(s(n), d, e) = e(n, R(n, d, e)) specifies how to compute at a successor in terms of the predecessor and the recursive result. The third and fourth Peano axioms (s(n) != 0 and injectivity of s) follow from defining equality by recursion using the universe V.

# Examples
- s(0) is 1, s(s(0)) is 2, etc.
- In the recursion schema: R(s(n), d, e) = e(n, R(n, d, e)).

# Relationships
## Builds Upon
- **natural-numbers**: s is a constructor of N.
## Enables
- **primitive-recursion**: The successor case of the R schema uses s.
## Related
- **canonical-injections**: Just as i and j are constructors for A + B, 0 and s are constructors for N.

# Common Errors
- **Error**: Assuming s is a function defined on N rather than a constructor.
  **Correction**: s is a primitive constructor of N, not a derived function. It is part of the definition of the type N itself.

# Common Confusions
- **Confusion**: Conflating s(n) with n + 1.
  **Clarification**: s(n) is the primitive notation; n + 1 is a derived notion defined using s.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.7.

# Verification Notes
Extracted from Section 1.7. High confidence.
