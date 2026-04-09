---
# === CORE IDENTIFICATION ===
concept: Well-Defined Function
slug: well-defined-function

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 20
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends: []
related:
  - equivalence-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A relation is well-defined if each element in the domain is assigned to a unique element in the range, regardless of how the input is represented.

# Core Definition

"A relation is well-defined if each element in the domain is assigned to a unique element in the range" (Judson, p. 20). This is especially important when elements can have multiple representations, such as fractions or equivalence classes.

# Prerequisites

- **Mapping** — Well-definedness is a property that relations must have to be mappings

# Key Properties

1. If $a_1 = a_2$ in the domain, then $f(a_1) = f(a_2)$
2. Critical when the domain consists of equivalence classes
3. Must be verified whenever elements have multiple representations

# Construction / Recognition

## To Verify Well-Definedness:
1. Suppose two representations of the same element: $a_1 = a_2$
2. Show that $f(a_1) = f(a_2)$
3. If this fails for any case, the relation is not well-defined

# Context & Application

Well-definedness is crucial when defining operations on equivalence classes, such as addition and multiplication modulo $n$. One must verify that the result does not depend on the choice of representative from each equivalence class.

# Examples

**Example 1** (p. 20): Consider $f: \mathbb{Q} \to \mathbb{Z}$ given by $f(p/q) = p$. Since $1/2 = 2/4$, we would need $f(1/2) = f(2/4)$, but $f(1/2) = 1$ and $f(2/4) = 2$. Since $1 \neq 2$, this relation is not well-defined.

# Relationships

## Builds Upon
- **mapping** — Well-definedness is required for a relation to be a mapping

## Related
- **equivalence-class** — Well-definedness must be checked when defining functions on equivalence classes
- **modular-arithmetic** — Operations mod $n$ require well-definedness verification

# Common Errors

- **Error**: Defining a function on equivalence classes without checking well-definedness
  **Correction**: Always verify that the function's output is independent of the choice of representative

# Common Confusions

- **Confusion**: Thinking well-definedness is always obvious
  **Clarification**: When elements have multiple representations (as with fractions or equivalence classes), well-definedness must be explicitly verified

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 20.

# Verification Notes

- Definition source: Direct from p. 20
- Confidence: HIGH — explicit definition with counterexample
- Cross-reference status: Verified
- Uncertainties: None
