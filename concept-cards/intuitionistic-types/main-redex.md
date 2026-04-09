---
# === CORE IDENTIFICATION ===
concept: Main Redex
slug: main-redex

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
  - "head redex"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - major-subterm
  - contraction
extends:
  - formal-expression
related:
  - normal-term-structure
  - introduction-form-vs-elimination-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

The main redex of a term is found by tracing the major subterm chain: for a redex, it is the redex itself; for a non-redex elimination form, it is the main redex of its major subterm.

# Core Definition

Martin-Lof writes: "The main redex of a redex is the redex itself, and the main redex of a term which has elimination form but is not a redex is the main redex of its major subterm." (Section 4.4)

The main redex is located at the "head" of a term's elimination spine. It is found by starting at the outermost elimination form and repeatedly taking major subterms until either:
- A redex is found (an elimination form whose major subterm has introduction form) -- this is the main redex.
- A constant or free variable is reached -- in this case, there is no main redex.

# Prerequisites

- **major-subterm**: The main redex is defined by iterating the major subterm operation.
- **contraction**: A redex is a term where contraction can be applied.

# Key Properties

1. A term of elimination form either contains a main redex or its major subterm chain terminates at a constant or free variable.
2. A normal term cannot contain a main redex (since a main redex could be contracted).
3. In a closed term without constants, if the term has elimination form, it must contain a main redex -- because the major subterm chain cannot terminate at a constant or free variable.
4. Therefore, in the constant-free closed system, a normal term cannot have elimination form, which forces normal terms to have introduction form (Section 4.4).

# Construction / Recognition

## To Find the Main Redex:
1. Start with a term t of elimination form.
2. If t is a redex (its major subterm has introduction form), then t itself is the main redex.
3. Otherwise, let t' be the major subterm of t.
4. If t' has elimination form, repeat from step 2 with t'.
5. If t' is a constant or free variable, there is no main redex.
6. If t' has introduction form, then t is the main redex (this is case 2 restated).

# Context & Application

The concept of main redex is introduced in Section 4.4 specifically to analyze the structure of normal terms. The key argument is: a closed normal term (in the system without constants) cannot have elimination form, because that would require a main redex (which contradicts normality) or a constant/variable (which contradicts being closed and constant-free). This forces closed normal terms into introduction form, yielding the canonical forms table.

# Examples

- ((lambda x)b[x])(a): This is a redex. Its main redex is itself.
- f(a) where f is a constant: The major subterm is f, a constant. There is no main redex. This term is stuck (and normal if a is normal).
- E(D(c, (lambda x)d[x], (lambda y)e[y]), (lambda u)(lambda v)g[u,v]) where c = i(a): The major subterm is D(c,...). The major subterm of D(c,...) is c = i(a), which has introduction form. So D(c,...) is a redex and is the main redex of the whole term.

# Relationships

## Builds Upon
- major-subterm: The chain that leads to the main redex.
- contraction: What happens at a redex.

## Enables
- normal-term-structure: The absence of main redexes in normal terms forces canonical forms.

# Common Errors

- **Error**: Thinking the main redex is any redex appearing anywhere in the term.
  **Correction**: The main redex is specifically the one found by tracing the major subterm chain from the outermost elimination form. A term may contain other redexes in non-major positions.

# Common Confusions

- **Confusion**: Conflating "main redex" with "outermost redex."
  **Clarification**: The main redex follows the major subterm spine. In b(a), the major subterm is b, not a. So even if a contains a redex, the main redex is determined by tracing through b.

# Source Reference

Martin-Lof, P. (1972). "An Intuitionistic Theory of Types." Section 4.4: The form of the normal terms.

# Verification Notes

Confidence: high. Explicitly defined in Section 4.4 with a clear inductive characterization.
