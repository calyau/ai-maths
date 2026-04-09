---
# === CORE IDENTIFICATION ===
concept: Contraction
slug: contraction

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
  - "rules of contraction"
  - "contr"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - formal-expression
extends: []
related:
  - redex-and-contractum
  - reduction
  - conversion
contrasts_with:
  - reduction
  - conversion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes contraction from reduction from conversion?"
---

# Quick Definition

A contraction is a single computational step that replaces a redex (an expression matching the left-hand side of a contraction rule) with its contractum (the corresponding right-hand side). Contraction is the atomic operation from which reduction and conversion are built.

# Core Definition

Section 2.4.2 gives six contraction rules, each corresponding to an elimination rule applied to a canonical (introduced) argument:

1. **Beta-contraction** (Pi): (lambda x)b[x](a) contr b[a]
2. **Sigma-contraction**: E((a,b), (lambda x)(lambda y)d[x,y]) contr d[a,b]
3. **Disjoint-union contraction** (+): D(i(a), (lambda x)d[x], (lambda y)e[y]) contr d[a] and D(j(b), (lambda x)d[x], (lambda y)e[y]) contr e[b]
4. **Finite-type contraction**: R_n(m, c_1, ..., c_n) contr c_m
5. **Recursion base**: R(0, d, (lambda x)(lambda y)e[x,y]) contr d
6. **Recursion step**: R(s(a), d, (lambda x)(lambda y)e[x,y]) contr e[a, R(a, d, (lambda x)(lambda y)e[x,y])]

Each rule takes an eliminator applied to a constructor and "computes" by substituting the constructor's arguments into the body of the eliminator.

# Prerequisites

- formal-expression: Contraction is defined on formal expressions, not just well-typed terms.

# Key Properties

1. Contraction is a local, single-step operation -- it replaces one redex occurrence.
2. Each contraction rule pairs an elimination form with the corresponding introduction form.
3. The rules are the computational heart of the theory: they define what it means for a term to compute.
4. Contraction on its own is not transitive or symmetric -- those properties belong to reduction and conversion.

# Construction / Recognition

## To Construct/Create:
Identify a subexpression that matches the left-hand side of one of the six contraction rules, and replace it with the corresponding right-hand side.

## To Identify/Recognize:
A contraction has occurred when exactly one redex in an expression has been replaced by its contractum.

# Context & Application

Contraction rules are the foundation of the operational semantics of the theory. They generalize beta-reduction from the lambda calculus to all the type formers. Reduction is defined as repeated contraction; conversion is defined as the ability to reduce to a common expression. The Church-Rosser property is ultimately about the confluence of these contraction steps.

# Examples

Beta-contraction: (lambda x)(x + x)(3) contr 3 + 3

Sigma-contraction: E((a, b), (lambda x)(lambda y)x) contr a (this is the left projection p[c])

Recursion-step contraction: R(s(s(0)), d, (lambda x)(lambda y)e[x,y]) contr e[s(0), R(s(0), d, (lambda x)(lambda y)e[x,y])]

# Relationships

## Builds Upon
- formal-expression: Contraction is defined on the class of formal expressions.

## Enables
- redex-and-contractum: These terms name the two sides of a contraction rule.
- reduction: Reduction is repeated contraction of parts.
- conversion: Conversion is defined via reduction, which is defined via contraction.

## Contrasts With
- reduction: Reduction is the transitive closure -- zero or more contractions of subexpressions.
- conversion: Conversion is symmetric -- two expressions convert if they reduce to a common form.

# Common Errors

- **Error**: Confusing contraction with reduction.
  **Correction**: Contraction is a single rule application to one redex. Reduction is a sequence of zero or more contractions applied to subexpressions throughout the expression.

# Common Confusions

- **Confusion**: The recursion-step rule looks like it duplicates the recursion operator R.
  **Clarification**: This is correct and essential: R(s(a), d, e) unfolds to e[a, R(a, d, e)], making the recursive call explicit. This corresponds to the standard computational behavior of primitive recursion.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 2.4.2: Rules of contraction.

# Verification Notes

Confidence: high. All six rules are explicitly stated in 2.4.2 with precise notation.
