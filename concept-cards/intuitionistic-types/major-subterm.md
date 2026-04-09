---
# === CORE IDENTIFICATION ===
concept: Major Subterm
slug: major-subterm

# === CLASSIFICATION ===
category: normalization
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "An Intuitionistic Theory of Types"
source_slug: intuitionistic-types
authors: "Per Martin-Lof"
chapter: "The Normalization Theorem and Its Consequences"
chapter_number: 4
pdf_page: 34
section: "4.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "head position"
  - "principal argument"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - introduction-form-vs-elimination-form
extends: []
related:
  - main-redex
  - normal-term-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The major subterm of a term in elimination form is the subterm that occupies the "scrutinee" or "head" position -- the subterm whose form determines whether a contraction can occur.

# Core Definition

Martin-Lof writes: "The major subterm of a term which has elimination form, is defined by stipulating that the major subterm of b(a) is b and that the major subterm of E(c, (lambda x)(lambda y)d[x,y]), D(c, (lambda x)d[x], (lambda y)e[y]), R_n(c, c_1, ..., c_n) and R(c, d, (lambda x)(lambda y)e[x,y]) in all cases is c." (Section 4.4)

In each elimination form, the major subterm is the distinguished argument that is being "eliminated" or "inspected":

| Elimination form | Major subterm |
|---|---|
| b(a) | b |
| E(c, (lambda x)(lambda y)d[x,y]) | c |
| D(c, (lambda x)d[x], (lambda y)e[y]) | c |
| R_n(c, c_1, ..., c_n) | c |
| R(c, d, (lambda x)(lambda y)e[x,y]) | c |

# Prerequisites

- **introduction-form-vs-elimination-form**: The concept of major subterm only applies to terms in elimination form.

# Key Properties

1. Every elimination form has exactly one major subterm.
2. A redex is an elimination form whose major subterm has introduction form. For example, ((lambda x)b[x])(a) is a redex because the major subterm (lambda x)b[x] has introduction form.
3. For application b(a), the major subterm is the function b (not the argument a).
4. For all other elimination forms, the major subterm is the first argument c (the "scrutinee").
5. When forming a term of elimination form, no free variable in its major subterm becomes bound (Section 4.4).

# Construction / Recognition

## To Identify the Major Subterm:
1. Determine that the term has elimination form.
2. If the term is an application b(a), the major subterm is b.
3. If the term is E(c,...), D(c,...), R_n(c,...), or R(c,...), the major subterm is c.

## Tracing the Major Subterm Chain:
Starting from a term of elimination form, repeatedly take the major subterm of the major subterm until reaching either:
- A term of introduction form (in which case the original term contains a redex), or
- A constant or free variable (in which case the original term is "stuck" -- it cannot reduce at the head).

# Context & Application

The major subterm is essential for the analysis in Section 4.4 that determines the form of normal terms. Martin-Lof observes: "If a term has elimination form, then either it contains a main redex or else by taking the major subterm of its major subterm of ... of its major subterm we reach a constant or a free variable."

This means that in the constant-free, closed case, a normal term of elimination form is impossible: tracing the major subterm chain would eventually require a constant or free variable, but neither exists. Therefore, closed normal terms (in the system without constants) must have introduction form.

# Examples

- In b(a): the major subterm is b. If b = (lambda x)d[x], then b(a) is a redex.
- In E((a,b), (lambda x)(lambda y)d[x,y]): the major subterm is (a,b). Since it has introduction form, this is a redex.
- In D(c, (lambda x)d[x], (lambda y)e[y]) where c is a constant: the major subterm is c. Since c is a constant (not introduction form), this is not a redex -- it is stuck.
- In R(f(a), d, (lambda x)(lambda y)e[x,y]): the major subterm is f(a), which itself has elimination form. Tracing further, the major subterm of f(a) is f.

# Relationships

## Builds Upon
- introduction-form-vs-elimination-form: Major subterm is defined only for elimination forms.

## Enables
- main-redex: Defined in terms of tracing the major subterm chain.
- normal-term-structure: The canonical forms table relies on major subterm analysis.

# Common Errors

- **Error**: Thinking the major subterm of b(a) is a.
  **Correction**: It is b. The function position is the major subterm of an application, not the argument.

# Common Confusions

- **Confusion**: Conflating "major subterm" with "largest subterm."
  **Clarification**: "Major" here means "principal" or "head" -- the subterm whose form determines whether reduction can occur. It is a distinguished positional notion, not a size comparison.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.4: The form of the normal terms.

# Verification Notes

Confidence: high. The definition is given explicitly in Section 4.4 with a complete enumeration of all elimination forms.
