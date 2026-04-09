---
# === CORE IDENTIFICATION ===
concept: Conjunction (as Cartesian Product)
slug: conjunction

# === CLASSIFICATION ===
category: foundations
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Informal Explanations of the Basic Concepts"
chapter_number: 1
pdf_page: 0
section: "1.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "A & B"
  - "logical and"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartesian-product-of-two-types
  - proposition
  - propositions-as-types
extends: []
related:
  - existential-quantification
  - implication
contrasts_with:
  - implication

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does conjunction relate to the Cartesian product?"
---

# Quick Definition

Conjunction A & B is represented by the Cartesian product A x B; a proof is a pair (a, b) where a proves A and b proves B.

# Core Definition

Martin-Lof writes: "If A and B both represent propositions, then A x B represents their conjunction A & B." (Section 1.4)

Since A x B is the type of pairs (a, b) with a in A and b in B, a proof of A & B consists of a proof of A together with a proof of B.

# Prerequisites

- **cartesian-product-of-two-types**: Conjunction is the logical reading of A x B.
- **proposition**: Both A and B must represent propositions.
- **propositions-as-types**: The identification of propositions with types underlies the correspondence.

# Key Properties

1. A & B is represented by A x B.
2. A proof of A & B is a pair: one proof of A and one proof of B.
3. Conjunction is the non-dependent special case of existential quantification.
4. The projections p and q extract the individual proofs: p extracts the proof of A, q the proof of B.

# Construction / Recognition

## To Construct/Create:
1. Prove A by constructing a in A.
2. Prove B by constructing b in B.
3. Form the pair (a, b) of type A x B, which is the proof of A & B.

## To Identify/Recognize:
1. A conjunction A & B corresponds to the product type A x B.
2. Proofs are pairs; projections give the component proofs.

# Context & Application

Conjunction completes the basic set of logical connectives covered in Sections 1.2-1.4 of the paper. Together with implication (A -> B), universal quantification (Pi type), and existential quantification (Sigma type), it demonstrates how all the standard logical operations arise naturally from type-forming operations.

# Examples

From Section 1.4: If A and B represent propositions, A x B represents A & B.

From Section 1.4 (Girard's paradox): P(A, <) x Q(A, <) conjoins the propositions that an ordering is transitive and free from infinite descending chains.

# Relationships

## Builds Upon
- cartesian-product-of-two-types: Conjunction is the logical reading of A x B.

## Enables
- Combining multiple conditions in type-theoretic formalization.

## Related
- existential-quantification: Conjunction is the non-dependent special case of existential quantification.
- implication: Conjunction (pairs/products) and implication (functions/arrows) are the two basic propositional connectives treated in these sections.

## Contrasts With
- implication: Conjunction (A x B, pairs) vs. implication (A -> B, functions).

# Common Errors

- **Error**: Attempting to prove A & B by proving A or B alone.
  **Correction**: A proof of A & B requires *both* a proof of A and a proof of B, combined as a pair.

# Common Confusions

- **Confusion**: Confusing conjunction (A & B / A x B) with the dependent existential (exists x in A)B(x).
  **Clarification**: Conjunction is the special case where B does not depend on x. In the dependent case, the type of the second component varies with the first.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 1.4: Disjoint union of a family of types.

# Verification Notes

Confidence: high. Conjunction is explicitly identified with A x B in Section 1.4.
