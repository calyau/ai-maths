---
# === CORE IDENTIFICATION ===
concept: Contrapositive
slug: contrapositive

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
aliases:
  - proof by contrapositive

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-proof
extends: []
related:
  - proof-by-contradiction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The contrapositive of "If $p$, then $q$" is "If not $q$, then not $p$." Proving the contrapositive is logically equivalent to proving the original statement.

# Core Definition

"Sometimes it is easier to prove the contrapositive of a statement. Proving the statement 'If $p$, then $q$' is exactly the same as proving the statement 'If not $q$, then not $p$'" (Judson, p. 15).

# Prerequisites

- **Mathematical proof** — The contrapositive is a proof strategy

# Key Properties

1. "If $p$ then $q$" is logically equivalent to "If not $q$ then not $p$"
2. Different from the converse ("If $q$ then $p$"), which is NOT equivalent
3. Often easier to prove than the direct statement

# Context & Application

Proof by contrapositive is frequently used in abstract algebra. For example, proving that a function is one-to-one often uses the contrapositive: instead of proving $a_1 \neq a_2 \Rightarrow f(a_1) \neq f(a_2)$, we prove $f(a_1) = f(a_2) \Rightarrow a_1 = a_2$.

# Examples

**Example 1** (p. 15): Instead of directly proving "If $p$ then $q$," we can equivalently prove "If not $q$ then not $p$."

# Relationships

## Builds Upon
- **mathematical-proof** — A proof strategy

## Related
- **proof-by-contradiction** — Another indirect proof strategy

# Common Confusions

- **Confusion**: Confusing the contrapositive with the converse
  **Clarification**: The contrapositive of "if $p$ then $q$" is "if not $q$ then not $p$" (equivalent). The converse is "if $q$ then $p$" (NOT equivalent).

# Source Reference

Chapter 1: Preliminaries, Section 1.1, page 15.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence: HIGH — explicit statement
- Cross-reference status: Verified
- Uncertainties: None
