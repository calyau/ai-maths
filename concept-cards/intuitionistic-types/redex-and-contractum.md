---
# === CORE IDENTIFICATION ===
concept: Redex and Contractum
slug: redex-and-contractum

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
section: "2.4.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "reducible expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - formal-expression
  - contraction
extends: []
related:
  - normal-form
  - reduction
contrasts_with:
  - normal-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a redex, and what is a normal form?"
---

# Quick Definition

A redex (reducible expression) is an expression that matches the left-hand side of one of the rules of contraction. Its contractum is the corresponding right-hand side.

# Core Definition

Martin-Lof writes (after 2.4.2): "An expression which has the form of the left hand member of one of the rules of contraction is called a redex and the corresponding right hand member is its contractum."

The six forms of redex are:
1. (lambda x)b[x](a) -- a lambda applied to an argument
2. E((a,b), (lambda x)(lambda y)d[x,y]) -- Sigma elimination applied to a pair
3. D(i(a), (lambda x)d[x], (lambda y)e[y]) or D(j(b), ...) -- case analysis applied to an injection
4. R_n(m, c_1, ..., c_n) -- finite-type elimination applied to a numeral
5. R(0, d, (lambda x)(lambda y)e[x,y]) -- recursion applied to zero
6. R(s(a), d, (lambda x)(lambda y)e[x,y]) -- recursion applied to a successor

Each redex has a unique contractum determined by the corresponding contraction rule.

# Prerequisites

- formal-expression: Redexes are identified within the class of formal expressions.
- contraction: The contraction rules define what counts as a redex.

# Key Properties

1. A redex is always an eliminator applied to a constructor (an introduction form).
2. Each redex has exactly one contractum.
3. An expression may contain multiple redexes as subexpressions.
4. Contracting a redex may create new redexes (e.g., substitution may produce new beta-redexes).

# Construction / Recognition

## To Identify/Recognize:
Check whether a subexpression matches one of the six left-hand side patterns listed above. If so, it is a redex.

## To Construct/Create:
Apply any elimination form to the corresponding introduction form. For instance, applying a lambda abstraction to an argument creates a beta-redex.

# Context & Application

The notion of redex is central to computation in type theory. Finding and contracting redexes is how terms are evaluated. The normalization theorem (Chapter 4) guarantees that every well-typed term can be reduced to a normal form by repeatedly contracting redexes.

# Examples

- (lambda x)x(a) is a redex; its contractum is a.
- E((3, 5), (lambda x)(lambda y)x) is a redex; its contractum is 3.
- R_2(1, c_1, c_2) is a redex; its contractum is c_1.
- R(s(0), d, (lambda x)(lambda y)e[x,y]) is a redex; its contractum is e[0, R(0, d, (lambda x)(lambda y)e[x,y])].

# Relationships

## Builds Upon
- contraction: The contraction rules define redexes and their contracta.

## Enables
- reduction: Reduction proceeds by contracting redexes.
- normal-form: An expression with no redexes is in normal form.

## Contrasts With
- normal-form: A normal form is an expression containing no redexes whatsoever.

# Common Errors

- **Error**: Thinking that contracting one redex always brings the expression closer to normal form.
  **Correction**: Contraction may introduce new redexes. However, the normalization theorem guarantees that for well-typed terms, the process terminates.

# Common Confusions

- **Confusion**: Whether a redex must be at the top level of the expression.
  **Clarification**: A redex can occur as a subexpression at any depth. Reduction allows contracting redexes anywhere within an expression.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.2, paragraph following the contraction rules.

# Verification Notes

Confidence: high. The definition is given explicitly in the text immediately after the contraction rules.
