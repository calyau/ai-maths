---
# === CORE IDENTIFICATION ===
concept: Mathematical Proof
slug: mathematical-proof

# === CLASSIFICATION ===
category: foundations
subcategory: logic-and-proofs
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 14
section: "A Short Note on Proofs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - proof

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - counterexample
  - contrapositive
  - proof-by-contradiction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is a mathematical proof?"
---

# Quick Definition

A mathematical proof is a convincing logical argument about the accuracy of a statement. It uses axioms and previously established results to derive new conclusions through rigorous reasoning.

# Core Definition

"A mathematical proof is nothing more than a convincing argument about the accuracy of a statement" (Judson, p. 14). In abstract mathematics, an axiomatic approach is taken: one starts with a collection of objects $S$ and assumes rules (axioms) about their structure, then derives other information about $S$ using logical arguments. A statement that has been proven true is called a **proposition**; a proposition of major importance is called a **theorem**. Supporting propositions are called **lemmas**, and easily derived consequences are called **corollaries**.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A theorem cannot be proved by example; however, a **counterexample** suffices to disprove a statement
2. Quantifiers (only, for all, for every, for some) have distinct meanings and must be used carefully
3. Never assume any hypothesis not explicitly stated in the theorem
4. To show an object exists and is unique: first show existence, then assume two such objects $r$ and $s$ and show $r = s$
5. Proving "If $p$, then $q$" is equivalent to proving the contrapositive "If not $q$, then not $p$"
6. Proof by contradiction assumes the desired statement is false and derives a contradiction

# Construction / Recognition

## To Construct a Direct Proof:
1. Identify the hypothesis $p$ and conclusion $q$
2. Assume the hypothesis is true
3. Use logical steps (definitions, axioms, previously proven results) to arrive at the conclusion

## To Construct a Proof by Contradiction:
1. Assume the statement you wish to prove is false
2. Derive logical consequences of this assumption
3. Arrive at a statement that contradicts a known truth

# Context & Application

Mathematical proof is the foundation of all abstract mathematics, including group theory and abstract algebra. Unlike laboratory sciences where experiments verify theories, mathematics relies on logical arguments for rigor. The ability to read and construct proofs is essential for studying abstract algebra.

# Examples

**Example 1** (p. 14): The statement "2$x$ = 6 exactly when $x$ = 4" is shown false by evaluating $2 \cdot 4 = 8 \neq 6$.

**Example 2** (p. 14): The quadratic formula is proved by completing the square, demonstrating a chain of equalities from $ax^2 + bx + c = 0$ to $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

# Relationships

## Builds Upon
- No prerequisites within this source

## Enables
- **set** — Set theory proofs require proof techniques
- **equivalence-relation** — Verifying equivalence relation properties requires proof
- **group** — Group theory is built on proving properties from axioms

## Related
- **counterexample** — Standard way to disprove a statement
- **contrapositive** — Alternative proof strategy
- **proof-by-contradiction** — Alternative proof strategy

# Common Errors

- **Error**: Attempting to prove a theorem by checking examples
  **Correction**: Examples can illustrate but never prove a general theorem; a logical argument covering all cases is required

- **Error**: Assuming hypotheses not stated in the theorem
  **Correction**: Only use explicitly stated hypotheses and previously proven results

# Common Confusions

- **Confusion**: Believing that many confirming examples constitute a proof
  **Clarification**: No finite number of examples can prove a universal statement; a single counterexample can disprove one

- **Confusion**: Confusing the converse with the contrapositive
  **Clarification**: "If $p$ then $q$" is equivalent to "If not $q$ then not $p$" (contrapositive), but NOT equivalent to "If $q$ then $p$" (converse)

# Source Reference

Chapter 1: Preliminaries, Section 1.1 "A Short Note on Proofs," pages 14-16.

# Verification Notes

- Definition source: Direct quote from p. 14
- Key Properties: Items 1-6 are direct from the "Cautions and Suggestions" list on p. 15
- Confidence: HIGH — explicit discussion with clear definitions
- Cross-reference status: All slug references verified against planned extractions
- Uncertainties: None
