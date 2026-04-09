---
# === CORE IDENTIFICATION ===
concept: Primitive Recursion
slug: primitive-recursion

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
  - "R operator"
  - "recursion schema"
  - "natural number elimination"
  - "natrec"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - natural-numbers
  - successor-function
  - pi-type
related:
  - mathematical-induction
  - definition-by-cases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a function by recursion on natural numbers?"
---

# Quick Definition
The R operator defines functions out of the natural numbers by recursion: given a base value d for 0 and a step function e for the successor case, R(n, d, e) computes a value for each natural number n.

# Core Definition
Martin-Lof defines: "Given an object d of type C(0) and a function e of type (Pi x in N)(C(x) -> C(s(x))), we may introduce a function of type (Pi x in N)C(x) whose value for the argument n will be denoted R(n,d,e) by the recursion schema: R(0,d,e) = d, R(s(n),d,e) = e(n,R(n,d,e))." (Section 1.7)

# Prerequisites
- **Natural numbers**: R is the eliminator for the type N.
- **Successor function**: The step case pattern-matches on s(n).
- **Cartesian product of a family of types (Pi type)**: The result type C(x) can depend on x, and e is typed using Pi.

# Key Properties
1. R(0, d, e) = d -- the base case returns d.
2. R(s(n), d, e) = e(n, R(n, d, e)) -- the step case applies e to n and the recursive result.
3. The result type C(x) may depend on x in N, making this a dependent eliminator.
4. d has type C(0); e has type (Pi x in N)(C(x) -> C(s(x))).
5. The resulting function (lambda x)R(x, d, e) has type (Pi x in N)C(x).

# Construction / Recognition
## To Construct/Create:
1. Specify the type family C over N.
2. Provide the base case d of type C(0).
3. Provide the step function e of type (Pi x in N)(C(x) -> C(s(x))).
4. R(n, d, e) then computes the result for any n in N.

## To Identify/Recognize:
1. A function on natural numbers defined by giving a base value and a step that refers to the predecessor's result.
2. The presence of the R operator or a recursion schema with cases for 0 and s(n).

# Context & Application
Primitive recursion is the fundamental way to define functions on natural numbers in Martin-Lof's theory. It is the computational analogue of mathematical induction: when C(n) represents a proposition, the recursion schema becomes the induction principle. Martin-Lof notes that N "is just the prime example of a type introduced by an ordinary inductive definition" (Section 1.7).

# Examples
From Section 1.8, equality on natural numbers is defined by (double) recursion:
- E(0,0) = top, E(s(m),0) = bottom, E(0,s(n)) = bottom, E(s(m),s(n)) = E(m,n).

This is possible "by recursion if only the propositions alias types bottom and top were objects of some type V" (Section 1.8), motivating the introduction of the universe.

# Relationships
## Builds Upon
- **natural-numbers**: R is the eliminator for N.
- **successor-function**: The step case decomposes s(n).
## Enables
- **mathematical-induction**: Induction is the propositional reading of recursion.
- Equality on natural numbers (via recursion into V).
## Related
- **definition-by-cases**: D is the analogous eliminator for A + B.

# Common Errors
- **Error**: Forgetting that e receives both n and R(n,d,e) as arguments.
  **Correction**: The step function e takes two arguments: the predecessor n and the accumulated result R(n,d,e). This is what makes it primitive recursion rather than mere iteration.

# Common Confusions
- **Confusion**: Conflating primitive recursion with general recursion.
  **Clarification**: Primitive recursion (the R operator) always terminates because it follows the structure of the natural number. General recursion may not terminate and is not directly supported.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.7.

# Verification Notes
Extracted directly from Section 1.7. Computation rules quoted verbatim. High confidence.
