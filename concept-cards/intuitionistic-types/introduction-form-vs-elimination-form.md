---
# === CORE IDENTIFICATION ===
concept: Introduction Form vs Elimination Form
slug: introduction-form-vs-elimination-form

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
section: "4.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "canonical form vs non-canonical form"
  - "constructor vs destructor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type
  - pi-introduction-rule
  - pi-elimination-rule
  - sigma-introduction-rule
  - sigma-elimination-rule
extends: []
related:
  - normal-term-structure
  - major-subterm
  - main-redex
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes introduction rules from elimination rules?"
---

# Quick Definition

A closed term has introduction form if it was constructed by an introduction rule (lambda, pairing, injection) and elimination form if it was constructed by an elimination rule (application, E, D, R_n, R). Every closed term that is not a constant must have one form or the other.

# Core Definition

Martin-Lof writes: "It will be convenient to say that a term has *introduction* or *elimination form* depending on whether it has been formed by means of one of the introduction or one of the elimination rules. Thus, unless it is a constant, a closed term necessarily has either introduction or elimination form." (Section 4.1)

**Introduction forms** (canonical constructors):
- (lambda x)b[x] -- Pi-introduction
- (a, b) -- Sigma-introduction
- i(a), j(b) -- +-introduction
- 0, s(a) -- N-introduction
- 1, 2, ..., n -- N_n-introduction
- (Pi x in A)B[x], (Sigma x in A)B[x], A + B, N_0, N_1, ..., N -- V-introduction

**Elimination forms** (destructors/observers):
- b(a) -- Pi-elimination (application)
- E(c, (lambda x)(lambda y)d[x,y]) -- Sigma-elimination
- D(c, (lambda x)d[x], (lambda y)e[y]) -- +-elimination
- R_n(c, c_1, ..., c_n) -- N_n-elimination
- R(c, d, (lambda x)(lambda y)e[x,y]) -- N-elimination (recursion)

# Prerequisites

- **type**: Introduction and elimination forms are relative to a type.
- **pi-introduction-rule**, **pi-elimination-rule**, etc.: The specific rules whose application determines the form.

# Key Properties

1. Every closed term is either a constant, has introduction form, or has elimination form. These three cases are exhaustive and mutually exclusive (for closed terms).
2. A redex arises precisely when an elimination form is applied directly to an introduction form (e.g., ((lambda x)b[x])(a)).
3. A normal term cannot contain a redex, so in a normal term of elimination form, tracing the major subterm chain must eventually reach a constant or free variable rather than an introduction form.
4. The computability predicate phi_A is defined with separate clauses for introduction forms (clause 1), normal non-introduction forms (clause 2), and elimination forms reducing to computable terms (clause 3).

# Construction / Recognition

## To Identify the Form of a Closed Term:
1. Look at the outermost constructor:
   - If it is lambda, a pair, an injection, zero, successor, or a numeral: introduction form.
   - If it is application, E, D, R_n, or R: elimination form.
   - If it is a bare constant symbol: neither (constant).

## Why This Matters for Normalization:
- Introduction-form terms are "values" -- they compute no further (unless their subterms contain redexes).
- Elimination-form terms are "computations" -- they may contract if their major subterm is an introduction form.
- The interplay between introduction and elimination is what drives computation.

# Context & Application

The introduction/elimination distinction is central to the normalization proof and to understanding the structure of normal terms (Section 4.4). The computability predicate treats these two forms differently: introduction forms are computable when their components satisfy the appropriate conditions, while elimination forms are computable when they reduce to something computable.

This distinction also underlies the table in Section 4.4: closed normal terms of a given type must have introduction form (since an elimination form in normal position would require a constant or free variable at the end of its major subterm chain, and in the constant-free closed case, this is impossible).

# Examples

- (lambda x)x has introduction form (Pi-introduction).
- f(a) has elimination form (Pi-elimination), where f is the major subterm.
- ((lambda x)x)(a) has elimination form and is a redex, because its major subterm (lambda x)x has introduction form.
- (0, s(0)) has introduction form (Sigma-introduction).
- E((0, s(0)), (lambda x)(lambda y)y) has elimination form and is a redex.

# Relationships

## Builds Upon
- The specific introduction and elimination rules from Chapter 2.

## Enables
- normal-term-structure: The canonical forms table follows from analyzing what forms normal terms can take.
- main-redex: A redex is an elimination form whose major subterm has introduction form.
- computability-predicate: Defined by separate clauses for introduction and elimination forms.

## Contrasts With
- The two forms contrast with each other: introduction builds data, elimination consumes it.

# Common Errors

- **Error**: Thinking "introduction form" means the term is fully reduced.
  **Correction**: A term can have introduction form at the top level but still contain redexes in its subterms. For example, (lambda x)(((lambda y)y)(x)) has introduction form but is not normal.

# Common Confusions

- **Confusion**: Conflating "elimination form" with "redex."
  **Clarification**: A redex is an elimination form whose major subterm has introduction form. An elimination form whose major subterm is a constant or another elimination form is not a redex.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.1, paragraph defining introduction and elimination form.

# Verification Notes

Confidence: high. The distinction is explicitly defined and named in Section 4.1, and pervades the entire normalization proof.
