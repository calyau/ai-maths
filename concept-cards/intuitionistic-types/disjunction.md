---
# === CORE IDENTIFICATION ===
concept: Disjunction
slug: disjunction

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
  - "A v B"
  - "logical or"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - proposition
  - disjoint-union-of-two-types
  - canonical-injections
related:
  - definition-by-cases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does disjunction relate to the disjoint union?"
---

# Quick Definition
In the propositions-as-types correspondence, the disjunction A v B is represented by the disjoint union A + B. A proof of A v B is either i(a) where a is a proof of A, or j(b) where b is a proof of B.

# Core Definition
Martin-Lof states: "When A and B both represent propositions, A+B represents their disjunction A v B." (Section 1.5)

# Prerequisites
- **Proposition**: Must understand propositions as types under the Curry-Howard correspondence.
- **Disjoint union of two types**: The type A + B is the computational representation of disjunction.
- **Canonical injections**: i and j provide the two ways to prove A v B.

# Key Properties
1. A proof of A v B is constructive: it must specify which disjunct is proved.
2. i(a) proves A v B by proving A; j(b) proves A v B by proving B.
3. The disjunction property holds: a proof of A v B always reveals which of A or B is proved.
4. Disjunction elimination corresponds to definition by cases (the D operator).

# Construction / Recognition
## To Construct/Create:
1. To prove A v B, either prove A and apply i, or prove B and apply j.

## To Identify/Recognize:
1. Look for propositions joined by "or" / v / disjunction.
2. In type-theoretic notation, this appears as A + B where A and B represent propositions.

# Context & Application
Intuitionistic disjunction is strictly stronger than classical disjunction: it carries the information of which disjunct holds. This is the computational content of disjunction -- a program of type A + B must decide which branch to take. This contrasts with classical logic where A v B can be proved without determining which disjunct holds.

# Examples
From the source context: if we have a proof a of proposition A, then i(a) is a proof of A v B. To use a proof of A v B, we apply D(c, d, e), providing what to do in each case.

# Relationships
## Builds Upon
- **disjoint-union-of-two-types**: A v B is represented by A + B.
- **canonical-injections**: The two introduction rules for disjunction.
## Enables
- **definition-by-cases**: Disjunction elimination is case analysis.
## Related
- **proposition**: Disjunction is a logical operation on propositions.

# Common Errors
- **Error**: Assuming disjunction can be proved without deciding which disjunct holds.
  **Correction**: Intuitionistic disjunction requires specifying which disjunct is proved. This is reflected in the tagged nature of A + B.

# Common Confusions
- **Confusion**: Conflating intuitionistic and classical disjunction.
  **Clarification**: Classical A v B can be true without either disjunct being established (e.g., via excluded middle). Intuitionistic A v B (= A + B) always comes with a witness for one side.

# Source Reference
Martin-Lof, P. (1972). "An Intuitionistic Theory of Types," Section 1.5.

# Verification Notes
Extracted from Section 1.5. The logical reading is stated explicitly in the source. High confidence.
