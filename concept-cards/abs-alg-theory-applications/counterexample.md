---
# === CORE IDENTIFICATION ===
concept: Counterexample
slug: counterexample

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
pdf_page: 15
section: "A Short Note on Proofs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-proof
extends: []
related:
  - contrapositive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A counterexample is a specific instance that disproves a general statement. While a theorem cannot be proved by example, a single counterexample suffices to show a statement is false.

# Core Definition

"A theorem cannot be proved by example; however, the standard way to show that a statement is not a theorem is to provide a counterexample" (Judson, p. 15).

# Prerequisites

- **Mathematical proof** — Counterexamples are tools in mathematical reasoning

# Key Properties

1. A single counterexample disproves a universal statement
2. No number of examples can prove a universal statement
3. Counterexamples must satisfy all hypotheses but violate the conclusion

# Context & Application

Counterexamples are used throughout abstract algebra to show that certain properties do not hold. For example, showing that a particular group is not abelian by exhibiting two elements that don't commute.

# Examples

**Example 1** (p. 14): The statement "2$x$ = 6 exactly when $x$ = 4" is disproved by the counterexample $x = 3$ (since $2 \cdot 3 = 6$ but $3 \neq 4$).

**Example 2** (p. 52): $GL_2(\mathbb{R})$ under multiplication is NOT a subgroup of $(M_2(\mathbb{R}), +)$ because $I + (-I) = 0$, and the zero matrix is not in $GL_2(\mathbb{R})$.

# Relationships

## Builds Upon
- **mathematical-proof** — Tool in mathematical reasoning

# Common Confusions

- **Confusion**: Thinking many confirming examples constitute a proof
  **Clarification**: Only logical arguments prove theorems; examples cannot

# Source Reference

Chapter 1: Preliminaries, Section 1.1, page 15.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence: HIGH — explicit statement
- Cross-reference status: Verified
- Uncertainties: None
