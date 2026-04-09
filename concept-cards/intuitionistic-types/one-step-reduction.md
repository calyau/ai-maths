---
# === CORE IDENTIFICATION ===
concept: One-Step Reduction
slug: one-step-reduction

# === CLASSIFICATION ===
category: reduction-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "Formalization of an Intuitionistic Theory of Types"
chapter_number: 2
pdf_page: 9
section: "2.4.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "red_1"
  - "parallel reduction"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - contraction
extends:
  - contraction
related:
  - reduction
  - church-rosser-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Church-Rosser property?"
---

# Quick Definition

One-step reduction (a red_1 b) is the operation of contracting some, possibly all or none, of the redexes in an expression a simultaneously, working from the inside out. It is the key technical device used to prove the Church-Rosser property.

# Core Definition

Martin-Lof writes (2.4.3): "We shall say that a reduces in one step and write a red_1 b if b is obtained by contracting some, possibly all or none, of the redexes in a, starting from within and proceeding outwards."

Reduction in n steps is then defined inductively:
- a red_0 a
- a red_{n+1} b means there exists c such that a red_n c and c red_1 b

The number n can be taken to be the total number of individual contractions carried out.

# Prerequisites

- contraction: One-step reduction is built from simultaneous contraction of multiple redexes.

# Key Properties

1. One-step reduction is reflexive: a red_1 a (by contracting no redexes).
2. One-step reduction can contract multiple redexes simultaneously.
3. The "inside-out" order ensures that when an outer redex is contracted, its inner subexpressions have already been processed.
4. New redexes may arise from contraction, but these are not contracted in the same step.
5. The diamond property holds for one-step reduction (Lemma 2.4.3.2): if a red_1 b and a red_1 c, then there exists d with b red_1 d and c red_1 d.

# Construction / Recognition

## To Perform:
1. Identify all redexes in the expression.
2. Choose a subset to contract (possibly empty, possibly all).
3. Contract the chosen redexes starting from the innermost and proceeding outward.

# Context & Application

One-step reduction is not the main computational notion of the theory (that is ordinary reduction). Rather, it is a technical measure of "reduction length" introduced specifically for the Church-Rosser proof. The key insight is that one-step reduction satisfies a diamond property (Lemma 2.4.3.2), and this diamond property lifts to the full Church-Rosser property for multi-step reduction via Lemma 2.4.3.3.

# Examples

Given (lambda x)(x, x)(a) where no redexes occur in a:
- Contracting the beta-redex gives (a, a) -- this is one step: a red_1 (a, a).
- Contracting nothing gives (lambda x)(x, x)(a) itself -- also a valid one step (the identity case).

Given E((lambda x)x(a), b), (lambda u)(lambda v)u):
- One step could contract both the inner beta-redex and the outer Sigma-elimination, or just one of them.

# Relationships

## Builds Upon
- contraction: One-step reduction is parallel contraction of chosen redexes.

## Enables
- church-rosser-property: The diamond property of one-step reduction (2.4.3.2) is the core of the Church-Rosser proof.
- reduction: Multi-step reduction is iterated one-step reduction.

# Common Errors

- **Error**: Thinking one-step reduction contracts exactly one redex.
  **Correction**: It contracts any subset of the redexes -- zero, one, several, or all.

# Common Confusions

- **Confusion**: Why "inside-out" rather than "outside-in"?
  **Clarification**: The inside-out order is needed to make the diamond lemma work. Contracting inner redexes first means outer contractions see already-simplified subexpressions, which simplifies the inductive argument.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.3, paragraph defining one-step reduction.

# Verification Notes

Confidence: high. The definition is given explicitly in 2.4.3 and used throughout the Church-Rosser proof.
